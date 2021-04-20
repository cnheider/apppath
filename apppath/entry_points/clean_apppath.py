#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
from shutil import rmtree

from apppath import AppPath

__author__ = "Christian Heider Nielsen"
__doc__ = r"""This script will clean a apppath directory of an app"""


def clean_arg():
    """"""
    parser = argparse.ArgumentParser(description="Apppath Clean Path")
    parser.add_argument("APP_NAME", metavar="Name", type=str, help="App name to clean AppPath for")
    parser.add_argument(
        "--DIR",
        "-d",
        type=str,
        default="cache",
        metavar="DIR",
        help="Which AppPath directory to clean (default: 'cache')",
    )

    args = parser.parse_args()
    project_app_path = AppPath(args.APP_NAME)

    if args.DIR == "data":
        directory = project_app_path.user_data
    elif args.DIR == "config":
        directory = project_app_path.user_config
    elif args.DIR == "cache":
        directory = project_app_path.user_cache
    elif args.DIR == "logs":
        directory = project_app_path.user_log
    else:
        raise NotADirectoryError(args.DIR)

    print(f"Wiping {directory}")
    if directory.exists():
        rmtree(directory)
    else:
        directory.mkdir()


if __name__ == "__main__":
    clean_arg()
