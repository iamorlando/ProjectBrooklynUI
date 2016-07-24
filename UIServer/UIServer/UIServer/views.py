"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from UIServer import app
import zmq
import simplejson
import time

@app.route('/')
@app.route('/home')
def home():
    """
    just a crazy placeholder website for now
    """
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
@app.route('/test')
def doTest():
    """
    testing my calling js code with this
    """
    print 'hello world'
    return

@app.route('/Trades')
def getTrades():
    """
    an endpoint to test zmq and connectivity with the pivot engine.
    may be useful in later to get a list of trades.
    """
    port = 5556
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:%s" % port)

    topic = "TradeListRequest"
    messagedata ="no need to specify data to request trades here"
    socket.send("%s %s" %(topic,messagedata))
    #when debuging, the msg is received by pivot engine, but a threadsleep here may be necesary 
    
    print "%s %s" %(topic,messagedata)
    return listenForTradeRequestsResults()

def listenForTradeRequestsResults():
    port = 5557

    # Socket to talk to server
    context = zmq.Context()
    socket = context.socket(zmq.SUB)

    print "listening for a trade list"
    socket.connect ("tcp://localhost:%s" % port)

    topicfilter = "TradeList"
    socket.setsockopt(zmq.SUBSCRIBE, topicfilter)
    string=socket.recv()
    print "trade list received!"
    topic, messagedata = string.split()
    print messagedata
    return 
    