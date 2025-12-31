from pathlib import Path
import sys
import argparse
from typing import Any

# Import our modular components
from src.common.web_client import http_get
from src.integration.aoe2_introspection import introspect_aoe2sp_effects
from src.knowledge_builders.attributes_builder import build_attributes_knowledge
from src.knowledge_builders.effects_builder import build_effects_knowledge
from src.writers.markdown_writer import generate_table, generate_list
from src.writers.python_writer import write_python_module

UGC_ATTRIBUTES_URL = "https://ugc.aoe2.rocks/general/attributes/attributes/"
UGC_EFFECTS_URL = "https://ugc.aoe2.rocks/scenarios/triggers/effects/effects/"
OUT_DIR = Path("docs/trigger_knowledge")
CACHE_DIR = OUT_DIR / "_cache"


def run_attributes_pipeline(force_fail: bool = False) -> bool:
    print("Building Attributes Knowledge...")
    try:
        html = http_get(UGC_ATTRIBUTES_URL, CACHE_DIR / "ugc_attributes.html")
        data = build_attributes_knowledge(html)
        
        # Write Python
        write_python_module(OUT_DIR / "attributes_knowledge.py", "ATTRIBUTES", data)
        
        # Write Markdown
        items = [
            f"**{a['id']} {a['name']}**: {a['description']} (Source: {a['source']})"
            for a in data.values()
        ]
        md_content = (
            "# Trigger Knowledge: Attributes (subset)\n\n"
            "Generated file. Do not hand-edit; run tools/build_trigger_knowledge.py.\n\n"
            + generate_list(items)
        )
        (OUT_DIR / "attributes_knowledge.md").write_text(md_content, encoding="utf-8")
        
        print("[OK] Attributes knowledge generated")
        return True
    except Exception as e:
        print(f"[FAIL] Attributes knowledge failed: {e}")
        return False


def run_effects_pipeline(force_fail: bool = False) -> bool:
    print("Building Effects Knowledge...")
    try:
        html = http_get(UGC_EFFECTS_URL, CACHE_DIR / "ugc_effects.html")
        aoe2_methods = introspect_aoe2sp_effects()
        
        merged_dict = build_effects_knowledge(html, aoe2_methods)
        
        # Write Python
        write_python_module(OUT_DIR / "effects_knowledge.py", "EFFECTS", merged_dict)
        
        # Write Markdown
        headers = ["AoE2SP Method", "Signature", "UGC Name", "UGC Fields", ""]
        rows = []
        for row_data in merged_dict.values():
            fields = ", ".join(row_data.get("ugc_config_fields") or [])
            rows.append([
                f"`{row_data['method']}`",
                f"`{row_data['signature']}`",
                str(row_data.get("ugc_name") or ""),
                fields,
                str(row_data.get("ugc_url") or "")
            ])
            
        md_content = (
            "# Trigger Knowledge: Effects\n"
            "Generated file. Do not hand-edit; run tools/build_trigger_knowledge.py.\n"
            + generate_table(headers, rows)
        )
        (OUT_DIR / "effects_knowledge.md").write_text(md_content, encoding="utf-8")

        print("[OK] Effects knowledge generated")
        return True
    except Exception as e:
        print(f"[FAIL] Effects knowledge failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def build_trigger_knowledge() -> int:
    parser = argparse.ArgumentParser(description="Build Trigger Knowledge")
    parser.add_argument("--attributes", action="store_true", help="Build attributes knowledge")
    parser.add_argument("--effects", action="store_true", help="Build effects knowledge")
    parser.add_argument("--all", action="store_true", help="Build both")
    
    args = parser.parse_args()
    
    if not (args.attributes or args.effects or args.all):
        args.all = True
    
    do_attrs = args.attributes or args.all
    do_effects = args.effects or args.all
    
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    
    success = True
    
    if do_attrs:
        if not run_attributes_pipeline():
            success = False
            
    if do_effects:
        if not run_effects_pipeline():
            success = False
            
    return 0 if success else 1
