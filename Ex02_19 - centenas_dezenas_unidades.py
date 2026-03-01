
def codigo():
    ### --------------------------------------------------------------------------------------
    #   Ex02_19 -   Ler um número inferior a 1000. O mesmo retorna o número de
    #               centenas, dezenas e unidades.
    #               Obs.: Observar os termos no plural, virgula e a colocação do "e"

    frase_str = []

    frase_str.clear()
    n1 = int(input("Digite um número: "))

    cen = int (n1/100)
    
    dez = n1 % 100
    dez = int (dez/10) 
    
    uni = int (n1%10)

    if uni >= 1:
        str1 = str(uni)
        str2="unidade" if uni==1 else "unidades"     
        str3 = str1 + " " + str2
        frase_str.append(str3)

    if dez >= 1:
        str1 = str(dez)
        str2="dezena" if dez==1 else "dezenas"     
        str3 = str1 + " " + str2
        frase_str.append(str3)

    if cen >= 1:
        str1 = str(cen)
        str2="centena" if cen==1 else "centenas"  
        str3 = str1 + " " + str2
        frase_str.append(str3)

    ans = len(frase_str)

    if ans==3: print(f" O número {n1} possui {frase_str[2]}, {frase_str[1]} e {frase_str[0]}.")
    if ans==2: print(f" O número {n1} possui {frase_str[1]} e {frase_str[0]}.")
    if ans==1: print(f" O número {n1} possui {frase_str[0]}.")


    ### --------------------------------------------------------------------------------------


sair = "c"
while sair !="s":
    print("""
          




          """)
    codigo()
    sair = input ("""
        . . . . . . . . . . . . . . Digite qualquer yecla para continuar ou [s] para SAIR......
                  """)
