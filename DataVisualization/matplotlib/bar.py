#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 20:55:00 2020

@author: zaron
"""

import matplotlib.pyplot as plt
import pickle

# load data
with open('coding-exp-by-dev-type.pickle', 'rb') as f:
    data = pickle.load(f)

# split into two lists
dev_types, years_exp = zip(*data)

bar_coords = range(len(dev_types))

plt.barh(bar_coords, years_exp)
plt.xlabel('years')
plt.title('Years of Coding Experience by Developer Type')
plt.yticks(bar_coords, dev_types, fontsize=8)
plt.tight_layout()
plt.show()