# -*- coding: utf-8 -*-
# Copyright (c) 2015-2016, Exa Analytics Development Team
# Distributed under the terms of the Apache License 2.0
"""
Exawidgets
#############
This package provides a bridge between exa containers and jupyter js widgets.
"""

def _jupyter_nbextension_paths():
    """
    Automatically generated by the `cookiecutter`_.
    .. _cookiecutter: https://github.com/jupyter/widget-cookiecutter
    """
    return [{
        'section': "notebook",
        'src': "../build/widgets",
        'dest': "jupyter-exawidgets",
        'require': "jupyter-exawidgets/extension"
    }]


from .example import HelloWorld
from . import widget
from .widget import ContainerWidget
from ._version import __version__
