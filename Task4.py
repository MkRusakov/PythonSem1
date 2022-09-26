# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# def RangePoint (quarter):
#     if quarter == 1:
#         print("Coordinates of point: 0 < X < +∞ and 0 < Y < +∞ ")
#     elif quarter == 2:
#         print("Coordinates of point: 0 > X > -∞ and 0 < Y < +∞ ")
#     elif quarter == 3:
#         print("Coordinates of point: 0 > X > -∞ and 0 > Y > -∞ ")
#     elif quarter == 4:
#         print("Coordinates of point: 0 < X < +∞ and 0 > Y > -∞ ")

# Или вот так:
def RangePoint (quarter):
    if quarter == 1:
        print("Coordinates of point: X = (0; +∞); Y = (0; +∞)")
    elif quarter == 2:
        print("Coordinates of point: X = (0; -∞); Y = (0; +∞)")
    elif quarter == 3:
        print("Coordinates of point: X = (0; -∞); Y = (0; -∞)")
    elif quarter == 4:
        print("Coordinates of point: X = (0; +∞); Y = (0; -∞)")

RangePoint(1)
RangePoint(2)
RangePoint(3)
RangePoint(4)
