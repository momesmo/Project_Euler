def names_score(filename):
    file = open(filename)
    names_not = file.readlines()
    names = names_not[0].replace("\"","").split(",")
    names.sort()
    name_score = 0
    total_score = 0
    for i in range(len(names)):
        name = names[i]
        for c in name:
            name_score+=ord(c.lower())-96
        total_score += name_score*(i+1)
        print(i, "*", name_score, "=", name_score*(i+1), total_score)
        name_score = 0
    return total_score

print(names_score("p022_names.txt"))
