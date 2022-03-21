# print lists

def print_result2(result_list, doc_name):

    file = doc_name

    if file == "list_with_topic_numbers":
        open("docs\\4_list_with_topic_numbers.txt", 'w').close()
        f = open("docs\\4_list_with_topic_numbers.txt", "a")

    for i in result_list:

        topicid = i[0]
        print(topicid)
        f.write("topic id:" + str(topicid) + "\n")

        numoftopic = i[1]
        print(numoftopic)
        f.write("number of topic:" + str(numoftopic) + "\n")

        topic = i[2]
        print(topic)
        f.write("topic:" + topic + "\n")

        summery = i[3]
        print(summery)
        f.write("summery :" + summery + "\n")

        f.write("\n-------------------------\n")

    f.close()

