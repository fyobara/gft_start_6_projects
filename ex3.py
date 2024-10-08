class Hero:
    def __init__(self, nome, idade, tipo) -> None:
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def ataque(self):
        if self.tipo == "Mago":
            print("Mago atacou usando Magia")
        elif self.tipo == "Guerreiro":
            print("Guerreiro atacou usando Espada")
        elif self.tipo == "Monge":
            print("Monge atacou usando Artes Marciais")
        elif self.tipo == "Ninja":
            print("Ninja atacou usando Shuriken")
        else:
            print(f"{self.tipo} atacou usando Nada")

def main():

    nome = input("Insira o Nome do Herói")
    idade = int(input("Insira a Idade do Herói"))
    tipo = input("Insira o Tipo do Herói")

    heroi = Hero(nome, idade, tipo)
    heroi.ataque()


if __name__ == "__main__":
    main()