def my_function(x, y):
    if x % y == 0:
        print("x ist durch y teilbar")
    if y == 0:
        print("Es ist nicht möglich durch 0 zu teilen!")
    if x == y:
        print("x und y sind gleich")


print(my_function(1, 2))