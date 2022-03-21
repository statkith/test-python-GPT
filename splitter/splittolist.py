# split the source file

from splitter.patterncheck import matchtpara, matchtopic


def splitbyurl(url, maxlen):
    with open(url, encoding="utf-8") as f:  # url = txt file location

        string_val = ''
        string_val2 = ''
        para_list = []  # in this list first value is topic others are paragraphs
        all_para = []  # in this list contain all the para lists

        start = 0
        topiccount = 0
        slength = 0
        paracount = 0

        # split the doc line by line
        for x in f.read().split("\n"):

            topic = matchtopic(x)  # check the line is a topic or not | return topic=1 / not = 0
            para = matchtpara(x)  # check the line is starting a new para or not | return para=1 / not = 0

            # if the line is a topic
            if topic == 1:

                # check is it a new topic
                if start >= 1:
                    if string_val2 != '':
                        para_list.append(string_val2)
                        string_val2 = ''
                        paracount = 0

                    all_para.append(para_list)  # store the para list in the main list (all_list)
                    para_list = []  # clear the para list
                    topiccount += 1

                para_list.append(x)  # store the topic in the para list
                start += 1

            # if the line is not starting a new para
            elif para == 0:
                string_val += x  # store the lines in a string

            # if par end (find a space,tab or a empty in a new line)
            else:
                slength = len(string_val) + len(string_val2)

                if string_val != '':  # if the line not an empty string

                    if slength <= maxlen:  # para less than min character limit

                        if paracount == 0:
                            string_val2 = string_val2 + string_val
                            string_val = ''
                            paracount += 1
                        else:
                            string_val2 = string_val2 + string_val
                            string_val = ''
                            paracount += 1

                    elif slength >= maxlen and paracount >= 1:  # para greater than max character limit
                        if string_val2 != None:
                            para_list.append(string_val2)  # store the string value in the para list
                            string_val2 = string_val
                            string_val = ''

                    else:
                        para_list.append(string_val)
                        string_val = ''

                string_val += x  # find a space or a tab store the val in the string

        if topiccount < start:

            if string_val != '':
                para_list.append(string_val)  # store the string value in the para list

            if string_val2 != '':
                para_list.append(string_val2)

            all_para.append(para_list)  # store the lines in a string

        '''
        all_para = [[para_list],[para_list],[para_list]]
        para_list = ["subtopic","para1 string","para2 string"]
        '''

    # topiccount = 0
    # paracount = 0
    #
    # for i in all_para:
    #     topiccount += 1
    #     print("topics no:", topiccount)  # topic number
    #     for x in i:
    #         paracount += 1
    #
    #     print("# of para:", paracount)  # Number of para

    return all_para
