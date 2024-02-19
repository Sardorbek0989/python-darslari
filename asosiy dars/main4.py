sekund = int(input("sekundni kirit: "))

soat = sekund // 3600
sekund %= 3600

minut = sekund // 60
sekund %= 60

print(soat, minut, sekund)