idade = int(input("Digite sua idade: "))
autorizacao = input("POSSUI AUTORIZAÇÃO?: sim/não").strip().lower()

if idade < 0:
    print("idade invalida")

elif idade < 12:
    print("Entrada somente com responsável")

elif idade <= 17 and autorizacao == "sim":
    print("Entrada permitida com autorização")

elif idade <= 17:
    print("Precisa de autorização")

elif idade <= 59:
    print("Entrada liberada")
else:
    print("Entrada liberada — melhor idade")