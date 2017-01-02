def make_indent(indents=1, tab_settings=None):
    if tab_settings is None:
        return " " * (indents * 4)

    if tab_settings.use_spaces:
        return " " * (indents * tab_settings.tab_n)
    else:
        return "\t" * (indents * tab_settings.tab_n)


def tab_settings_spaces(tab_n=4):
    return TabSettings(use_spaces=True, tab_n=tab_n)


def tab_settings_tabs():
    return TabSettings(use_spaces=False, tab_n=1)


class TabSettings(object):
    def __init__(self, use_spaces=True, tab_n=None):
        if use_spaces and tab_n is None:
            tab_n = 4
        elif not use_spaces and tab_n is None:
            tab_n = 1

        self._use_spaces = use_spaces
        self.tab_n = tab_n

    @property
    def use_spaces(self):
        return self._use_spaces

    @use_spaces.setter
    def use_spaces(self, value):
        self._use_spaces = bool(value)

    @property
    def use_tabs(self):
        return not self._use_spaces

    @use_tabs.setter
    def use_tabs(self, value):
        self._use_spaces = not bool(value)
