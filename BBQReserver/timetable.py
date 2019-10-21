
    class Timetable:

        def __init__(self, waitingList, date, id, reservations):
            self.reservations = reservations
            self.id = id
            self.waitingList = waitingList
            self.date = date