import re
from .css import create_css
from .style import create_style
from .selector import create_selector


def write_css(css_object, filepath):
    css_object.to_file(filepath)


def read_css(filepath):
    with open(filepath) as fid:
        css_string = fid.read()
    return css_from_string(css_string)


def css_from_string(css_string):
    selector_matcher = re.compile('([\-_a-zA-Z0-9\[\]()#@:=+>/$^"~*., ]+)[ \n\t\r]*\{([^{]*)}')
    matches = selector_matcher.findall(css_string)

    css_object = create_css()
    for match in matches:
        selector_string = match[0]
        style_string = match[1]
        the_selector = selector_from_string(selector_string)
        if the_selector is None:
            print('das ier none')
        the_style = style_from_string(style_string)
        the_selector.style = the_style
        css_object.append_selector(the_selector)

    return css_object


def selector_from_string(selector_string):
    selector_string = selector_string.strip().replace('\n', '').replace('\t', '').replace('\r', '')
    selector_matcher = re.compile('([\-_a-zA-Z0-9\[\]()"*~=+^$>/#@:. ]*)')
    matches = selector_matcher.findall(selector_string)

    selector_list = []
    for match in matches:
        match = match.strip()
        if not match:
            continue
        selector_list.append(match)

    return create_selector(selector_list)


def style_from_string(style_string):
    style_string = style_string.strip().replace('\n', '').replace('\t', '').replace('\r', '')

    matcher = re.compile('([\-_a-zA-Z0-9@*]*)[ ]*[:][ ]*([\-_a-zA-Z0-9"()./#% ]+)[;]*')
    matches = matcher.findall(style_string)
    the_style = create_style()

    for match in matches:
        the_style.set_property(match[0], match[1])

    return the_style

