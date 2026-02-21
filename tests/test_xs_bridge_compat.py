import unittest
from pathlib import Path

from src.integration.xs_bridge_contract import (
    BridgeContractError,
    bridge_variable_ids,
    build_bridge_trigger_update_snippet,
)


class TestXsBridgeCompat(unittest.TestCase):
    def test_bridge_variable_ids_snapshot(self):
        self.assertEqual(
            {
                "target_player": 50,
                "mode": 51,
                "switch_pulse": 52,
            },
            bridge_variable_ids(),
        )

    def test_bridge_variable_ids_match_xs_script(self):
        xs_path = Path("AI_Scripting/rpg_xs_bridge_v3.xs")
        source = xs_path.read_text(encoding="utf-8", errors="replace")
        var_ids = bridge_variable_ids()
        self.assertIn(f"int cVarTargetPlayer = {var_ids['target_player']};", source)
        self.assertIn(f"int cVarMode = {var_ids['mode']};", source)
        self.assertIn(f"int cVarSwitchPulse = {var_ids['switch_pulse']};", source)

    def test_build_trigger_update_snippet_snapshot(self):
        snippet = build_bridge_trigger_update_snippet(
            {
                "target_player": 2,
                "mode": 1,
                "switch_pulse": 42,
            }
        )
        self.assertEqual(
            "xsSetTriggerVariable(50, 2);\n"
            "xsSetTriggerVariable(51, 1);\n"
            "xsSetTriggerVariable(52, 42);\n",
            snippet,
        )

    def test_invalid_payload_raises_bridge_contract_error(self):
        with self.assertRaises(BridgeContractError) as ctx:
            build_bridge_trigger_update_snippet({"target_player": 2, "mode": 1})
        self.assertEqual("bridge_contract_error", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
