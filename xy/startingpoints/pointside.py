import math

# box size (main topic box in the middle)
boxwidth = 320
boxheight = 320

anglex1 = boxheight/boxwidth
anglex2 = math.degrees(math.atan(anglex1))
anglex3 = 90 - anglex2

def startside(numoftopics, topicnum):

        angle = math.degrees(math.radians(360/numoftopics * (topicnum-1)))

        if numoftopics > 2:    # set the 1st topic to the top center
            angle = angle-90

        if 0-anglex2 <= angle <= 0+anglex2:
            return "right"
        elif 90-anglex3 < angle < 90+anglex3:
            return "bottom"
        elif 180-anglex2 <= angle <= 180+anglex2:
            return "left"
        else:
            return "top"


