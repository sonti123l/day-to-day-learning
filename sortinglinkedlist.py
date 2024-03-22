class Initializing:
    def __init__(self, a):
        self.a = a


class linked_list():

    def new_linkedlist(self):
        my_object = Initializing(int(input()))
        count = 0
        a = 0
        b = 0
        new_list = []
        for i in range(my_object.a):
            x = int(input("enter array list elements:"))
            new_list.append(x)
        for j in range(len(new_list)):
            if new_list[j] == 0:
                count += 1
            elif new_list[j] == 1:
                a += 1
            elif new_list[j] == 2:
                b += 1
            else:
                print("no element given")
        return count, a, b




object=linked_list()
a, b, c = object.new_linkedlist()
list_2 = []

for i in range(a):
    list_2.append(0)
for i in range(b):
    list_2.append(1)
for i in range(c):
    list_2.append(2)

print(list_2)
