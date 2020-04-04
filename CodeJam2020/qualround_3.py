num_cases = int(input())
i = 1
while num_cases > 0:

    lines = int(input())
    times = []
    while lines > 0:
        line = input()
        t1, t2 = line.split(" ")[0], line.split(" ")[1]
        times.append((int(t1), int(t2)))
        lines -= 1

    sol = ""
    j, c = [], []
    for time in times:
        if sol == "":
            sol += "J"
            j.append(time)
        else:
            check_j = True
            for interval in j:
                inter = [p for p in range(interval[0], interval[1])]
                for k in range(time[0], time[1] + 1):
                    if k in inter:
                        check_j = False
                        break

            if check_j:
                sol += "J"
                j.append(time)
            else:
                check_c = True
                for interval in c:
                    inter = [p for p in range(interval[0], interval[1])]
                    for k in range(time[0], time[1] + 1):
                        if k in inter:
                            check_c = False
                            break
                print(j, c, time)

                if check_c:
                    sol += "C"
                    c.append(time)
                elif not check_c and not check_j:
                    sol = "IMPOSSIBLE"
                    break


    print("Case #{}: {}".format(i, sol))
    i += 1
    num_cases -= 1
