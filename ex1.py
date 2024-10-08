xp = int(input("Insira seu XP: "))

if xp < 1000:
    print("Seu Nível é Ferro")
elif xp < 2000:
    print("Seu Nível é Bronze")
elif xp < 5000:
    print("Seu Nível é Prata")
elif xp < 7000:
    print("Seu Nível é Ouro")
elif xp < 8000:
    print("Seu Nível é Platina")
elif xp < 9000:
    print("Seu Nível é Ascendente")
elif xp < 10000:
    print("Seu Nível é Imortal")
else:
    print("Seu Nível é Radiante")