# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 10:59:02 2021
@author: user
"""

import seaborn as sb
import matplotlib.pyplot as m

i=sb.load_dataset("titanic")
sb.swarmplot(x="survived",y="age",data=i)
m.show()