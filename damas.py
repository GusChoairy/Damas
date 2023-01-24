
def seleciona_peca():
        linha_peca = int(input("Linha: "))
        coluna_peca = int(input("Coluna: "))
        print()
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

def testa_movimentacao():
    linha = int(input("Linha: "))
    coluna = int(input("Coluna: "))
    print()

    
    if tabuleiro[linha][coluna] == "0" and (linha+coluna)%2==0:
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

print("\nInforme a peça que deseja mover atravez da linha e da coluna\n")

while seleciona_peca() == False:
    seleciona_peca()
    break

while testa_movimentacao() == False:
    print("Mover peça para: \n")
    linha = int(input("Linha: "))
    coluna = int(input("Coluna: "))
    testa_movimentacao(linha,coluna)


