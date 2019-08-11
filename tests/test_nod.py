#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest

from warg.named_ordered_dictionary import IllegalAttributeKey

__author__ = "cnheider"


def test_attribute_assignment():
  nodict = NamedOrderedDictionary()
  nodict.paramA = "str_parameter"
  nodict.paramB = 10
  assert nodict.paramA == "str_parameter"
  assert nodict.paramB == 10


def test_16():
  nodict = NamedOrderedDictionary({"paramA":"str_parameter", "paramB":10})
  assert nodict.paramA == "str_parameter"
  assert nodict.paramB == 10


def test_15():
  nodict = NamedOrderedDictionary()
  nodict.update({"paramA":20, "paramB":"otherparam", "paramC":5.0})
  nodict.paramA = 10
  assert nodict.paramA == 10
  assert nodict.paramB == "otherparam"


def test_11():
  nodict = NamedOrderedDictionary()
  nodict["paramA"] = 10
  assert nodict.paramA == 10


def test_14():
  vals = [1, 3, 5]
  nodict = NamedOrderedDictionary(10, val2=2, *vals)
  nolist = nodict.as_list()
  assert nolist[0] == 10
  assert nodict.val2 == 2
  assert nolist[-2] == vals[-1]


def test_1():
  nodict = NamedOrderedDictionary("str_parameter", 10)
  odict = {**nodict}
  assert nodict.as_list()[0] == list(odict.values())[0]


def test_13():
  nodict = NamedOrderedDictionary("str_parameter", 10)
  nodict.update(arg1=20, arg0="otherparam")
  assert nodict.arg0 == "otherparam"
  assert nodict.arg1 == 20


def test_12():
  nodict = NamedOrderedDictionary("str_parameter", 10)
  nodict.update({"arg1":20, "arg0":"otherparam"})
  assert nodict.arg0 == "otherparam"
  assert nodict.arg1 == 20


def test_no_existing_attr():
  nodict = NamedOrderedDictionary(paramA="str_parameter", paramB=10)
  nodict.update(20, "otherparam")
  assert nodict.paramB == "otherparam"
  assert nodict.paramA == 20
  assert nodict.get("paramC") == None


def test_existing_map_unpacking():
  nodict = NamedOrderedDictionary(paramA="str_parameter", paramB=10)
  nodict.update(20, "otherparam")
  nodict = NamedOrderedDictionary(paramC="str_parameter", **nodict)
  assert nodict.paramB == "otherparam"
  assert nodict.paramA == 20
  assert nodict.get("paramC") != None


def test_as_list():
  arg0, arg1 = NamedOrderedDictionary("str_parameter", 10).as_list()
  assert arg0 == "str_parameter"
  assert arg1 == 10


def test_access_operators():
  arg0, arg1 = NamedOrderedDictionary("str_parameter", 10).as_list()
  columns = NamedOrderedDictionary.nod_of(arg1, aræa=arg0)
  assert columns["arg1"] == arg1
  assert columns.arg1 == arg1
  assert columns["aræa"] == arg0
  assert columns / "aræa" == arg0
  assert id(columns / "aræa") == id(columns["aræa"])


def test_new_attr_on_existing():
  a = NamedOrderedDictionary(4, 2)
  a.list = "a"
  assert a.list == "a"


def test_addition_arithmetic():
  a = NamedOrderedDictionary(4, 2)
  b = a + a
  assert a.as_list() == [8, 4]


def test_illegal_overwrite():
  with pytest.raises(IllegalAttributeKey) as exc_info:
    NamedOrderedDictionary(update=2)

  assert exc_info.type is IllegalAttributeKey
