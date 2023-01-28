
def seleciona_peca():
    
    if vez == "Jog1" or vez == "Inicio":
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


def movimenta(linha_peca,coluna_peca):
    print()
    global vez
    if vez =="Jog1" or vez == "Inicio" and tabuleiro[linha_peca][coluna_peca] == "1":


        if linha_peca - linha == 1 and coluna_peca - coluna == 1:
            tabuleiro[linha_peca - 1][coluna_peca - 1] = tabuleiro[linha_peca][coluna_peca]
            tabuleiro[linha_peca][coluna_peca] = "0"
            vez ="Jog2"

            return True
        
        elif linha_peca - linha == -1 and coluna_peca - coluna == 1:
            tabuleiro[linha_peca + 1][coluna_peca - 1] = tabuleiro[linha_peca][coluna_peca]
            tabuleiro[linha_peca][coluna_peca] = "0"
            vez="Jog2"

            return True
        
        elif linha_peca - linha == -1 and coluna_peca - coluna == -1:
            tabuleiro[linha_peca + 1][coluna_peca + 1] = tabuleiro[linha_peca][coluna_peca]
            tabuleiro[linha_peca][coluna_peca] = "0"
            vez="Jog2"

            return True
        
        elif linha_peca - linha == 1 and coluna_peca - coluna == -1:
            tabuleiro[linha_peca - 1][coluna_peca + 1] = tabuleiro[linha_peca][coluna_peca]
            tabuleiro[linha_peca][coluna_peca] = "0"
            vez="Jog2"
            
            return True
        

    elif tabuleiro[linha_peca][coluna_peca] == "2":

        if linha_peca - linha == 1 and coluna_peca - coluna == 1:
            tabuleiro[linha_peca - 1][coluna_peca - 1] = tabuleiro[linha_peca][coluna_peca]
            tabuleiro[linha_peca][coluna_peca] = "0"
            vez="Jog1"
            
            return True
        
        elif linha_peca - linha == -1 and coluna_peca - coluna == 1:
            tabuleiro[linha_peca + 1][coluna_peca - 1] = tabuleiro[linha_peca][coluna_peca]
            tabuleiro[linha_peca][coluna_peca] = "0"
            vez="Jog1"
            
            return True
        
        elif linha_peca - linha == -1 and coluna_peca - coluna == -1:
            tabuleiro[linha_peca + 1][coluna_peca + 1] = tabuleiro[linha_peca][coluna_peca]
            tabuleiro[linha_peca][coluna_peca] = "0"
            vez="Jog1"
            
            return True
        
        elif linha_peca - linha == 1 and coluna_peca - coluna == -1:
            tabuleiro[linha_peca - 1][coluna_peca + 1] = tabuleiro[linha_peca][coluna_peca]
            tabuleiro[linha_peca][coluna_peca] = "0"
            vez="Jog1"
            
            return True

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

def rodada(vez):
    if vez == "Jog1":
        rodada_Brancas+=1
        return "Jog2"
    elif vez == "Jog2":
        rodada_Pretas +=1
        return "Jog1"

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

print("\nInforme a peça que deseja mover atravez da linha e da coluna")

while True:
    print()

    if vez == "Jog1":
        print("Jogador 1, Escolha a peça para andar")
    else:
        print("Jogador 2, Escolha a peça para andar")

    print()
    print("Andar com a peça: \n")
    linha_peca = int(input("Linha: "))
    coluna_peca = int(input("Coluna: "))

    seleciona_peca()

    print()
    print("Mover para: ")
    linha = int(input("Linha: "))
    coluna = int(input("Coluna: "))
    print(vez)    
    movimenta(linha_peca,coluna_peca)
    print(vez)
    estado_inicial()


