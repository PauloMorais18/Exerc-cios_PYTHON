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
        palpite = input("Digite uma letra ou chute a palavra inteira: ").lower()

        if len(palpite) == 1:  # Se o palpite for uma letra
            if palpite in letras_corretas:
                print("Correto!")
                for i in range(len(palavra)):
                    if palavra[i] == palpite:
                        palavra_escondida[i] = palpite
                print(" ".join(palavra_escondida))
                if "_" not in palavra_escondida:
                    print("Parabéns! Você venceu!")
                    break
            else:
                print("Errado!")
                letras_incorretas.add(palpite)
                tentativas -= 1
                print("Tentativas restantes:", tentativas)
                print("Letras incorretas:", " ".join(letras_incorretas))
        else:  # Se o palpite for a palavra inteira
            if palpite == palavra:
                print("Parabéns! Você acertou a palavra!")
                break
            else:
                print("Palavra incorreta! Tente novamente.")
                tentativas -= 1
                print("Tentativas restantes:", tentativas)

    print("Fim do jogo! A palavra correta era:", palavra)

def main():
    palavra = escolher_palavra()
    jogar(palavra)

if __name__ == "__main__":
    main()
