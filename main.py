color1 = input()
color2 = input()

red = 'красный'
blue = 'синий'
yellow = 'желтый'

if (color1 == red and color2 == blue) or (color2 == red and color1 == blue):
    print('фиолетовый')
elif (color1 == red and color2 == yellow) or (color2 == red and color1 == yellow):
    print('оранжевый')
elif (color1 == blue and color2 == yellow) or (color2 == blue and color1 == yellow):
    print('зеленый')
elif color1 == color2 == red:
    print(red)
elif color1 == color2 == blue:
    print(blue)
elif color1 == color2 == yellow:
    print(yellow)      
else:
    print('ошибка цвета')