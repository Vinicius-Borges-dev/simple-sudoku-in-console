# Importação da classe random para gerar números aleatórios
import random


# Função que valida o sudoku verificando se o número é repetido nas linhas e/ou colunas
def sudokuValidate(sudoku, linha, coluna, numero):

    for i in range(9):
        if sudoku[linha][i] == numero:
            return False
        if sudoku[i][coluna] == numero:
            return False
    return True


# Função que cria o sudoku percorrendo um range de 0 a 8 criando uma matriz 9x9 preenchida com "_"
def createSudoku():
    sudoku = []

    # Cria 9 linhas
    for row in range(9):
        sudoku.append([])
        # Cria 9 colunas com "_"
        for col in range(9):
            sudoku[row].append("_")

    return sudoku


# Função que preenche o sudoku com números aleatórios
def fillSudoku(sudoku):

    # Cria 30 numeros aleatórios em posições aleatórias
    for i in range(20):

        # Tenta adicionar um número aleatório com base na validação de linhas e colunas
        while True:
            randomRow = random.randint(0, 8)
            randomCol = random.randint(0, 8)
            randomNum = str(random.randint(1, 9))

            # Se o espaço estiver vazio e ter validação confirmada, adicionar o número
            if sudoku[randomRow][randomCol] == "_" and sudokuValidate(
                sudoku, randomRow, randomCol, randomNum
            ):
                sudoku[randomRow][randomCol] = randomNum
                break

    printSudoku(sudoku)


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
        choiceRow = input("Escolha a linha de 0 a 8: ")
        choiceCol = input("Escolha a coluna de 0 a 8: ")

        # Condições que privam o usuário de digita uma posição inválida ou deixe os campos vazios
        if choiceRow != "" or choiceCol != "":
            choiceRow = int(choiceRow)
            choiceCol = int(choiceCol)

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
                        if sudokuValidate(sudoku, choiceRow, choiceCol, choiceNumber):
                            sudoku[choiceRow][choiceCol] = choiceNumber
                            printSudoku(sudoku)
                            break
                        else:
                            print("Já existe esse numero na linha ou coluna")
                            continue
        else:
            print("Campos vazios")
            print()


sudoku = createSudoku()
fillSudoku(sudoku)
startGame()
