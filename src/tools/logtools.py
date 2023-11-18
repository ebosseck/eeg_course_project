from typing import List, Union

STYLE_DEFAULT = 0
STYLE_BOLD = 1
STYLE_ITALIC = 3
STYLE_UNDERLINE = 4
STYLE_HIGHLIGHT = 7
STYLE_STRIKETHROUGH = 9
STYLE_THICK_UNDERLINE = 21
STYLE_OUTLINE = 51
STYLE_THICK_OUTLINE = 52

STYLE_TEXT_BLACK = 30
STYLE_TEXT_LIGHT_RED = 31
STYLE_TEXT_DARK_GREEN = 32
STYLE_TEXT_DARK_YELLOW = 33
STYLE_TEXT_DARK_BLUE = 34
STYLE_TEXT_DARK_PURPLE = 35
STYLE_TEXT_DARK_CYAN = 36
STYLE_TEXT_GRAY = 37
STYLE_TEXT_DARK_GRAY = 90
STYLE_TEXT_RED = 91
STYLE_TEXT_GREEN = 92
STYLE_TEXT_YELLOW = 93
STYLE_TEXT_BLUE = 94
STYLE_TEXT_PURPLE = 95
STYLE_TEXT_CYAN = 96
STYLE_TEXT_WHITE = 97

STYLE_HIGHLIGHT_BLACK = 40
STYLE_HIGHLIGHT_LIGHT_RED = 41
STYLE_HIGHLIGHT_DARK_GREEN = 42
STYLE_HIGHLIGHT_DARK_YELLOW = 43
STYLE_HIGHLIGHT_DARK_BLUE = 44
STYLE_HIGHLIGHT_DARK_PURPLE = 45
STYLE_HIGHLIGHT_DARK_CYAN = 46
STYLE_HIGHLIGHT_GRAY = 47
STYLE_HIGHLIGHT_DARK_GRAY = 100
STYLE_HIGHLIGHT_RED = 101
STYLE_HIGHLIGHT_GREEN = 102
STYLE_HIGHLIGHT_YELLOW = 103
STYLE_HIGHLIGHT_BLUE = 104
STYLE_HIGHLIGHT_PURPLE = 105
STYLE_HIGHLIGHT_CYAN = 106
STYLE_HIGHLIGHT_WHITE = 107

ENABLE_FANCY_LOG = True

org_print = print

def __buildStyleString(style: Union[int, List[int]]):
    if isinstance(style, list):
        return "".join('\033[{}m'.format(s) for s in style)
    else:
        return "\033[{}m".format(style)

def formatString(*content, style: Union[int, List[int]], sep=' '):
    if not ENABLE_FANCY_LOG:
        return sep.join(str(arg) for arg in content)
    return ''.join([__buildStyleString(style), sep.join(str(arg) for arg in content), __buildStyleString(0)])

def print(*args, style: Union[int, List[int]] = 0, sep=' ', end='\n', file=None):
    if not ENABLE_FANCY_LOG:
        org_print(*args, sep=sep, end=end, file=file)
    org_print(''.join([__buildStyleString(style), sep.join(str(arg) for arg in args), __buildStyleString(0)]), end=end, file=file)
