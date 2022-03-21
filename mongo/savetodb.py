from mongo.mongodb import db, printdb


def savedb(test_list, width, height,mapname):

    nodes = []
    node1 = {
                "id": "default",
                "type": "defaultnode",
                "position": {
                    "x": width - 160,  # if box with 320
                    "y": height,
                },
                "targetPosition": "top",
                "data": [
                    {
                        "topic": ""
                    }
                ],
                "style": [{
                    "background": "FFFFFF",
                    "color": "#333",
                    "borderRadius": "100%",
                    "width": 320,
                }]
            }
    nodes.append(node1)

    # nodes list
    for x in test_list:

        topicid = x[0]
        xval = x[1]
        yval = x[2]
        topic = x[3]
        summery = x[4]

        topics = {"id": topicid,
                  "position": {
                      "x": xval,
                      "y": yval
                    },
                  "targetPosition": "top",
                  "data": [
                      {
                          "topic": topic,
                          "image": "https://image.freepik.com/free-vector/modern-company-letterhead_1435-1042.jpg",
                          "summery": summery,
                      }
                    ],
                  "style": [{
                    "background": "FFFFFF",
                    "color": "#333",
                    "width": 450,
                    "height": 150
                    }]
                  }

        nodes.append(topics)

    # edges list
    edges = []
    for y in test_list:
        topic = y[0]

        lines = {
            "id": "default-%s" % topic,
            "source": "default",
            "target": "%s" % topic,
            "sourceHandle": "h-%s" % topic,
            "style": {
                "stroke": "yellow",
                "strokeWidth": "5"
            }
        }
        edges.append(lines)

    # starting points
    startpoint = []

    for z in test_list:
        topic = z[0]
        side = z[5]
        pointval = z[6]

        if side=="top" or side =="bottom":
            sidex = "left"
        else:
            sidex = "top"

        points={
            "id" : "h-%s" % topic,
            "type" : "source",
            "style" : [
                {
                    sidex : pointval
                }
            ],
            "position" : side
        }

        startpoint.append(points)


    # save to db
    savetodb ={
        "_id": mapname,
        "startingPoints": startpoint,
        "nodes": nodes,
        "edges": edges
        }


    db(savetodb)  # add to db
    printdb()     # print db
