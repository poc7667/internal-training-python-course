#!/usr/bin/python
# -*- coding: utf-8 -*-
import uniout

vvtk_name_list =[
    ["稽核室","A00699","黃莉婷",],
    ["董事長室","A00001","陳文昌",]
]
vvtk_staff_dict = {}

for person in vvtk_name_list:
    depart = person[0]
    staff_id = int(person[1][1:]) # "A00699" -> 699
    name = person[2]
    vvtk_staff_dict[name] = [depart, staff_id]

print(vvtk_name_list)
print(vvtk_staff_dict)