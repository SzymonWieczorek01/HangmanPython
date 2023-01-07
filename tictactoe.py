# write your code here
grid_layout = "_________"

print("---------")
print("|"+" "+f"{grid_layout[0]}"+" "+f"{grid_layout[1]}"+" "+f"{grid_layout[2]}"+" "+"|")
print("|"+" "+f"{grid_layout[3]}"+" "+f"{grid_layout[4]}"+" "+f"{grid_layout[5]}"+" "+"|")
print("|"+" "+f"{grid_layout[6]}"+" "+f"{grid_layout[7]}"+" "+f"{grid_layout[8]}"+" "+"|")
print("---------")

grid_matrix = [[[grid_layout[0]], [grid_layout[1]], [grid_layout[2]]], # 1 wiersz
               [[grid_layout[3]], [grid_layout[4]], [grid_layout[5]]], # 2 wiersz
               [[grid_layout[6]], [grid_layout[7]], [grid_layout[8]]]] # 3 wiersz

move = "X"
# taking players input

while True:
    while True:
        player_move = input()
        cords = player_move.split()
        x = int(cords[0]) - 1
        y = int(cords[1]) - 1

        if x > 2 or x < 0 or y > 2 or y < 0:
            print("Coordinates should be from 1 to 3!")
        else:
            break

    if type(x) != int or type(y) != int:
        print("You should enter numbers!")

    if grid_matrix[x][y][0] == "_":
        grid_matrix[x][y][0] = move
        if move == "X":
            move = "O"
        else:
            move = "X"
        print("---------")
        print("|"+" "+f"{grid_matrix[0][0][0]}"+" "+f"{grid_matrix[0][1][0]}"+" "+f"{grid_matrix[0][2][0]}"+" "+"|")
        print("|"+" "+f"{grid_matrix[1][0][0]}"+" "+f"{grid_matrix[1][1][0]}"+" "+f"{grid_matrix[1][2][0]}"+" "+"|")
        print("|"+" "+f"{grid_matrix[2][0][0]}"+" "+f"{grid_matrix[2][1][0]}"+" "+f"{grid_matrix[2][2][0]}"+" "+"|")
        print("---------")
    else:
        print("This cell is occupied! Choose another one!")

    winner = []
    won_results = 0
    empty_spaces = [grid_matrix[n][j][0] for n in range(3) for j in range(3)]
    x = empty_spaces.count("_")

    for grid in grid_matrix:  # sprawdzanie wierszy

        if grid[0][0][0] != "_" and grid[0][0] == grid[1][0] == grid[2][0]:
            won_results += 1
            print("????")

        if won_results == 1:
            print(f"{grid[0][0]} wins!")
            break

        if grid_matrix[0][0][0] != "_" and grid_matrix[0][0] == grid_matrix[1][1] == grid_matrix[2][2]: # sprawdzenie po skosie
            won_results += 1
            print(f"{grid_matrix[0][0][0]} wins")
            break

        if grid_matrix[0][2][0] != "_" and grid_matrix[0][2] == grid_matrix[1][1] == grid_matrix[2][0]: # i po tym drugim skosie też xD
            won_results += 1
            print(f"{grid_matrix[0][2][0]} wins")
            break

        for col in range(3):  # sprawdzanie kolumn

            if grid_matrix[0][col][0] != "_" and grid_matrix[0][col] == grid_matrix[1][col] == grid_matrix[2][col]:
                winner.append(grid_matrix[0][col])
                won_results += 1

        if won_results == 1:
            print(f"{winner[0][0]} wins")
            break

        if won_results == 0 and x == 0:
            print("Draw")
            break

    if won_results == 0 and x == 0:
        break

    if won_results == 1:
        break
'''if won_results == 0 and number_of_empty != 0 and ((0 <= number_of_x - number_of_o <= 1) or (0 <= number_of_o - number_of_x <= 1)):
    print("Game not finished")

if won_results > 1 or (number_of_x - number_of_o > 1) or (number_of_o - number_of_x > 1):
    print("Impossible")
'''
