# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
def function (X, Y, Z):
    print(not (X or Y or Z) == (not X and not Y and not Z))
function(1, 2, 3)
function(3, 2, 1)
function(2, 2, 2)

