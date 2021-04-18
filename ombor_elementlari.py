# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 17:47:30 2021

@author: Fotth_feruz
"""


ombor = [] # bo'sh ro'yxat
print("Ro'xatni to'diring")
k=int(input("Ro'yxat elementlari soni nechta:\n>>>"))
for n in range(k): # n bu yerda 0 dan k gacha qiymatlar oladi
    ombor.append(input(f"{n+1}-ro'yxat elementlarini kiriting: \n>>>"))
print(ombor)
