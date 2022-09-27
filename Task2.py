# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
import random
def function (X, Y, Z):
    print(not (X or Y or Z) == ((not X) and (not Y) and (not Z)))
function(random.choice([True, False]), random.choice([True, False]), random.choice([True, False]))
