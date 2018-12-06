#Homework 9
#1. Remember how you used ord() to calculate distance between 2 words in homework a couple of
#weeks ago. You will need to use the same source to help implement a little bit of the the auto-correct
#function commonly used today
#Your program asks the user to enter a 4 letter word (with typo) that starts with an H. Enter a misspelled
#word. For example, your program should be able to auto-correct
#heas - heat
#hinc - hind
#hout - hour
#Your program flow:
#def Distance(a,b): # This function should return a distance between 2 words
# You can probably reuse much of the code from your homework 6
#word = input(“Enter a 4 letter word (with typos) that begins with an H: ”)
# Use the 4 letter h list in this week’s packet
#Assign min_distance a really large number
#for i in wordlist: # This allows you to go through the word list.
#dist=Distance(word, i)
#...
#...
#...
#print(“Auto-correct thinks that the word is”, found_word)

def distance():
    h_word_order_dict = {'haaf': 6, 'haar': 12, 'habu': 18, 'hack': 24, 'hade': 30, 'hadj': 36, 'hads': 42, 'haed': 48, 'haem': 54, 'haen': 60, 'haes': 66, 'haet': 72, 'haff': 78, 'haft': 84, 'hagg': 90, 'hags': 96, 'haha': 102, 'hahs': 108, 'haik': 114, 'hail': 120, 'hain': 126, 'hair': 132, 'haji': 138, 'hajj': 144, 'haka': 150, 'hake': 156, 'haku': 162, 'hale': 168, 'half': 174, 'hall': 180, 'halm': 186, 'halo': 192, 'halt': 198, 'hame': 204, 'hams': 210, 'hand': 216, 'hang': 222, 'hank': 228, 'hant': 234, 'haps': 240, 'hapu': 246, 'hard': 252, 'hare': 258, 'hark': 264, 'harl': 270, 'harm': 276, 'harn': 282, 'haro': 288, 'harp': 294, 'hart': 300, 'hash': 306, 'hask': 312, 'hasp': 318, 'hast': 324, 'hate': 330, 'hath': 336, 'hats': 342, 'haud': 348, 'hauf': 354, 'haul': 360, 'haut': 366, 'have': 372, 'hawk': 378, 'hawm': 384, 'haws': 390, 'hays': 396, 'haze': 402, 'hazy': 408, 'head': 414, 'heal': 420, 'heap': 426, 'hear': 432, 'heat': 438, 'hebe': 444, 'hech': 450, 'heck': 456, 'heed': 462, 'heel': 468, 'heft': 474, 'hehs': 480, 'heid': 486, 'heil': 492, 'heir': 498, 'held': 504, 'hele': 510, 'hell': 516, 'helm': 522, 'helo': 528, 'help': 534, 'heme': 540, 'hemp': 546, 'hems': 552, 'hend': 558, 'hens': 564, 'hent': 570, 'heps': 576, 'hept': 582, 'herb': 588, 'herd': 594, 'here': 600, 'herl': 606, 'herm': 612, 'hern': 618, 'hero': 624, 'hers': 630, 'hery': 636, 'hesp': 642, 'hest': 648, 'hete': 654, 'heth': 660, 'hets': 666, 'hewn': 672, 'hews': 678, 'heys': 684, 'hick': 690, 'hide': 696, 'hied': 702, 'hies': 708, 'high': 714, 'hike': 720, 'hila': 726, 'hild': 732, 'hili': 738, 'hill': 744, 'hilt': 750, 'hims': 756, 'hind': 762, 'hing': 768, 'hins': 774, 'hint': 780, 'hioi': 786, 'hips': 792, 'hipt': 798, 'hire': 804, 'hish': 810, 'hisn': 816, 'hiss': 822, 'hist': 828, 'hits': 834, 'hive': 840, 'hiya': 846, 'hizz': 852, 'hoar': 858, 'hoas': 864, 'hoax': 870, 'hobo': 876, 'hobs': 882, 'hock': 888, 'hods': 894, 'hoed': 900, 'hoer': 906, 'hoes': 912, 'hogg': 918, 'hogh': 924, 'hogs': 930, 'hoha': 936, 'hohs': 942, 'hoik': 948, 'hoka': 954, 'hoke': 960, 'hoki': 966, 'hold': 972, 'hole': 978, 'holk': 984, 'holm': 990, 'holp': 996, 'hols': 1002, 'holt': 1008, 'holy': 1014, 'homa': 1020, 'home': 1026, 'homo': 1032, 'homs': 1038, 'homy': 1044, 'hond': 1050, 'hone': 1056, 'hong': 1062, 'honk': 1068, 'hons': 1074, 'hood': 1080, 'hoof': 1086, 'hook': 1092, 'hoon': 1098, 'hoop': 1104, 'hoot': 1110, 'hope': 1116, 'hops': 1122, 'hora': 1128, 'hore': 1134, 'hori': 1140, 'horn': 1146, 'hors': 1152, 'hose': 1158, 'hoss': 1164, 'host': 1170, 'hote': 1176, 'hots': 1182, 'houf': 1188, 'hout': 1194, 'hove': 1200, 'howe': 1206, 'howf': 1212, 'howk': 1218, 'howl': 1224, 'hows': 1230, 'hoya': 1236, 'hoys': 1242, 'hubs': 1248, 'huck': 1254, 'hued': 1260, 'huer': 1266, 'hues': 1272, 'huff': 1278, 'huge': 1284, 'hugs': 1290, 'hugy': 1296, 'huhu': 1302, 'huia': 1308, 'huic': 1314, 'huis': 1320, 'hula': 1326, 'hule': 1332, 'hulk': 1338, 'hull': 1344, 'huma': 1350, 'humf': 1356, 'hump': 1362, 'hums': 1368, 'hung': 1374, 'hunh': 1380, 'hunk': 1386, 'huns': 1392, 'hunt': 1398, 'hups': 1404, 'hurl': 1410, 'hurt': 1416, 'hush': 1422, 'husk': 1428, 'huso': 1434, 'huss': 1440, 'huts': 1446, 'hwan': 1452, 'hwyl': 1458, 'hyed': 1464, 'hyen': 1470, 'hyes': 1476, 'hyke': 1482, 'hyla': 1488, 'hyle': 1494, 'hymn': 1500, 'hype': 1506, 'hypo': 1512, 'hyps': 1518, 'hyte': 1524}

    user_h_word = input("Please type in a 4 letter word beginning with an H that has one or more typos. If the word is longer than 4 letters, it will be shortened!")
    user_h_word = user_h_word.lower()[:4]

    order_sum = 0
    for i in range(0, len(user_h_word)):
        order_sum += int(ord(user_h_word[i]))
    print("Order Sum: {}".format(order_sum))

    distance_dict = {}
    minimum_distance = 20
    
    for key, value in h_word_order_dict.items():
        distance = abs(int(order_sum) - int(value))
        if distance < minimum_distance:
            minimimum_distance = distance

            distance_dict["{} - {}".format(user_h_word,key)] = distance

    minimum = 15
    for key, value in distance_dict.items():
        if int(distance_dict[key]) < minimum:
            minimum = int(distance_dict[key])
            min_value_key = key
    

    words = min_value_key.split()
    word_list = []
    for word in words:
        word_list.append(word)
    print("The User Word, {}, has been autocorrected to {}".format(word_list[0].title(), word_list[2].title()))

distance()



#2. Write a recursive function that helps you calculate the function defined as follows
#f(6) = 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6
#Hint: If n=1, the value is 1. Otherwise, the value is 1/n + 1/(n-1). Keep decrementing n each time

def add_fractions(n):
    number_string = ""
    my_list = []
    number_list = []
    one_list = []
    if n == 1:
        my_list.append("1 +")
        one_list.append("1 +")
        number_list.append("1 +")
        number_string += "{} +".format(n)
        print("{} +".format(n))
        return 1
    elif n > 1:
        my_list.append("1/{}".format(n))
        number_list.append("1/{} +".format(n))
        add_fractions(n-1)

    for i in range(0, len(my_list)):
        number_string += "{} +".format(my_list[i])

    final_list = one_list + number_list
    print(final_list[0])


add_fractions(6)

#Jack's Solution
# def f(n):
#     if n == 1:
#         return 1
#     else:
#         return 1/n + f(n)



#3. Write a recursive function that accepts 2 arguments into the parameters x and y. The function should
#return the value of x times y. Remember, multiple can be done as follows:
#7 x 4 = 4 + 4 + 4 + 4 + 4 + 4 + 4
#print(Mult(7,4))
#28

# def multiple(x,y):
#     if y == 1:
#         print("x = {}, y = {}".format(x,y))
#         return 1
#     elif y < 0:
#         print("x = {}, y = {}".format(x,y))
#         print(x - multiple(x, y+1))
#         return(x - multiple(x, y+1))
#     else:
#         print("x = {}, y = {}".format(x,y))
#         print(x + multiple(x, y-1))
#         return x + multiple(x, y-1)

# multiple(7,4)

my_list = []
product_list = []
def multiple(x,y):
    product = x * y
    product_list.append(product)
    if x == 1:
        my_list.append(y)
        print(my_list)
        my_string = ""
        for i in range(0, len(my_list)):
            if i != len(my_list) - 1:
                my_string += "{} + ".format(my_list[i])
            else:
                my_string += "{}".format(my_list[i])
        my_string += " = {}".format(product_list[0])
        print(my_string)
        return product
    elif x > 1:
        my_list.append(y)
        return x + multiple(x-1, y)

multiple(7,4)



#4. Use a recursive function to help you print out the Fibonacci sequence (Optional)
#The Fibonacci sequence is 1,2,3,5,8,13,...
#Hint:
#If there are less than 3 numbers, the sequence is 1,2.
#If there are 3, the sequence is 1,2, sum of the previous 2 numbers.