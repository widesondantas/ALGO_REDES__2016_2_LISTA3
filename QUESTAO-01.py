or i in range(10):

    respostas = [input("Telefonou para a vítima?"),
                 input("Esteve no local do crime?"),
                 input("Mora perto da vítima?"),
                 input("Devia para a vítima?"),
                 input("Já trabalhou com a vítima?")]

    contador_sim = respostas.count("sim")

    if contador_sim == 5:
        print('ASSASSINO')
        break
    elif contador_sim == 3 or contador_sim == 4:
        print('CUMPLICE')
    elif contador_sim == 2:
        print('SUSPEITO')
    else:
        print('INOCENTE')