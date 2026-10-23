
while True:
    print("\n--- Calculadora ---")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Saindo da calculadora...")
        break

    if opcao not in ("1", "2", "3", "4"):
        print("Opção inválida!")
        continue

    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        resultado = numero1 + numero2

    elif opcao == "2":
        resultado = numero1 - numero2

    elif opcao == "3":
        resultado = numero1 * numero2

    elif opcao == "4":
        if numero2 == 0:
            print("Não é possível dividir por zero.")
            continue

        resultado = numero1 / numero2

    print("Resultado:", resultado)
