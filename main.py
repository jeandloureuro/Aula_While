
# pontos = 0
# questao = 1
#
# while questao <= 3:
#     resposta = input(f"Resposta da questão {questao}: ")
#
#     if questao == 1 and resposta == "b":
#         pontos += 1
#
#     elif questao == 2 and resposta == "a":
#         pontos += 1
#
#     elif questao == 3 and resposta == "d":
#         pontos += 1
#     questao += 1
# print(f"O aluno fez {pontos} posto(s).")

#
# n = 1
# soma = 0
#
# while n <= 10:
#
#     x = float(input(f"Digit o numero {n}: "))
#       soma = soma + x
#       n += 1
#
#     print(f"Soma = {soma:.2f}")
#     print(f"Soma = {soma/ (n - 1):.2f}")

#
# deposito = float(input(f"Coloque um valor de deposito: "))
# juros = float(input(f"Coloque um valor de juros: "))
# mes = 1
#
# while mes <= 24:
#
#     Total_de_ganho = (deposito * juros + deposito)/100
#
#     deposito += int(input(f"Coloque o valor mensal: "))
#
#     print(f"Total Ganho: {Total_de_ganho:.4f}")
#
#     mes += 1


soma = 0
while True:
    num = input("Digite um número a somar ou fim para sair: ")

    if num == "fim":

        break

    soma += float(num)

