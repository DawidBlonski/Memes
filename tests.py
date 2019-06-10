from main import calculate
import unittest


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.false_str_usb_size = 'f'

        self.usb_size = 1

        self.good_memes = [
            ("rollsafe.jpg", 205, 6),
            ("sad_pepe_compilation.gif", 410, 10),
            ("yodeling_kid.avi", 605, 12),
        ]

    def test_data_test(self):
        self.assertEqual(calculate(self.usb_size,self.good_memes),
                         (22, {"sad_pepe_compilation.gif", "yodeling_kid.avi"}))

    def test_no_data(self):
        assert calculate(0, []) == (0, set())
        print(self.good_memes)

    def test_duplicate(self):
        self.assertEqual(calculate(self.usb_size,self.good_memes*2),
                         (22, {"sad_pepe_compilation.gif", "yodeling_kid.avi"}))



