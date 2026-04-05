import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class TestAgentDocs(unittest.TestCase):
    def setUp(self):
        self.required_docs = [
            ROOT / "AGENT_START_HERE.md",
            ROOT / "docs" / "README.md",
            ROOT / "docs" / "agent" / "README.md",
            ROOT / "docs" / "agent" / "scenario_builder" / "README.md",
            ROOT / "docs" / "agent" / "scenario_builder" / "WHERE_TO_FIND_THINGS.md",
            ROOT / "docs" / "agent" / "scenario_builder" / "TRIGGER_LOOKUP_INDEX.md",
            ROOT / "docs" / "agent" / "scenario_builder" / "PARSER_MANAGERS_GUIDE.md",
            ROOT / "docs" / "agent" / "scenario_builder" / "XS_PROJECT_FILES_GUIDE.md",
            ROOT / "docs" / "agent" / "scenario_builder" / "GENIE_WORKFLOW_GUIDE.md",
            ROOT / "docs" / "agent" / "scenario_builder" / "DAT_LOOKUP_INDEX.md",
            ROOT / "docs" / "agent" / "scenario_builder" / "MAP_IDEA_TO_IMPLEMENTATION.md",
            ROOT / "examples" / "README.md",
            ROOT / "examples" / "xs" / "README.md",
            ROOT / "docs" / "agent" / "navigation" / "KNOWLEDGE_MAP.md",
            ROOT / "docs" / "agent" / "navigation" / "RETRIEVAL_RULES.md",
            ROOT / "docs" / "agent" / "navigation" / "CROSS_DOMAIN_WORKFLOWS.md",
            ROOT / "docs" / "agent" / "references" / "REFERENCE_PROJECTS.md",
            ROOT / "docs" / "agent" / "references" / "patterns" / "README.md",
            ROOT / "docs" / "agent" / "references" / "recipes" / "README.md",
            ROOT / "docs" / "agent" / "domains" / "XS_AGENT_GUIDE.md",
            ROOT / "docs" / "agent" / "domains" / "AI_SCRIPT_AGENT_GUIDE.md",
            ROOT / "docs" / "agent" / "domains" / "TRIGGER_AGENT_GUIDE.md",
            ROOT / "docs" / "agent" / "domains" / "TRIGGER_CONDITIONS_EFFECTS_GUIDE.md",
            ROOT / "docs" / "agent" / "domains" / "DAT_AGENT_GUIDE.md",
            ROOT / "docs" / "agent_database" / "genie_dat_concepts.json",
            ROOT / "docs" / "agent" / "routing" / "knowledge_map.json",
            ROOT / "docs" / "agent" / "routing" / "query_router.json",
            ROOT / "docs" / "agent" / "references" / "reference_projects.json",
            ROOT / "docs" / "agent" / "references" / "patterns" / "trigger_xs_patterns.json",
            ROOT / "docs" / "agent" / "references" / "patterns" / "genie_workflow_patterns.json",
            ROOT / "docs" / "agent" / "references" / "patterns" / "reference_patterns_eval.json",
            ROOT / "docs" / "agent" / "references" / "recipes" / "scenario_recipes.json",
            ROOT / "docs" / "agent" / "references" / "recipes" / "parser_manager_patterns.json",
            ROOT / "docs" / "agent" / "references" / "recipes" / "genie_recipes.json",
            ROOT / "docs" / "agent" / "references" / "recipes" / "reference_recipes_eval.json",
            ROOT / "docs" / "agent" / "routing" / "agent_query_map.json",
            ROOT / "docs" / "trigger_knowledge" / "conditions_knowledge.json",
            ROOT / "docs" / "trigger_knowledge" / "condition_usage_playbook.md",
            ROOT / "docs" / "trigger_knowledge" / "effect_usage_playbook.md",
            ROOT / "docs" / "trigger_knowledge" / "condition_usage_playbook.json",
            ROOT / "docs" / "trigger_knowledge" / "effect_usage_playbook.json",
            ROOT / "docs" / "trigger_knowledge" / "condition_project_usage.json",
            ROOT / "docs" / "trigger_knowledge" / "effect_project_usage.json",
            ROOT / "docs" / "trigger_knowledge" / "project_usage_knowledge.md",
        ]
        self.readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.agent_start = (ROOT / "AGENT_START_HERE.md").read_text(encoding="utf-8")
        self.knowledge_map_md = (
            ROOT / "docs" / "agent" / "navigation" / "KNOWLEDGE_MAP.md"
        ).read_text(
            encoding="utf-8"
        )

    def test_required_agent_docs_exist(self):
        for path in self.required_docs:
            self.assertTrue(path.exists(), f"Missing required agent-facing file: {path}")

    def test_readme_references_main_agent_entrypoints(self):
        self.assertIn("AGENT_START_HERE.md", self.readme)
        self.assertIn("docs/README.md", self.readme)
        self.assertIn("docs/agent/README.md", self.readme)
        self.assertIn("docs/agent/scenario_builder/README.md", self.readme)
        self.assertIn("docs/agent/scenario_builder/WHERE_TO_FIND_THINGS.md", self.readme)
        self.assertIn("docs/agent/scenario_builder/TRIGGER_LOOKUP_INDEX.md", self.readme)
        self.assertIn("docs/agent/scenario_builder/PARSER_MANAGERS_GUIDE.md", self.readme)
        self.assertIn("docs/agent/scenario_builder/XS_PROJECT_FILES_GUIDE.md", self.readme)
        self.assertIn("docs/agent/scenario_builder/GENIE_WORKFLOW_GUIDE.md", self.readme)
        self.assertIn("docs/agent/scenario_builder/DAT_LOOKUP_INDEX.md", self.readme)
        self.assertIn("docs/agent/scenario_builder/MAP_IDEA_TO_IMPLEMENTATION.md", self.readme)
        self.assertIn("examples/xs/README.md", self.readme)
        self.assertIn("docs/agent/navigation/KNOWLEDGE_MAP.md", self.readme)
        self.assertIn("docs/agent/navigation/RETRIEVAL_RULES.md", self.readme)
        self.assertIn("docs/agent/navigation/CROSS_DOMAIN_WORKFLOWS.md", self.readme)
        self.assertIn("docs/agent/references/REFERENCE_PROJECTS.md", self.readme)
        self.assertIn("docs/agent/references/patterns/README.md", self.readme)
        self.assertIn("docs/agent/references/recipes/README.md", self.readme)
        self.assertIn("docs/agent/references/recipes/scenario_recipes.json", self.readme)
        self.assertIn("docs/agent/references/recipes/parser_manager_patterns.json", self.readme)
        self.assertIn("docs/agent/references/recipes/genie_recipes.json", self.readme)
        self.assertIn("docs/agent_database/genie_dat_concepts.json", self.readme)
        self.assertIn("docs/agent/routing/agent_query_map.json", self.readme)
        self.assertIn("docs/agent/domains/TRIGGER_CONDITIONS_EFFECTS_GUIDE.md", self.readme)
        self.assertIn("docs/trigger_knowledge/conditions_knowledge.json", self.readme)
        self.assertIn("docs/trigger_knowledge/condition_usage_playbook.md", self.readme)
        self.assertIn("docs/trigger_knowledge/effect_usage_playbook.md", self.readme)
        self.assertIn("docs/trigger_knowledge/condition_usage_playbook.json", self.readme)
        self.assertIn("docs/trigger_knowledge/effect_usage_playbook.json", self.readme)
        self.assertIn("docs/trigger_knowledge/condition_project_usage.json", self.readme)
        self.assertIn("docs/trigger_knowledge/effect_project_usage.json", self.readme)

    def test_agent_start_references_domain_guides(self):
        for path_text in (
            "docs/agent/domains/XS_AGENT_GUIDE.md",
            "docs/agent/domains/AI_SCRIPT_AGENT_GUIDE.md",
            "docs/agent/domains/TRIGGER_AGENT_GUIDE.md",
            "docs/agent/domains/TRIGGER_CONDITIONS_EFFECTS_GUIDE.md",
            "docs/agent/domains/DAT_AGENT_GUIDE.md",
            "docs/README.md",
            "docs/agent/README.md",
            "docs/agent/scenario_builder/README.md",
            "docs/agent/scenario_builder/WHERE_TO_FIND_THINGS.md",
            "docs/agent/scenario_builder/TRIGGER_LOOKUP_INDEX.md",
            "docs/agent/scenario_builder/PARSER_MANAGERS_GUIDE.md",
            "docs/agent/scenario_builder/XS_PROJECT_FILES_GUIDE.md",
            "docs/agent/scenario_builder/GENIE_WORKFLOW_GUIDE.md",
            "docs/agent/scenario_builder/DAT_LOOKUP_INDEX.md",
            "docs/agent/scenario_builder/MAP_IDEA_TO_IMPLEMENTATION.md",
            "examples/xs/README.md",
            "docs/agent/routing/knowledge_map.json",
            "docs/agent/routing/query_router.json",
            "docs/agent/routing/agent_query_map.json",
            "docs/agent_database/genie_dat_concepts.json",
            "docs/trigger_knowledge/condition_usage_playbook.json",
            "docs/trigger_knowledge/effect_usage_playbook.json",
            "docs/trigger_knowledge/conditions_knowledge.json",
            "docs/trigger_knowledge/effects_knowledge.json",
            "docs/trigger_knowledge/condition_project_usage.json",
            "docs/trigger_knowledge/effect_project_usage.json",
            "docs/agent/references/REFERENCE_PROJECTS.md",
            "docs/agent/references/reference_projects.json",
            "docs/agent/references/patterns/README.md",
            "docs/agent/references/patterns/trigger_xs_patterns.json",
            "docs/agent/references/patterns/genie_workflow_patterns.json",
            "docs/agent/references/recipes/README.md",
            "docs/agent/references/recipes/scenario_recipes.json",
            "docs/agent/references/recipes/parser_manager_patterns.json",
            "docs/agent/references/recipes/genie_recipes.json",
        ):
            self.assertIn(path_text, self.agent_start)

    def test_core_domain_terms_appear_in_main_docs(self):
        required_terms = ("xs", "ai scripts", "scenario triggers", ".dat/genie tooling")
        for text in (
            self.readme.lower(),
            self.agent_start.lower(),
            self.knowledge_map_md.lower(),
        ):
            for term in required_terms:
                self.assertIn(term, text)

    def test_trigger_guide_keeps_architecture_topics(self):
        trigger_guide = (
            ROOT / "docs" / "agent" / "domains" / "TRIGGER_AGENT_GUIDE.md"
        ).read_text(encoding="utf-8").lower()
        required_terms = (
            "modular",
            "data-driven",
            "balancing",
            "apply_",
            "aoe_variables",
            "dictionary.py",
            "xs variables",
        )
        for term in required_terms:
            self.assertIn(term, trigger_guide)

    def test_trigger_conditions_effects_guide_mentions_usage_and_reference_projects(self):
        guide = (
            ROOT / "docs" / "agent" / "domains" / "TRIGGER_CONDITIONS_EFFECTS_GUIDE.md"
        ).read_text(encoding="utf-8").lower()
        required_terms = (
            "condition_usage_playbook.md",
            "effect_usage_playbook.md",
            "conditions_knowledge.json",
            "effects_knowledge.json",
            "condition_project_usage.json",
            "effect_project_usage.json",
            "display_timer",
            "display_instructions",
            "send_chat",
            "change_view",
            "lordsofdiplomacy - easy mode",
            "goku rpg project",
            "hide_and_seek",
        )
        for term in required_terms:
            self.assertIn(term, guide)

    def test_dat_guide_keeps_architecture_topics(self):
        dat_guide = (
            ROOT / "docs" / "agent" / "domains" / "DAT_AGENT_GUIDE.md"
        ).read_text(encoding="utf-8").lower()
        required_terms = (
            "modular",
            "apply_",
            "workspace",
            "genieworkspace",
            "graphic_manager",
            "sound_manager",
            "tech_manager",
            "civ_manager",
            "genie_dat_concepts.json",
            "genie_dat_retriever.py",
            "data-driven",
            "config/ids.py",
            "json",
            "balancing",
        )
        for term in required_terms:
            self.assertIn(term, dat_guide)

    def test_xs_guide_mentions_curated_examples(self):
        xs_guide = (
            ROOT / "docs" / "agent" / "domains" / "XS_AGENT_GUIDE.md"
        ).read_text(encoding="utf-8").lower()
        required_terms = (
            "examples/xs/",
            "practical xs example",
            "examples/xs/readme.md",
            "extern int",
            "xstriggervariable",
            "xssettriggervariable",
            "output destination",
            "ask the user where the generated `.xs` file should be placed",
        )
        for term in required_terms:
            self.assertIn(term, xs_guide)

    def test_retrieval_rules_cover_generated_xs_output_guidance(self):
        retrieval_rules = (
            ROOT / "docs" / "agent" / "navigation" / "RETRIEVAL_RULES.md"
        ).read_text(encoding="utf-8").lower()
        required_terms = (
            "ask the user for the output location",
            "machine-specific absolute paths",
            "hardcoded xs output path",
        )
        for term in required_terms:
            self.assertIn(term, retrieval_rules)

    def test_scenario_builder_where_to_find_things_is_explicit(self):
        where_to_find = (
            ROOT / "docs" / "agent" / "scenario_builder" / "WHERE_TO_FIND_THINGS.md"
        ).read_text(encoding="utf-8").lower()
        required_terms = (
            "where are conditions",
            "where are effects",
            "unitmanager",
            "mapmanager",
            "dat_lookup_index.md",
            "genie_dat_concepts.json",
            "xs project files guide",
            "map idea to implementation",
            "scenario_recipes.json",
            "parser_manager_patterns.json",
            "genie_recipes.json",
        )
        for term in required_terms:
            self.assertIn(term, where_to_find)

    def test_parser_managers_guide_covers_unit_and_map_manager(self):
        parser_guide = (
            ROOT / "docs" / "agent" / "scenario_builder" / "PARSER_MANAGERS_GUIDE.md"
        ).read_text(encoding="utf-8").lower()
        required_terms = (
            "unitmanager",
            "mapmanager",
            "add_unit",
            "get_units_in_area",
            "filter_units_by_const",
            "change_ownership",
            "get_square_2d",
            "terrain",
        )
        for term in required_terms:
            self.assertIn(term, parser_guide)

    def test_map_idea_workflow_mentions_registry_layers_and_managers(self):
        workflow = (
            ROOT / "docs" / "agent" / "scenario_builder" / "MAP_IDEA_TO_IMPLEMENTATION.md"
        ).read_text(encoding="utf-8").lower()
        required_terms = (
            "aoe_variables",
            "unitmanager",
            "mapmanager",
            "xs",
            ".dat/genie tooling",
            "dictionary.py",
            "ask the user where to place the generated `.xs`",
            "scenario_recipes.json",
            "parser_manager_patterns.json",
            "genie_recipes.json",
        )
        for term in required_terms:
            self.assertIn(term, workflow)

    def test_genie_workflow_guide_covers_workspace_managers_and_linking(self):
        genie_guide = (
            ROOT / "docs" / "agent" / "scenario_builder" / "GENIE_WORKFLOW_GUIDE.md"
        ).read_text(encoding="utf-8").lower()
        required_terms = (
            "genieworkspace",
            "unit_manager",
            "graphic_manager",
            "sound_manager",
            "tech_manager",
            "civ_manager",
            "standing_sprite_id1",
            "link_components.py",
            "dat_lookup_index.md",
            "genie_dat_concepts.json",
            "ask the user where the modified `.dat` should be written",
        )
        for term in required_terms:
            self.assertIn(term, genie_guide)

    def test_recipe_readme_explains_low_token_goal(self):
        recipes_readme = (
            ROOT / "docs" / "agent" / "references" / "recipes" / "README.md"
        ).read_text(encoding="utf-8").lower()
        required_terms = (
            "fast rag",
            "compact",
            "low-token",
            "scenario_recipes.json",
            "parser_manager_patterns.json",
            "genie_recipes.json",
        )
        for term in required_terms:
            self.assertIn(term, recipes_readme)


class TestKnowledgeMapJson(unittest.TestCase):
    def setUp(self):
        self.path = ROOT / "docs" / "agent" / "routing" / "knowledge_map.json"
        self.data = json.loads(self.path.read_text(encoding="utf-8"))

    def test_schema_shape(self):
        self.assertEqual(1, self.data.get("version"))
        self.assertIn("domains", self.data)
        self.assertIsInstance(self.data["domains"], list)
        self.assertEqual(4, len(self.data["domains"]))

    def test_domain_entries_have_required_keys(self):
        required_keys = {
            "id",
            "title",
            "summary",
            "open_first",
            "canonical_docs",
            "canonical_data",
            "common_queries",
            "related_domains",
        }
        for entry in self.data["domains"]:
            self.assertTrue(required_keys.issubset(entry.keys()), entry)
            self.assertIsInstance(entry["open_first"], list)
            self.assertGreater(len(entry["open_first"]), 0)
            self.assertIsInstance(entry["canonical_docs"], list)
            self.assertIsInstance(entry["canonical_data"], list)
            self.assertIsInstance(entry["common_queries"], list)
            self.assertIsInstance(entry["related_domains"], list)

    def test_expected_domain_ids_present(self):
        ids = {entry["id"] for entry in self.data["domains"]}
        self.assertEqual(
            {"xs", "ai_scripts", "scenario_triggers", "dat_genie_tooling"},
            ids,
        )

    def test_all_open_first_paths_exist(self):
        for entry in self.data["domains"]:
            for relpath in entry["open_first"]:
                self.assertTrue(
                    (ROOT / relpath).exists(),
                    f"Missing open_first path for {entry['id']}: {relpath}",
                )

    def test_all_canonical_paths_exist(self):
        for entry in self.data["domains"]:
            for key in ("canonical_docs", "canonical_data"):
                for relpath in entry[key]:
                    self.assertTrue(
                        (ROOT / relpath).exists(),
                        f"Missing {key} path for {entry['id']}: {relpath}",
                    )


class TestQueryRouterJson(unittest.TestCase):
    def setUp(self):
        self.path = ROOT / "docs" / "agent" / "routing" / "query_router.json"
        self.data = json.loads(self.path.read_text(encoding="utf-8"))

    def test_schema_shape(self):
        self.assertEqual(1, self.data.get("version"))
        self.assertIn("rules", self.data)
        self.assertIsInstance(self.data["rules"], list)
        self.assertGreater(len(self.data["rules"]), 0)

    def test_rule_entries_have_required_keys(self):
        required_keys = {"query_term", "normalized_term", "target_domains", "priority"}
        for rule in self.data["rules"]:
            self.assertTrue(required_keys.issubset(rule.keys()), rule)
            self.assertIsInstance(rule["query_term"], str)
            self.assertIsInstance(rule["normalized_term"], str)
            self.assertIsInstance(rule["target_domains"], list)
            self.assertGreater(len(rule["target_domains"]), 0)
            self.assertIsInstance(rule["priority"], int)

    def test_router_targets_known_domains(self):
        allowed_domains = {"xs", "ai_scripts", "scenario_triggers", "dat_genie_tooling"}
        for rule in self.data["rules"]:
            self.assertTrue(set(rule["target_domains"]).issubset(allowed_domains), rule)


class TestAgentQueryMapJson(unittest.TestCase):
    def setUp(self):
        self.path = ROOT / "docs" / "agent" / "routing" / "agent_query_map.json"
        self.data = json.loads(self.path.read_text(encoding="utf-8"))

    def test_schema_shape(self):
        self.assertIn("intents", self.data)
        self.assertIsInstance(self.data["intents"], list)
        self.assertGreater(len(self.data["intents"]), 0)

    def test_intent_entries_have_required_keys(self):
        required_keys = {"intent", "dataset_path", "lookup_keys", "fallback_strategy"}
        for entry in self.data["intents"]:
            self.assertTrue(required_keys.issubset(entry.keys()), entry)
            self.assertIsInstance(entry["intent"], str)
            self.assertIsInstance(entry["dataset_path"], str)
            self.assertTrue((ROOT / entry["dataset_path"]).exists(), entry)
            self.assertIsInstance(entry["lookup_keys"], list)
            self.assertGreater(len(entry["lookup_keys"]), 0)
            self.assertIsInstance(entry["fallback_strategy"], str)

    def test_pattern_intents_present(self):
        intents = {entry["intent"] for entry in self.data["intents"]}
        self.assertIn("find_genie_dat_concept", intents)
        self.assertIn("find_trigger_condition", intents)
        self.assertIn("find_trigger_condition_usage", intents)
        self.assertIn("find_trigger_condition_playbook", intents)
        self.assertIn("find_trigger_effect_usage", intents)
        self.assertIn("find_trigger_effect_playbook", intents)
        self.assertIn("find_trigger_xs_pattern", intents)
        self.assertIn("find_genie_workflow_pattern", intents)
        self.assertIn("find_scenario_recipe", intents)
        self.assertIn("find_parser_manager_pattern", intents)
        self.assertIn("find_genie_recipe", intents)


class TestReferenceProjectsJson(unittest.TestCase):
    def setUp(self):
        self.path = ROOT / "docs" / "agent" / "references" / "reference_projects.json"
        self.data = json.loads(self.path.read_text(encoding="utf-8"))

    def test_schema_shape(self):
        self.assertEqual(1, self.data.get("version"))
        self.assertIn("projects", self.data)
        self.assertIsInstance(self.data["projects"], list)
        self.assertEqual(4, len(self.data["projects"]))

    def test_project_entries_have_required_keys(self):
        required_keys = {
            "id",
            "title",
            "path",
            "priority",
            "role",
            "use_for",
            "representative_paths",
            "avoid_for",
        }
        for project in self.data["projects"]:
            self.assertTrue(required_keys.issubset(project.keys()), project)
            self.assertIsInstance(project["id"], str)
            self.assertIsInstance(project["title"], str)
            self.assertIsInstance(project["path"], str)
            self.assertIsInstance(project["priority"], int)
            self.assertIsInstance(project["use_for"], list)
            self.assertGreater(len(project["use_for"]), 0)
            self.assertIsInstance(project["representative_paths"], list)
            self.assertGreater(len(project["representative_paths"]), 0)
            self.assertIsInstance(project["avoid_for"], list)

    def test_expected_reference_projects_present(self):
        ids = {project["id"] for project in self.data["projects"]}
        self.assertEqual(
            {
                "lords_of_diplomacy_easy_mode",
                "goku_rpg_genie_code",
                "goku_rpg_project",
                "hide_and_seek",
            },
            ids,
        )


class TestReferencePatternDatasets(unittest.TestCase):
    def setUp(self):
        self.trigger_path = (
            ROOT / "docs" / "agent" / "references" / "patterns" / "trigger_xs_patterns.json"
        )
        self.genie_path = (
            ROOT / "docs" / "agent" / "references" / "patterns" / "genie_workflow_patterns.json"
        )
        self.trigger_data = json.loads(self.trigger_path.read_text(encoding="utf-8"))
        self.genie_data = json.loads(self.genie_path.read_text(encoding="utf-8"))

    def test_pattern_dataset_schema(self):
        required_keys = {
            "id",
            "title",
            "summary",
            "primary_domains",
            "reference_projects",
            "representative_paths",
            "when_to_use",
            "key_points",
            "query_terms",
            "pitfalls",
        }
        for dataset in (self.trigger_data, self.genie_data):
            self.assertIsInstance(dataset, list)
            self.assertGreater(len(dataset), 0)
            for entry in dataset:
                self.assertTrue(required_keys.issubset(entry.keys()), entry)
                self.assertIsInstance(entry["id"], str)
                self.assertIsInstance(entry["title"], str)
                self.assertIsInstance(entry["primary_domains"], list)
                self.assertGreater(len(entry["primary_domains"]), 0)
                self.assertIsInstance(entry["reference_projects"], list)
                self.assertGreater(len(entry["reference_projects"]), 0)
                self.assertIsInstance(entry["representative_paths"], list)
                self.assertGreater(len(entry["representative_paths"]), 0)
                self.assertIsInstance(entry["query_terms"], list)
                self.assertGreater(len(entry["query_terms"]), 0)

    def test_expected_pattern_ids_present(self):
        trigger_ids = {entry["id"] for entry in self.trigger_data}
        genie_ids = {entry["id"] for entry in self.genie_data}
        self.assertIn("aoe_variables_central_registry", trigger_ids)
        self.assertIn("dictionary_balance_layer", trigger_ids)
        self.assertIn("xs_file_generation_pipeline", trigger_ids)
        self.assertIn("xs_output_path_configuration", trigger_ids)
        self.assertIn("genie_workspace_orchestrator", genie_ids)
        self.assertIn("genie_template_copy_and_link", genie_ids)
        self.assertIn("genie_manager_asset_ownership", genie_ids)
        self.assertIn("genie_component_linking_workflow", genie_ids)
        self.assertIn("genie_output_path_configuration", genie_ids)


class TestReferenceRecipeDatasets(unittest.TestCase):
    def setUp(self):
        self.scenario_path = (
            ROOT / "docs" / "agent" / "references" / "recipes" / "scenario_recipes.json"
        )
        self.parser_path = (
            ROOT / "docs" / "agent" / "references" / "recipes" / "parser_manager_patterns.json"
        )
        self.genie_path = (
            ROOT / "docs" / "agent" / "references" / "recipes" / "genie_recipes.json"
        )
        self.scenario_data = json.loads(self.scenario_path.read_text(encoding="utf-8"))
        self.parser_data = json.loads(self.parser_path.read_text(encoding="utf-8"))
        self.genie_data = json.loads(self.genie_path.read_text(encoding="utf-8"))

    def test_recipe_dataset_schema(self):
        required_keys = {
            "id",
            "title",
            "summary",
            "primary_domains",
            "reference_projects",
            "when_to_use",
            "steps",
            "best_files",
            "query_terms",
            "pitfalls",
        }
        for dataset in (self.scenario_data, self.parser_data, self.genie_data):
            self.assertIsInstance(dataset, list)
            self.assertGreater(len(dataset), 0)
            for entry in dataset:
                self.assertTrue(required_keys.issubset(entry.keys()), entry)
                self.assertIsInstance(entry["id"], str)
                self.assertIsInstance(entry["title"], str)
                self.assertIsInstance(entry["primary_domains"], list)
                self.assertGreater(len(entry["primary_domains"]), 0)
                self.assertIsInstance(entry["reference_projects"], list)
                self.assertGreater(len(entry["reference_projects"]), 0)
                self.assertIsInstance(entry["steps"], list)
                self.assertGreater(len(entry["steps"]), 0)
                self.assertIsInstance(entry["best_files"], list)
                self.assertGreater(len(entry["best_files"]), 0)

    def test_expected_recipe_ids_present(self):
        scenario_ids = {entry["id"] for entry in self.scenario_data}
        parser_ids = {entry["id"] for entry in self.parser_data}
        genie_ids = {entry["id"] for entry in self.genie_data}
        self.assertIn("quest_system_flow", scenario_ids)
        self.assertIn("teleport_system", scenario_ids)
        self.assertIn("unit_manager_cleanup_regions", parser_ids)
        self.assertIn("map_manager_terrain_scan", parser_ids)
        self.assertIn("create_unit_with_linked_graphic", genie_ids)
        self.assertIn("link_main_and_dead_units", genie_ids)


class TestReferenceRecipesEvalJson(unittest.TestCase):
    def setUp(self):
        self.path = (
            ROOT / "docs" / "agent" / "references" / "recipes" / "reference_recipes_eval.json"
        )
        self.data = json.loads(self.path.read_text(encoding="utf-8"))

    def test_schema_shape(self):
        self.assertEqual(1, self.data.get("schema_version"))
        self.assertIn("cases", self.data)
        self.assertIsInstance(self.data["cases"], list)
        self.assertGreater(len(self.data["cases"]), 0)

    def test_cases_have_required_keys(self):
        for case in self.data["cases"]:
            self.assertTrue({"id", "query", "expected_any"}.issubset(case.keys()), case)
            self.assertIsInstance(case["id"], str)
            self.assertIsInstance(case["query"], str)
            self.assertIsInstance(case["expected_any"], list)
            self.assertGreater(len(case["expected_any"]), 0)


class TestReferencePatternsEvalJson(unittest.TestCase):
    def setUp(self):
        self.path = (
            ROOT / "docs" / "agent" / "references" / "patterns" / "reference_patterns_eval.json"
        )
        self.data = json.loads(self.path.read_text(encoding="utf-8"))

    def test_schema_shape(self):
        self.assertEqual(1, self.data.get("schema_version"))
        self.assertIn("cases", self.data)
        self.assertIsInstance(self.data["cases"], list)
        self.assertGreater(len(self.data["cases"]), 0)

    def test_cases_have_required_keys(self):
        for case in self.data["cases"]:
            self.assertTrue({"id", "query", "expected_any"}.issubset(case.keys()), case)
            self.assertIsInstance(case["id"], str)
            self.assertIsInstance(case["query"], str)
            self.assertIsInstance(case["expected_any"], list)
            self.assertGreater(len(case["expected_any"]), 0)


class TestDatabaseManifestEntries(unittest.TestCase):
    def setUp(self):
        self.path = ROOT / "docs" / "agent_database" / "database_manifest.json"
        self.data = json.loads(self.path.read_text(encoding="utf-8"))

    def test_pattern_datasets_present(self):
        entries = {entry["dataset_id"]: entry for entry in self.data}
        self.assertIn("trigger_conditions", entries)
        self.assertIn("trigger_condition_usage", entries)
        self.assertIn("trigger_condition_playbook", entries)
        self.assertIn("trigger_effect_usage", entries)
        self.assertIn("trigger_effect_playbook", entries)
        self.assertIn("genie_dat_concepts", entries)
        self.assertIn("trigger_xs_patterns", entries)
        self.assertIn("genie_workflow_patterns", entries)
        self.assertIn("scenario_recipes", entries)
        self.assertIn("parser_manager_patterns", entries)
        self.assertIn("genie_recipes", entries)

    def test_pattern_dataset_record_counts_match_files(self):
        entries = {entry["dataset_id"]: entry for entry in self.data}
        conditions_data = json.loads(
            (
                ROOT
                / "docs"
                / "trigger_knowledge"
                / "conditions_knowledge.json"
            ).read_text(encoding="utf-8")
        )
        condition_usage = json.loads(
            (
                ROOT
                / "docs"
                / "trigger_knowledge"
                / "condition_project_usage.json"
            ).read_text(encoding="utf-8")
        )
        condition_playbook = json.loads(
            (
                ROOT
                / "docs"
                / "trigger_knowledge"
                / "condition_usage_playbook.json"
            ).read_text(encoding="utf-8")
        )
        effect_usage = json.loads(
            (
                ROOT
                / "docs"
                / "trigger_knowledge"
                / "effect_project_usage.json"
            ).read_text(encoding="utf-8")
        )
        effect_playbook = json.loads(
            (
                ROOT
                / "docs"
                / "trigger_knowledge"
                / "effect_usage_playbook.json"
            ).read_text(encoding="utf-8")
        )
        genie_concepts = json.loads(
            (
                ROOT
                / "docs"
                / "agent_database"
                / "genie_dat_concepts.json"
            ).read_text(encoding="utf-8")
        )
        trigger_data = json.loads(
            (
                ROOT
                / "docs"
                / "agent"
                / "references"
                / "patterns"
                / "trigger_xs_patterns.json"
            ).read_text(encoding="utf-8")
        )
        genie_data = json.loads(
            (
                ROOT
                / "docs"
                / "agent"
                / "references"
                / "patterns"
                / "genie_workflow_patterns.json"
            ).read_text(encoding="utf-8")
        )
        scenario_recipes = json.loads(
            (
                ROOT
                / "docs"
                / "agent"
                / "references"
                / "recipes"
                / "scenario_recipes.json"
            ).read_text(encoding="utf-8")
        )
        parser_patterns = json.loads(
            (
                ROOT
                / "docs"
                / "agent"
                / "references"
                / "recipes"
                / "parser_manager_patterns.json"
            ).read_text(encoding="utf-8")
        )
        genie_recipes = json.loads(
            (
                ROOT
                / "docs"
                / "agent"
                / "references"
                / "recipes"
                / "genie_recipes.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(41, len(conditions_data))
        self.assertEqual(41, len(condition_usage))
        self.assertEqual(41, len(condition_playbook))
        self.assertEqual(102, len(effect_usage))
        self.assertEqual(102, len(effect_playbook))
        self.assertEqual(12, len(genie_concepts))
        self.assertEqual(8, len(trigger_data))
        self.assertEqual(10, len(genie_data))
        self.assertEqual(18, len(scenario_recipes))
        self.assertEqual(6, len(parser_patterns))
        self.assertEqual(16, len(genie_recipes))
        self.assertEqual(len(conditions_data), entries["trigger_conditions"]["record_count"])
        self.assertEqual(
            len(condition_usage),
            entries["trigger_condition_usage"]["record_count"],
        )
        self.assertEqual(
            len(condition_playbook),
            entries["trigger_condition_playbook"]["record_count"],
        )
        self.assertEqual(
            len(effect_usage),
            entries["trigger_effect_usage"]["record_count"],
        )
        self.assertEqual(
            len(effect_playbook),
            entries["trigger_effect_playbook"]["record_count"],
        )
        self.assertEqual(len(genie_concepts), entries["genie_dat_concepts"]["record_count"])
        self.assertEqual(len(trigger_data), entries["trigger_xs_patterns"]["record_count"])
        self.assertEqual(len(genie_data), entries["genie_workflow_patterns"]["record_count"])
        self.assertEqual(len(scenario_recipes), entries["scenario_recipes"]["record_count"])
        self.assertEqual(len(parser_patterns), entries["parser_manager_patterns"]["record_count"])
        self.assertEqual(len(genie_recipes), entries["genie_recipes"]["record_count"])


class TestGenieDatConceptDataset(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(
            (
                ROOT
                / "docs"
                / "agent_database"
                / "genie_dat_concepts.json"
            ).read_text(encoding="utf-8")
        )

    def test_schema(self):
        required_keys = {
            "id",
            "name",
            "display_name",
            "category",
            "summary",
            "why_it_matters",
            "owners",
            "exact_terms",
            "aliases",
            "related_fields",
            "how_it_works",
            "project_evidence",
            "best_files",
            "pitfalls",
            "query_terms",
        }
        self.assertEqual(12, len(self.data))
        for entry in self.data:
            self.assertTrue(required_keys.issubset(entry.keys()), entry)
            self.assertIsInstance(entry["owners"], list)
            self.assertGreater(len(entry["owners"]), 0)
            self.assertIsInstance(entry["exact_terms"], list)
            self.assertGreater(len(entry["exact_terms"]), 0)

    def test_expected_ids_present(self):
        ids = {entry["id"] for entry in self.data}
        self.assertIn("unit_sprite_link_fields", ids)
        self.assertIn("civ_global_resource_slots", ids)
        self.assertIn("tech_definition_and_research_location", ids)
        self.assertIn("item_resource_effect_tech_pipeline", ids)


class TestTriggerKnowledgeDatasets(unittest.TestCase):
    def setUp(self):
        self.conditions = json.loads(
            (
                ROOT
                / "docs"
                / "trigger_knowledge"
                / "conditions_knowledge.json"
            ).read_text(encoding="utf-8")
        )
        self.condition_usage = json.loads(
            (
                ROOT
                / "docs"
                / "trigger_knowledge"
                / "condition_project_usage.json"
            ).read_text(encoding="utf-8")
        )
        self.condition_playbook = json.loads(
            (
                ROOT
                / "docs"
                / "trigger_knowledge"
                / "condition_usage_playbook.json"
            ).read_text(encoding="utf-8")
        )
        self.effect_usage = json.loads(
            (
                ROOT
                / "docs"
                / "trigger_knowledge"
                / "effect_project_usage.json"
            ).read_text(encoding="utf-8")
        )
        self.effect_playbook = json.loads(
            (
                ROOT
                / "docs"
                / "trigger_knowledge"
                / "effect_usage_playbook.json"
            ).read_text(encoding="utf-8")
        )

    def test_conditions_schema(self):
        required_keys = {
            "condition_id",
            "internal_name",
            "display_name",
            "description",
            "signature",
            "parameters",
            "notes",
        }
        self.assertEqual(41, len(self.conditions))
        for entry in self.conditions:
            self.assertTrue(required_keys.issubset(entry.keys()), entry)
            self.assertIsInstance(entry["condition_id"], int)
            self.assertIsInstance(entry["internal_name"], str)
            self.assertIsInstance(entry["parameters"], list)
            self.assertIsInstance(entry["notes"], list)

    def test_usage_schema(self):
        required_keys = {
            "internal_name",
            "display_name",
            "usage_status",
            "usage_count",
            "used_in_projects",
            "project_summaries",
            "examples",
        }
        self.assertEqual(41, len(self.condition_usage))
        self.assertEqual(102, len(self.effect_usage))
        for dataset in (self.condition_usage, self.effect_usage):
            for entry in dataset:
                self.assertTrue(required_keys.issubset(entry.keys()), entry)
                self.assertIsInstance(entry["usage_count"], int)
                self.assertIsInstance(entry["used_in_projects"], list)
                self.assertIsInstance(entry["project_summaries"], list)
                self.assertIsInstance(entry["examples"], list)

    def test_playbook_schema(self):
        required_keys = {
            "internal_name",
            "display_name",
            "family",
            "primary_role",
            "how_it_is_used",
            "architecture_notes",
            "common_pairings",
            "real_project_usage_summary",
            "reference_examples",
        }
        self.assertEqual(41, len(self.condition_playbook))
        self.assertEqual(102, len(self.effect_playbook))
        for dataset in (self.condition_playbook, self.effect_playbook):
            for entry in dataset:
                self.assertTrue(required_keys.issubset(entry.keys()), entry)
                self.assertIsInstance(entry["how_it_is_used"], str)
                self.assertTrue(entry["how_it_is_used"])
                self.assertIsInstance(entry["common_pairings"], list)
                self.assertGreater(len(entry["common_pairings"]), 0)
                self.assertIsInstance(entry["reference_examples"], list)

    def test_deep_playbooks_cover_major_patterns(self):
        condition_by_name = {entry["internal_name"]: entry for entry in self.condition_playbook}
        effect_by_name = {entry["internal_name"]: entry for entry in self.effect_playbook}
        self.assertIn("core trigger-state gate", condition_by_name["variable_value"]["how_it_is_used"].lower())
        self.assertIn("heartbeat condition", condition_by_name["timer"]["how_it_is_used"].lower())
        self.assertIn("trigger-to-xs execution bridge", effect_by_name["script_call"]["how_it_is_used"].lower())
        self.assertIn("data-driven design", effect_by_name["modify_attribute"]["architecture_notes"].lower())

    def test_communication_semantics_are_stored_for_key_effects(self):
        effect_by_name = {entry["internal_name"]: entry for entry in self.effect_playbook}
        self.assertEqual("all_players_visible", effect_by_name["display_timer"]["audience_scope"])
        self.assertEqual("high_frequency", effect_by_name["display_timer"]["recommended_frequency"])
        self.assertEqual("all_players_visible", effect_by_name["display_instructions"]["audience_scope"])
        self.assertEqual("low_frequency", effect_by_name["display_instructions"]["recommended_frequency"])
        self.assertEqual("selected_player_only", effect_by_name["send_chat"]["audience_scope"])
        self.assertEqual("low", effect_by_name["send_chat"]["attention_strength"])
        self.assertEqual("selected_player_or_targeted_players", effect_by_name["change_view"]["audience_scope"])
        self.assertIn("debug", effect_by_name["send_chat"]["best_use"].lower())
        self.assertIn("global-event", effect_by_name["display_timer"]["best_use"].lower())

    def test_real_project_usage_contains_expected_patterns(self):
        condition_names = {entry["internal_name"] for entry in self.condition_usage if entry["usage_count"] > 0}
        effect_names = {entry["internal_name"] for entry in self.effect_usage if entry["usage_count"] > 0}
        for name in ("variable_value", "timer", "script_call", "objects_in_area"):
            self.assertIn(name, condition_names)
        for name in ("modify_attribute", "activate_trigger", "change_variable", "play_sound"):
            self.assertIn(name, effect_names)


if __name__ == "__main__":
    unittest.main()

