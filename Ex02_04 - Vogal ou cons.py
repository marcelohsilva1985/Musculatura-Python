def codigo():
    ### --------------------------------------------------------------------------------------
    #   Ex17 -  Identificar se uma letra digitada pelo usuário é uma vogal ou consoante.
    # 
    #           if in "AEIOUaeiou"
    
    letra = input("Digite uma letra: ")

    resultado="VOGAL" if letra in "aeiouAEIOU" else "CONSOANTE"

    print(f" A letra digitada [[{letra}]] é uma {resultado}")

    ### --------------------------------------------------------------------------------------


sair = "c"
while sair !="s":
    print("""
          




          """)
    codigo()
    sair = input ("""
        . . . . . . . . . . . . . . Digite qualquer yecla para continuar ou [s] para SAIR......
                  """)
