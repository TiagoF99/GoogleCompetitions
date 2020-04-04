num_cases = int(input())
i = 1
while num_cases > 0:

    string = input()
    sol = ''
    for char in string:
        if sol == '':
            sol += '(' * int(char)
            sol += char
        else:
            if char == sol[-1]:
                sol += char
            else:
                sol += ')' * int(sol[-1])
                sol += '(' * int(char)
                sol += char

    if sol[-1] != ')':
        sol += ')'*int(sol[-1])
    print(sol)

    print("Case #{}: {}".format(i, sol))
    i += 1
    num_cases -= 1

