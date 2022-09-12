a = int(input("Введите колиечство билетов:"))
if a <= 0:
    raise ValueError("Введите число больше нуля")
L = [int(input("Введите возраст покупателя билета № %d: "%(j+1))) for j in range(a)]

S = 0
for k in range(len(L)):
    if L[k] < 18:
            S = S+0 #Вероятно это не нужно, делала для наглядности
    elif 18<=L[k]<25:
            S=S+990
    elif L[k]>=25:
            S=S+1390

if a>3:
    cost=S-(S*10/100)
else:
    cost=S
print ("Стоимость ваших билетов:")
print (cost)
