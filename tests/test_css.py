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
        try:
            os.mkdir(self.dump_folder)
        except FileExistsError:
            shutil.rmtree(self.dump_folder, ignore_errors=True)
            os.mkdir(self.dump_folder)

    def tearDown(self):
        os.chdir(self.original_path)

    def test_css_1(self):
        s1 = selector.create_class_selector('myclass')
        s2 = selector.create_element_selector('p')
        s3 = selector.create_id_selector('myid')
        c1 = css.CSS(selectors=[s1, s2, s3])
        c2 = css.create_css(selectors=[s1, s2, s3])
        expected_output = '.myclass {\n}\n' \
                          'p {\n}\n' \
                          '#myid {\n}'

        self.assertEqual(str(c1), expected_output)
        self.assertEqual(str(c2), expected_output)

    def test_css_2(self):
        s1 = selector.create_class_selector('myclass')
        s2 = selector.create_element_selector('p')
        s3 = selector.create_id_selector('myid')
        c1 = css.create_css()
        c1.add_selector(s1)
        c1.add_selector(s2)
        c1.add_selector(s3)
        c2 = css.create_css()
        c2.add_selectors([s1, s2, s3])
        expected_output = '.myclass {\n}\n' \
                          'p {\n}\n' \
                          '#myid {\n}'

        self.assertEqual(str(c1), expected_output)
        self.assertEqual(str(c2), expected_output)

    def test_css_3(self):
        c = css.create_css()
        c.add_element_selector('p', class_tag='aclass', style=[('color', 'red')])
        c.add_class_selector('myclass', style=[('color', 'blue')])
        c.add_id_selector('myid', style=[('color', 'black')])

        expected_output = 'p.aclass {\n    color: red;\n}\n' \
                          '.myclass {\n    color: blue;\n}\n' \
                          '#myid {\n    color: black;\n}'

        self.assertEqual(str(c), expected_output)

    def test_css_4(self):
        s1 = selector.create_element_selector('p', class_tag='aclass')
        s2 = selector.create_class_selector('myclass')
        s3 = selector.create_id_selector('myid')
        c = css.create_css()
        c.add_selector_group(selectors=[s1, s2, s3], style=[('color', 'red')])

        expected_output = 'p.aclass, .myclass, #myid {\n    color: red;\n}'

        self.assertEqual(str(c), expected_output)

    def test_css_5(self):
        c = css.create_css()
        s1 = c.add_element_selector('p', class_tag='aclass', style=[('color', 'red')])
        s2 = c.add_class_selector('myclass', style=[('color', 'blue')])
        s3 = c.add_id_selector('myid', style=[('color', 'black')])

        self.assertEqual(str(s1), 'p.aclass {\n    color: red;\n}')
        self.assertEqual(str(s2), '.myclass {\n    color: blue;\n}')
        self.assertEqual(str(s3), '#myid {\n    color: black;\n}')

    def test_css_write_1(self):
        filepath = os.path.join(self.dump_folder, 'test1.css')

        c = css.create_css()
        c.add_element_selector('p', class_tag='aclass', style=[('color', 'red')])
        c.add_class_selector('myclass', style=[('color', 'blue')])
        c.add_id_selector('myid', style=[('color', 'black')])

        css_string = str(c)
        c.to_file(filepath)
        with open(filepath) as fid:
            read_string = fid.read()
        self.assertEqual(css_string, read_string)

    def test_css_write_2(self):
        filepath = os.path.join(self.dump_folder, 'test2.css')

        c = css.create_css()
        c.add_element_selector('p', class_tag='aclass', style=[('color', 'red')])
        c.add_class_selector('myclass', style=[('color', 'blue')])
        c.add_id_selector('myid', style=[('color', 'black')])

        css_string = str(c)
        c.to_file(filepath)
        with open(filepath) as fid:
            read_string = fid.read()
        self.assertEqual(css_string, read_string)


if __name__ == 'main':
    unittest.main()
