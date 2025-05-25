import unittest
from Uloha2 import split_line_to_time_and_text


class TestCaseSplitLineToTimeAndText(unittest.TestCase):

    # Otestujem správne rozdelenie riadku
    def test_line_with_time_and_text(self):
        line = "12:23:59.969  configuration for relay"
        time, text = split_line_to_time_and_text(line)
        self.assertEqual(time, "12:23:59.969")
        self.assertEqual(text, "configuration for relay")


if __name__ == '__main__':
    unittest.main()
