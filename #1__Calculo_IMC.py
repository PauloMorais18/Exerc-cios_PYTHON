'''Escreva um código que calcule o IMC'''


def calcular_imc(peso, altura):
  imc = peso / (altura ** 2)
  return imc

def classificar(imc):
  if imc < 18.5:
      return "abaixo do peso"
  elif 18.5 <= imc < 25:
      return "peso normal"
  elif 25 <= imc < 30:
      return "sobrepeso"
  elif 30 <= imc < 35:
      return "obesidade grau 1"
  elif 35 <= imc < 40:
      return "obesidade grau 2"
  else:
      return "obesidade grau 3"

def main():
  peso = float(input("Digite o peso: "))
  altura = float(input("Digite a altura: "))
  imc = calcular_imc(peso, altura)
  classificacao = classificar(imc)
  print(f"O IMC é {imc:.2f} e a classificação é {classificacao}")

if __name__ == "__main__":
  main()
