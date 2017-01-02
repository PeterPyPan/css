from .style import Style
from .utils import make_indent


def create_element_selector(element_tag, class_tag=None, style=None):
    return ElementSelector(element_tag=element_tag, class_tag=class_tag, style=style)


def create_class_selector(class_tag, style=None):
    return ClassSelector(class_tag=class_tag, style=style)


def create_id_selector(id_tag, style=None):
    return IdSelector(id_tag=id_tag, style=style)


def create_selector_group(selectors, style=None):
    return SelectorGroup(selectors=selectors, style=style)


class Selector(object):
    def __init__(self, style=None):
        if style is None:
            style = Style()
        elif not isinstance(style, Style):
            style = Style(style_dict=style)
        self.style = style

    @property
    def selector_string(self):
        raise NotImplementedError('This should be implemented in subclasses')

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


class ElementSelector(Selector):
    def __init__(self, element_tag, class_tag=None, style=None):
        super(ElementSelector, self).__init__(style=style)
        self._element_tag = element_tag
        self._class_tag = class_tag

    @property
    def selector_string(self):
        if self._class_tag is None:
            return self._element_tag
        else:
            return "%s.%s" % (self._element_tag, self._class_tag)


class ClassSelector(Selector):
    def __init__(self, class_tag, style=None):
        super(ClassSelector, self).__init__(style=style)
        self._class_tag = class_tag

    @property
    def selector_string(self):
        return ".%s" % self._class_tag


class IdSelector(Selector):
    def __init__(self, id_tag, style=None):
        super(IdSelector, self).__init__(style=style)
        self._id_tag = id_tag

    @property
    def selector_string(self):
        return "#%s" % self._id_tag


class SelectorGroup(Selector):
    def __init__(self, selectors, style=None):
        super(SelectorGroup, self).__init__(style=style)
        self._selectors = selectors

    @property
    def selector_string(self):
        return ", ".join([x.selector_string for x in self._selectors])
