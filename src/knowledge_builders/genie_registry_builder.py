from typing import Any, Dict, List, Optional, Set

def build_genie_registry(datasets: Dict[str, Dict[int, str]]) -> List[Dict[str, Any]]:
    """
    Merges datasets (units, heroes, buildings, other) into a unified registry.
    Priority for Name Selection: heroes > units > buildings > other.
    
    Returns:
        List of records sorted by ID.
    """
    
    # Priority order
    PRIORITY = ["heroes", "units", "buildings", "other"]
    
    # 1. Collect all IDs
    all_ids: Set[int] = set()
    for name in PRIORITY:
        all_ids.update(datasets.get(name, {}).keys())
        
    registry: List[Dict[str, Any]] = []
    
    for gid in sorted(all_ids):
        # Gather data for this ID from all sources
        sources_found = []
        name_candidates = {} # source -> name
        
        for source in PRIORITY:
            d = datasets.get(source, {})
            if gid in d:
                sources_found.append(source)
                name_candidates[source] = d[gid]
                
        # Determine Primary Name
        primary_name = None
        # Since we iterate PRIORITY, the first one found is the highest priority
        for source in PRIORITY:
             if source in name_candidates:
                 primary_name = name_candidates[source]
                 break
        
        # Facets
        is_hero = "heroes" in sources_found
        is_unit = "units" in sources_found
        is_building = "buildings" in sources_found
        is_other = "other" in sources_found
        
        # Heuristic for movable
        # If it's a hero or unit, it's likely movable. 
        # But buildings are definitely not. 
        # If something is BOTH unit and building (unlikely but possible in dataset overlaps?), treat as building regarding movability?
        # Requirement: "heroes true; buildings false; other false; units true"
        # We can just OR them or prioritize. 
        # If is_building is true, is_movable should be false?
        # Let's stick to the requested simple heuristic:
        # "heroes true; buildings false; other false; units true"
        # Determine mostly by the Primary Source? Or logical OR/AND?
        # A Hero Building? 
        # Let's use: True if (is_hero or is_unit) AND not is_building. 
        # Because a building should never be movable unless it's a "packed" unit which is weird.
        # Simple implementation based on prompt:
        
        # Prompt says: "heroes true; buildings false; other false; units true"
        # This implies standard defaults. If checks conflict, we need a rule.
        # "buildings false" overrides "units true" (e.g. maybe a static unit?).
        
        if is_building:
            is_movable = False
        elif is_hero or is_unit:
            is_movable = True
        else:
            is_movable = False # other
            
        # Aliases & Issues
        aliases = []
        issues = []
        
        uni_names = list(set(name_candidates.values()))
        if len(uni_names) > 1:
            issues.append(f"Name conflict: {name_candidates}")
            # Add non-primary names to aliases
            for name in uni_names:
                if name != primary_name:
                    aliases.append(name)
        
        # Construct Record
        record = {
            "genie_id": gid,
            "name": primary_name,
            "sources": sources_found,
            "facets": {
                "is_unit_dataset": is_unit,
                "is_hero": is_hero,
                "is_building": is_building,
                "is_other": is_other,
                "is_movable": is_movable
            },
            "aliases": sorted(aliases),
            "issues": sorted(issues)
        }
        registry.append(record)
        
    return registry
