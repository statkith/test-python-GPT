from gpt import set_openai_key
from GPT_out.first_hie import first_hierarchy_output
from print.print import print_result
from convert.converter import convert

from splitter.splittolist import splitbyurl

from topic_num.topic_count import topicnum
from print.print2 import print_result2
from print.print3 import print_result3
from mongo.savetodb import savedb
from xy.addxy import addcordinates
from break_list.breaklist import breaklistintochunks
from mongo.cleardb import cleardatabase

def gpt3(url,width,height):

        print(width)
        print(height)

        # Your API KEY
        KEY_NAME = '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'

        first_hie_max_token = 90
        first_hie_temperature = 0

        # file location word document .docx
        source_doc_url = url

        # text file location auto convert and save in this location no need to change
        txt_url = "convert\\sample.txt"

        # para character limit
        maxlength = 760      # maximum length for a paragraph

    # if __name__ == '__main__':
        set_openai_key(KEY_NAME)

        convert(source_doc_url, txt_url)  # convert the doc file

        print("first input")
        input1 = splitbyurl(txt_url, maxlength)
        print_result(input1, "raw_input")               # raw input

        # get the 1st GPT_out output from GPT , send the source file
        first_output = first_hierarchy_output(txt_url, maxlength, first_hie_temperature, first_hie_max_token )

        print("first output with filter")
        print_result(first_output, "filter_out")        # filtered openai output

        # list_with_topic_num = topicnum(first_output)    # add topic numbers to the list
        # print_result2(list_with_topic_num, "list_with_topic_numbers")

        # list_with_xy = addcordinates(list_with_topic_num, width, height)    # add xy,points to the list
        # print_result3(list_with_xy, "list_with_points")
        #
        # savedb(list_with_xy, width, height)                      # save list in db

        breaklist = breaklistintochunks(first_output,10) # break the list in to parts

        cleardatabase()
        count = 1
        for x in breaklist:

                list_with_topic_num = topicnum(x)    # add topic numbers to the list
                print_result2(list_with_topic_num, "list_with_topic_numbers")

                list_with_xy = addcordinates(list_with_topic_num, width, height)    # add xy,points to the list
                print_result3(list_with_xy, "list_with_points")

                mapname = "map"+str(count)
                count +=1

                savedb(list_with_xy, width, height, mapname)                      # save list in db


        return "done"

# gpt3()