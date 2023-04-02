x = int(input())  # ввод количества монеток
count_heads = 0  # счетчик решек
count_tails = 0  # счетчик гербов

for i in range(x):
    side = input()  # ввод стороны монетки

    if side == 'Орел':  # проверка на решку
        count_heads += 1
    else:  # если не решка, то герб
        count_tails += 1

min_flips = min(count_heads, count_tails)  # вычисляем минимальное количество переворотов
print(min_flips)  # выводим на экран