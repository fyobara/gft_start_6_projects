vitorias = int(input("Insira o Número de Vitórias: "))
derrotas = int(input("Insira o Número de Derrotas: "))
saldo = vitorias - derrotas

if saldo < 10:
    print(f"O Herói tem de saldo de {saldo} e Seu Nível é Ferro")
elif saldo < 20:
    print(f"O Herói tem de saldo de {saldo} e Seu Nível é Bronze")
elif saldo < 50:
    print(f"O Herói tem de saldo de {saldo} e Seu Nível é Prata")
elif saldo < 80:
    print(f"O Herói tem de saldo de {saldo} e Seu Nível é Ouro")
elif saldo < 90:
    print(f"O Herói tem de saldo de {saldo} e Seu Nível é Diamante")
elif saldo < 10000:
    print(f"O Herói tem de saldo de {saldo} e Seu Nível é Lendário")
else:
    print(f"O Herói tem de saldo de {saldo} e Seu Nível é Imortal")