import unittest
from css import selector
from css import style


class TestStyle(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_element_selector(self):
        s = selector.create_element_selector('p', class_tag='test')
        self.assertEqual(s.selector_string, 'p.test')
        self.assertEqual(str(s), 'p.test {\n}')

        style_obj = style.Style([('color', 'red')])
        s = selector.create_element_selector('p', class_tag='test', style=style_obj)
        self.assertEqual(str(s), 'p.test {\n%s\n}' % style_obj.get_string(indent=1))

    def test_class_selector(self):
        s = selector.create_class_selector('myclass')
        self.assertEqual(s.selector_string, '.myclass')
        self.assertEqual(str(s), '.myclass {\n}')

        style_obj = style.Style([('color', 'red')])
        s = selector.create_class_selector('myclass', style=style_obj)
        self.assertEqual(str(s), '.myclass {\n%s\n}' % style_obj.get_string(indent=1))

    def test_id_selector(self):
        s = selector.create_id_selector('myid')
        self.assertEqual(s.selector_string, '#myid')
        self.assertEqual(str(s), '#myid {\n}')

        style_obj = style.Style([('color', 'red')])
        s = selector.create_id_selector('myid', style=style_obj)
        self.assertEqual(str(s), '#myid {\n%s\n}' % style_obj.get_string(indent=1))

    def test_selector_group(self):
        selectors = [selector.create_element_selector('p'),
                     selector.create_class_selector('myclass'),
                     selector.create_id_selector('myid')]

        s = selector.create_selector_group(selectors)
        self.assertEqual(s.selector_string, 'p, .myclass, #myid')
        self.assertEqual(str(s), 'p, .myclass, #myid {\n}')

        style_obj = style.Style([('color', 'red')])
        s = selector.create_selector_group(selectors, style=style_obj)
        self.assertEqual(str(s), 'p, .myclass, #myid {\n%s\n}' % style_obj.get_string(indent=1))


if __name__ == 'main':
    unittest.main()
