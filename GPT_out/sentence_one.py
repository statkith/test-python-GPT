

def first_sentence(list1):
    string_val1 = ''
    string_val2 = ''
    sub_list = []
    full_list = []

    for i in list1:

        topic = i[0]  # index 0 contain the topic
        sub_list.append(topic)  # store the topic in the sub list

        for query in i[1:]:
            string_val1 = ''
            string_val1 = query.split(".")  # split by dot
            string_val2 += (string_val1[0] + ". ") # get the first sentence and add a .

        sub_list.append(string_val2.replace("\n", ""))  # store the string val in the sub list remove new lines
        full_list.append(sub_list)
        sub_list = []
        string_val2 = ''

    return full_list #return summary with 1st line
