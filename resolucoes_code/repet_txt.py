# Vamos solicitar uma string e um número inteiro como entrada.

palavra = input("Digite uma palavra: ")
numero = int(input("Digite um número: "))

mensagem = f"Palavra: {palavra}, número de vezes que irá repetir {numero}"

print(mensagem)
print((palavra + " ") * numero)

