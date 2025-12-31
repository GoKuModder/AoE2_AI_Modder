from typing import Any, Dict, List
import inspect
import pkgutil
import importlib
import re

def introspect_aoe2sp_effects() -> Dict[str, Any]:
    """
    Introspects AoE2ScenarioParser NewEffectSupport to obtain methods + signatures.
    """
    try:
        from AoE2ScenarioParser.objects.support.new_effect import NewEffectSupport  # type: ignore
    except ImportError as e:
        raise RuntimeError(
            "Could not import AoE2ScenarioParser. Ensure your venv/interpreter is set correctly."
        ) from e

    methods: Dict[str, Any] = {}
    for name, fn in inspect.getmembers(NewEffectSupport, predicate=inspect.isfunction):
        if name.startswith("_"):
            continue
        sig_obj = inspect.signature(fn)
        sig = str(sig_obj)
        params = []
        for p in sig_obj.parameters.values():
            if p.name == "self":
                continue
            
            # Extract type annotation if available
            type_str = ""
            if p.annotation != inspect.Parameter.empty:
                # Handle string annotations vs type objects
                if isinstance(p.annotation, str):
                    type_str = p.annotation
                else:
                    try:
                        type_str = p.annotation.__name__
                    except AttributeError:
                        type_str = str(p.annotation)

            params.append({
                "name": p.name,
                "type": type_str,
                "default": str(p.default) if p.default != inspect.Parameter.empty else None
            })

        methods[name] = {"name": name, "signature": f"{name}{sig}", "params": params}
    return methods


def introspect_object_attributes_enum() -> Dict[int, str]:
    """
    Introspects AoE2ScenarioParser ObjectAttribute enum to obtain {value: name} mapping.
    """
    try:
        from AoE2ScenarioParser.datasets.trigger_lists.object_attribute import ObjectAttribute  # type: ignore
    except ImportError as e:
        raise RuntimeError(
            "Could not import AoE2ScenarioParser.datasets.trigger_lists.object_attribute.ObjectAttribute. "
            "Ensure your venv/interpreter is set correctly."
        ) from e

    # Extract enum members: value -> name
    # e.g. 0 -> "HIT_POINTS"
    return {member.value: member.name for member in ObjectAttribute}


def introspect_genie_datasets() -> Dict[str, Dict[int, str]]:
    """
    Returns a dictionary of datasets:
    {
        "units": {id: name, ...},
        "heroes": {id: name, ...},
        "buildings": {id: name, ...},
        "other": {id: name, ...}
    }
    """
    try:
        from AoE2ScenarioParser.datasets.units import UnitInfo
        from AoE2ScenarioParser.datasets.heroes import HeroInfo
        from AoE2ScenarioParser.datasets.buildings import BuildingInfo
        from AoE2ScenarioParser.datasets.other import OtherInfo
    except ImportError as e:
        raise RuntimeError(
            "Could not import AoE2ScenarioParser datasets (UnitInfo, HeroInfo, etc.). "
            "Ensure your venv/interpreter is set correctly."
        ) from e

    def _extract(enum_cls) -> Dict[int, str]:
        # Value tuple format: (ID, ...) - we assume index 0 is always ID
        return {m.value[0]: m.name for m in enum_cls}

    return {
        "units": _extract(UnitInfo),
        "heroes": _extract(HeroInfo),
        "buildings": _extract(BuildingInfo),
        "other": _extract(OtherInfo),
    }

def introspect_dataset_dependencies() -> Dict[str, List[Dict[str, str]]]:
    """
    Introspects AoE2ScenarioParser.datasets.trigger_lists to find datasets 
    that are linked to specific effects via their docstrings.
    
    Returns:
        Dict[EffectNameURI, List[DatasetInfo]]
        e.g. {"change_color_mood": [{"name": "ColorMood", "module": "color_mood"}]}
        
        EffectName is simplified to match UGC URI/Method usage (lowercase, underscores).
    """
    try:
        import AoE2ScenarioParser.datasets.trigger_lists as tl
    except ImportError as e:
        raise RuntimeError("Could not import AoE2ScenarioParser.datasets.trigger_lists") from e

    dependencies = {}

    for _, mod_name, _ in pkgutil.iter_modules(tl.__path__):
        try:
            full_mod_name = f"AoE2ScenarioParser.datasets.trigger_lists.{mod_name}"
            module = importlib.import_module(full_mod_name)
            
            # Inspect classes in the module
            for cls_name, cls_obj in inspect.getmembers(module, inspect.isclass):
                doc = inspect.getdoc(cls_obj)
                if doc:
                    # Heuristic parsing for "Used in the 'X' effect"
                    # Normalize docstring whitespace globally to handle line breaks in the middle of phrases
                    doc_norm = re.sub(r'\s+', ' ', doc)
                    lower_doc = doc_norm.lower()
                    
                    if "used in the '" in lower_doc:
                        start_idx = lower_doc.find("used in the '") + len("used in the '")
                        end_idx = lower_doc.find("'", start_idx)
                        if end_idx != -1:
                            effect_name = doc_norm[start_idx:end_idx].strip()
                            effect_key = effect_name.lower().replace(" ", "_")
                            
                            if effect_key not in dependencies:
                                dependencies[effect_key] = []
                            
                            dependencies[effect_key].append({
                                "name": cls_name,
                                "module": mod_name
                            })
                            
        except Exception:
            # Skip modules that fail to import or parse
            continue
            
    return dependencies
