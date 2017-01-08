import os
import shutil
import unittest
from css import css
from css import selector


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

    def test_css_1(self):
        s1 = selector.create_selector('.myclass')
        s2 = selector.create_selector('p')
        s3 = selector.create_selector('#myid')
        c1 = css.CSS(selectors=[s1, s2, s3])
        c2 = css.create_css(selectors=[s1, s2, s3])
        expected_output = '.myclass {\n}\n' \
                          'p {\n}\n' \
                          '#myid {\n}'

        self.assertEqual(str(c1), expected_output)
        self.assertEqual(str(c2), expected_output)

    def test_css_2(self):
        s1 = selector.create_selector('.myclass')
        s2 = selector.create_selector('p')
        s3 = selector.create_selector('#myid')
        c1 = css.create_css()
        c1.append_selector(s1)
        c1.append_selector(s2)
        c1.append_selector(s3)
        c2 = css.create_css()
        c2.append_selectors([s1, s2, s3])
        expected_output = '.myclass {\n}\n' \
                          'p {\n}\n' \
                          '#myid {\n}'

        self.assertEqual(str(c1), expected_output)
        self.assertEqual(str(c2), expected_output)

    def test_css_3(self):
        c = css.create_css()
        c.add_selector('p.aclass', style=[('color', 'red')])
        c.add_selector('.myclass', style=[('color', 'blue')])
        c.add_selector('#myid', style=[('color', 'black')])

        expected_output = 'p.aclass {\n    color: red;\n}\n' \
                          '.myclass {\n    color: blue;\n}\n' \
                          '#myid {\n    color: black;\n}'

        self.assertEqual(str(c), expected_output)

    def test_css_4(self):
        c = css.create_css()
        c.add_selector(selectors=['p.aclass', '.myclass', '#myid'], style=[('color', 'red')])

        expected_output = 'p.aclass, .myclass, #myid {\n    color: red;\n}'

        self.assertEqual(str(c), expected_output)

    def test_css_5(self):
        c = css.create_css()
        s1 = c.add_selector('p.aclass', style=[('color', 'red')])
        s2 = c.add_selector('.myclass', style=[('color', 'blue')])
        s3 = c.add_selector('#myid', style=[('color', 'black')])

        self.assertEqual(str(s1), 'p.aclass {\n    color: red;\n}')
        self.assertEqual(str(s2), '.myclass {\n    color: blue;\n}')
        self.assertEqual(str(s3), '#myid {\n    color: black;\n}')

if __name__ == 'main':
    unittest.main()
