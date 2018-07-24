def read_in_word(filename):
    file = open(filename)
    word_not = file.readlines()
    words = word_not[0].replace("\"", "").split(",")
    tri_nums = [1]
    num_tri_words = 0
    for word in words:
        word_val = 0
        for l in word:
            word_val += ord(l.lower())-96
        while word_val > tri_nums[-1]:
            tri_nums.append(0.5 * len(tri_nums) * (len(tri_nums) + 1))
        if word_val in tri_nums:
            num_tri_words += 1
    return num_tri_words


print(read_in_word("p042_words.txt"))