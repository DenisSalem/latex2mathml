#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2016-2020, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
import pytest

from latex2mathml.symbols_parser import convert_symbol


@pytest.mark.parametrize(
    "name, latex, expected",
    [("Operator plus", "+", "0002B"), ("Alias command", r"\to", "02192")],
)
def test_convert_symbol(name, latex, expected):
    assert convert_symbol(latex) == expected, name
