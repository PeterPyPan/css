import os
import shutil
import unittest
from css import css
from css import io


class TestStyle(unittest.TestCase):
    def setUp(self):
        self.original_path = os.getcwd()
        self.dump_folder = '.\\dump_folder'
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        if os.path.isdir(self.dump_folder):
            shutil.rmtree(self.dump_folder, ignore_errors=True)
            os.mkdir(self.dump_folder)
        else:
            os.mkdir(self.dump_folder)

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

if __name__ == 'main':
    unittest.main()
