def codigo():
    ### --------------------------------------------------------------------------------------
    #   Ex02_05 -   Calcular media e indicar status de aprovação de um aluno (3 opções)
    
    n1 = int(input("Digite a primeira nota do aluno: "))
    n2 = int(input("Digite a segunda nota do aluno: "))
             
    media = (n1+n2)/2

    if (0<= media <7): status="REPROVADO"
    elif (7<= media <10): status="APROVADO"
    elif (media ==10): status="APROVADO COM DISTINÇÃO"
 
    if (not (0<= n1 <=10)) or (not (0<= n2 <=10)):
        print("\n Uma das entradas foi incorreta!")
    else:
        print(f"\n O aluno foi {status}. O mesmo atingiu a média final de {media} pontos.")

    ### --------------------------------------------------------------------------------------


sair = "c"
while sair !="s":
    print("""
          




          """)
    codigo()
    sair = input ("""
        . . . . . . . . . . . . . . Digite qualquer yecla para continuar ou [s] para SAIR......
                  """)
