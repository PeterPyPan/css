import os
import shutil
import unittest
from css import css
from css import io


class TestIO(unittest.TestCase):
    def setUp(self):
        self.original_path = os.getcwd()
        self.dump_folder = '.\\dump_folder'
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        if os.path.isdir(self.dump_folder):
            shutil.rmtree(self.dump_folder, ignore_errors=True)
            os.mkdir(self.dump_folder)
        else:
            os.mkdir(self.dump_folder)
        self.maxDiff = None

    def tearDown(self):
        os.chdir(self.original_path)

    def test_css_write_1(self):
        filepath = os.path.join(self.dump_folder, 'test1.css')

        c = css.create_css()
        c.add_selector('p.aclass', style=[('color', 'red')])
        c.add_selector('.myclass', style=[('color', 'blue')])
        c.add_selector('#myid', style=[('color', 'black')])

        css_string = str(c)
        io.write_css(c, filepath)
        with open(filepath) as fid:
            read_string = fid.read()
        self.assertEqual(css_string, read_string)

    def test_css_write_2(self):
        filepath = os.path.join(self.dump_folder, 'test2.css')

        c = css.create_css()
        c.add_selector('p.aclass', style=[('color', 'red')])
        c.add_selector('.myclass', style=[('color', 'blue')])
        c.add_selector('#myid', style=[('color', 'black')])

        css_string = str(c)
        io.write_css(c, filepath)
        with open(filepath) as fid:
            read_string = fid.read()
        self.assertEqual(css_string, read_string)

    def test_style_from_string(self):
        style_string = 'color: red;\ntext-align: center;'
        st = io.style_from_string(style_string)
        self.assertEqual(style_string, st.get_string())

    def test_selector_from_string_1(self):
        selector_string = 'p.class'
        expected = 'p.class {\n}'
        sel = io.selector_from_string(selector_string)
        self.assertEqual(expected, sel.get_string())

    def test_selector_from_string_2(self):
        selector_string = ' \n\t\r p.class \n\t\r'
        expected = 'p.class {\n}'
        sel = io.selector_from_string(selector_string)
        self.assertEqual(expected, sel.get_string())

    def test_selector_from_string_3(self):
        selector_string = 'p.class, #myid'
        expected = 'p.class, #myid {\n}'
        sel = io.selector_from_string(selector_string)
        self.assertEqual(expected, sel.get_string())

    def test_selector_from_string_4(self):
        selector_string = 'p.class,#myid'
        expected = 'p.class, #myid {\n}'
        sel = io.selector_from_string(selector_string)
        self.assertEqual(expected, sel.get_string())

    def test_selector_from_string_5(self):
        selector_string = ' \n\t\r p.class \n\t\r , \n\r\t #myid \n\t\r '
        expected = 'p.class, #myid {\n}'
        sel = io.selector_from_string(selector_string)
        self.assertEqual(expected, sel.get_string())

    def test_selector_from_string_6(self):
        selector_string = 'p class'
        expected = 'p class {\n}'
        sel = io.selector_from_string(selector_string)
        self.assertEqual(expected, sel.get_string())

    def test_read_css(self):
        css_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_data', 'css_test.css')
        css_object = io.read_css(css_file)

        with open(css_file) as fid:
            read_string = fid.read()
        self.assertEqual(str(css_object), read_string)

if __name__ == 'main':
    unittest.main()
