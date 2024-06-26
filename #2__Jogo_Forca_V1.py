'''Code um jogo de forca'''

import random

def escolher_palavra():
    palavras = ["python", "chocolate", "computador"]
    return random.choice(palavras)

def jogar(palavra):
    letras_corretas = set(palavra)
    letras_incorretas = set()
    tentativas = 6
    palavra_escondida = ["_" if letra.isalpha() else letra for letra in palavra]

    print("Bem-vindo ao jogo da forca!")
    print(" ".join(palavra_escondida))

    while tentativas > 0:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas:
            print("Correto!")
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_escondida[i] = letra
            print(" ".join(palavra_escondida))
            if "_" not in palavra_escondida:
                print("Parabéns! Você venceu!")
                break
        else:
            print("Errado!")
            letras_incorretas.add(letra)
            tentativas -= 1
            print("Tentativas restantes:", tentativas)
            print("Letras incorretas:", " ".join(letras_incorretas))

    print("Fim do jogo! A palavra correta era:", palavra)

def main():
    palavra = escolher_palavra()
    jogar(palavra)

if __name__ == "__main__":
    main()
