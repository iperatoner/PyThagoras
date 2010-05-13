#!/usr/bin/env python3

'''
@author: stfischr
@modified: E.C.
'''

from decimal import *
import math

getcontext().prec = 100

class Triangle(object):
    
    def __init__(self):
        self._line_a =  0
        self._line_b = 0
        self._line_c = 0
        self._line_p = 0
        self._line_q = 0
        self._line_h = 0
        self._area_A = 0
        self._angle_alpha = 0
        self._angle_beta = 0
        
        self.triangle_vars = [self._line_a, self._line_b, self._line_c,
                              self._line_p, self._line_q, self._line_h,
                              self._area_A, self._angle_alpha, self._angle_beta]

        self.valid_triangle = False
        self.exact_triangle = True
        

    def validation(self, triangle_vars):
        # Zählt die gegebenen Werte (0 entspricht "unbekannt")
        # Bin mir nicht sicher, ob wir das nicht besser in die API oder
        # in die jeweiligen Interfaces einbauen sollten
        self.number_of_not_0 = 0
        if 0 in self.triangle_vars:
            for i in self.triangle_vars:
                if i != 0:
                    self.number_of_not_0 += 1

        if self.number_of_not_0 == 2:
            self.valid_triangle = True
        elif self.triangle_vars[-1] != 0 and self.triangle_vars[-2] != 0:
            self.valid_triangle = False
        else:
            self.valid_triangle = False
            

    def set_value(self, triangle_vars):
        # Funktion erlaubt bequem per Übergabe einer Liste das setzen der Werte
        self.triangle_vars = triangle_vars
        self.validation(dreieck.triangle_vars)

 

    def get_value(self):
        return self.triangle_vars, self.exact_triangle

    def calc_a(self):
        if self._line_a == 0:
            if self._line_b != 0 and self._line_c != 0:
                a = (self._line_c**2 - self._line_b**2).sqrt()

            elif self._line_b != 0 and self._anchor_beta != 0:
                a = self._line_b/math.tan(self._anchor_beta)
                
            elif self._line_c != 0 and self._line_p != 0:
                a = math.sqrt(self._line_c * self._line_p)

            elif self._line_c != 0 and self._angle_alpha != 0:
                a = math.sin(self._angle_alpha) * self._line_c

            elif self._line_h != 0 and self._anchor_beta != 0:
                a = self._line_h/math.sin(self._anchor_beta)

            elif self._line_b != 0 and self._anchor_alpha != 0:
                a = b*math.tan(self._anchor_alpha)

            elif self._line_c != 0 and self._anchor_beta != 0:
                a = c*math.cos(self._anchor_beta)

            elif self._line_p != 0 and self._anchor_beta != 0:
                a = self._line_p/math.cos(self._anchor_beta)

            elif self._line_h != 0 and self._anchor_beta != 0:
                a = self._line_h / math.sin(self._anchor_beta)

            elif self._area_A != 0 and self._line_b != 0:
                a = self._area_A/(0.5*self._line_b)

            elif self._line_p != 0 and self._line_h != 0:
                a = math.sqrt(self._line_p**2 + self._line_h**2)

            self._line_a = a

        return self._line_a

    def calc_b(self):
        if self._line_b == 0:
            if self._line_a != 0 and self._line_c != 0:
                b = (self._line_c**2 - self._line_b**2).sqrt()

            '''elif self._line_c != 0 and self._line_p != 0:
                a = (self._line_c * self._line_p).sqrt()

            elif self._line_c != 0 and self._angle_alpha != 0:
                a = math.sin(self._angle_alpha) * self._line_c

            elif self._line_h != 0 and self._anchor_beta != 0:
                a = self._line_h/math.sin(self._anchor_beta)

            self._line_a = a

        return self._line_a'''


    def calc_c(self):
        if self._line_c == 0:
            if self._line_a != 0 and self._line_b != 0:   
                c = (self._line_a**2 + self._line_b**2).sqrt()
                
            elif self._line_h != 0 and self._area_A != 0:
                c = self._area_A*2 / self._line_h
                
            elif self._line_p != 0 and self._line_q != 0:
                c = self._line_p + self._line_q

            elif self._line_a != 0 and self._angle_alpha != 0:
                c = self._line_a / math.sin(self._angle_alpha)

            elif self._line_b != 0 and self._angle_beta != 0:
                c = self._line_b / math.sin(self._angle_beta)

            self._line_c = c

        return self._line_c

    def calc_alpha(self):
        if self._angle_alpha == 0:
            if self._angle_beta != 0:
                alpha = (90 - self._angle_beta)

            elif self._line_a != 0 and self._line_c != 0:
                alpha = math.asin(self._line_a / self._line_c)

            elif self._line_h != 0 and self._line_b != 0:
                alpha = math.asin(self._line_h / self._line_b)

            self._angle_alpha = alpha

        return self._angle_alpha

    def calc_beta(self):
        if self._angle_beta == 0:
            if self._angle_alpha != 0:
                alpha = (90 - self._angle_alpha)

            elif self._line_a != 0 and self._line_c != 0:
                beta = math.asin(self._line_b / self._line_c)

            elif self._line_h != 0 and self._line_a != 0:
                beta = math.asin(self._line_h / self._line_a)

            self._angle_beta = beta

        return self._angle_beta
        

dreieck = Triangle()
dreieck.set_value([0, 0, 35, 0, 0, 0, 0, 0, 21])
print("Valid triangle: " + str(dreieck.valid_triangle))
print(dreieck.get_value())
