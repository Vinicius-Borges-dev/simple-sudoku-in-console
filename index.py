# Importação da classe random para gerar números aleatórios
import random


# Função que valida o sudoku verificando se o número é repetido nas linhas e/ou colunas
def sudokuValidateRowsAndCols(sudoku, row, col, num):

    # percorre todos as colunas da mesma linha e a todas as linhas na mesma coluna
    for i in range(len(sudoku)):
        if sudoku[row][i] == num or sudoku[i][col] == num: return False
        
    return True


def quadValidate(sudoku, row, col, num):
    
    # Calcula e descobre o inicio do quadrante
    iRow = (row // 3) * 3
    iCol = (col // 3) * 3

    # Percorre todo o quadrante
    for i in range(3):
        for j in range(3):
            
            # Se encontrar esse número no quadrante, retorna false
            if sudoku[iRow + i][iCol + j] == num: 
                return False
    
    return True



# Função que cria o sudoku percorrendo um range de 0 a 8 criando uma matriz 9x9 preenchida com "_"
def createSudoku():
    sudoku = []

    # Cria 9 linhas
    for row in range(9):
        sudoku.append([])
        
        # Cria 9 colunas e as preenche com "_"
        for col in range(9):
            sudoku[row].append("_")

    return sudoku




# Função que preenche o sudoku com números "aleatórios"
def fillSudoku(sudoku):

    # os dois laços foram criados para percorrer todas posições do sudoku
    for row in range(len(sudoku)):
        for col in range(len(sudoku)):
            
            # se o espaço em questão estiver vazio
            if sudoku[row][col] == "_":
                
                # cria e embaralha os números possiveis
                nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                random.shuffle(nums)
                
                # para cada número
                for num in nums:
                    
                    # valida se aquele número é repetido na linha ou coluna
                    if sudokuValidateRowsAndCols(sudoku, row, col, str(num)) and quadValidate(sudoku, row, col, str(num)):
                        
                        # Se sim, adiciona aquele número na posição
                        sudoku[row][col] = str(num)
                        
                        # Chama a si próprio para preencher a próxima posição
                        if fillSudoku(sudoku):
                            
                            # se não existir mais espaços restantes, finaliza
                            return True
                        
                        else:
                            
                            # Caso o número testado não seja validado naquela posição, deixa em branco para testar outro número
                            sudoku[row][col] = "_"
                #  Se nenhum número puder ser inserído, finaliza
                return False
            
    #  Se não tiver mais espaço vazio, termina
    return True

# Cria uma interface que indica todas as posições posiveis dentro do sudoku
def printSudoku(sudoku):
    linhaExterna = 0
    colunaExterna = 0
    print("    ", end="")
    while linhaExterna < len(sudoku):
        print(linhaExterna, end="    ")
        linhaExterna += 1
    print()

    for linha in sudoku:
        print(f"{colunaExterna} {linha}")
        colunaExterna += 1
        print()

    print()

# função que remove números aleatórios para começar o jogo
def removeNumbers(sudoku):
    while True:
        choice = int(input("Quantos números serão removidos? "))    
        
        if choice <= 0 or choice >= len(sudoku) ** 2:
            print("Escolha um número válido")
        else:
            
            # escolhe randomicamente 5 número a serem tirados do tabuleiro
            while choice > 0:
                randomRow = random.randint(0, (len(sudoku) - 1))
                randomCol = random.randint(0, (len(sudoku) - 1))
                
                if sudoku[randomRow][randomCol] != "_":
                    sudoku[randomRow][randomCol] = "_"
                    choice -= 1
            
            break
        
        

def finalVerification(sudoku):
    count = 0
    for row in sudoku:
        count += row.count("_")
    
    if count == 0:
        return True
    
    return False

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
                    if int(choiceNumber) < 1 or int(choiceNumber) > 9:
                        print("Número inválido")
                    else:

                        # A cada adição, verifica se o numero é repetido na linha ou na coluna em que está inserido
                        if sudokuValidateRowsAndCols(sudoku, choiceRow, choiceCol, choiceNumber) and quadValidate(sudoku, choiceRow, choiceCol, choiceNumber):
                            sudoku[choiceRow][choiceCol] = choiceNumber
                            printSudoku(sudoku)
                            if finalVerification(sudoku):
                                print("Você ganhou!")
                                return
                            
                            break
                        else:
                            print("Já existe esse numero na linha, coluna ou quadrante")
                            continue
        else:
            print("Campos vazios")
            print()





sudoku = createSudoku()

fillSudoku(sudoku)

removeNumbers(sudoku)

printSudoku(sudoku)

startGame()