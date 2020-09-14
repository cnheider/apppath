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
  """
asses_kws_to rmtree from shutil
:param path:
:type path:
:param kwargs:
:type kwargs:
"""
  rmtree(str(path), **kwargs)


def ensure_existence(
    out: pathlib.Path,
    *,
    enabled: bool = True,
    declare_file: bool = False,
    overwrite_on_wrong_type: bool = False,
    force_overwrite: bool = False,
    verbose: bool = False,
    ) -> pathlib.Path:
  """

:param verbose:
:type verbose:
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
    if not out.parent.exists():
      if verbose:
        print("Creating parents")
      out.parent.mkdir(parents=True, exist_ok=True)

    if out.is_file() or ("." in out.name and ".d" not in out.name) or declare_file:
      if (
          out.exists()
          and (out.is_dir() or ("." not in out.name and ".d" in out.name))
          and ((declare_file and overwrite_on_wrong_type) or force_overwrite)
      ):
        if verbose:
          print("Removing tree")
        path_rmtree(out)
      if out.is_file() and not out.exists():
        out.touch(exist_ok=True)
    else:
      if (
          out.exists()
          and out.is_file()
          and ((not declare_file and overwrite_on_wrong_type) or force_overwrite)
      ):
        if verbose:
          print("Deleting file")
        out.unlink()  # missing_ok=True)
      if not out.exists():
        out.mkdir(parents=True, exist_ok=True)

  return out


if __name__ == "__main__":

  def main():
    """

"""
    ensure_existence(pathlib.Path.cwd() / "exclude", force_overwrite=True)
    ensure_existence(pathlib.Path.cwd() / "exclude" / "0.log")
    ensure_existence(pathlib.Path.cwd() / "exclude" / "log.d")
    ensure_existence(pathlib.Path.cwd() / "exclude" / "log.d" / "log.a")

    from apppath import PROJECT_APP_PATH

    ensure_existence(PROJECT_APP_PATH.user_log / "exclude" / "log.d" / "log.a")

    def recurse_test():
      """

"""
      ensure_existence(pathlib.Path.cwd() / "exclude" / "spodakjioj" / "log.d" / "log.a")
      ensure_existence(pathlib.Path.cwd() / "exclude" / "spodakjioj" / "log.d" / "log.csv")

    recurse_test()


  main()
