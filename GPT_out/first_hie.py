# first GPT_out

from gpt import GPT
from splitter.splittolist import splitbyurl
from GPT_out.filter import filterlist
from GPT_out.sentence_one import first_sentence
from print.print import print_result
# from evaluation.list_maker import top_ten_lines


def first_hierarchy_output(url, maxlen, temp, max_token):
    # Construct GPT object and show some examples
    gpt = GPT(engine="ada",
              temperature=temp,
              max_tokens=max_token,
              )


    # ----------------import list------------------#

    get_list = splitbyurl(url, maxlen)  # send the source file, para length | receive the list contain topic and para
    sub_list = []  # to store sub lists
    first_hierarchy_return_list = []  # main list to return the list after GPT send the summery

    # ---------------Get response-----------------#

    for i in get_list:

        topic = i[0]  # every list 1st block contain a topic
        sub_list.append(topic)  # store the topic in the 1st block of the sub list

        # read the list from index 1 , index 0 contain the topic
        for query in i[1:]:
            response = gpt.get_top_reply(query)  # send the string to GPT and receive the value
            sub_list.append(response)  # store the value in the sub list

        first_hierarchy_return_list.append(sub_list)  # store the sub list in the main list
        sub_list = []  # clear the sublist

        '''
        first_hierarchy_return_list = [[sub_list],[sub_list],[sub_list] ]
        sub_list = ["topic","GPT output for para1","GPT output for para2"]
        '''

    # raw output from openai
    print("openai output")
    print_result(first_hierarchy_return_list, "openai_out")

    # filter list remove unwanted new lines,spaces and combine all the paras to a single para
    # first_hierarchy_full = filterlist(first_hierarchy_return_list)

    # filter list - get the first sentence  from each output and combine all the sentences to a single para
    first_sentence_only = first_sentence(first_hierarchy_return_list)
    '''
    first_hierarchy = [[sub_list], [sub_list], [sub_list]]
    sub_list = ["topic", "summary"]
    '''

    #top ten sentences
    # final_list = top_ten_lines(first_sentence_only)
    '''
    final_list = [[sub_list], [sub_list], [sub_list]]
    sub_list = ["topic", "summary"]
    '''


    return first_sentence_only  # return the main list



