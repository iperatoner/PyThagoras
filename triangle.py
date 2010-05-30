#!/usr/bin/env python3

import math


class Triangle(object):
    
    def __init__(self):
        self._line_a = 0 """a First (right) cathetus of the triangle """
        self._line_b = 0 """b Second (left) cathetus of the triangle """
        self._line_c = 0 """c Hypotenuse of the triangle"""
        self._line_p = 0 """p Part of c right of the intersection with h"""
        self._line_q = 0 """q Part of c left of the intersection with h"""
        self._line_h = 0 """h Height of the triangle"""
        self._area_A = 0 """A Area of the triangle"""
        self._angle_alpha = 0 """alpha Angle between line b and c"""
        self._angle_beta = 0 """beta Angle between line a and c"""
        
        self.triangle_vars = [self._line_a, self._line_b, self._line_c,
                              self._line_p, self._line_q, self._line_h,
                              self._area_A, self._angle_alpha, self._angle_beta]
                              """Array for comfortably handing over the
                               variables"""

        self.valid_triangle = False 
        """Information whether the triangle is valid"""
        self.exact_triangle = True
        

    def validation(self, triangle_vars):
        """ Validates the provided informations (0 equals unknown)"""
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
        """ Set-Method enabling a comfortable way of handing over 
        the necessary information as a list"""
        self.triangle_vars = triangle_vars
        self.validation(dreieck.triangle_vars)

 

    def get_value(self):
        """ Get-Method for handing over the variable-values"""
        return self.triangle_vars, self.exact_triangle

    def calc_a(self):
        """ Method for calculating the value of line_a if still missing"""
        if self._line_a == 0:
            if self._line_b != 0 and self._line_c != 0:
                self._line_a = (self._line_c**2 - self._line_b**2).sqrt()

            elif self._line_b != 0 and self._angle_beta != 0:
                self._line_a = self._line_b/math.tan(self._angle_beta)
                
            elif self._line_c != 0 and self._line_p != 0:
                self._line_a = math.sqrt(self._line_c * self._line_p)

            elif self._line_c != 0 and self._angle_alpha != 0:
                self._line_a = math.sin(self._angle_alpha) * self._line_c

            elif self._line_h != 0 and self._angle_beta != 0:
                self._line_a = self._line_h/math.sin(self._angle_beta)

            elif self._line_b != 0 and self._angle_alpha != 0:
                self._line_a = b*math.tan(self._angle_alpha)

            elif self._line_c != 0 and self._angle_beta != 0:
                self._line_a = c*math.cos(self._angle_beta)

            elif self._line_p != 0 and self._angle_beta != 0:
                self._line_a = self._line_p/math.cos(self._angle_beta)

            elif self._line_h != 0 and self._angle_beta != 0:
                self._line_a = self._line_h / math.sin(self._angle_beta)

            elif self._area_A != 0 and self._line_b != 0:
                self._line_a = self._area_A/(0.5*self._line_b)

            elif self._line_p != 0 and self._line_h != 0:
                self._line_a = math.sqrt(self._line_p**2 + self._line_h**2)

        return self._line_a

    def calc_b(self):
        """ Method for calculating the value of line_b if still missing"""
        if self._line_b == 0:
            if self._line_a != 0 and self._line_c != 0:
                self._line_b = math.sqrt(self._line_c**2 - self._line_a**2)

            elif self._line_a != 0 and self._area_A != 0:
                self._line_b = self._area_A/(0.5*self._line_a)

            elif self._line_c != 0 and self._angle_alpha != 0:
                self._line_b = math.cos(self._angle_alpha) * self._line_c

            elif self._line_a != 0 and self._angle_beta != 0:
                self._line_b = self._line_a/math.tan(self._angle_beta)
            
            elif self._line_a != 0 and self._angle_beta != 0:
                self._line_b = math.tan(self._angle_beta) * self._line_a

            elif self._line_c != 0 and self._angle_beta != 0:
                self._line_b = self._line_c * math.sin(self._angle_beta)

            elif self._line_h != 0 and self._line_q != 0:
                self._line_b = math.sqrt(self._line_h**2 - self._line_q**2)

            elif self._line_q != 0 and self._angle_alpha != 0:
                self._line_b = self._line_q / math.cos(self._angle_alpha)

            elif self._line_h != 0 and self._angle_alpha != 0:
                self._line_b = self._line_h / math.sin(self._angle_alpha)

        return self._line_a


    def calc_c(self):
        """ Method for calculating the value of line_c if still missing"""
        if self._line_c == 0:
            if self._line_a != 0 and self._line_b != 0:   
                self._line_c = math.sqrt(self._line_a**2 + self._line_b**2)
                
            elif self._line_h != 0 and self._area_A != 0:
                self._line_c = self._area_A*2 / self._line_h
                
            elif self._line_p != 0 and self._line_q != 0:
                self._line_c = self._line_p + self._line_q

            elif self._line_a != 0 and self._angle_alpha != 0:
                self._line_c = self._line_a / math.sin(self._angle_alpha)

            elif self._line_b != 0 and self._angle_beta != 0:
                self._line_c = self._line_b / math.sin(self._angle_beta)

            elif self._line_b != 0 and self._angle_alpha != 0:
                self._line_c = self._line_b / math.cos(self._angle_alpha)

            elif self._line_a != 0 and self._angle_beta != 0:
                self._line_c = self._line_a / math.cos(self._angle_beta)

            elif self._line_p != 0 and self._line_b != 0:
                self._line_c = ((math.sqrt(4*self._line_b**2+p**2))+p)/2

            elif self._line_q != 0 and self._line_q != 0:
                self._line_c = ((math.sqrt(4*self._line_a**2+q**2))+q)/2

        return self._line_c

    def calc_p(self):
        """ Method for calculating the value of line_p if still missing"""
        if self._line_p == 0:
            if self._line_a != 0 and self._line_q != 0:   
                self._line_p = ((math.sqrt(4*(a**2)+q**2))-q)/2
                
            elif self._line_h != 0 and self._line_a != 0:
                self._line_p = math.sqrt(a**2-h**2)
                
            elif self._line_c != 0 and self._line_q != 0:
                self._line_p = self._line_h**2/self._line_q

            elif self._line_q != 0 and self._area_A != 0:
                self._line_p = ((-6*math.sqrt(3)*self._area_A*
                      math.sqrt(27*self._area_A**2+self._line_q**4)+
                      54*self._area_A**2+self._line_q**4)**(1/3)+
                     (6*math.sqrt(3)*self._area_A*
                      math.sqrt(27*self._area_A**2+self._line_q**4)+
                      54*self._area_A**2+self._line_q**4)**(1/3)-2*
                     self._line_q**(4/3))/(3*self._line_q**(1/3))
                
            elif self._line_h != 0 and self._angle_beta != 0:
                self._line_p = self._line_h/math.sin(self._angle_beta)

            elif self._line_h != 0 and self._area_A != 0:
                self._line_p = 2*self._area_A/self._line_h
            
        return self._line_p

    def calc_q(self):
        """ Method for calculating the value of line_q if still missing"""
        if self._line_q == 0:
            if self._line_b != 0 and self._line_p != 0:   
                self._line_q = ((math.sqrt(4*(b**2)+p**2))-p)/2
                
            elif self._line_h != 0 and self._line_b != 0:
                self._line_q = math.sqrt(b**2-h**2)

            elif self._line_c != 0 and self._line_p != 0:
                self._line_q = self._line_h**2/self._line_p

            elif self._line_p != 0 and self._area_A != 0:
                self._line_q = ((-6*math.sqrt(3)*self._area_A*
                      math.sqrt(27*self._area_A**2+self._line_p**4)+
                      54*self._area_A**2+self._line_p**4)**(1/3)+
                     (6*math.sqrt(3)*self._area_A*
                      math.sqrt(27*self._area_A**2+self._line_p**4)+
                      54*self._area_A**2+self._line_p**4)**(1/3)-2*
                     self._line_p**(4/3))/(3*self._line_p**(1/3))

            elif self._line_h != 0 and self._angle_alpha != 0:
                self._line_q = self._line_h/math.sin(self._angle_alpha)

            elif self._line_h != 0 and self._area_A != 0:
                self._line_q = 2*self._area_A/self._line_h

        return self._line_q

    def calc_h(self):
        """ Method for calculating the value of line_h if still missing"""
        if self._line_h == 0:
            if self._line a != 0 and self._line_ p != 0:
                self._line_h = math.sqrt(a**2-p**2)

            elif self._line_b != 0 and self._line_q != 0:
                self._line_h = math.sqrt(b**2-q**2)

            elif self._line_c != 0 and self._area_A != 0:
                self._line_h = (2*self._area_A)/self._line_c

            elif self._line_p != 0 and self._line_q != 0:
                self._line_h = math.sqrt(self._line_p*self._line_q)

            elif self._line_p != 0 and self._angle_beta != 0:
                self._line_h = self._line_p*math.cos(self._angle_beta)

            elif self._line_q != 0 and self._angle_alpha != 0:
                self._line_h = self._line_q*math.cos(self._angle_alpha)

        return self._line_h

    def clac_A(self):
        """ Method for calculating the value of the area A if still missing"""
        if self._area_A == 0:
            if self._line_a != 0 and self._line_b != 0:
                self._area_A = 0.5*(self._line_a*self._line_b)

            if self._line_c != 0 and self._line_h != 0:
                self._area_A = 0.5*(self._line_c*self._line_h)

        return self._area_A
    
    def calc_alpha(self):
        """ Method for calculating the value of the the angle alpha
         if still missing"""
        if self._angle_alpha == 0:
            if self._angle_beta != 0:
                self._angle_alpha = (90 - self._angle_beta)

            elif self._line_a != 0 and self._line_c != 0:
                self._angle_alpha = math.asin(self._line_a / self._line_c)

            elif self._line_h != 0 and self._line_b != 0:
                self._angle_alpha = math.asin(self._line_h / self._line_b)

        return self._angle_alpha

    def calc_beta(self):
        """ Method for calculating the value of the the angle beta
         if still missing"""
        if self._angle_beta == 0:
            if self._angle_alpha != 0:
                self._angle_beta = (90 - self._angle_alpha)

            elif self._line_a != 0 and self._line_c != 0:
                self._angle_beta = math.asin(self._line_b / self._line_c)

            elif self._line_h != 0 and self._line_a != 0:
                self._angle_beta = math.asin(self._line_h / self._line_a)

        return self._angle_beta
        

dreieck = Triangle()
dreieck.set_value([0, 0, 0, 0, 3, 0, 8, 0, 0])
print("Valid triangle: " + str(dreieck.valid_triangle))
print(dreieck.get_value())
