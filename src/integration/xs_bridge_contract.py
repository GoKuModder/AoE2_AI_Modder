from __future__ import annotations

from typing import Mapping, TypedDict


class BridgePayload(TypedDict):
    target_player: int
    mode: int
    switch_pulse: int


_BRIDGE_VAR_IDS: BridgePayload = {
    "target_player": 50,
    "mode": 51,
    "switch_pulse": 52,
}

_PAYLOAD_KEYS = tuple(_BRIDGE_VAR_IDS.keys())


class BridgeContractError(ValueError):
    def __init__(self) -> None:
        super().__init__("bridge_contract_error")


def bridge_variable_ids() -> BridgePayload:
    return dict(_BRIDGE_VAR_IDS)


def validate_bridge_payload(payload: Mapping[str, object]) -> BridgePayload:
    if not isinstance(payload, Mapping):
        raise BridgeContractError()

    keys = set(payload.keys())
    expected = set(_PAYLOAD_KEYS)
    if keys != expected:
        raise BridgeContractError()

    normalized: BridgePayload = {
        "target_player": _require_int(payload["target_player"]),
        "mode": _require_int(payload["mode"]),
        "switch_pulse": _require_int(payload["switch_pulse"]),
    }
    return normalized


def build_bridge_trigger_update_snippet(payload: Mapping[str, object]) -> str:
    validated = validate_bridge_payload(payload)
    lines = []
    for key in _PAYLOAD_KEYS:
        lines.append(f"xsSetTriggerVariable({_BRIDGE_VAR_IDS[key]}, {validated[key]});")
    return "\n".join(lines) + "\n"


def _require_int(value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise BridgeContractError()
    return value
