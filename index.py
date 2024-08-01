def createSudoku():
    sudoku = []
    
    for row in range(9):
        sudoku.append([])
        for col in range(9):
            sudoku[row].append("+")
                
    return sudoku

