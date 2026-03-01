def codigo():
    ### --------------------------------------------------------------------------------------
    #   Ex17 -  A partir da informação de uma área a ser pintada, o programa mostra quantas
    #           latas de tinta serão necessárias para a tarefa.
    #           Obs.:   . A lata de 18l custa R$ 80 // e a lata de 3,6l custa R$ 25) 
    #                   . Cada litro pinta 6m²

    area = float(input("Qual a medida da área (em m2) a ser pintada: "))

    if area <=0:
        print("Área com valor inválido!")

    else:
        ## Latas 18 litros ----------------------------
        Resto_G = area % (18*6)
        Latas_G = area / (18*6)
        Latas_G = int (Latas_G)

        if Resto_G != 0.0:            
            Latas_G += 1

        print(f"\n Galão 18 litros: Para a área informada, serão necessárias {Latas_G} latas.")


        ## Latas 3,6 litros ---------------------------
        Resto_P = area % (21.6)
        Latas_P = area / (21.6)
        Latas_P = int (Latas_P)

        if Resto_P != 0.0:            
            Latas_P += 1

        print(f" Galão 3,6 litros: Para a área informada, serão necessárias {Latas_P} latas.")



        ## Situação Mista -----------------------------
        if (Resto_G == 0):
            Misto_G = Latas_G
        else:
            Misto_G = Latas_G - 1
        
        Resto_M = Resto_G % (3.6*6)
        Misto_P = Resto_G / (3.6*6)
        Misto_P = int (Misto_P)

        if Resto_M != 0.0:            
            Misto_P += 1

        print(f" Misto: Para a área informada [[Latas 18l: {Misto_G}]]      |||    [[latas 3,6l: {Misto_P}]]")

    ### --------------------------------------------------------------------------------------


sair = "c"
while sair !="s":
    print("""
          




          """)
    codigo()
    sair = input ("""
        . . . . . . . . . . . . . . Digite qualquer yecla para continuar ou [s] para SAIR......
                  """)
