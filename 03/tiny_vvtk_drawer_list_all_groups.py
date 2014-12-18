#!/usr/bin/python
# -*- coding: utf-8 -*-
import uniout

vvtk_name_list =[
    ["稽核室","A00699","黃莉婷",],
    ["董事長室","A00001","陳文昌"],
    ["董事長室","A00002","許維城"],
    ["董事長室","A00003","批歐西"],
]
vvtk_staff_dict = {}

for person in vvtk_name_list:
    depart = person[0]
    staff_id = int(person[1][1:]) # "A00699" -> 699
    name = person[2]
    if depart not in vvtk_staff_dict:
        vvtk_staff_dict[depart] = []
    vvtk_staff_dict[depart].append([name, staff_id])

for depart in vvtk_staff_dict.keys(): # fetch all keys in  vvtk_staff_dict
    print("{0}: number of members {1}".format(depart, len(vvtk_staff_dict[depart])))
    for person in vvtk_staff_dict[depart]:
        print(person)