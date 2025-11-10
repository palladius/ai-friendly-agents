import unittest
from src.config import load_config
from src.data_classes import Family

class TestConfig(unittest.TestCase):
    def test_load_config(self):
        """Tests that the configuration is loaded correctly."""
        config = load_config("etc/sample-family.yaml")
        self.assertIsInstance(config, Family)
        self.assertEqual(config.Family[0].Name, "Riccardo")
        self.assertEqual(config.Address.City, "Springfield")
        self.assertEqual(config.Budget.TotalBudget, 5000)

if __name__ == "__main__":
    unittest.main()
