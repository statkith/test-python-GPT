# print lists

def print_result3(result_list, doc_name):

    file = doc_name

    if file == "list_with_points":
        open("docs\\5_list_with_points.txt", 'w').close()
        f = open("docs\\5_list_with_points.txt", "a")


    for i in result_list:

        topicid = i[0]
        print(topicid)
        f.write("topic id:" + str(topicid) + "\n")

        xval = i[1]
        print(xval)
        f.write("xval:" + str(xval) + "\n")

        yval = i[2]
        print(yval)
        f.write("yval:" + str(yval) + "\n")

        topic = i[3]
        print(topic)
        f.write("topic:" + topic + "\n")

        summery = i[4]
        print(summery)
        f.write("summery :" + summery + "\n")

        side = i[5]
        print(side)
        f.write("side :" + side + "\n")

        pointval = i[6]
        print(pointval)
        f.write("pointval :" + str(pointval) + "\n")

        f.write("\n-------------------------\n")

    f.close()

