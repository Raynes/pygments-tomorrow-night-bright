# -*- coding: utf-8 -*-
"""
tomorrow night bright
---------------------

Port of the tomorrow night bright color scheme for Vim.
"""

from pygments.style import Style
from pygments.token import Comment, Error, Keyword, Name, Number, Operator, \
                           Punctuation, String, Text

BACKGROUND   = "#000000"
CURRENT_LINE = "#2a2a2a"
SELECTION    = "#424242"
FOREGROUND   = "#eaeaea"
COMMENT      = "#969896"
RED          = "#d54e53"
ORANGE       = "#e78c45"
YELLOW       = "#e7c547"
GREEN        = "#b9ca4a"
AQUA         = "#70c0b1"
BLUE         = "#7aa6da"
PURPLE       = "#c397d8"


class TomorrownightbrightStyle(Style):

    """
    Port of the tomorrow night bright color scheme.
    """

    default_style = ''

    background_color = BACKGROUND
    highlight_color = SELECTION

    styles = {
        
        Comment:            COMMENT,
        Text:               FOREGROUND,

        Keyword:            PURPLE,
        Operator.Word:      '',

        String:             GREEN,
        String.Char:        FOREGROUND,

        Name.Builtin:       RED,
        Name.Variable:      '',
        Name.Constant:      GREEN,
        Name.Class:         BLUE,
        Name.Function:      BLUE,
        Name.Namespace:     BLUE,
        #Name.Exception:     '',
        Name.Tag:           BLUE,
        #Name.Attribute:     '',
        Name.Decorator:     AQUA,
}
