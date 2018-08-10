# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 17:35:59 2018

@author: ZZw
"""
import numpy as np
from matplotlib import pyplot as plt
from collections import deque
class Sequence:
    def __init__(self,length, width, pocket,cut_depth ):
        self.a = "aba"
        self.length = length
        self.width = width
        self.pocket = pocket
        self.cut_depth = cut_depth 
        self.num_pocket = pocket.shape[0]
        self.machine = self.machine_area()
        self.machined = self.machine_area()
        self.have_machined = []
        self.part = np.ones([self.width,self.length])
    #测试 用于绘制零件
    def draw_part(self):
        part = self.part.copy()
        for pockets in self.pocket: 
            part[pockets[1]:pockets[3],pockets[0]:pockets[2]]=2
        plt.imshow(part)
    def draw_part_machined(self):
        plt.imshow(self.part)
        
    #加工的区域
    def machined_area(self,med):   
        allowed = self.allow_machine()
        if med not in allowed:
            raise ValueError("machined area not in the allowd machine area")
        for i,po in enumerate(self.machined):
            if (po[0] == med) and (med in allowed):
                self.machined[i].popleft()
                self.have_machined.append(med)
                self.part[med[1]:med[3],med[0]:med[2]] = -1
                
    #可以加工的区域
    def machine_area(self):
        machine = list()
        for j,pockets in enumerate(self.pocket):
            po = deque()
            cut_layer = int((pockets[3]-pockets[1])/self.cut_depth)
            for i in range(cut_layer+1):
                po.append([pockets[0],pockets[1]+i*self.cut_depth,pockets[2],pockets[1]+(i+1)*self.cut_depth])
            machine.append(po)
        return(machine)
    #允许加工的区域
    def allow_machine(self):
        allowed = []
        for i,po in enumerate(self.machined):
            pc = po.copy()
            allowed.append(pc.popleft())
        return(allowed)
       
    def reward(self):
        print(0)
        
    
    
if __name__ == "__main__":
    length = 68
    width = 30
    cut_depth = 2
    pocket = np.array([[4,0,16,20],[20,0,32,20],[36,0,48,20],[52,0,64,20]])
    Se = Sequence(length,width,pocket,cut_depth)
    allow = Se.allow_machine()
    med = [4,0,16,2]
    print(Se.machine)
    Se.machined_area(med)
    print(Se.machined)
    allow = Se.allow_machine()
    print(allow)
    Se.draw_part_machined()
    
    med = [4,2,16,4]
    print(Se.machine)
    Se.machined_area(med)
    print(Se.machined)
    allow = Se.allow_machine()
    print(allow)
    Se.draw_part_machined()
    
    med = [20,0,32,2]
    print(Se.machine)
    Se.machined_area(med)
    print(Se.machined)
    allow = Se.allow_machine()
    print(allow)
    Se.draw_part_machined()
    
    
