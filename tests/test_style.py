import unittest
from css import style


class TestStyle(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_style_1(self):
        s = style.Style([('text-align', 'center'), ('color', 'red')])
        expected_output = "text-align: center;\ncolor: red;"
        self.assertEqual(str(s), expected_output)

    def test_style_2(self):
        s = style.Style()
        s.set_property('text-align', 'center')
        s.set_property('color', 'red')

        self.assertEqual(s.get_property('text-align'), 'center')
        self.assertEqual(s.get_property('color'), 'red')

        s.set_property('color', 'blue')
        self.assertEqual(s.get_property('color'), 'blue')

    def test_style_3(self):
        s = style.Style([('text-align', 'center'), ('color', 'red')])
        expected_output = "    text-align: center;\n    color: red;"
        self.assertEqual(s.get_string(indent=1), expected_output)


if __name__ == 'main':
    unittest.main()
