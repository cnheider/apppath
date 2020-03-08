#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Christian Heider Nielsen"
__doc__ = r"""

           Created on 08/03/2020
           """

import pathlib

__all__ = ["ensure_existence"]


def ensure_existence(out: pathlib.Path, *, enabled: bool = True):
    if enabled:
        if not out.exists():
            out.mkdir(parents=True)
