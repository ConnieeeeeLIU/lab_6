#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 15:22:44 2018

@author: liuconnie
"""

import random

def pancake(lst):
    for i in range(len(lst)):
        max_index = lst.index(max(lst[:len(lst)-i]))
        first_half = lst[:max_index+1]
        first_half.reverse()
        second_half = lst[max_index+1:len(lst)-i]
        layer_lst = []
        layer_lst = first_half + second_half
        layer_lst.reverse()
        new_lst = layer_lst + lst[len(lst)-i:]
        lst = new_lst
            
    return lst
    
    
    
def main():
    n = int(input("n: "))
    lst = random.sample([i for i in range(100)],n)
    print(lst)
    print(pancake(lst))
    
main()