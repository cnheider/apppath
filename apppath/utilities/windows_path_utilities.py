#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

__author__ = "Christian Heider Nielsen"
__doc__ = ""

__all__ = ["get_win_folder", "SYSTEM"]

from typing import Any

PY3 = sys.version_info[0] == 3

if PY3:
  unicode = str


def _get_win_folder_from_registry(csidl_name: Any) -> Any:
  """This is a fallback technique at best. I'm not sure if using the
registry for this guarantees us the correct answer for all CSIDL_*
names.
"""
  if PY3:
    import winreg as _winreg
  else:
    import _winreg

  shell_folder_name = {
      "CSIDL_APPDATA":       "AppData",
      "CSIDL_COMMON_APPDATA":"Common AppData",
      "CSIDL_LOCAL_APPDATA": "Local AppData",
      }[csidl_name]

  key = _winreg.OpenKey(
      _winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
      )
  dir, type = _winreg.QueryValueEx(key, shell_folder_name)
  return dir


def _get_win_folder_with_pywin32(csidl_name: Any) -> Any:
  from win32com.shell import shellcon, shell

  dir = shell.SHGetFolderPath(0, getattr(shellcon, csidl_name), 0, 0)
  # Try to make this a unicode path because SHGetFolderPath does
  # not return unicode strings when there is unicode data in the
  # path.
  try:
    dir = unicode(dir)

    # Downgrade to short path name if have highbit chars. See
    # <http://bugs.activestate.com/show_bug.cgi?id=85099>.
    has_high_char = False
    for c in dir:
      if ord(c) > 255:
        has_high_char = True
        break
    if has_high_char:
      try:
        import win32api

        dir = win32api.GetShortPathName(dir)
      except ImportError:
        pass
  except UnicodeError:
    pass
  return dir


def _get_win_folder_with_ctypes(csidl_name: Any) -> Any:
  from ctypes import windll, create_unicode_buffer

  csidl_const = {"CSIDL_APPDATA":26, "CSIDL_COMMON_APPDATA":35, "CSIDL_LOCAL_APPDATA":28}[csidl_name]

  buf = create_unicode_buffer(1024)
  windll.shell32.SHGetFolderPathW(None, csidl_const, None, 0, buf)

  # Downgrade to short path name if have highbit chars. See
  # <http://bugs.activestate.com/show_bug.cgi?id=85099>.
  has_high_char = False
  for c in buf:
    if ord(c) > 255:
      has_high_char = True
      break
  if has_high_char:
    buf2 = create_unicode_buffer(1024)
    if windll.kernel32.GetShortPathNameW(buf.value, buf2, 1024):
      buf = buf2

  return buf.value


def _get_win_folder_with_jna(csidl_name: Any) -> Any:
  import array
  from com.sun import jna
  from com.sun.jna.platform import win32

  buf_size = win32.WinDef.MAX_PATH * 2
  buf = array.zeros("c", buf_size)
  shell = win32.Shell32.INSTANCE
  shell.SHGetFolderPath(None, getattr(win32.ShlObj, csidl_name), None, win32.ShlObj.SHGFP_TYPE_CURRENT, buf)
  dir = jna.Native.toString(buf.tostring()).rstrip("\0")

  # Downgrade to short path name if have highbit chars. See
  # <http://bugs.activestate.com/show_bug.cgi?id=85099>.
  has_high_char = False
  for c in dir:
    if ord(c) > 255:
      has_high_char = True
      break
  if has_high_char:
    buf = array.zeros("c", buf_size)
    kernel = win32.Kernel32.INSTANCE
    if kernel.GetShortPathName(dir, buf, buf_size):
      dir = jna.Native.toString(buf.tostring()).rstrip("\0")

  return dir


get_win_folder = None

if sys.platform.startswith("java"):
  import platform

  os_name = platform.java_ver()[3][0]
  if os_name.startswith("Windows"):  # "Windows XP", "Windows 7", etc.
    SYSTEM = "win32"
  elif os_name.startswith("Mac"):  # "Mac OS X", etc.
    SYSTEM = "darwin"
  else:  # "Linux", "SunOS", "FreeBSD", etc.
    # Setting this to "linux2" is not ideal, but only Windows or Mac
    # are actually checked for and the rest of the module expects
    # *sys.platform* style strings.
    SYSTEM = "linux2"
else:
  SYSTEM = sys.platform

if SYSTEM == "win32":  # IMPORT TESTS
  try:
    from win32com import shell

    get_win_folder = _get_win_folder_with_pywin32
  except ImportError:
    try:
      from ctypes import windll

      get_win_folder = _get_win_folder_with_ctypes
    except ImportError:
      try:
        from com.sun import jna

        get_win_folder = _get_win_folder_with_jna
      except ImportError:
        get_win_folder = _get_win_folder_from_registry
