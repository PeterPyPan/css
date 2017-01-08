from collections import OrderedDict
from .utils import make_indent


def create_style(style_dict=None):
    return Style(style_dict)


class Style(object):
    def __init__(self, style_dict=None):
        self._style_dict = OrderedDict()
        if style_dict is None:
            return

        style_dict = OrderedDict(style_dict)
        for key, value in style_dict.items():
            self.set_property(key, value)

    def set_property(self, key, value):
        self._style_dict[key] = value

    def get_property(self, key):
        return self._style_dict.get(key, None)

    def get_string(self, indent=0, tab_settings=None):
        """
        Returns a string with 'key: value;' pairs separated by newlines.

        Args:
            indent: number of indents before each key, value line
            tab_settings: TabSettings object

        Returns:

        """
        indent = make_indent(indent, tab_settings)
        style_list = []
        for key, value in self._style_dict.items():
            style_list.append("%s%s: %s;" % (indent, key, value))
        return "\n".join(style_list)

    def __str__(self):
        return self.get_string()

    def items(self):
        return self._style_dict.items()
