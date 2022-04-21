list = [17, 38, 10, 25, 72]
list.sort()
# print(list)
list.append(12)
list.reverse()
# print(list)
# print(list.index(17))
list.remove(38)
# print(list[2:3])
# print(list[:2])
# print(list[3:])
# print(list[-1])

truc = []
machin = [0.0, 0.0, 0.0, 0.0, 0.0]
# for i in range(0,3):
#    print(i)
# for i in range(4,7):
#    print(i)
# for i in range(2,8,2):
#    print(i)
chose = [0, 1, 2, 3, 4, 5]
# print(chose.__contains__(3),chose.__contains__(6))
c2 = [item + 3 for item in chose]
# print(c2)
c3 = [item + 3 for item in chose if item > 2]
# print(c3)
l4 = [(a, b) for a in "abc" for b in "de"]
# print(l4)
l5 = [i for i in range(0, 10)]
# print(sum(l5))
x = {"a", "b", "c", "d"}
y = {"s", "b", "d"}


# print(x)
# print(y)
# print(x.__contains__("c"))
# print(y.__contains__("a"))
# print(x-y)
# print(x.union(y))
# print(x.intersection(y))


def compterMots(char):
    listeMots = char.split()
    dic = {}
    for mot in listeMots:
        if dic.keys().__contains__(mot):
            dic[mot] += 1
        else:
            dic[mot] = 1
    return dic


print(compterMots("les chaussettes de l'archiduchesse sont les chaussettes de la reine"))
dico = {"Au": {"Te/Tf": [2970, 1063], "Z/A": [79, 196.967]}, "Ga": {"Te/Tf": [2237, 29.8], "Z/A": [31, 169.72]}}
print (dico["Au"]["Z/A"][0])


def pile (*args):
    list = []
    for i in args:
        list.append(i)
    return list


def empile (el, pile):
    pile.append(el)


def depile (pile):
    return pile.pop()


pileFifo = []


def pileFifo (*args):
    for i in args:
        pileFifo.append(i)


def empileFifo (el):
    pileFifo.insert(0, el)


def depileFifo (pile):
    return pile.pop()