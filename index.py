
import random

def validaSudoku(sudoku, linha, coluna, numero):
    for i in range(len(sudoku)):
        if sudoku[linha][i] == numero or sudoku[i][coluna] == numero: return False
    return True


def createSudoku():
    sudoku = []
    
    for row in range(9):
        sudoku.append([])
        for col in range(9):
            for i in range(20):
                sudoku[row].append('+')
                
    return sudoku

def fillSudoku(sudoku):
    counter = 0
    while counter <= 20:
        randomRow = random.randint(0, len(sudoku))
        randomCol = random.randint(0, len(sudoku))
        randomNumber = random.randint(1,9)
        if validaSudoku(sudoku, sudoku[randomRow], sudoku[randomCol], randomNumber):
            sudoku[randomRow][randomCol] = str(randomNumber)
            break
        counter += 1


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
    while True:
        choiceRow = int(input("Escolha a linha de 0 a 8: "))
        choiceCol = int(input("Escolha a coluna de 0 a 8: "))
        
        if choiceRow < 0 or choiceRow > 8 or choiceCol < 0 or choiceCol > 8:
            print("Posição inválida")
        else:
            while True:
                choiceNumber = input("Escolha um número entre 1 e 9: ")
                if int(choiceNumber) < 1 or int(choiceNumber) > 8:
                    print("Número inválido")
                else:
                    if validaSudoku(sudoku, choiceRow, choiceCol, choiceNumber):
                        sudoku[choiceRow][choiceCol] = choiceNumber
                        printSudoku(sudoku)
                        break
                    else:
                        print("Já existe esse numero na linha ou coluna")
                        continue
            

sudoku = createSudoku()
fillSudoku(sudoku)
printSudoku(sudoku)
startGame()