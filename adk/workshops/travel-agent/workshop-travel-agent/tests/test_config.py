import unittest
import os
from src.config import load_config
from src.data_classes import Family

class TestConfig(unittest.TestCase):
    def test_load_config(self):
        """Tests that the configuration is loaded correctly."""
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        config_path = os.path.join(project_root, "etc", "sample-family.yaml")
        config = load_config(config_path)
        self.assertIsInstance(config, Family)
        self.assertEqual(config.Family[0].Name, "Riccardo")
        self.assertEqual(config.Address.City, "Springfield")
        self.assertEqual(config.Budget.TotalBudget, 5000)

if __name__ == "__main__":
    unittest.main()
