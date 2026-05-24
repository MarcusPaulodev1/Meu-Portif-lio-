import random


class Perfil:
    def __init__(self, nivel=1, experiencia=0):
        self.nivel = nivel
        self.experiencia = experiencia

    def ganhar_experiencia(self, xp):
        self.experiencia += xp

        if self.experiencia >= 100:
            self.nivel += 1
            self.experiencia -= 100
            print(f"Você subiu para o nível {self.nivel}!")


class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.perfil = Perfil()
        self.personagens = []

    def adicionar_personagem(self, personagem):
        self.personagens.append(personagem)


class Personagem:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.vida = 100
        self.ataque = random.randint(10, 20)
        self.defesa = random.randint(3, 8)
        self.missoes = []

    def atacar(self):
        return random.randint(5, self.ataque)

    def defender(self, dano):
        dano_final = max(0, dano - self.defesa)
        self.vida -= dano_final
        return dano_final

    def esta_vivo(self):
        return self.vida > 0


class Missao:
    def __init__(self, nome, dificuldade):
        self.nome = nome
        self.dificuldade = dificuldade
        self.recompensa_xp = dificuldade * 30

    def gerar_inimigo(self):
        nomes = ["Goblin", "Lobo Sombrio", "Orc", "Esqueleto"]

        return {
            "nome": random.choice(nomes),
            "vida": 40 + self.dificuldade * 20,
            "ataque": 8 + self.dificuldade * 5
        }


def batalha(personagem, missao):
    inimigo = missao.gerar_inimigo()

    print(f"\nMissão iniciada: {missao.nome}")
    print(f"Inimigo encontrado: {inimigo['nome']}")

    while personagem.esta_vivo() and inimigo["vida"] > 0:
        dano_personagem = personagem.atacar()
        inimigo["vida"] -= dano_personagem

        print(f"{personagem.nome} causou {dano_personagem} de dano.")

        if inimigo["vida"] <= 0:
            break

        dano_inimigo = random.randint(3, inimigo["ataque"])
        dano_recebido = personagem.defender(dano_inimigo)

        print(f"{inimigo['nome']} causou {dano_recebido} de dano.")
        print(f"Vida de {personagem.nome}: {personagem.vida}")

    if personagem.esta_vivo():
        print("\nMissão concluída com sucesso!")
        return True
    else:
        print("\nVocê foi derrotado na missão.")
        return False


def main():
    print("=== RPG Simples Aleatório ===")

    nome_jogador = input("Digite o nome do jogador: ")
    jogador = Jogador(nome_jogador)

    nome_personagem = input("Digite o nome do personagem: ")

    classe = random.choice([
        "Guerreiro",
        "Mago",
        "Arqueiro",
        "Paladino"
    ])

    personagem = Personagem(nome_personagem, classe)
    jogador.adicionar_personagem(personagem)

    print(f"\nPersonagem criado: {personagem.nome}")
    print(f"Classe aleatória: {personagem.classe}")
    print(f"Ataque: {personagem.ataque}")
    print(f"Defesa: {personagem.defesa}")

    missoes = [
        Missao("Explorar a Floresta Perdida", 1),
        Missao("Derrotar os Bandidos", 2),
        Missao("Invadir a Cripta Sombria", 3)
    ]

    while personagem.esta_vivo():
        print("\nEscolha uma missão:")

        for i, missao in enumerate(missoes):
            print(f"{i + 1} - {missao.nome} | Dificuldade {missao.dificuldade}")

        escolha = input("Digite o número da missão ou 0 para sair: ")

        if escolha == "0":
            print("Jogo encerrado.")
            break

        if escolha.isdigit() and 1 <= int(escolha) <= len(missoes):
            missao = missoes[int(escolha) - 1]
            personagem.missoes.append(missao)

            venceu = batalha(personagem, missao)

            if venceu:
                jogador.perfil.ganhar_experiencia(missao.recompensa_xp)

                personagem.vida = min(100, personagem.vida + 20)

                print(f"XP atual: {jogador.perfil.experiencia}")
                print(f"Nível atual: {jogador.perfil.nivel}")
                print(f"Vida recuperada: {personagem.vida}")

        else:
            print("Opção inválida.")

    print("\n=== Resumo Final ===")
    print(f"Jogador: {jogador.nome}")
    print(f"Personagem: {personagem.nome}")
    print(f"Classe: {personagem.classe}")
    print(f"Nível: {jogador.perfil.nivel}")
    print(f"Missões jogadas: {len(personagem.missoes)}")


if __name__ == "__main__":
    main()
