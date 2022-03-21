
def topiccount(list):
    numoftopic =0

    for i in list:
        numoftopic += 1

    return numoftopic


def topicnum(list):
    sub_list = []
    main_list = []

    numoftopic = topiccount(list)  # no of topics
    topicnum = 1

    for i in list:

        sub_list.append(topicnum)   # topicnumber
        topicnum +=1

        sub_list.append(numoftopic)  # no of topics

        topic = i[0]            # list 1st block contain a topic
        sub_list.append(topic)

        length = len(i)
        if length > 1:
            summery = i[1]            # list 2nd block contain summery
            sub_list.append(summery)
        else:
            sub_list.append("no summery")

        main_list.append(sub_list)  # store the sub list in the main list
        sub_list = []  # clear the sublist

        '''
        [topic_number, number_of_topics,topic,summery]
        '''

    return main_list
