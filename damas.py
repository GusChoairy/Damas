
def seleciona_peca(linha_peca,coluna_peca):
       
        if vez == "Jog1":
            if tabuleiro[linha_peca][coluna_peca] == "1" or tabuleiro[linha_peca][coluna_peca] == "11":
                return True
            else:
                print("Oção invalida! \nEscolha Novamente!")
                return False
        else:
            if tabuleiro[linha_peca][coluna_peca] == "2" or tabuleiro[linha_peca][coluna_peca] == "22":
                return True
            else:
                print("Oção invalida! \nEscolha Novamente!")
                return False

def movimenta(linha,coluna):
    if vez=="Jog1" and tabuleiro[linha_peca][coluna_peca] == "1":
        if linha_peca - linha == 1 and coluna_peca - coluna == 1:
            tabuleiro[linha_peca - 1][coluna_peca - 1] = tabuleiro[linha_peca][coluna_peca]
            return True
        elif linha_peca - linha == -1 and coluna_peca - coluna == 1:
            tabuleiro[linha_peca + 1][coluna_peca - 1] = tabuleiro[linha_peca][coluna_peca]
            return True
        elif linha_peca - linha == -1 and coluna_peca - coluna == -1:
            tabuleiro[linha_peca + 1][coluna_peca + 1] = tabuleiro[linha_peca][coluna_peca]
            return True
        elif linha_peca - linha == 1 and coluna_peca - coluna == -1:
            tabuleiro[linha_peca - 1][coluna_peca + 1] = tabuleiro[linha_peca][coluna_peca]
            return True
    elif tabuleiro[linha_peca][coluna_peca] == "2":
        if linha_peca - linha == 1 and coluna_peca - coluna == 1:
            tabuleiro[linha_peca - 1][coluna_peca - 1] = tabuleiro[linha_peca][coluna_peca]
            return True
        elif linha_peca - linha == -1 and coluna_peca - coluna == 1:
            tabuleiro[linha_peca + 1][coluna_peca - 1] = tabuleiro[linha_peca][coluna_peca]
            return True
        elif linha_peca - linha == -1 and coluna_peca - coluna == -1:
            tabuleiro[linha_peca + 1][coluna_peca + 1] = tabuleiro[linha_peca][coluna_peca]
            return True
        elif linha_peca - linha == 1 and coluna_peca - coluna == -1:
            tabuleiro[linha_peca - 1][coluna_peca + 1] = tabuleiro[linha_peca][coluna_peca]
            return True

def movimenta_peca():
    print("Mover peça para \n")
    linha = int(input("Linha: "))
    coluna = int(input("Coluna: "))
    print()

    
    if tabuleiro[linha_peca][coluna_peca] == "1" or tabuleiro[linha_peca][coluna_peca] == "2" and (linha+coluna)%2==0:
        tabuleiro[linha][coluna] = tabuleiro[linha_peca][coluna_peca]
        return True
    else:
        return False

def estado_inicial():
    for linha in range(0,8):
        for coluna in range(0,8):
        
            if tabuleiro[linha][coluna] == "2":
                print("\033[;40mP \033[m",end="")
            elif tabuleiro[linha][coluna] == "0" and (linha+coluna)%2!= 0:
                print("\033[;107m  \033[m",end="")
            elif tabuleiro[linha][coluna]=="1":
                print("\033[;40mB \033[m",end="")
            elif tabuleiro[linha][coluna]=="0" and (linha+coluna)%2== 0:
                print("\033[;40m  \033[m",end="")
        print()

tabuleiro=[
        ["2","0","2","0","2","0","2","0"],
        ["0","2","0","2","0","2","0","2"],
        ["2","0","2","0","2","0","2","0"],
        ["0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0"],
        ["0","1","0","1","0","1","0","1"],
        ["1","0","1","0","1","0","1","0"],
        ["0","1","0","1","0","1","0","1"]]


vez="Jog1"
pecas_Pretas = []
pecas_Brancas = []

print()
print("=~"*2,"Damas","~="*2)
print("\nInicio de jogo\n")

estado_inicial()

print("\nInforme a peça que deseja mover atravez da linha e da coluna\n0")
linha_peca = int(input("Linha: "))
coluna_peca = int(input("Coluna: "))
while seleciona_peca(linha_peca,coluna_peca) == False:

    linha_peca = int(input("\nLinha: "))
    coluna_peca = int(input("Coluna: "))
    print()
    seleciona_peca(linha_peca,coluna_peca)
    break

print("Mover para: ")
linha = int(input("Linha: "))
coluna = int(input("Coluna: "))
movimenta(linha,coluna)

#while testa_movimentacao() == False:
#    print("Mover peça para: \n")
#    linha = int(input("Linha: "))
#    coluna = int(input("Coluna: "))
#    testa_movimentacao(linha,coluna)


