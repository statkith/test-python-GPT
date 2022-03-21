from xy.coordination import values
from xy.startingpoints.pointside import startside
from xy.startingpoints.pointvalue import startval,noofval,pointval

def addcordinates(list,width,height):

    no_of_points = noofval(list)
    staring_val = startval(list,no_of_points)

    sublist = []
    mainlist = []

    for x in list:

        topicid = x[0]
        sublist.append(topicid)  # add topic number

        numoftopics = x[1]

        xylist = values(numoftopics, topicid,width,height)  # get x,y values

        xval = xylist[0]
        sublist.append(xval)  # add x val

        yval = xylist[1]
        sublist.append(yval)  # add y val

        topic = x[2]
        sublist.append(topic)  # add topic

        summery = x[3]
        sublist.append(summery)  # add summery

        side = startside(numoftopics, topicid)
        sublist.append(side)     # add side

        stat_point_val = pointval(staring_val, topicid)
        sublist.append(stat_point_val)  # add val

        mainlist.append(sublist)
        sublist = []

    return mainlist
