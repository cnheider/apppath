#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Christian Heider Nielsen"
__doc__ = r"""

           Created on 31-01-2021
           """

import subprocess
import sys
from enum import Enum
from pathlib import Path

from apppath.app_path import AppPath

__all__ = ["AppPathSubDirEnum", "open_app_path", "system_open_path"]


class AppPathSubDirEnum(Enum):
    data = "data"
    config = "config"
    cache = "cache"
    log = "log"


def system_open_path(path: Path, *, verbose: bool = False) -> None:
    directory = str(path)
    if verbose:
        print(
            f"Opening the directory ({directory}) using the systems default file manager"
        )

    if sys.platform == "win32":
        subprocess.Popen(["start", directory], shell=True)

    elif sys.platform == "darwin":
        subprocess.Popen(["open", directory])

    else:
        # try:
        subprocess.Popen(["xdg-open", directory])
        # except OSError:


def open_app_path(
    app_path: AppPath,
    sub_dir: AppPathSubDirEnum,
    site: bool = False,
    verbose: bool = False,
) -> None:
    if not site:
        if sub_dir == AppPathSubDirEnum.data:
            directory = app_path.user_data
        elif sub_dir == AppPathSubDirEnum.config:
            directory = app_path.user_config
        elif sub_dir == AppPathSubDirEnum.cache:
            directory = app_path.user_cache
        elif sub_dir == AppPathSubDirEnum.log:
            directory = app_path.user_log
        else:
            raise NotADirectoryError(
                f"{sub_dir} not in user options (data,config,cache,logs)"
            )
    else:
        if sub_dir == AppPathSubDirEnum.data:
            directory = app_path.site_data
        elif sub_dir == AppPathSubDirEnum.config:
            directory = app_path.site_config
        else:
            raise NotADirectoryError(f"{sub_dir} not in site options (data,config)")

    if verbose:
        print(
            f"Opening the directory ({directory})"
            f" of the {app_path.app_name} app using the default file manager"
        )

    system_open_path(directory, verbose=verbose)


if __name__ == "__main__":

    def aisahd():
        from apppath import PROJECT_APP_PATH

        open_app_path(PROJECT_APP_PATH, AppPathSubDirEnum("data"))

    aisahd()
