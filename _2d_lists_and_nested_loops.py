#2 d loops and nested loops

number_grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [0]
        ]
print("2D Loop")
print(number_grid[1][2])
print("\n")

print("Nested for loop")
for row in number_grid:
        for col in row:
                print(col)
