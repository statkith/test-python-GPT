import numpy as np


def get_top_ten(list):
    top_id = np.argsort(list)[-5:]
    top_values = [list[i] for i in top_id]
    # print(top_values)
    open("docs\\evaluation\\top_val.txt", 'w').close()
    f = open("docs\\evaluation\\top_val.txt", "a")
    f.write(str(top_values)+"\n")

    return top_values


def final_summary(summary, evalue1):

    sub_list =''
    topv_values = get_top_ten(evalue1)

    for i in summary:

        evalue2 = i[1]
        for val in topv_values:
            if evalue2 == val:
                sub_list += (i[0] + ". ")

    print(sub_list)

    open("docs\\evaluation\\top_sentence.txt", 'w').close()
    f = open("docs\\evaluation\\top_sentence.txt", "a")
    f.write(str(sub_list) + "\n")

    return sub_list

# list2=[3,2,1,5,6,4,7]
# list=[["a",7],["b",2],["c",1],["d",5],["e",6],["f",4]]
#
# final_summary(list,list2)