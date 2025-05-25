import unittest
from Uloha2 import split_line_to_time_and_text, TIME_PATTERN


class TestCaseSplitLineToTimeAndText(unittest.TestCase):

    # Otestujem správne rozdelenie riadku
    def test_line_with_time_and_text(self):
        line = "12:23:59.969  configuration for relay"
        time, text = split_line_to_time_and_text(line)
        self.assertEqual(time, "12:23:59.969")
        self.assertEqual(text, "configuration for relay")

    # Otestujem riadok len s casom, bez textu
    def test_line_with_only_time(self):
        line = "12:34:56"
        time, text = split_line_to_time_and_text(line)
        self.assertEqual(time, "12:34:56")
        self.assertEqual(text, "")

   # Otestujem riadok s viacerymi medzerami medzi casom a textom
    def test_line_with_multiple_spaces(self):
        line = "12:34:56    configuration for relay"
        time, text = split_line_to_time_and_text(line)
        self.assertEqual(time, "12:34:56")
        self.assertEqual(text, "configuration for relay")

    def test_time_pattern_valid(self):
        valid_times = ["00:00:00", "12:34:56", "23:59:59.123", "01:02:03.0001"]
        for t in valid_times:
            self.assertTrue(TIME_PATTERN.match(t), f"{t} should be valid")

    def test_time_pattern_invalid(self):
        invalid_times = ["12-34:56", "99:99", "abcd", "123456"]
        for t in invalid_times:
            self.assertFalse(TIME_PATTERN.match(t), f"{t} should be invalid")
if __name__ == '__main__':
    unittest.main()
