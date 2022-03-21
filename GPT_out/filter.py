

def filterlist(list1):
    string_val1 = ''
    string_val2 = ''
    sub_list = []
    full_list = []

    for i in list1:

        topic = i[0]  # index 0 contain the topic
        sub_list.append(topic)  # store the topic in the sub list

        for query in i[1:]:
            string_val1 = ''
            string_val1 = query.replace("\n", "")  # store the value in string
            string_val2 += string_val1


        sub_list.append(string_val2)  # store the string val in the sub list
        full_list.append(sub_list)
        sub_list = []
        string_val2 = ''

    return full_list
