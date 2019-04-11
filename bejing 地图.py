# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 09:33:56 2018

@author: microsoft
"""
import urllib.request as req
import os
import conda

conda_file_dir = conda.__file__
conda_dir = conda_file_dir.split('lib')[0]
proj_lib = os.path.join(os.path.join(conda_dir, 'share'), 'proj')
os.environ["PROJ_LIB"] = proj_lib
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from numpy import *
from pylab import *



map = Basemap(projection='robin', lon_0=0, resolution='c')
                                      #设定了投影方法，球形的地球表面投影到平面地图
Labeijing=39.91
Lobeijing=116.39
x,y=map(Lobeijing,Labeijing)
map.scatter(x,y,s=10,marker='o',color='r')
map.scatter(x,y,s=60,marker='o',color='none',edgecolor='r')
# 标记汉字“北京”字样
plt.text(x, y,u'北京', color = 'b', fontsize=10)
# 绘制地图（元素）：
map.drawcoastlines(linewidth=0.25)               #绘制海岸线
map.drawcountries(linewidth=0.25)                #绘制国界线
map.drawmapboundary(fill_color=(0.8, 0.95, 1.0)) #画出地图边界，并填充背景（海洋）
                                                 #color第四位为透明度
map.fillcontinents(color=(1,0.9,0.7),lake_color=(0.8, 0.95, 1.0),zorder=0)
                                                 #填充大陆
plt.show()