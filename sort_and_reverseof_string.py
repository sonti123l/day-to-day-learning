def reverse_words_order_and_swap_cases(name_word):
    list_1 = []
    list_2 = []
    full_name = ""
    for i in name_word:
        list_1.append(i)
    for k in list_1:
        if k.islower() == True:
            list_2.append(k.upper())
        elif k == " ":
            list_2.append(k)
        elif k.isupper() == True:
            list_2.append(k.lower())


    value=len(list_2)-1
    while value >= 0:
        full_name += list_2[value]
        value-=1

    name = full_name.split(" ")
    for i in range(len(name)):
        var_name = name[i]
        print(var_name[::-1], end=" ")


int_name = input()
reverse_words_order_and_swap_cases(name_word=int_name)
