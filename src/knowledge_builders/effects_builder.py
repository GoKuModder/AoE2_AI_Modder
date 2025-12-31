from typing import Any, Dict, List, Optional

def build_effects_knowledge(
    ugc_data: Dict[str, Any], 
    aoe2_methods: Dict[str, Any],
    dataset_dependencies: Optional[Dict[str, List[Dict[str, str]]]] = None
) -> List[Dict[str, Any]]:
    """
    Builds the final Effects Knowledge list matching the new JSON schema.
    
    Args:
        ugc_data: Parsed JSON data from UGC.
        aoe2_methods: Dict of method info from AoE2ScenarioParser (params are now detailed).
        dataset_dependencies: Mapping of effect_name -> list of dataset dicts (name, module).
        
    Returns:
         List of dictionaries matching the target JSON schema, sorted by ID.
    """
    merged_list = []
    dataset_dependencies = dataset_dependencies or {}

    # Map method names to UGC IDs to handle cases where we iterate via methods
    # But wait, the previous logic iterated aoe2_methods. 
    # The requirement is "Sort by effect id". Effect ID comes from UGC JSON keys.
    # So we should iterate UGC keys and try to find matching method, OR iterate methods and try to find UGC.
    # If we iterate UGC keys, we might miss methods not in UGC?
    # The requirement says "Generate one section per effect". 
    # Let's iterate AoE2SP methods as the source of truth for "Available Effects" in the parser.
    # But we need the ID.
    
    # Let's create a map of normalized method name -> UGC data
    ugc_map = {}
    for uid, u_record in ugc_data.items():
        if "name" in u_record:
            # Normalize: "Change Diplomacy" -> "change_diplomacy"
            norm_name = u_record["name"].lower().replace(" ", "_").replace("-", "_")
            ugc_map[norm_name] = {**u_record, "id": uid}
            
    # Also create a reverse map for "Method not in UGC"? 
    # Ideally we find the ID. If no ID found, what do we do? 
    # For now, let's process all aoe2_methods. If found in UGC, we use that ID. 
    # If not found, we might skip or put at end.
    
    entries = []

    for method_name, method_info in aoe2_methods.items():
        method_key = method_name.lower().replace("_", "")
        
        # Try to find match in UGC
        ugc_match = None
        # We need a robust match. 
        # ugc_map keys might be 'change_diplomacy' -> 'changediplomacy'
        
        for u_name, u_record in ugc_map.items():
            u_key = u_name.replace("_", "")
            if u_key == method_key:
                ugc_match = u_record
                break
        
        effect_id = ugc_match["id"] if ugc_match else "9999" # Sort at end
        
        # Build Parameters List
        params_out = []
        raw_params = method_info.get("params", []) # List[Dict]
        
        deps = dataset_dependencies.get(method_name, [])
        
        for p in raw_params:
            p_name = p["name"]
            p_type = p["type"]
            p_desc = "" # We don't have descriptions in UGC anymore
            
            # Dataset Linking
            p_dataset = None
            
            # Heuristic match
            for dep in deps:
                # dep = {name: ColorMood, module: ...}
                # Check if param name matches dataset name
                # e.g. param "color_mood", dataset "ColorMood"
                if p_name.replace("_", "").lower() == dep["name"].lower():
                    # found it
                    # Construct doc reference url? 
                    # "https://ksneijders.github.io/AoE2ScenarioParser/api_docs/datasets/trigger_lists/color_mood/"
                    # We can just provide the name for the frontend/markdown generator to linkify
                    p_dataset = {
                        "name": dep["name"],
                        "module": dep["module"]
                    }
                    break

            params_out.append({
                "name": p_name,
                "type": p_type,
                "description": p_desc,
                "dataset": p_dataset
            })

        entry = {
            "effect_id": effect_id,
            "internal_name": method_name,
            "display_name": ugc_match["name"] if ugc_match else method_name,
            "description": ugc_match.get("desc", "") if ugc_match else "",
            "signature": method_info["signature"],
            "parameters": params_out
        }
        entries.append(entry)

    # Sort: Primary by integer ID (if parsable), secondary by name
    def sort_key(e):
        try:
            return int(e["effect_id"])
        except ValueError:
            return 99999

    entries.sort(key=sort_key)
    
    return entries
