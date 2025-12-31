from typing import Any, Dict, List, Optional
# No BS4 needed anymore

def build_effects_knowledge(
    ugc_data: Dict[str, Any], 
    aoe2_methods: Dict[str, Any],
    dataset_dependencies: Optional[Dict[str, List[Dict[str, str]]]] = None
) -> Dict[str, Any]:
    """
    Builds the final Effects Knowledge dictionary by merging UGC JSON data with AoE2SP introspection.
    
    Args:
        ugc_data: Parsed JSON data from UGC.
        aoe2_methods: Dict of method info from AoE2ScenarioParser.
        dataset_dependencies: Mapping of effect_name -> list of dataset dicts (name, module).
        
    Returns:
         Dictionary {method_name: {data...}}
    """
    merged = {}
    
    dataset_dependencies = dataset_dependencies or {}

    for method_name, method_info in sorted(aoe2_methods.items()):
        # Attempt to match UGC title
        # Method names are snake_case (e.g., change_color_mood)
        # UGC JSON has keys as IDs "1", "2"... values {name: "Change Diplomacy", ...}
        
        ugc_match = None
        method_key = method_name.lower().replace("_", "")
        
        # Iterate over JSON values to find match by name
        for u_record in ugc_data.values():
            u_name = u_record.get("name", "")
            u_key = u_name.lower().replace(" ", "").replace("-", "")
            
            if u_key == method_key:
                ugc_match = u_record
                break
                
        # Merge Logic
        desc = None
        if ugc_match:
            desc = ugc_match.get("desc")
        
        row = {
            "method": method_name,
            "signature": method_info["signature"],
            "params": method_info["params"],
            "ugc_name": ugc_match["name"] if ugc_match else None,
            "ugc_description": desc,
            # No URL in JSON structure provided, assuming description is key
        }
        
        # Param Processing with Dataset Linking
        
        final_config_fields = []
        if ugc_match:
            # attributes in JSON are just a list of strings: ["diplomacy", "source_player"]
            ugc_attrs = ugc_match.get("attrs", [])
            
            # Helper to check if a param involves a dataset
            deps = dataset_dependencies.get(method_name, [])
            
            for attr_name in ugc_attrs:
                # JSON attr_name is raw key, e.g. "source_player"
                # We want to display it properly. Title Case?
                display_name = attr_name.replace("_", " ").title()
                
                # Logic to match param name to dataset
                linked_ds = []
                for dep in deps:
                    # Normalize dep name and attr name
                    # dep['name'] = ColorMood -> colormood
                    # attr_name = color_mood -> colormood
                    if dep["name"].lower() == attr_name.lower().replace("_", ""):
                        linked_ds.append(dep["name"])
                    elif dep["module"].lower() == attr_name.lower().replace("_", ""):
                        linked_ds.append(dep["name"])
                        
                if linked_ds:
                    ds_str = ", ".join(linked_ds)
                    final_config_fields.append(f"{display_name} (Dataset: {ds_str})")
                else:
                    final_config_fields.append(display_name)
        
        row["ugc_config_fields"] = final_config_fields
        merged[method_name] = row
            
    return merged
