import unittest

from src.integration.xs_injector import (
    build_array_create_and_get_snippet,
    inject_xs_code,
    make_xs_array_create_statement,
    make_xs_array_get_statement,
)


class TestXsInjector(unittest.TestCase):
    def test_make_create_statement_int(self):
        line = make_xs_array_create_statement(
            array_id_var="aHeroIds",
            array_type="int",
            size=8,
            default_value=-1,
            debug_name="hero_ids",
        )
        self.assertEqual(line, 'aHeroIds = xsArrayCreateInt(8, -1, "hero_ids");')

    def test_make_get_statement_vector(self):
        line = make_xs_array_get_statement(
            out_var="heroPos",
            array_type="vector",
            array_id_var="aHeroPos",
            index_expr="i",
        )
        self.assertEqual(line, "heroPos = xsArrayGetVector(aHeroPos, i);")

    def test_inject_append(self):
        base = "rule a\nactive\n{\n}\n"
        updated = inject_xs_code(base, "int x = 0;")
        self.assertIn("int x = 0;", updated)

    def test_inject_marker(self):
        base = "int x = 0;\n// MARKER\nrule a\nactive\n{\n}\n"
        updated = inject_xs_code(base, "int y = 1;", marker="MARKER")
        self.assertIn("// MARKER\nint y = 1;\nrule a", updated)

    def test_build_create_and_get_snippet(self):
        snippet = build_array_create_and_get_snippet(
            array_id_var="aInjected",
            value_var="val",
            array_type="int",
            size=4,
            default_value=0,
            debug_name="inj",
            index_expr="0",
        )
        self.assertIn('aInjected = xsArrayCreateInt(4, 0, "inj");', snippet)
        self.assertIn("val = xsArrayGetInt(aInjected, 0);", snippet)


if __name__ == "__main__":
    unittest.main()
