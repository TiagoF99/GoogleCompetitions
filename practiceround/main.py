import os


def parse(file, name):

    with open(file) as f:
        nums_1 = None
        nums_2 = None
        for line in f:
            line = line.strip()
            if nums_1 is None:
                nums_1 = line.split(" ")
            else:
                nums_2 = line.split(" ")
        capacity = int(nums_1[0])
        to_p = []
        for idx, item in enumerate(nums_2):
            to_p.append((int(item), idx))
        to_p.sort(key=lambda x: x[0], reverse=True)

        assigned = {}
        i = 0
        while capacity >= 0 and i < len(to_p):
            if to_p[i][0] <= capacity:
                assigned[to_p[i][1]] = to_p[i][0]
                capacity -= to_p[i][0]
            i+=1

        first_line = str(len(assigned)) + "\n"
        second_line = ""
        for idx, item in enumerate(nums_2):
            if idx in assigned:
                second_line += (str(idx) + " ")
        second_line = second_line.strip()
        print(first_line)
        print(second_line)

        with open("./output/" + name + "_output", "w") as output:
            output.write(first_line)
            output.write(second_line)
        output.close()







if __name__ == "__main__":

    for file in os.listdir("./data"):
        parse("./data/" + file, file)
