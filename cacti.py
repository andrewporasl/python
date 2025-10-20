def cacti_number(a):
    plot = [row[:] for row in a]
    r = len(plot)
    c = len(plot[0])
    total = 0

    for row in range (r):
        for cell in range(c):
            if plot [row][cell] == 0:
                up = (row > 0 and plot[row - 1][cell] == 1)
                down = (row < r - 1 and plot[row + 1][cell] == 1)
                left = (cell > 0 and plot[row][cell - 1] == 1)
                right = (cell < c - 1 and plot[row][cell + 1] == 1)

                if not (up or down or left or right):
                    plot[row][cell] = 2
                    total += 1



    return total