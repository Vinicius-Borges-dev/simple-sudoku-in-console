# Importação do metodo random para gerar números aleatórios
import random

# Função que valida o sudoku verificando se o número é repetido nas linhas e/ou colunas
def validaSudoku(sudoku, linha, coluna, numero):
    
    # laço de repetição que percorre todo o tamanho do sudoku
    for i in range(len(sudoku)):
        
        # Caso encontre mais algum número igual na linha ou coluna, retorna false
        if sudoku[linha][i] == numero or sudoku[i][coluna] == numero: return False
    
    # caso contrário, retorna true
    return True

# Função que cria o sudoku percorrendo um range de 0 a 8 criando uma matriz 9x9 preenchida com "_"
def createSudoku():
    sudoku = []
    
    for row in range(9):
        sudoku.append([])
        for col in range(9):
            sudoku[row].append('_')
                
    return sudoku

# Função que preenche o sudoku com números aleatórios
def fillSudoku():
    count = 0
    
    # Através de um laço de repetição ele gera números aleatórios para a coluna e a linha da matriz, junto com um número aleatório para preencher o espaço
    while count <= 50:
        randomRow = random.randint(0, 8)
        randomCol = random.randint(0, 8)
        randomNum = random.randint(1,9)
        
        # Toda vez que gerar números novos, verifica se os mesmos são repetidas na linha e coluna em que estão e insere o valor na matriz, caso a validação retorne um true
        if validaSudoku(sudoku, randomRow, randomCol, randomNum):
            sudoku[randomRow][randomCol] = str(randomNum)
            count += 1
            

# Cria uma interface que indica todas as posições posiveis dentro do sudoku
def printSudoku(sudoku):
    linhaExterna = 0
    colunaExterna = 0
    print("    ", end="")
    while linhaExterna <= 8:
        print(linhaExterna, end="    ")
        linhaExterna += 1
    print()

    for linha in sudoku:
        print(f"{colunaExterna} {linha}")
        colunaExterna += 1
        print()

    print()
    
def startGame():
    
    # Cria um laço infinito até que o usuario preencha a ultima posição
    
    while True:
        choiceRow = int(input("Escolha a linha de 0 a 8: "))
        choiceCol = int(input("Escolha a coluna de 0 a 8: "))
        
        # Condições que privam o usuário de digita uma posição inválida
        if choiceRow < 0 or choiceRow > 8 or choiceCol < 0 or choiceCol > 8:
            print("Posição inválida")
        else:
            # Caso contrário, inicia um loop para pedir o numero a ser adicionado no sudoku
            while True:
                choiceNumber = input("Escolha um número entre 1 e 9: ")
                if int(choiceNumber) < 1 or int(choiceNumber) > 8:
                    print("Número inválido")
                else:
                    
                    # A cada adição, verifica se o numero é repetido na linha ou na coluna em que está inserido
                    if validaSudoku(sudoku, choiceRow, choiceCol, choiceNumber):
                        sudoku[choiceRow][choiceCol] = choiceNumber
                        printSudoku(sudoku)
                        continue
                    else:
                        print("Já existe esse numero na linha ou coluna")
                        continue
            

sudoku = createSudoku()
fillSudoku()
printSudoku(sudoku)
startGame()