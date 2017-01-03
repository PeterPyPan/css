from .selector import Selector
from .selector import create_element_selector, create_class_selector, create_id_selector, create_selector_group


def create_css(selectors=None):
    return CSS(selectors=selectors)


class CSS(object):
    def __init__(self, selectors=None):
        self._selectors = []
        if selectors is None:
            selectors = []
        self.add_selectors(selectors)

    def add_selector(self, selector):
        if not isinstance(selector, Selector):
            raise ValueError('An object of type Selector is expected.')
        self._selectors.append(selector)

    def add_selectors(self, selectors):
        for selector in selectors:
            self.add_selector(selector)

    def get_string(self, indent=0, tab_settings=None):
        style_list = []
        for selector in self._selectors:
            style_list.append(selector.get_string(indent, tab_settings))
        return "\n".join(style_list)

    def __str__(self):
        return self.get_string()

    def add_element_selector(self, element_tag, class_tag=None, style=None):
        s = create_element_selector(element_tag, class_tag=class_tag, style=style)
        self.add_selector(s)
        return s

    def add_class_selector(self, class_tag, style=None):
        s = create_class_selector(class_tag, style=style)
        self.add_selector(s)
        return s

    def add_id_selector(self, id_tag, style=None):
        s = create_id_selector(id_tag, style=style)
        self.add_selector(s)
        return s

    def add_selector_group(self, selectors, style=None):
        s = create_selector_group(selectors, style=style)
        self.add_selector(s)
        return s
