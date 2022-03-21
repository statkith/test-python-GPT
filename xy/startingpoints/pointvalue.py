from xy.startingpoints.pointside import startside

boxwidth = 320
boxheight = 320


def startval(list, noofval):
    mainlist = []
    sublist = []
    leftno = 0
    rightno = 0
    topno = 0
    bottomno = 0

    for x in list:

        topicnum = x[0]
        numoftopics = x[1]

        x = startside(numoftopics, topicnum)

        sublist.append(topicnum)

        if x == "left":
            leftno += 1
            sublist.append(x)
            sublist.append(leftno)
            sublist.append(noofval[0])

        elif x == "bottom":
            bottomno += 1
            sublist.append(x)
            sublist.append(bottomno)
            sublist.append(noofval[1])

        elif x == "right":
            rightno += 1
            sublist.append(x)
            sublist.append(rightno)
            sublist.append(noofval[2])

        elif x == "top":
            topno += 1
            sublist.append(x)
            sublist.append(topno)
            sublist.append(noofval[3])

        mainlist.append(sublist)
        sublist = []

    return mainlist


# calculate number of topic per side
def noofval(list):
    leftno = 0
    rightno = 0
    topno = 0
    bottomno = 0
    sidevals = []

    for x in list:

        topicnum = x[0]
        numoftopics = x[1]

        x = startside(numoftopics, topicnum)

        if x == "left":
            leftno += 1

        elif x == "bottom":
            bottomno += 1

        elif x == "right":
            rightno += 1

        elif x == "top":
            topno += 1

    sidevals.append(leftno)
    sidevals.append(bottomno)
    sidevals.append(rightno)
    sidevals.append(topno)

    return sidevals


def pointval(pointlist, topicid):
    x = pointlist[topicid - 1]
    id = x[0]
    side = x[1]
    sideno = x[2]
    noofval = x[3]
    print(side)

    if side == "right" :
        starting_val = (boxheight / (noofval + 1)) * sideno
    elif side == "left":
        starting_val = boxheight - ((boxheight / (noofval + 1)) * sideno)
    elif side == "bottom":
        starting_val = boxwidth - ((boxwidth / (noofval + 1)) * sideno)
    elif side == "top" and id == 1:
        starting_val = boxwidth/2
    elif side == "top" and id <5:
        starting_val = boxwidth/2 + ((boxwidth / (noofval + 1)) * (sideno-1) )
    else:
        starting_val = (boxwidth / (noofval + 1)) * (sideno-((noofval + 1)/2))



    return round(starting_val,1)
