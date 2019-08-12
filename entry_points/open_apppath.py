#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import subprocess
import sys

from apppath import AppPath

__author__ = 'cnheider'
__doc__ = r'''This script will open data the directory of an app'''


def open_arg():
  parser = argparse.ArgumentParser(description='Apppath Open Path')
  parser.add_argument('APP_NAME',
                      metavar='Name',
                      type=str,
                      help="App name to open AppPath for",
                      )
  parser.add_argument("--DIR",
                      "-d",
                      type=str,
                      default='data',
                      metavar="DIR",
                      help="Which AppPath directory to open (default: 'data')",
                      )

  args = parser.parse_args()
  PROJECT_APP_PATH = AppPath(args.APP_NAME)

  print(f'Opening default data directory ({PROJECT_APP_PATH.user_data})'
        f' of the {args.APP_NAME} app using the default filemanager')

  if sys.platform == 'win32':
    subprocess.Popen(['start', PROJECT_APP_PATH.user_data], shell=True)

  elif sys.platform == 'darwin':
    subprocess.Popen(['open', PROJECT_APP_PATH.user_data])

  else:
    # try:
    subprocess.Popen(['xdg-open', PROJECT_APP_PATH.user_data])
  # except OSError:


if __name__ == '__main__':
  open_arg()
