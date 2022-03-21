from evaluation.doc_similarity_evaluation import doc_similarity_evaluation
from evaluation.top_ten import final_summary


def top_ten_lines(list):
    # print(list)
    sub_list = []
    full_list = []

    summary_list = []
    summary_with_val = []
    evalution_val_list = []

    for query in list:

        topic = query[0]  # every list 1st block contain a topic
        sub_list.append(topic)  # store the topic in the 1st block of the sub list

        # summary in index 1 , index 0 contain the topic
        string_val1 = query[1].split(".")

        for sentence in string_val1[:-1]:
            # print(sentence)
            summary_with_val.append(sentence)

            # get doc summary evaluation value
            ev_val = doc_similarity_evaluation([topic],[sentence])

            summary_with_val.append(ev_val)
            evalution_val_list.append(ev_val)

            summary_list.append(summary_with_val)
            summary_with_val=[]

        # print(summary_list)
        # print(evalution_val_list)

        '''
            summary_list = [[summary1,evalue1], [summary2,evalue2]]
            evalution_val_list = ["evalue1", "evalue2"]
        '''

        # get the top valued sentences
        final_sum = final_summary(summary_list,evalution_val_list)
        sub_list.append(final_sum)

        summary_list = []
        evalution_val_list =[]

        full_list.append(sub_list)
        sub_list = []

    # print(full_list)
        '''
            full_list = [[topic1,summary1], [topic2,summary2]]
        '''

    return full_list


# list = [["1.1 What is UX?", "1User experience is the process of designing a product, system or service that makes users feel good about using it. 2User experience is about how you feel when using a product. 3 I’m not sure what to do. 4 Functional Design: The design that is designed to work with the user. 5 Functional design is the process of designing a product to do what itis designed to do. 6 Design is about the experience. 7 The car is a great tool for creating the experience of driving. 8 Experience design is a process that starts with the customer. 9  Design is a process of creating something that’s not there yet. 10 UX is a problem solving discipline."],
#         ["1.2 What is UX?", "2User experience is the process of designing a product, system or service that makes users feel good about using it. 2User experience is about how you feel when using a product.  3I’m not sure what to do. 4 Functional Design: The design that is designed to work with the user. 5 Functional design is the process of designing a product to do what itis designed to do. 6 Design is about the experience. 7 The car is a great tool for creating the experience of driving. 8 Experience design is a process that starts with the customer. 9 Design is a process of creating something that’s not there yet. 10  UX is a problem solving discipline."]]
#
#
# top_ten_lines(list)
