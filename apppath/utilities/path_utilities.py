#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Christian Heider Nielsen"
__doc__ = r"""

           Created on 08/03/2020
           """

import pathlib

__all__ = ["ensure_existence", "path_rmtree"]

from shutil import rmtree

# from warg import passes_kws_to

# @passes_kws_to(rmtree) Throws error due to import issues
def path_rmtree(path: pathlib.Path, **kwargs) -> None:
    rmtree(str(path), **kwargs)


def ensure_existence(
    out: pathlib.Path,
    *,
    enabled: bool = True,
    declare_file: bool = False,
    overwrite_on_wrong_type: bool = False,
    force_overwrite: bool = False,
) -> pathlib.Path:
    """

  :param overwrite_on_wrong_type:
  :type overwrite_on_wrong_type:
  :param force_overwrite:
  :type force_overwrite:
:param declare_file:
:type declare_file:
:param out:
:type out:
:param enabled:
:type enabled:
:return:
:rtype:
"""
    if enabled:
        if out.is_file() or ("." in out.name and ".d" not in out.name) or declare_file:
            if (not out.is_file() and declare_file and overwrite_on_wrong_type) or force_overwrite:
                path_rmtree(out)
            ensure_existence(out.parent)
            if not out.exists():
                out.touch()
        else:
            if (out.is_file() and not declare_file and overwrite_on_wrong_type) or force_overwrite:
                out.unlink(missing_ok=True)
            if not out.exists():
                out.mkdir(parents=True)
    return out


if __name__ == "__main__":
    ensure_existence(pathlib.Path.cwd() / "exclude")
    ensure_existence(pathlib.Path.cwd() / "exclude" / "0.log")
    ensure_existence(pathlib.Path.cwd() / "exclude" / "log.d")
    ensure_existence(pathlib.Path.cwd() / "exclude" / "log.d" / "log.a")
