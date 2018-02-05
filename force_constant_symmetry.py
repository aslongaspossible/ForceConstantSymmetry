# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 11:00:29 2018

I have a force constants matrix and want to make it an invariant symmetric
matrix under some space group.

@author: Luddite
"""

import numpy as np

class ForceConstantSymmetry:
    
    def __strToFloat(self,strLine):
        return list(map(float,strLine));
    
    def __init__(self, fcPathname="FORCE_CONSTANTS"):
        with open(fcPathname, 'r') as fcFile:
            order=int(fcFile.readline());
            fcMatrix=[];
            for row in range(0,order):
                fcSubline=[];
                for column in range(0,order):
                    fcFile.readline();
                    fcLine=fcFile.readline();
                    fcSubX=self.__strToFloat(fcLine.split());
                    fcLine=fcFile.readline();
                    fcSubY=self.__strToFloat(fcLine.split());
                    fcLine=fcFile.readline();
                    fcSubZ=self.__strToFloat(fcLine.split());
                    fcSubline.append(np.vstack([fcSubX, fcSubY, fcSubZ]));
                fcMatrix.append(np.hstack(fcSubline));
            self.__originFC=np.vstack(fcMatrix);
            
    
                    
                    
            
        