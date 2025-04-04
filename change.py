def change():
    expense = 23.75
    money = 100
    print("ingresar gasto:")
    print(expense)
    print("dinero recibido")
    print(money)
    vuelto = money - expense
    pesos = int(vuelto)
    centavos = int(round((vuelto - pesos) *100))
    print("\nVuelto\n")
    print(f"pesos:\n{pesos}")
    print(f"centavos:\n{centavos}")
