#!/usr/bin/python
# -*- coding: utf-8 -*-
from pprint import pprint
import uniout
import pdb
raw_name_list =[
    "黃莉婷",
    "陳文昌"
]

staffs = {}
override_counter = 0

for name in raw_name_list:
    print name
    print name.decode('utf-8')[0] 