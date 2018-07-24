import num2words

def return_letter_count(num):
    s = 0
    for i in range(1, num + 1):
        w = num2words.num2words(i, False, 'en')
        s += len(w.replace(" ", "").replace("-", ""))
    return s

print(return_letter_count(1000))
