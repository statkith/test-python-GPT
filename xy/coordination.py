import math

# screen size

card2width = 450 # cards around the main topic
card2height = 450 # cards around the main topic



distance = 600  # distance from the center point


def values(numoftopics, topicnum,width,height):
    # width = 1200
    # height = 800

    x1 = width   # center point x
    y1 = height   # center point x

    if topicnum == 0:        # *** main topic in the middle not
        x = x1
        y = y1
        return x, y

    else:                    # sub topics

        angle = math.degrees(math.radians(360/numoftopics * (topicnum-1)))

        if numoftopics > 2:    # set the 1st topic to the top center
            angle = angle-90

        a = newangle(angle)
        x2 = xval(a)
        y2 = yval(a)

        x = round(x2, 1)
        y = round(y2, 1)

        if 90 < angle <= 180:
            x = x1 - x - card2width
            y = y1 + y
            return round(x, 1), round(y, 1)
        elif 180 < angle <= 270:
            x = x1-x - card2width
            y = y1-y
            return round(x, 1), round(y, 1)
        elif angle == -90 or angle == 90:
            x = x1 + x - card2width/2
            y = y1 + y
            return round(x, 1), round(y, 1)
        else:
            x = x1 + x
            y = y1 + y
            return round(x, 1), round(y, 1)


def newangle(angle):
    if angle <= 90:
        return angle
    elif 90 < angle <= 180:
        return 180 - angle
    elif 180 < angle <= 270:
        return angle - 180
    else:
        return 360 - angle


def xval(angle):
    x = math.cos(math.radians(angle))*distance
    return x


def yval(angle):
    x = math.sin(math.radians(angle))*distance
    return x


