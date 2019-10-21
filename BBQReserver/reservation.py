
class  Reservation:
   def __init__(self, userId, datetime, peopleNum, info , slot):
       self.slot = slot
       self.info = info
       self.peopleNum = peopleNum
       self.datetime = datetime
       self.userId = userId