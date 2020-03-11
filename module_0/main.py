import random
r_number = int(input('Введите число от 1 до 100'))

x = 1
y = 100
guess = random.randint(x,y)
count = 1

if r_number == guess:
    print('С первой попытки!')
else:
    while guess != r_number:
        if r_number > guess:
            print("Загаданное число больше: ", guess)
            x = guess
            guess = random.randint(x,y)
            count += 1
        elif r_number < guess:
            print("Загаданное число меньше: ", guess)
            y = guess
            guess = random.randint(x,y)
            count += 1
    print (r_number)
    print ('Вы угадали с', count, 'попытки')
