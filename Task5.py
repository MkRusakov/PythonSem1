# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
from math import sqrt
import math
# Расскажите, пожалуйста, про две команды сверху. Почему они автоматически появились и почему без них код не работает?
def DistancePoints (X1, Y1, X2, Y2):
    result = math.sqrt((X2 - X1) * (X2 - X1) + (Y2 - Y1)* (Y2 - Y1))
    print(round(result, 2))
DistancePoints(3, 6, 2, 1)
DistancePoints(7, -5, 1, -1)