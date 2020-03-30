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
        if out.is_file() or ("." in out.name and ".d" not in out.name):
            ensure_existence(out.parent)
            if not out.exists():
                out.touch()
        else:
            if not out.exists():
                out.mkdir(parents=True)
    return out


if __name__ == "__main__":
    ensure_existence(pathlib.Path.cwd() / "exclude")
    ensure_existence(pathlib.Path.cwd() / "exclude" / "0.log")
    ensure_existence(pathlib.Path.cwd() / "exclude" / "log.d")
    ensure_existence(pathlib.Path.cwd() / "exclude" / "log.d" / "log.a")
