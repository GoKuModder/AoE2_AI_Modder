from pathlib import Path
import sys
import argparse
import json
from typing import Any, Dict, List

# Import our modular components
from src.common.web_client import http_get
from src.integration.aoe2_introspection import introspect_aoe2sp_effects, introspect_object_attributes_enum, introspect_genie_datasets, introspect_dataset_dependencies
from src.knowledge_builders.attributes_builder import build_attributes_knowledge
from src.knowledge_builders.effects_builder import build_effects_knowledge
from src.knowledge_builders.genie_registry_builder import build_genie_registry
from src.writers.markdown_writer import generate_table, generate_list
from src.writers.python_writer import write_python_module

# Resolve project root (assuming this file is in src/builds/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
UGC_ATTRIBUTES_URL = "https://ugc.aoe2.rocks/general/attributes/attributes/"
UGC_EFFECTS_JSON_URL = "https://raw.githubusercontent.com/Divy1211/AoE2DE_UGC_Guide/main/docs/scenarios/triggers/effects/effects.json"

OUT_DIR = PROJECT_ROOT / "docs" / "trigger_knowledge"
CACHE_DIR = OUT_DIR / "_cache"


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


def build_trigger_knowledge() -> int:
    parser = argparse.ArgumentParser(description="Build Trigger Knowledge")
    parser.add_argument("--attributes", action="store_true", help="Build attributes knowledge")
    parser.add_argument("--effects", action="store_true", help="Build effects knowledge")
    parser.add_argument("--registry", action="store_true", help="Build genie object registry")
    parser.add_argument("--all", action="store_true", help="Build both")
    
    args = parser.parse_args()
    
    if not (args.attributes or args.effects or args.registry or args.all):
        args.all = True
    
    do_attrs = args.attributes or args.all
    do_effects = args.effects or args.all
    do_registry = args.registry or args.all
    
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    
    success = True
    
    if do_attrs:
        if not run_attributes_pipeline():
            success = False
            
    if do_effects:
        if not run_effects_pipeline():
            success = False

    if do_registry:
        if not run_registry_pipeline():
            success = False
            
    return 0 if success else 1
