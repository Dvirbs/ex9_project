car_color = str(input('\n*** write the first capital latter of car color that you wont to move (Blue-->B): *** \n'))
while (len(car_color) != 1) or (type(car_color) != str) or car_color.islower():
    car_color = str(
        input('\n*** write the first capital latter of car color that you wont to move (Blue-->B) *** \n'))