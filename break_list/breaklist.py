my_list = [1, 2, 3, 4, 5,
			6, 7, 8, 9]

def breaklistintochunks(my_list,size):

    n = size

    # using list comprehension
    final = [my_list[i * n:(i + 1) * n] for i in range((len(my_list) + n - 1) // n )]
    print (final)
    return final


count = 1
name = "map"+str(count)
print (name)