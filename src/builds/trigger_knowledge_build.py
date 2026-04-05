from pathlib import Path
import sys
import argparse
import json
from typing import Any, Dict, List

# Import our modular components
from src.common.web_client import http_get
from src.integration.aoe2_introspection import (
    introspect_aoe2sp_conditions,
    introspect_aoe2sp_effects,
    introspect_object_attributes_enum,
    introspect_genie_datasets,
    introspect_dataset_dependencies,
)
from src.knowledge_builders.attributes_builder import build_attributes_knowledge
from src.knowledge_builders.conditions_builder import build_conditions_knowledge
from src.knowledge_builders.effects_builder import build_effects_knowledge
from src.knowledge_builders.genie_registry_builder import build_genie_registry
from src.knowledge_builders.trigger_project_usage_builder import build_trigger_project_usage
from src.knowledge_builders.trigger_usage_playbook_builder import (
    build_condition_playbook,
    build_effect_playbook,
)
from src.writers.markdown_writer import generate_table, generate_list
from src.writers.python_writer import write_python_module

# Resolve project root (assuming this file is in src/builds/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
UGC_ATTRIBUTES_URL = "https://ugc.aoe2.rocks/general/attributes/attributes/"
UGC_EFFECTS_JSON_URL = "https://raw.githubusercontent.com/Divy1211/AoE2DE_UGC_Guide/main/docs/scenarios/triggers/effects/effects.json"

OUT_DIR = PROJECT_ROOT / "docs" / "trigger_knowledge"
CACHE_DIR = OUT_DIR / "_cache"
REFERENCE_PROJECTS_JSON = (
    PROJECT_ROOT / "docs" / "agent" / "references" / "reference_projects.json"
)


def run_conditions_pipeline(force_fail: bool = False) -> bool:
    print("Building Conditions Knowledge...")
    try:
        from AoE2ScenarioParser.datasets import conditions as aoe2sp_conditions  # type: ignore
    except ImportError as e:
        raise RuntimeError(
            "Could not import AoE2ScenarioParser.datasets.conditions. Ensure your interpreter is set correctly."
        ) from e

    try:
        source_text = Path(aoe2sp_conditions.__file__).read_text(encoding="utf-8")
        condition_methods = introspect_aoe2sp_conditions()
        conditions_list = build_conditions_knowledge(source_text, condition_methods)

        legacy_dict = {
            item["internal_name"]: {
                "method": item["internal_name"],
                "signature": item["signature"],
                "params": [p["name"] for p in item["parameters"]],
                "description": item["description"],
                "notes": item["notes"],
            }
            for item in conditions_list
        }
        write_python_module(OUT_DIR / "conditions_knowledge.py", "CONDITIONS", legacy_dict)

        (OUT_DIR / "conditions_knowledge.json").write_text(
            json.dumps(conditions_list, indent=2),
            encoding="utf-8",
        )

        md_lines = [
            "# Trigger Knowledge: Conditions",
            "Generated file. Do not hand-edit; run tools/build_trigger_knowledge.py.",
            "Data source: canonical `conditions_knowledge.json`.",
            "",
            "## Index",
            "| ID | Name | Method |",
            "|---|---|---|",
        ]
        for entry in conditions_list:
            cid = entry["condition_id"]
            name = entry["display_name"]
            method = entry["internal_name"]
            anchor = name.lower().replace(" ", "-").replace("(", "").replace(")", "")
            md_lines.append(f"| {cid} | [{name}](#{anchor}) | `{method}` |")

        md_lines.append("")

        for entry in conditions_list:
            cid = entry["condition_id"]
            name = entry["display_name"]
            desc = entry["description"] or "*No description provided.*"
            sig = entry["signature"]
            params = entry["parameters"]
            notes = entry.get("notes", [])

            md_lines.append(f"## {cid}. {name}")
            md_lines.append(f"`{sig}`")
            md_lines.append("")
            md_lines.append(desc)
            md_lines.append("")

            if params:
                md_lines.append("**Parameters:**")
                for param in params:
                    param_type = param["type"] or "Any"
                    default = (
                        f", default={param['default']}"
                        if param["default"] is not None
                        else ""
                    )
                    md_lines.append(f"- `{param['name']}` ({param_type}{default})")
            else:
                md_lines.append("*No parameters.*")

            if notes:
                md_lines.append("")
                md_lines.append("**Notes:**")
                for note in notes:
                    md_lines.append(f"- {note}")

            md_lines.append("")

        (OUT_DIR / "conditions_knowledge.md").write_text(
            "\n".join(md_lines),
            encoding="utf-8",
        )

        print("[OK] Conditions knowledge generated")
        print(f"  - {OUT_DIR / 'conditions_knowledge.json'} (Canonical)")
        print(f"  - {OUT_DIR / 'conditions_knowledge.md'}")
        return True
    except Exception as e:
        print(f"[FAIL] Conditions knowledge failed: {e}")
        import traceback

        traceback.print_exc()
        return False


def run_attributes_pipeline(force_fail: bool = False) -> bool:
    print("Building Attributes Knowledge...")
    try:
        # 1. Inputs
        html = http_get(UGC_ATTRIBUTES_URL, CACHE_DIR / "ugc_attributes.html")
        parser_enums = introspect_object_attributes_enum()
        
        # 2. Build (Unified)
        data = build_attributes_knowledge(html, parser_enums)
        
        # 3. Validation & Reporting
        ugc_only = [r for r in data.values() if r["ugc_name"] and not r["parser_enum_name"]]
        parser_only = [r for r in data.values() if r["parser_enum_name"] and not r["ugc_name"]]
        matched = [r for r in data.values() if r["ugc_name"] and r["parser_enum_name"]]
        
        print("\n--- Attribute Mapping Report ---")
        print(f"Total Unique IDs: {len(data)}")
        print(f"Matched: {len(matched)}")
        print(f"UGC Only (Unmapped): {len(ugc_only)}")
        print(f"Parser Only (No UGC): {len(parser_only)}")
        
        if ugc_only:
            print("\n[FAIL] The following UGC Attributes have no Parser Enum mapping:")
            for r in ugc_only:
                print(f"  ID {r['id']}: {r['ugc_name']}")
        
        if parser_only:
            print("\n[INFO] The following Parser Enums have no UGC Documentation (benign):")
            for r in parser_only:
                print(f"  ID {r['id']}: {r['parser_enum_name']}")

        # QA: Name Mismatch
        mismatches = []
        for r in matched:
            # Normalize for loose comparison: uppercase, replace spaces with underscores, remove non-alphanumeric
            u_norm = r["ugc_name"].upper().replace(" ", "_").replace("/", "_").replace("-", "_")
            p_norm = r["parser_enum_name"].upper()
            if u_norm != p_norm:
                mismatches.append(f"ID {r['id']}: '{r['ugc_name']}' vs '{r['parser_enum_name']}'")
        
        if mismatches:
            print("\n[WARN] Name Normalization Differences (IDs match, just informative):")
            for m in mismatches[:10]:
                print(f"  {m}")
            if len(mismatches) > 10: print(f"  ... and {len(mismatches) - 10} more")

        # FAIL if any UGC attribute is unmapped
        if ugc_only:
            print("\n[CRITICAL ERROR] Mapping incomplete. See list above.")
            return False

        # 4. Outputs
        
        # A) Python Module (Legacy support + Enum linkage)
        write_python_module(OUT_DIR / "attributes_knowledge.py", "ATTRIBUTES", data)
        
        # B) JSON Dataset (New)
        (OUT_DIR / "attributes_dataset.json").write_text(
            json.dumps(data, indent=2, sort_keys=True), encoding="utf-8"
        )
        
        # C) Markdown (Enriched)
        lines = []
        lines.append("# Trigger Knowledge: Attributes (Unified)\n")
        lines.append("Generated file. Do not hand-edit; run tools/build_trigger_knowledge.py.\n")
        
        for aid, r in sorted(data.items()):
            name = r['ugc_name'] or "(Undocumented in UGC)"
            enum_ref = f"`ObjectAttribute.{r['parser_enum_name']}`" if r['parser_enum_name'] else "NO_ENUM_MAPPING"
            desc = r['description'] or ""
            # Link usage removed as per user request (reduced bloat)
            hint = f"<br> *{r['usage_hint']}*" if r['usage_hint'] else ""
            
            lines.append(f"- **{aid} {name}** ({enum_ref}): {desc} {hint}")
            
        (OUT_DIR / "attributes_knowledge.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        
        print(f"\n[OK] Attributes knowledge generated")
        print(f"  - {OUT_DIR / 'attributes_knowledge.py'}")
        print(f"  - {OUT_DIR / 'attributes_knowledge.md'}")
        print(f"  - {OUT_DIR / 'attributes_dataset.json'}")
        return True

    except Exception as e:
        print(f"[FAIL] Attributes knowledge failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def run_effects_pipeline(force_fail: bool = False) -> bool:
    print("Building Effects Knowledge...")
    try:
        # Fetch JSON raw text
        json_text = http_get(UGC_EFFECTS_JSON_URL, CACHE_DIR / "ugc_effects.json")
        try:
             ugc_json_data = json.loads(json_text)
        except json.JSONDecodeError as e:
             print(f"[WARN] Failed to parse JSON, re-fetching... Error: {e}")
             raise
             
        aoe2_methods = introspect_aoe2sp_effects()
        dataset_deps = introspect_dataset_dependencies()
        
        # Build List of Data
        effects_list = build_effects_knowledge(ugc_json_data, aoe2_methods, dataset_deps)
        
        # 1. Write Python (Legacy format or New?)
        # Legacy writer expects Dict[str, val]. building a dict for it.
        legacy_dict = {
            item["internal_name"]: {
                "method": item["internal_name"],
                "signature": item["signature"], 
                "params": [p["name"] for p in item["parameters"]], # Simplify param format for legacy
                "ugc_name": item["display_name"],
                "ugc_description": item["description"],
                "ugc_config_fields": [p["name"] for p in item["parameters"]], # Approximately correct
            } for item in effects_list
        }
        write_python_module(OUT_DIR / "effects_knowledge.py", "EFFECTS", legacy_dict)
        
        # 2. Write Canonical JSON
        (OUT_DIR / "effects_knowledge.json").write_text(
            json.dumps(effects_list, indent=2), encoding="utf-8"
        )
        
        # 3. Write Markdown (Section Based)
        md_lines = [
            "# Trigger Knowledge: Effects",
            "Generated file. Do not hand-edit; run tools/build_trigger_knowledge.py.", 
            "Data source: canonical `effects_knowledge.json`.",
            "",
            "## Index",
            "| ID | Name | Method |",
            "|---|---|---|",
        ]
        
        # Index Table
        for entry in effects_list:
            eid = entry["effect_id"]
            name = entry["display_name"]
            method = entry["internal_name"]
            anchor = name.lower().replace(" ", "-").replace("(", "").replace(")", "") # Basic GitHub slugify
            md_lines.append(f"| {eid} | [{name}](#{anchor}) | `{method}` |")
            
        md_lines.append("")
        
        # Sections
        for entry in effects_list:
            eid = entry["effect_id"]
            name = entry["display_name"]
            desc = entry["description"] or "*No description provided.*"
            sig = entry["signature"]
            params = entry["parameters"]
            
            md_lines.append(f"## {eid}. {name}")
            md_lines.append(f"`{sig}`\n")
            md_lines.append(f"{desc}\n")
            
            if params:
                md_lines.append("**Parameters:**")
                for p in params:
                    p_name = p["name"]
                    p_type = p["type"] or "Any"
                    p_ds = p.get("dataset")
                    
                    line = f"- `{p_name}` ({p_type})"
                    if p_ds:
                        # Linkify dataset if we knew the base URL, but for now just text
                        ds_name = p_ds["name"]
                        line += f" -> **Dataset: {ds_name}**"
                    
                    md_lines.append(line)
            else:
                 md_lines.append("*No parameters.*")
                 
            md_lines.append("") # Spacer
            
        (OUT_DIR / "effects_knowledge.md").write_text("\n".join(md_lines), encoding="utf-8")

        print("[OK] Effects knowledge generated")
        print(f"  - {OUT_DIR / 'effects_knowledge.json'} (Canonical)")
        print(f"  - {OUT_DIR / 'effects_knowledge.md'}")
        
        return True
    except Exception as e:
        print(f"[FAIL] Effects knowledge failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def run_registry_pipeline(force_fail: bool = False) -> bool:
    print("Building Genie Object Registry...")
    try:
        # 1. Introspect
        datasets = introspect_genie_datasets()
        
        # 2. Build
        registry = build_genie_registry(datasets)
        
        # 3. Validation Report (in memory stats)
        total_ids = len(registry)
        duplicates = [r for r in registry if len(r["sources"]) > 1]
        name_conflicts = [r for r in registry if r["issues"]]
        
        dataset_counts = {k: len(v) for k, v in datasets.items()}
        
        print("\n--- Genie Registry Report ---")
        print(f"Total Unique IDs: {total_ids}")
        print(f"Source Counts: {dataset_counts}")
        print(f"IDs in Multiple Datasets: {len(duplicates)}")
        print(f"Name Conflicts Resolved: {len(name_conflicts)}")
        
        if name_conflicts:
            print("\n[INFO] Name Conflicts (Showing first 10):")
            for r in name_conflicts[:10]:
                print(f"  ID {r['genie_id']}: Chosen='{r['name']}', Sources={r['sources']}, Issues={r['issues']}")
        
        # 4. Outputs
        out_json = OUT_DIR / "genie_registry.json"
        out_json.write_text(json.dumps(registry, indent=2), encoding="utf-8")
        
        out_md = OUT_DIR / "genie_registry_report.md"
        report_lines = [
            "# Genie Object Registry Report",
            f"**Total IDs**: {total_ids}",
            f"**Sources**: {dataset_counts}",
            "",
            "## Duplicates & Conflicts",
            f"- **Multi-Source IDs**: {len(duplicates)}",
            f"- **Name Conflicts**: {len(name_conflicts)}",
            "",
            "## Sample Conflicts",
        ]
        for r in name_conflicts:
            report_lines.append(f"- **{r['genie_id']}**: {r['name']} {r['issues']}")
            
        out_md.write_text("\n".join(report_lines), encoding="utf-8")
        
        print(f"\n[OK] Genie Registry generated")
        print(f"  - {out_json}")
        print(f"  - {out_md}")
        return True
    except Exception as e:
        print(f"[FAIL] Genie Registry failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def run_usage_pipeline(force_fail: bool = False) -> bool:
    print("Building Trigger Project Usage Knowledge...")
    try:
        conditions_path = OUT_DIR / "conditions_knowledge.json"
        effects_path = OUT_DIR / "effects_knowledge.json"
        if not conditions_path.exists():
            raise FileNotFoundError(
                f"Missing conditions knowledge: {conditions_path}. Run the conditions pipeline first."
            )
        if not effects_path.exists():
            raise FileNotFoundError(
                f"Missing effects knowledge: {effects_path}. Run the effects pipeline first."
            )
        if not REFERENCE_PROJECTS_JSON.exists():
            raise FileNotFoundError(
                f"Missing reference project metadata: {REFERENCE_PROJECTS_JSON}"
            )

        condition_entries = json.loads(conditions_path.read_text(encoding="utf-8"))
        effect_entries = json.loads(effects_path.read_text(encoding="utf-8"))
        usage_payload = build_trigger_project_usage(
            condition_entries,
            effect_entries,
            REFERENCE_PROJECTS_JSON,
        )

        condition_usage = usage_payload["conditions"]
        effect_usage = usage_payload["effects"]

        (OUT_DIR / "condition_project_usage.json").write_text(
            json.dumps(condition_usage, indent=2),
            encoding="utf-8",
        )
        (OUT_DIR / "effect_project_usage.json").write_text(
            json.dumps(effect_usage, indent=2),
            encoding="utf-8",
        )

        used_conditions = [entry for entry in condition_usage if entry["usage_count"] > 0]
        used_effects = [entry for entry in effect_usage if entry["usage_count"] > 0]
        top_conditions = sorted(
            used_conditions,
            key=lambda entry: (-entry["usage_count"], entry["internal_name"]),
        )[:10]
        top_effects = sorted(
            used_effects,
            key=lambda entry: (-entry["usage_count"], entry["internal_name"]),
        )[:10]

        md_lines = [
            "# Trigger Knowledge: Real Project Usage",
            "Generated file. Do not hand-edit; run tools/build_trigger_knowledge.py.",
            "",
            "This file summarizes how AoE2ScenarioParser trigger conditions and effects are used in the local reference projects.",
            "",
            "Reference projects scanned:",
            "- `LordsOfDiplomacy - Easy Mode`",
            "- `GoKu RPG Project` (excluding `Difficulty`)",
            "- `Hide_and_Seek`",
            "",
            f"- Conditions observed in real projects: **{len(used_conditions)} / {len(condition_usage)}**",
            f"- Effects observed in real projects: **{len(used_effects)} / {len(effect_usage)}**",
            "",
            "## Most Used Conditions",
        ]

        if top_conditions:
            for entry in top_conditions:
                md_lines.append(
                    f"- `{entry['internal_name']}` ({entry['usage_count']} uses): "
                    + ", ".join(entry["used_in_projects"])
                )
        else:
            md_lines.append("- No condition usage observed.")

        md_lines.extend(["", "## Most Used Effects"])
        if top_effects:
            for entry in top_effects:
                md_lines.append(
                    f"- `{entry['internal_name']}` ({entry['usage_count']} uses): "
                    + ", ".join(entry["used_in_projects"])
                )
        else:
            md_lines.append("- No effect usage observed.")

        md_lines.extend(
            [
                "",
                "## How To Use The JSON",
                "- Use `condition_project_usage.json` when the question is about how a condition is used in real projects.",
                "- Use `effect_project_usage.json` when the question is about how an effect is used in real projects.",
                "- Join these usage datasets with `conditions_knowledge.json` and `effects_knowledge.json` for signatures and parameters.",
            ]
        )

        (OUT_DIR / "project_usage_knowledge.md").write_text(
            "\n".join(md_lines) + "\n",
            encoding="utf-8",
        )

        print("[OK] Trigger project usage knowledge generated")
        print(f"  - {OUT_DIR / 'condition_project_usage.json'}")
        print(f"  - {OUT_DIR / 'effect_project_usage.json'}")
        print(f"  - {OUT_DIR / 'project_usage_knowledge.md'}")
        return True
    except Exception as e:
        print(f"[FAIL] Trigger project usage failed: {e}")
        import traceback

        traceback.print_exc()
        return False


def run_playbook_pipeline(force_fail: bool = False) -> bool:
    print("Building Trigger Usage Playbooks...")
    try:
        conditions_path = OUT_DIR / "conditions_knowledge.json"
        effects_path = OUT_DIR / "effects_knowledge.json"
        condition_usage_path = OUT_DIR / "condition_project_usage.json"
        effect_usage_path = OUT_DIR / "effect_project_usage.json"
        required_paths = [
            conditions_path,
            effects_path,
            condition_usage_path,
            effect_usage_path,
        ]
        for path in required_paths:
            if not path.exists():
                raise FileNotFoundError(f"Missing required trigger dataset: {path}")

        condition_entries = json.loads(conditions_path.read_text(encoding="utf-8"))
        effect_entries = json.loads(effects_path.read_text(encoding="utf-8"))
        condition_usage = json.loads(condition_usage_path.read_text(encoding="utf-8"))
        effect_usage = json.loads(effect_usage_path.read_text(encoding="utf-8"))

        condition_playbook = build_condition_playbook(condition_entries, condition_usage)
        effect_playbook = build_effect_playbook(effect_entries, effect_usage)

        (OUT_DIR / "condition_usage_playbook.json").write_text(
            json.dumps(condition_playbook, indent=2),
            encoding="utf-8",
        )
        (OUT_DIR / "effect_usage_playbook.json").write_text(
            json.dumps(effect_playbook, indent=2),
            encoding="utf-8",
        )

        def _playbook_to_markdown(
            title: str,
            id_key: str,
            entries: List[Dict[str, Any]],
        ) -> str:
            lines = [
                f"# {title}",
                "Generated file. Do not hand-edit; run tools/build_trigger_knowledge.py.",
                "",
            ]
            for entry in entries:
                lines.append(f"## {entry[id_key]}. {entry['display_name']}")
                lines.append(f"**Method**: `{entry['internal_name']}`")
                lines.append(f"**Family**: `{entry['family']}`")
                lines.append(f"**Primary Role**: {entry['primary_role']}")
                lines.append("")
                lines.append("**How It Is Used**")
                lines.append(entry["how_it_is_used"])
                lines.append("")
                lines.append("**Architecture Notes**")
                lines.append(entry["architecture_notes"])
                lines.append("")
                lines.append("**Real Project Usage**")
                lines.append(entry["real_project_usage_summary"])
                lines.append("")
                lines.append("**Common Pairings**")
                for pairing in entry["common_pairings"]:
                    lines.append(f"- `{pairing}`")
                if "audience_scope" in entry:
                    lines.append("")
                    lines.append("**Communication Semantics**")
                    lines.append(f"- Audience Scope: `{entry['audience_scope']}`")
                    lines.append(f"- Attention Strength: `{entry['attention_strength']}`")
                    lines.append(f"- Recommended Frequency: `{entry['recommended_frequency']}`")
                    lines.append(f"- Best Use: {entry['best_use']}")
                if entry["reference_examples"]:
                    lines.append("")
                    lines.append("**Reference Examples**")
                    for example in entry["reference_examples"]:
                        lines.append(f"- `{example}`")
                lines.append("")
            return "\n".join(lines)

        (OUT_DIR / "condition_usage_playbook.md").write_text(
            _playbook_to_markdown(
                "Trigger Condition Usage Playbook",
                "condition_id",
                condition_playbook,
            ),
            encoding="utf-8",
        )
        (OUT_DIR / "effect_usage_playbook.md").write_text(
            _playbook_to_markdown(
                "Trigger Effect Usage Playbook",
                "effect_id",
                effect_playbook,
            ),
            encoding="utf-8",
        )

        print("[OK] Trigger usage playbooks generated")
        print(f"  - {OUT_DIR / 'condition_usage_playbook.json'}")
        print(f"  - {OUT_DIR / 'effect_usage_playbook.json'}")
        print(f"  - {OUT_DIR / 'condition_usage_playbook.md'}")
        print(f"  - {OUT_DIR / 'effect_usage_playbook.md'}")
        return True
    except Exception as e:
        print(f"[FAIL] Trigger usage playbooks failed: {e}")
        import traceback

        traceback.print_exc()
        return False


def build_trigger_knowledge() -> int:
    parser = argparse.ArgumentParser(description="Build Trigger Knowledge")
    parser.add_argument("--attributes", action="store_true", help="Build attributes knowledge")
    parser.add_argument("--conditions", action="store_true", help="Build conditions knowledge")
    parser.add_argument("--effects", action="store_true", help="Build effects knowledge")
    parser.add_argument("--registry", action="store_true", help="Build genie object registry")
    parser.add_argument("--usage", action="store_true", help="Build trigger condition/effect project usage datasets")
    parser.add_argument("--playbooks", action="store_true", help="Build deep trigger condition/effect usage playbooks")
    parser.add_argument("--all", action="store_true", help="Build both")
    
    args = parser.parse_args()
    
    if not (
        args.attributes
        or args.conditions
        or args.effects
        or args.registry
        or args.usage
        or args.playbooks
        or args.all
    ):
        args.all = True
    
    do_attrs = args.attributes or args.all
    do_conditions = args.conditions or args.all
    do_effects = args.effects or args.all
    do_registry = args.registry or args.all
    do_usage = args.usage or args.all
    do_playbooks = args.playbooks or args.all
    
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    
    success = True
    
    if do_attrs:
        if not run_attributes_pipeline():
            success = False

    if do_conditions:
        if not run_conditions_pipeline():
            success = False
            
    if do_effects:
        if not run_effects_pipeline():
            success = False

    if do_registry:
        if not run_registry_pipeline():
            success = False

    if do_usage:
        if not run_usage_pipeline():
            success = False

    if do_playbooks:
        if not run_playbook_pipeline():
            success = False
            
    return 0 if success else 1
