from rtpkt import rtpkt
INF = 999


class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = list()
        self.distanceTable = [[INF] * 4 for i in range(4)]
        self.myPacketsToSend = list()

    def addNeighbors(self, nodes):
        self.neighbors = nodes

    def rtinit(self):
        for n in self.neighbors:
            currentID = n.id
            minCost = [
                self.distanceTable[self.id][0],
                self.distanceTable[self.id][1],
                self.distanceTable[self.id][2],
                self.distanceTable[self.id][3]
            ]
            self.myPacketsToSend.append(rtpkt(self.id, currentID, minCost))

    def rtupdate(self, rtpacket):

        # unpack packet
        sourceID = rtpacket.sourceID
        destID = rtpacket.destID
        minCost = rtpacket.minCost

        row = sourceID
        for col in range(0, 4):  # copy over new values from packet
            self.distanceTable[row][col] = minCost[col]

        otherRows = [i for i in range(0, 4) if i != row]

        # now check and see if theres a better path
        for col in range(0, 4):
            for otherR in otherRows:
                if self.distanceTable[destID][otherR] + self.distanceTable[otherR][col] < self.distanceTable[destID][col]:
                    self.distanceTable[destID][col] = self.distanceTable[destID][otherR] + self.distanceTable[otherR][
                        col]

                    # create packets to send info for each neighbor
                    for n in self.neighbors:
                        currentID = n.id
                        minCost = [
                            self.distanceTable[self.id][0],
                            self.distanceTable[self.id][1],
                            self.distanceTable[self.id][2],
                            self.distanceTable[self.id][3]
                        ]
                        self.myPacketsToSend.append(rtpkt(self.id, currentID, minCost))
        self.print_node_vector()

    def printDistanceTable(self):
        print(f"D{self.id}  |    0   1   2   3")
        print("----|--------------------------------")
        for row in range(0, 4):
            print(f"{row}   |   ", end="")
            for col in range(0, 4):
                print(f"{self.distanceTable[row][col]:^5}", end="")
            print("")
        print()

    def print_node_vector(self):
        print(f"Node {self.id} current distance vector is {self.distanceTable[self.id]}")
