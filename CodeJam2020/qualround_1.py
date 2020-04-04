num_cases = int(input())
i = 1
while num_cases > 0:

    size_mat = int(input())
    matrix = []
    while size_mat > 0:
        row = input()
        matrix.append(row.split(" "))
        size_mat -= 1

    k, r, c = 0, 0, 0
    cols = {}
    for j in range(len(matrix)):
        for m in range(len(matrix[0])):
            if j == m:
                k += int(matrix[j][m])

            if m not in cols:
                cols[m] = [matrix[j][m]]
            else:
                cols[m].append(matrix[j][m])

    for row in matrix:
        rep = []
        for item in row:
            if item in rep:
                r += 1
                break
            else:
                rep.append(item)

    for col in cols:
        rep = []
        for item in cols[col]:
            if item in rep:
                c += 1
                break
            else:
                rep.append(item)

    print("Case #{}: {} {} {}".format(i, k, r, c))
    i += 1
    num_cases -= 1
