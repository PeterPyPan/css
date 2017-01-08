from .selector import Selector


def create_css(selectors=None):
    return CSS(selectors=selectors)


class CSS(object):
    def __init__(self, selectors=None):
        self._selectors = []
        if selectors is None:
            selectors = []
        self.append_selectors(selectors)

    def append_selector(self, selector):
        if not isinstance(selector, Selector):
            raise ValueError('An object of type Selector is expected.')
        self._selectors.append(selector)

    def append_selectors(self, selectors):
        for selector in selectors:
            self.append_selector(selector)

    def get_string(self, indent=0, tab_settings=None):
        style_list = []
        for selector in self._selectors:
            style_list.append(selector.get_string(indent, tab_settings))
        return "\n".join(style_list)

    def __str__(self):
        return self.get_string()

    def to_file(self, filepath):
        with open(filepath, 'wt') as fid:
            fid.write(str(self))

    def add_selector(self, selectors=None, style=None):
        if isinstance(selectors, Selector):
            raise ValueError('Use the append_selector to append a Selector object')

        s = Selector(selectors, style)
        self.append_selector(s)
        return s
