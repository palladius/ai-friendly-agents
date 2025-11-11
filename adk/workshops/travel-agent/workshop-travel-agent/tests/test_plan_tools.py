import unittest
from unittest.mock import patch, mock_open
from src.lib.file_tools import write_plan, list_plans, read_plan
from datetime import date, datetime
import os
from pathlib import Path

class TestPlanTools(unittest.TestCase):

    def setUp(self):
        self.test_dir = Path("out/travel_plans")
        self.test_dir.mkdir(exist_ok=True)

    @patch("os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    def test_write_plan(self, mock_file, mock_makedirs):
        plan_name = "Test Plan"
        test_date_str = "2025-11-11"
        test_date = datetime.strptime(test_date_str, "%Y-%m-%d")
        content = "This is a test plan."
        plan_id = 1
        
        result = write_plan(plan_name, test_date_str, content, plan_id)
        
        plan_folder_name = f"{test_date.strftime('%Y%m')}_{plan_name.replace(' ', '')}"
        expected_path = self.test_dir / plan_folder_name / f"PLAN_{plan_id}.md"
        
        mock_makedirs.assert_called_once_with(self.test_dir / plan_folder_name, exist_ok=True)
        mock_file.assert_called_once_with(expected_path, "w")
        mock_file().write.assert_called_once_with(content)
        self.assertEqual(result, f"Plan saved to {expected_path}")

    @patch("pathlib.Path.iterdir")
    def test_list_plans(self, mock_iterdir):
        mock_path1 = unittest.mock.MagicMock()
        mock_path1.__str__.return_value = "out/travel_plans/202511_TestPlan1"
        mock_path1.is_dir.return_value = True

        mock_path2 = unittest.mock.MagicMock()
        mock_path2.__str__.return_value = "out/travel_plans/202512_TestPlan2"
        mock_path2.is_dir.return_value = True

        mock_iterdir.return_value = [mock_path1, mock_path2]

        result = list_plans()
        self.assertEqual(len(result), 2)
        self.assertIn("out/travel_plans/202511_TestPlan1", result)
        self.assertIn("out/travel_plans/202512_TestPlan2", result)

    @patch("builtins.open", new_callable=mock_open, read_data="Test content")
    def test_read_plan(self, mock_file):
        test_path = "out/travel_plans/202511_TestPlan/PLAN_1.md"
        content = read_plan(test_path)
        mock_file.assert_called_once_with(test_path, "r")
        self.assertEqual(content, "Test content")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_read_plan_file_not_found(self, mock_file):
        test_path = "non_existent_file.md"
        result = read_plan(test_path)
        self.assertEqual(result, f"Error: File not found at {test_path}")

if __name__ == '__main__':
    unittest.main()
