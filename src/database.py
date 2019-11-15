from datetime import date, datetime

from sqlalchemy import create_engine, Column, Date, DateTime, Boolean, Integer, String, Text, ForeignKey, Index, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

print(1)
Session = sessionmaker()
# Create SQLite db or use existing one
engine = create_engine('sqlite:///sqlite3.db?check_same_thread=False')
# Create a base for the models to build upon.
Session.configure(bind=engine)
Base = declarative_base()
sess = Session()


class User(Base):
    __tablename__ = 'user'
    id_ = Column(Integer, primary_key=True)
    telegramID = Column(String, nullable=False)


class Message(Base):
    """
    Message to send via telegram 
    """

    __tablename__ = 'message'

    id_ = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id_"))
    text = Column(Text(), nullable=False)
    # Boolean field because I haven't found different statuses 
    # in Telegram API so far, like "recievied" or "has been read"
    is_sent = Column(Boolean(), default=False)


# class Notification(Message):
#     """Message for users in the waiting list"""

#     __tablename__ = 'notification'

#     id_ = Column(Integer, primary_key=True)


class Reservation(Base):
    """
    Reservation.
    Includes the date, the time and the user who's reserved the slot.
    """

    __tablename__ = 'reservation'

    id_ = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id_"), nullable=False)
    day = Column(DateTime(), nullable=False)
    slot = Column(Integer, nullable=False)
    is_expired = Column(Boolean(), default=False)
    is_confirmed = Column(Boolean(), default=False)
    unique_reserve = (UniqueConstraint('day', 'slot', name='_unique_reservation_'))


class WaitingList(Base):
    """
    List of users waiting for a slot in a particular date to be free
    """

    __tablename__ = 'waiting_list'

    id_ = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id_"), nullable=False)
    day = Column(Date(), nullable=False)


# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.

Base.metadata.create_all(engine)
print(0)

#Set reservations as expired
def set_expired_reservations():
    expired_entries = sess.query(Reservation).filter(Reservation.day < datetime.now()).all()
    for c in expired_entries:
        c.is_expired = True
    sess.commit()

def get_awaiting_users(day):
    awaiting_users = sess.query(WaitingList).filter(WaitingList.day == date(day.year, day.month, day.day)).all()
    return awaiting_users

