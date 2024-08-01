def createSudoku():
    sudoku = []
    
    for row in range(9):
        sudoku.append([])
        for col in range(9):
            sudoku[row].append("+")
                
    return sudoku

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
    
