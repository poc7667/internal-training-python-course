#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#standard lib
import argparse
import pprint
import re
import os
import pdb
from pprint import pprint
from timeit import default_timer as timer
#3rd part lib
# from common import *
import xlrd
from xlutils.copy import copy as xlscopy
import xlwt
# from __future__ import division # division
from collections import OrderedDict
from xlwt import Style
from xlrd import open_workbook,cellnameabs

def get_row(sht):
    for i_row in range(1,sht.nrows):
        name_list_row = ""
        for cell in sht.row_values(i_row):
            name_list_row += "\"{0}\",".format(cell)
        yield "[{0}],".format(name_list_row)

def read_vvtk_name_list(file_name):
    rd_bk = xlrd.open_workbook(file_name)
    with open('read_vvtk_name_list.txt', 'w') as outfile :
        for sheet_index in rd_bk._all_sheets_map:
            sht = rd_bk.sheet_by_index(0)
            for row in get_row(sht):
                print(row)
                outfile.write(str(row)+'\n')

read_vvtk_name_list(sys.argv[1])