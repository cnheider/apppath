#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import subprocess
import sys

from apppath import AppPath

__author__ = "Christian Heider Nielsen"
__doc__ = r"""This script will open data the directory of an app"""


def open_arg():
    parser = argparse.ArgumentParser(description="Apppath Open Path")
    parser.add_argument("APP_NAME", metavar="Name", type=str, help="App name to open AppPath for")
    parser.add_argument(
        "--DIR",
        "-d",
        type=str,
        default="data",
        metavar="DIR",
        help="Which AppPath directory to open (default: 'data')",
    )

    args = parser.parse_args()
    PROJECT_APP_PATH = AppPath(args.APP_NAME)

    if args.DIR == "data":
        directory = PROJECT_APP_PATH.user_data
    elif args.DIR == "config":
        directory = PROJECT_APP_PATH.user_config
    elif args.DIR == "cache":
        directory = PROJECT_APP_PATH.user_cache
    elif args.DIR == "logs":
        directory = PROJECT_APP_PATH.user_log
    else:
        raise NotADirectoryError(args.DIR)

    print(f"Opening the directory ({directory})" f" of the {args.APP_NAME} app using the default filemanager")

    if sys.platform == "win32":
        subprocess.Popen(["start", directory], shell=True)

    elif sys.platform == "darwin":
        subprocess.Popen(["open", directory])

    else:
        # try:
        subprocess.Popen(["xdg-open", directory])
    # except OSError:


if __name__ == "__main__":
    open_arg()
