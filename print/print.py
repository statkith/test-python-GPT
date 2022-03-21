# print lists

def print_result(result_list, doc_name):

    # C:\\Users\\Amila\\PycharmProjects\\mongotest\\docs\input1.txt

    file = doc_name

    if file == "raw_input":
        open("docs\\1_raw_input.txt", 'w').close()
        f = open("docs\\1_raw_input.txt", "a")

    elif file == "openai_out":
        open("docs\\2_openai_out.txt", 'w').close()
        f = open("docs\\2_openai_out.txt", "a")

    elif file == "filter_out":
        open("docs\\3_filter_out.txt", 'w').close()
        f = open("docs\\3_filter_out.txt", "a")



    for i in result_list:
        sub_list = 1
        topic = i[0]  #every list 1st block contain a topic
        print(topic)
        f.write(topic + "\n\n")

        for query in i[1:]:

            length = len(query)
            print("item", sub_list, "- len", length, "-", query + "\n") #other block contain paragraphs

            f.write(query + "\n&&\n")

            sub_list += 1

        f.write("\n----------------------------\n")

    f.close()

