from typing import Any, Dict
import inspect

def introspect_aoe2sp_effects() -> Dict[str, Any]:
    """
    Introspects AoE2ScenarioParser NewEffectSupport to obtain methods + signatures.
    """
    try:
        from AoE2ScenarioParser.objects.support.new_effect import NewEffectSupport  # type: ignore
    except ImportError as e:
        # Fallback/Mock for environments without the library (like this agent environment)
        # In a real run, this would raise. For strictly separating logic, we might want to fail hard,
        # but to allow "build effects" to run even here, we might return empty or mock if the user allows.
        # User constraint: "Parser API reality is the source of truth."
        # So we must fail if missing.
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
