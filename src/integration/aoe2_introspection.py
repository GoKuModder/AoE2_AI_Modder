from typing import Any, Dict
import inspect

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
        sig = str(inspect.signature(fn))
        params = [p.name for p in inspect.signature(fn).parameters.values() if p.name != "self"]
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
