# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 22:51:38 2024

@author: Luiz
"""


def min_val(my_dict):
    min_value = min(my_dict.values())
    return [key for key, value in my_dict.items() if value == min_value][0]


out = []


def find_closest(date):
    offset = {}
    for hour in [0, 6, 12, 18]:
        target = dt.datetime(
            date.year, 
            date.month, 
            date.day, 
            hour
            )
        if date.hour >= 18:
            target += dt.timedelta(days=1)
            
            return target
            
        offset[target] = abs(date - target).seconds / 3600

    return offset #min_val(offset)