word = input()
word = " ".join(word)   
word = word.split()
new_lst = []

while len(word) != 0:
    if len(word) == 1:
        new_lst.append(word[0])
        word.remove(word[0])
    elif len(word) == 2:
        if word[0] == "A" and word[1] == "A":
            new_lst.append(word[0])
            word.remove(word[0])
        elif word[0] == "A" and word[1] != "A":
            new_word = word[0] + word[1]
            new_lst.append(new_word)
            word.remove(word[0])
            word.remove(word[0])
        elif word[0] != "A" and word[1] != "A":
            new_lst.append(word[0])
            word.remove(word[0])
        elif word[0] != "A" and word[1] == "A":
            new_word = word[0] + word[1]
            new_lst.append(new_word)
            word.remove(word[0])
            word.remove(word[0]) 
    elif len(word) == 3:
        if word[0] == "A" and word[1] == "A":
            new_lst.append(word[0])
            word.remove(word[0])
        elif word[0] == "A" and word[1] != "A":
            new_word = word[0] + word[1]
            new_lst.append(new_word)
            word.remove(word[0])
            word.remove(word[0])
        elif word[0] != "A" and word[1] == "A" and word[2] != "A":
            new_word = word[0] + word[1] + word[2]
            new_lst.append(new_word)
            word.remove(word[0])
            word.remove(word[0])
            word.remove(word[0])
        elif word[0] != "A" and word[1] == "A":
            new_word = word[0] + word[1]
            new_lst.append(new_word)
            word.remove(word[0])
            word.remove(word[0])
        elif word[0] != "A" and word[1] != "A":
            new_lst.append(word[0])
            word.remove(word[0])
    else:
        if word[0] == "A" and word[1] == "A":
            new_lst.append(word[0])
            word.remove(word[0])
        elif word[0] == "A" and word[1] != "A" and word[2] == "A" and word[3] != "A":
            new_word = word[0] + word[1] + word[2] + word[3]
            new_lst.append(new_word)
            word.remove(word[0])
            word.remove(word[0])
            word.remove(word[0])
            word.remove(word[0])
        elif word[0] == "A" and word[1] != "A":
            new_word = word[0] + word[1]
            new_lst.append(new_word)
            word.remove(word[0])
            word.remove(word[0])
        elif word[0] != "A" and word[1] == "A" and word[2] != "A":
            new_word = word[0] + word[1] + word[2]
            new_lst.append(new_word)
            word.remove(word[0])
            word.remove(word[0])
            word.remove(word[0])
        elif word[0] != "A" and word[1] == "A":
            new_word = word[0] + word[1]
            new_lst.append(new_word)
            word.remove(word[0])
            word.remove(word[0])
        elif word[0] != "A" and word[1] != "A":
            new_lst.append(word[0])
            word.remove(word[0])



final = ""
for i in new_lst:
    final += i + " "
print(final[0:-1])
    


    
