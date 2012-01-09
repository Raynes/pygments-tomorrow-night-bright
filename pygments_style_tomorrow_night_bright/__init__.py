# -*- coding: utf-8 -*-
"""
tomorrow night bright
---------------------

Port of the tomorrow night bright color scheme for Vim.
"""

from pygments.style import Style
from pygments.token import Comment, Error, Keyword, Name, Number, Operator, \
                           Punctuation, String, Text


class TomorrowNightBrightStyle(Style):
    """
    Port of the tomorrow night bright color scheme.
    """

    default_style = ''

    background_color = '#000000'
    highlight_color = '#424242'

    styles = {
        Comment: 'italic #969896',

        Error: '#d54e53',

        Keyword: '#c397d8',
        Keyword.Reserved: '',
        Keyword.Type: '#e78c45',

        Name: '#eaeaea',
        Name.Attribute: '',
        Name.Builtin: '#8abeb7',
        Name.Builtin.Pseudo: '',
        Name.Class: '#e7c547',
        Name.Constant: '#e78c45',
        Name.Decorator: '#e7c547',
        Name.Function: '#70c0b1',
        Name.Tag: '#eaeaea',

        Number: '#eaeaea',

        Operator: '#8abeb7',
        Operator.Word: '',

        Punctuation: '#eaeaea',

        String: '#b9ca4a',
        String.Escape: '',

        Text: '#eaeaea',
}

