import re

#------Match  topic--------

def matchtopic(string):

    returnval = 0
    text = string

    pattern = re.compile(r'(\t|\s)*\d\.\d*\s*\w+') ## EX: 1.1 TOPIC (r'(\t|\s)*\d\.\d\s*\w+')
    matches = pattern.match(text)

    if matches == None:

        returnval = 0  ###not a topic

    else:

        returnval = 1  ### new topic

    return returnval


#------Match  para--------

def matchtpara(string):

    returnvalue = 0

    text = string

    pattern = re.compile(r'(\t|\s|^.{0}$)')  ##check the 1st character is a tab, space or empty
    matches = pattern.match(text)

    if matches == None:

        returnvalue = 0  # current paragraph

    else:

        returnvalue = 1  ### starting a new  paragraph

    return returnvalue






