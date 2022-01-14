from node import Node
INF = 999

node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)


def rtinit0():
    node0.distanceTable[0] = [0, 1, 3, 7]
    node0.addNeighbors([node1, node2, node3])
    node0.rtinit()


def rtinit1():
    node1.distanceTable[1] = [1, 0, 1, INF]
    node1.addNeighbors([node0, node2])
    node1.rtinit()


def rtinit2():
    node2.distanceTable[2] = [3, 1, 0, 2]
    node2.addNeighbors([node0, node1, node3])
    node2.rtinit()


def rtinit3():
    node3.distanceTable[3] = [7, INF, 2, 0]
    node3.addNeighbors([node0, node2])
    node3.rtinit()


def rtupdate0(rtpacket):
    print(f"rtupdate0() called, by a packet received from Sender id: {rtpacket.sourceID}")
    node0.rtupdate(rtpacket)


def rtupdate1(rtpacket):
    print(f"rtupdate1() called, by a packet received from Sender id: {rtpacket.sourceID}")
    node1.rtupdate(rtpacket)


def rtupdate2(rtpacket):
    print(f"rtupdate2() called, by a packet received from Sender id: {rtpacket.sourceID}")
    node2.rtupdate(rtpacket)


def rtupdate3(rtpacket):
    print(f"rtupdate3() called, by a packet received from Sender id: {rtpacket.sourceID}")
    node3.rtupdate(rtpacket)


def tolayer2(rtpkt):
    destID = rtpkt.destID
    srcID = rtpkt.sourceID
    contents = rtpkt.minCost
    print(f"\nsrc = {srcID}, dest = {destID}, contents={contents}")
    if destID == 0:
        rtupdate0(rtpkt)
    elif destID == 1:
        rtupdate1(rtpkt)
    elif destID == 2:
        rtupdate2(rtpkt)
    elif destID == 3:
        rtupdate3(rtpkt)


def printNodes():
    print("\n****************************************************")
    node0.printDistanceTable()
    node1.printDistanceTable()
    node2.printDistanceTable()
    node3.printDistanceTable()
    print("****************************************************\n")


rtinit0()
rtinit1()
rtinit2()
rtinit3()

while True:

    if len(node0.myPacketsToSend) != 0:
        while len(node0.myPacketsToSend) > 0:
            packet = node0.myPacketsToSend.pop(0)
            tolayer2(packet)
    elif len(node1.myPacketsToSend) != 0:
        while len(node1.myPacketsToSend) > 0:
            packet = node1.myPacketsToSend.pop(0)
            tolayer2(packet)

    elif len(node2.myPacketsToSend) != 0:
        while len(node2.myPacketsToSend) > 0:
            packet = node2.myPacketsToSend.pop(0)
            tolayer2(packet)

    elif len(node3.myPacketsToSend) != 0:
        while len(node3.myPacketsToSend) > 0:
            packet = node3.myPacketsToSend.pop(0)
            tolayer2(packet)
    else:
        break

printNodes()

print("-------------------Program done------------------")
