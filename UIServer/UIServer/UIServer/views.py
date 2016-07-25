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
   a page that shows up before you choose anything to view
    """
    return render_template(
        'welcome.html',
        title='start page',
        year=datetime.now().year,
    )

@app.route('/reports')
def reports():
    """
   a page that shows up before you choose anything to view
    """
    return render_template(
        'positions.html',
        title='Positions',
        year=datetime.now().year,
    )

@app.route('/help')
def help():
    """
   a page that shows up before you choose anything to view
    """
    return render_template(
        'welcome.html',
        title='start page',
        year=datetime.now().year,
    )

@app.route('/admin')
def admin():
    """
   a page that shows up before you choose anything to view
    """
    return render_template(
        'welcome.html',
        title='start page',
        year=datetime.now().year,
    )

@app.route('/positions')
def positions():
    """
   a page that shows up before you choose anything to view
    """
    return render_template(
        'positions.html',
        title='start page',
        year=datetime.now().year,
    )

@app.route('/greeks')
def greeks():
    """
   a page that shows up before you choose anything to view
    """
    return render_template(
        'welcome.html',
        title='start page',
        year=datetime.now().year,
    )

@app.route('/greekspl')
def greekspl():
    """
   a page that shows up before you choose anything to view
    """
    return render_template(
        'welcome.html',
        title='start page',
        year=datetime.now().year,
    )
@app.route('/valuation')
def valuation():
    """
   a page that shows up before you choose anything to view
    """
    return render_template(
        'welcome.html',
        title='start page',
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
    