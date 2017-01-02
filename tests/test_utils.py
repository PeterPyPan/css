import unittest
from css import utils


class TestStyle(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_tab_settings(self):
        ts = utils.TabSettings(tab_n=20)
        self.assertEqual(ts.tab_n, 20)
        self.assertEqual(ts.use_spaces, True)
        self.assertEqual(ts.use_tabs, False)

        ts = utils.TabSettings(use_spaces=False)
        self.assertEqual(ts.tab_n, 1)
        self.assertEqual(ts.use_spaces, False)
        self.assertEqual(ts.use_tabs, True)

        ts = utils.TabSettings(tab_n=10, use_spaces=False)
        self.assertEqual(ts.tab_n, 10)
        self.assertEqual(ts.use_spaces, False)
        self.assertEqual(ts.use_tabs, True)

        ts = utils.TabSettings()
        self.assertEqual(ts.tab_n, 4)
        self.assertEqual(ts.use_spaces, True)
        self.assertEqual(ts.use_tabs, False)

        ts.tab_n = 8
        self.assertEqual(ts.tab_n, 8)

        ts.use_tabs = True
        self.assertEqual(ts.use_spaces, False)
        self.assertEqual(ts.use_tabs, True)

        ts.use_spaces = True
        self.assertEqual(ts.use_spaces, True)
        self.assertEqual(ts.use_tabs, False)

    def tab_settings_tabs(self):
        ts = utils.tab_settings_tabs()
        self.assertEqual(ts.tab_n, 1)
        self.assertEqual(ts.use_tabs, True)

        ts = utils.tab_settings_tabs(tab_n=2)
        self.assertEqual(ts.tab_n, 2)
        self.assertEqual(ts.use_tabs, True)

    def tab_settings_spaces(self):
        ts = utils.tab_settings_spaces()
        self.assertEqual(ts.tab_n, 4)
        self.assertEqual(ts.use_spaces, True)

        ts = utils.tab_settings_spaces(tab_n=8)
        self.assertEqual(ts.tab_n, 8)
        self.assertEqual(ts.use_spaces, True)

    def test_make_indent(self):
        self.assertEqual(utils.make_indent(), '    ')
        self.assertEqual(utils.make_indent(0), '')
        self.assertEqual(utils.make_indent(1), '    ')
        self.assertEqual(utils.make_indent(2), '        ')

        ts = utils.TabSettings(tab_n=2)
        self.assertEqual(utils.make_indent(0, ts), '')
        self.assertEqual(utils.make_indent(1, ts), '  ')
        self.assertEqual(utils.make_indent(tab_settings=ts), '  ')

        ts = utils.TabSettings(use_spaces=False)
        self.assertEqual(utils.make_indent(0, ts), '')
        self.assertEqual(utils.make_indent(1, ts), '\t')
        self.assertEqual(utils.make_indent(2, ts), '\t\t')
        self.assertEqual(utils.make_indent(tab_settings=ts), '\t')


if __name__ == 'main':
    unittest.main()
