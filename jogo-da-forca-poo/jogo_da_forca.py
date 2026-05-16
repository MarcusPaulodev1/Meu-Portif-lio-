import os
import random


# =========================================================
# CLASSE BONECO
# =========================================================
# Responsável por:
# - controlar os erros do jogador
# - definir a dificuldade
# - mostrar o desenho da forca
# =========================================================
class Boneco:

    # Método construtor
    # Recebe a dificuldade escolhida pelo jogador
    def __init__(self, dificuldade):

        # Quantidade atual de erros
        self.erros = 0

        # Guarda a dificuldade escolhida
        self.dificuldade = dificuldade

        # =================================================
        # Configuração da dificuldade
        # =================================================
        # Fácil:
        # - mais chances de erro
        #
        # Normal:
        # - padrão tradicional
        #
        # Difícil:
        # - cada erro vale por 2
        # =================================================
        if dificuldade == "facil":
            self.max_erros = 8
            self.peso_erro = 1

        elif dificuldade == "normal":
            self.max_erros = 6
            self.peso_erro = 1

        else:  # difícil
            self.max_erros = 6
            self.peso_erro = 2

        # =================================================
        # Lista com os desenhos da forca
        # Cada posição representa um estágio do boneco
        # =================================================
        self.estagios = [

            # Estágio 0
            """
            
            
            
            
            =========
            """,

            # Estágio 1
            """
            |
            |
            |
            |
            =========
            """,

            # Estágio 2
            """
            +---.
            |
            |
            |
            =========
            """,

            # Estágio 3
            """
            +---.
            |   O
            |
            |
            =========
            """,

            # Estágio 4
            """
            +---.
            |   O
            |   |
            |
            =========
            """,

            # Estágio 5
            """
            +---.
            |   O
            |  /|
            |
            =========
            """,

            # Estágio 6
            """
            +---.
            |   O
            |  /|\\
            |
            =========
            """,

            # Estágio 7
            """
            +---.
            |   O
            |  /|\\
            |  /
            =========
            """,

            # Estágio 8
            """
            +---.
            |   O
            |  /|\\
            |  / \\
            =========
            """
        ]

    # =====================================================
    # Método responsável por aumentar os erros
    # =====================================================
    def avancar(self):

        # Soma os erros baseado na dificuldade
        self.erros += self.peso_erro

    # =====================================================
    # Verifica se o jogador perdeu
    # =====================================================
    def perdeu(self):

        # Retorna True se os erros atingirem o limite
        return self.erros >= self.max_erros

    # =====================================================
    # Retorna o desenho atual do boneco
    # =====================================================
    def desenhar(self):

        # Evita ultrapassar o tamanho da lista
        indice = min(self.erros, len(self.estagios) - 1)

        return self.estagios[indice]


# =========================================================
# CLASSE PALAVRASECRETA
# =========================================================
# Responsável por:
# - armazenar a palavra
# - controlar letras descobertas
# - verificar acertos
# =========================================================
class PalavraSecreta:

    # Método construtor
    def __init__(self, palavra):

        # Palavra escolhida para a partida
        self.palavra = palavra.lower()

        # Lista com "_" escondendo as letras
        # Exemplo:
        # python -> _ _ _ _ _ _
        self.letras_descobertas = ["_"] * len(palavra)

    # =====================================================
    # Verifica se a letra existe na palavra
    # =====================================================
    def tentar_letra(self, letra):

        letra = letra.lower()

        # Variável para descobrir se acertou
        acertou = False

        # Percorre toda a palavra
        for i in range(len(self.palavra)):

            # Se encontrar a letra:
            if self.palavra[i] == letra:

                # Revela a letra na posição correta
                self.letras_descobertas[i] = letra

                acertou = True

        # Retorna True ou False
        return acertou

    # =====================================================
    # Mostra a palavra parcialmente descoberta
    # =====================================================
    def mostrar(self):

        # Junta os caracteres com espaço
        return " ".join(self.letras_descobertas)

    # =====================================================
    # Verifica se o jogador venceu
    # =====================================================
    def venceu(self):

        # Se ainda existir "_", não venceu
        return "_" not in self.letras_descobertas


# =========================================================
# CLASSE JOGODAFORCA
# =========================================================
# Responsável por:
# - controlar o fluxo completo da partida
# - criar objetos
# - receber entradas do jogador
# - verificar vitória e derrota
# =========================================================
class JogoDaForca:

    # Método construtor
    def __init__(self):

        # Lista de palavras possíveis
        self.palavras = [
            "python",
            "programacao",
            "engenharia",
            "computador",
            "algoritmo",
            "desenvolvimento"
        ]

    # =====================================================
    # Limpa a tela do terminal
    # =====================================================
    def limpar_tela(self):

        # Windows usa "cls"
        # Linux/Mac usa "clear"
        os.system('cls' if os.name == 'nt' else 'clear')

    # =====================================================
    # Escolha da dificuldade
    # =====================================================
    def escolher_dificuldade(self):

        while True:

            print("================================")
            print("      JOGO DA FORCA")
            print("================================")
            print("Escolha a dificuldade:")
            print("1 - Fácil")
            print("2 - Normal")
            print("3 - Difícil")

            escolha = input("Digite a opção: ")

            # Retorna a dificuldade escolhida
            if escolha == "1":
                return "facil"

            elif escolha == "2":
                return "normal"

            elif escolha == "3":
                return "dificil"

            else:
                print("\nOpção inválida!")
                input("Pressione ENTER...")

    # =====================================================
    # Método principal do jogo
    # =====================================================
    def iniciar(self):

        # Escolhe a dificuldade
        dificuldade = self.escolher_dificuldade()

        # Escolhe uma palavra aleatória
        palavra = random.choice(self.palavras)

        # Cria os objetos principais
        boneco = Boneco(dificuldade)
        palavra_secreta = PalavraSecreta(palavra)

        # Lista de letras já utilizadas
        letras_usadas = []

        # =================================================
        # LOOP PRINCIPAL DO JOGO
        # =================================================
        while True:

            # Limpa a tela
            self.limpar_tela()

            # Mostra o estado atual do jogo
            print("================================")
            print("         JOGO DA FORCA")
            print("================================")

            print(boneco.desenhar())

            print("Palavra:", palavra_secreta.mostrar())

            print("\nLetras usadas:",
                  ", ".join(letras_usadas))

            # Recebe a letra digitada
            letra = input("\nDigite uma letra: ").lower()

            # =============================================
            # Validação da entrada
            # =============================================

            # Verifica se digitou apenas UMA letra
            if len(letra) != 1 or not letra.isalpha():

                print("\nDigite apenas UMA letra válida!")
                input("Pressione ENTER...")
                continue

            # Verifica se a letra já foi usada
            if letra in letras_usadas:

                print("\nVocê já tentou essa letra!")
                input("Pressione ENTER...")
                continue

            # Adiciona a letra na lista
            letras_usadas.append(letra)

            # =============================================
            # Verifica se acertou ou errou
            # =============================================
            if palavra_secreta.tentar_letra(letra):

                print("\nVocê acertou!")

            else:

                print("\nVocê errou!")

                # Avança o boneco
                boneco.avancar()

            # =============================================
            # Verifica vitória
            # =============================================
            if palavra_secreta.venceu():

                self.limpar_tela()

                print("================================")
                print("         VOCÊ VENCEU!")
                print("================================")

                print("\nPalavra:", palavra)

                break

            # =============================================
            # Verifica derrota
            # =============================================
            if boneco.perdeu():

                self.limpar_tela()

                print(boneco.desenhar())

                print("================================")
                print("         VOCÊ PERDEU!")
                print("================================")

                print("\nA palavra era:", palavra)

                break

            input("\nPressione ENTER para continuar...")


# =========================================================
# INÍCIO DO PROGRAMA
# =========================================================

# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":

    # Cria o jogo
    jogo = JogoDaForca()

    # Inicia a partida
    jogo.iniciar()
