import zmq
import simplejson
import time

def listenForTradeRequests():
    port = 5556

    # Socket to talk to server
    context = zmq.Context()
    socket = context.socket(zmq.SUB)

    print "listnening in for trade list requests..."
    socket.connect ("tcp://localhost:%s" % port)

    topicfilter = "TradeListRequest"
    socket.setsockopt(zmq.SUBSCRIBE, topicfilter)


    string = socket.recv()
    print "a msg was received!"
    time.sleep(10)
    sendBackTrades()
    return

def sendBackTrades():
    port = 5557
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:%s" % port)

    topic = "TradeList"
    dict = {'trades':['trade1','trade2']}

    #messagedata =simplejson.dumps(dict)
    messagedata ="simple debug data"
    socket.send("%s %s" %(topic,messagedata))
    print "%s %s" %(topic,messagedata)
    print "tradelist was sent!"

while True:
    listenForTradeRequests()
