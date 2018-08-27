

def find_char(word_list, char):
    new_list =[]
    for i in range(0, len(word_list)):
        if word_list[i].find(char) != -1:
            new_list.append(word_list[i])
    print new_list
# test_list = ["yo", "my", "name", "goes", "gonzo","boss"]
# find_char(test_list,"o")

my_string = ["apple", "a", "banana", "z", "kiwi", "w", "pineapple", "k"]
find_char(my_string,"a")