import collections


class UndergroundSystem:

    def __init__(self):
        self.i = collections.defaultdict(tuple)
        self.o = collections.defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.i[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.i[id]
        self.o[(stationName, start_station)].append(t-start_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.o[(endStation, startStation)])/len(self.o[(endStation, startStation)])
