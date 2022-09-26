# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
def function (X, Y, Z):
    print(not (X or Y or Z) == ((not X) and (not Y) and (not Z)))
function(10, -4, 3)
function(10, 4, -7)
function(-8, 2, 6)
function(8, 2, 6)
function(-8, -2, -6)
function(8, 8, 8)
function(-8, -8, -8)
function(0, 0, 0)
# И это правильно? Что-то я не совсем понял ТЗ
