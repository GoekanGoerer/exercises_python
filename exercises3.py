def steigung_funktion(x1, y1, x2, y2):
    my_steigung = (y2-y1)/(x2-x1)
    print(my_steigung)
    if my_steigung == 0:
        print("Die Steigung ist nicht definiert.")
    
    
steigung_funktion(4, 4, 8, 4)

