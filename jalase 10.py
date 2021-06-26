# class Triangle:
#     def __init__(self,angle1,angle2,angle3):
#         self.angle1 = int(angle1)
#         self.angle2 = int(angle2)
#         self.angle3 = int(angle3)
#
#     def set_angle1(self):
#         return self.angle1
#     def set_angle2(self):
#         return self.angle2
#     def set_angle3(self):
#         return self.angle3
#
#     def get_angles(self, angle1, angle2, angle3):
#         if angle1+angle2+angle3 != 180:
#             raise ValueError("180 nist")
#         else:
#             print('nist')
#
# myriangle = Triangle(100,10,70)
# tiangle1 = myriangle.set_angle1()
# tiangle2 = myriangle.set_angle2()
# tiangle3 = myriangle.set_angle3()
# print(myriangle.get_angles(tiangle1,tiangle2,tiangle3))
#




# class Shape():
#     def __init__(self):
#         self.height = 0
#         self.ghaede = 0
#     def mashat(self):
#         pass
#     def mohit(self):
#         pass
#
# class Triangle(Shape):
#     def masahat(self,height,ghaede):
#         return height * ghaede / 2
#
# class Square(Shape):
#     def mohit(self):
#         return self.ghaede * self.ghaede
#
#
# sh = Shape()
# tr=Triangle()
# print(tr.masahat(5,10))
# sq = Square()
# print(sq.mohit(5))




class Employee():
    def __init__(self,peronalcode,resume):
        self.__peronalcode = peronalcode
        self.__resume=resume

    def __str__(self):
        super().__init__().__str__()



class Hourly(Employee):
    def __init__(self,peronalcode,resume,hz):
        super().__init__(peronalcode,resume).__str__()
        self.__hz = hz



class Full_time(Employee):
    def __init__(self,peronalcode,resume,hoghogh):
        super(Full_time, self).__init__(peronalcode,resume)
        self.__hoghogh = hoghogh




