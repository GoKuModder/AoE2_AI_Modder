from typing import Any, Dict, List, Optional
from bs4 import BeautifulSoup, Tag
from src.knowledge_builders.utils import require_bs4, clean_ws

def build_effects_knowledge(
    html_content: str, 
    aoe2_methods: Dict[str, Any],
    dataset_dependencies: Optional[Dict[str, List[Dict[str, str]]]] = None
) -> Dict[str, Any]:
    """
    Builds the final Effects Knowledge dictionary by merging UGC data with AoE2SP introspection.
    
    Args:
        html_content: Raw HTML from UGC.
        aoe2_methods: Dict of method info from AoE2ScenarioParser.
        dataset_dependencies: Mapping of effect_name -> list of dataset dicts (name, module).
        
    Returns:
         Dictionary {method_name: {data...}}
    """
    ugc_data = parse_ugc_effects(html_content)
    merged = {}
    
    dataset_dependencies = dataset_dependencies or {}

    for method_name, method_info in sorted(aoe2_methods.items()):
        # Attempt to match UGC title
        # Method names are snake_case (e.g., change_color_mood)
        # UGC keys might be "Change Color Mood" or approximations
        
        # We try to find the best match in UGC keys
        # Simple heuristic: normalize both and match
        
        ugc_match = None
        # Try finding a direct match via expected title format
        expected_title = method_name.replace("_", " ").title()
        
        # Special case handling if needed, but generic normalize is robust
        # Let's iterate UGC to find match
        method_key = method_name.lower().replace("_", "")
        
        for u_title, u_record in ugc_data.items():
            u_key = u_title.lower().replace(" ", "").replace("-", "")
            if u_key == method_key:
                ugc_match = u_record
                break
                
        # Merge Logic
        row = {
            "method": method_name,
            "signature": method_info["signature"],
            "params": method_info["params"],
            "ugc_name": ugc_match["name"] if ugc_match else None,
            "ugc_url": ugc_match["url"] if ugc_match else None,
            "ugc_description": ugc_match["description"] if ugc_match else None, # New field
        }
        
        # Param Processing with Dataset Linking
        # We want to format params as "Param_Name: Description (Dataset: X)"
        
        final_config_fields = []
        if ugc_match:
            ugc_fields = ugc_match["config_fields"] # List of "Name: Description" strings
            
            # Helper to check if a param involves a dataset
            # We check if the METHOD has dependencies
            deps = dataset_dependencies.get(method_name, [])
            
            for field_str in ugc_fields:
                # Field string usually "Name: Description"
                if ":" in field_str:
                    p_name, p_desc = field_str.split(":", 1)
                    p_name = p_name.strip()
                    p_desc = p_desc.strip()
                    
                    # Logic to match param name to dataset
                    # Heuristic: if params have matching names to datasets
                    # Dataset names are CamelCase (ColorMood), param in field is Title Case (Color Mood)
                    
                    # Check against available deps for this effect
                    linked_ds = []
                    for dep in deps:
                        # Normalize dep name and param name
                        # dep['name'] = ColorMood -> colormood
                        # p_name = Color Mood -> colormood
                        if dep["name"].lower() == p_name.lower().replace(" ", ""):
                            linked_ds.append(dep["name"])
                        elif dep["module"].lower() == p_name.lower().replace(" ", ""): # 'color_mood' vs 'Color Mood'
                            linked_ds.append(dep["name"])
                            
                    if linked_ds:
                        ds_str = ", ".join(linked_ds)
                        final_config_fields.append(f"{p_name}: {p_desc} (Dataset: {ds_str})")
                    else:
                        final_config_fields.append(field_str)
                else:
                    final_config_fields.append(field_str)
        
        row["ugc_config_fields"] = final_config_fields
        merged[method_name] = row
            
    return merged


def parse_ugc_effects(html: str) -> Dict[str, Dict[str, Any]]:
    """
    Parses UGC HTML to extract effects.
    Expected structure: H3 (Title) -> Content (Description) -> UL/OL (Config attributes)
    """
    require_bs4()
    soup = BeautifulSoup(html, "html.parser")
    
    effects = {}
    
    # Iterate over H3 headers which seem to be the effect titles
    # e.g. <h3 id="31-ai-script-goal">3.1. AI Script Goal<a class="headerlink" ...></a></h3>
    
    for h3 in soup.find_all("h3"):
        text = clean_ws(h3.get_text())
        # Format "3.1. AI Script Goal" -> extract "AI Script Goal"
        # Split by first space after numbers? 
        # Usually starts with "X.Y. Name"
        
        parts = text.split(".", 2)
        if len(parts) >= 3:
            # "3.1. Name" -> parts ["3", "1", " Name"]
            name = parts[-1].strip()
            # If name ends with "¶", remove it (it's the headerlink text often captured)
            if name.endswith("¶"):
                name = name[:-1]
        else:
            name = text.replace("¶", "").strip()
            
        # Get anchor URL
        a_tag = h3.find("a", class_="headerlink")
        url_suffix = a_tag["href"] if a_tag else ""
        full_url = f"https://ugc.aoe2.rocks/scenarios/triggers/effects/effects/{url_suffix}"
        
        # Extract Description & Configs
        # Walk siblings until next header
        description_parts = []
        config_fields = []
        
        curr = h3.next_sibling
        while curr and query_tag_name(curr) not in ["h1", "h2", "h3", "h4"]:
            if isinstance(curr, Tag):
                # If it's a paragraph, it's likely description
                if curr.name == "p":
                    # UGC often puts a standalone ¶ link in a p tag, ignore it
                    p_text = clean_ws(curr.get_text())
                    if p_text != "¶":
                         description_parts.append(p_text)
                
                # If it's a code block (pre), it's likely just syntax example, can include or skip?
                # User asked for Description.
                # "This effect is used to..." is in <p> tags usually.
                
                # If it's a list (ol/ul), it's configuration
                elif curr.name in ["ol", "ul"]:
                     for li in curr.find_all("li"):
                         config_fields.append(clean_ws(li.get_text()))
                         
            curr = curr.next_sibling
            
        description = " ".join(description_parts).strip()
        
        effects[name] = {
            "name": name,
            "url": full_url,
            "description": description,
            "config_fields": config_fields
        }
        
    return effects

def query_tag_name(node) -> str:
    return node.name if isinstance(node, Tag) else ""
