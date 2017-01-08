from .style import Style
from .utils import make_indent


def create_selector(selectors=None, style=None):
    return Selector(selectors, style)


class Selector(object):
    def __init__(self, selectors=None, style=None):
        self._selectors = []
        if selectors is None:
            selectors = []
        if isinstance(selectors, str):
            selectors = [selectors]
        self.add_selectors(selectors)

        if style is None:
            style = Style()
        elif not isinstance(style, Style):
            style = Style(style_dict=style)
        self.style = style

    def add_selector(self, selector):
        selector = str(selector)
        if ',' in selector:
            raise ValueError('Group selectors must be added separately')
        if '\n' in selector or '\r' in selector or '\t' in selector:
            raise ValueError('Newline and tab characters are not allowed in selectors')
        self._selectors.append(selector)

    def add_selectors(self, selectors):
        for selector in selectors:
            self.add_selector(selector)

    @property
    def selector_string(self):
        if len(self._selectors) == 0:
            return ''
        sel_string = []
        for sel in self._selectors:
            sel_string.append(sel)
        return ", ".join(sel_string)

    def get_string(self, indent=0, tab_settings=None):
        string_list = list()
        string_list.append("%s%s {\n" % (make_indent(indent, tab_settings), self.selector_string))
        for style_key, style_value in self.style.items():
            string_list.append("%s%s: %s;\n" % (make_indent(indent + 1, tab_settings),
                                                str(style_key), str(style_value)))
        string_list.append("%s}" % make_indent(indent, tab_settings))

        return "".join(string_list)

    def __str__(self):
        return self.get_string()
