#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import subprocess
import sys

from apppath import AppPath

__author__ = "Christian Heider Nielsen"
__doc__ = r"""This script will open data the directory of an app"""

from apppath.system_open_path_utilities import AppPathSubDirEnum, open_app_path


def open_arg():
    """"""
    parser = argparse.ArgumentParser(description="Apppath Open Path")
    parser.add_argument(
        "APP_NAME", metavar="Name", type=str, help="App name to open AppPath for"
    )
    parser.add_argument(
        "--SITE",
        "-s",
        type=bool,
        default=False,
        metavar="SITE",
        help="Open user or site dirs (default: User)",
    )
    parser.add_argument(
        "--DIR",
        "-d",
        type=str,
        default="data",
        metavar="DIR",
        help="Which AppPath directory to open (default: 'data')",
    )

    args = parser.parse_args()
    project_app_path = AppPath(args.APP_NAME)

    open_app_path(project_app_path, AppPathSubDirEnum(args.DIR), args.SITE)


if __name__ == "__main__":
    open_arg()
