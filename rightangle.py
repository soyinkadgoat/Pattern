rows = int(input("Enter the total number of rows: "))

for i in range(rows + 1):
    for j in range(1, i + 1):
        if i < rows + 1:
            print("* ", end=' ')

    print()