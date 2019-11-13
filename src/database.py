from sqlalchemy import create_engine, Column, Date, Boolean, Integer, String, Text, ForeignKey, Index, UniqueConstraint
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


ts_08_10 = '08:00-10:00'
ts_10_12 = '10:00-12:00'
ts_12_14 = '12:00-14:00'
ts_14_16 = '14:00-16:00'
ts_16_18 = '16:00-18:00'
ts_18_21 = '18:00-21:00'
ts_21_24 = '21:00-00:00'

TIME_SLOTS = (
    8, ts_08_10,
    10, ts_10_12,
    12, ts_12_14,
    14, ts_14_16,
    16, ts_16_18,
    18, ts_18_21,
    21, ts_21_24,
)


class Reservation(Base):
    """
    Reservation.
    Includes the date, the time and the user who's reserved the slot.
    """

    __tablename__ = 'reservation'

    id_ = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id_"), nullable=False)
    day = Column(Date(), nullable=False)
    # We'll put either of 8, 10, 12, 14, 16, 18, 21 here
    slot = Column(Integer, nullable=False)
    unique_reserve = (UniqueConstraint('day', 'slot', name='_unique_reservation_'))


class WaitingList(Base):
    """
    List of users waiting for a slot in a particular date to be free
    """

    __tablename__ = 'waiting_list'

    id_ = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id_"), nullable=False)
    reservation_id = Column(Integer, ForeignKey("reservation.id_"), nullable=False)


# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.

Base.metadata.create_all(engine)
print(0)
