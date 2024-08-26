from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import StaleDataError
from sqlalchemy.orm.exc import StaleDataError
from datetime import datetime, timedelta
#import psycopg2
Base=declarative_base()

class Events(Base):
    __tablename__='events'
    id=Column(Integer,primary_key=True)
    title = Column(String)
    description = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    version=Column(Integer,nullable=False,default=0)

engine=create_engine('postgresql://username:password@localhost/mydatabase')
Session=sessionmaker(bind=engine)
session=Session()

def create_event(title, description, start_time, end_time):
    event=Events(title=title, description=description, start_time=start_time, end_time=end_time)
    session.add(event)
    session.commit()
    print("Event created with ID:", event.id)

#row update via optimistic locking
def update_event(event_id,title,description):
    try:
        event=session.query(Events).filter(Events.id==event_id).one()
        event.title = title
        event.description = description
        event.version += 1
        session.commit()
        print("Event updated")
    except StaleDataError:
        session.rollback()
        print("Event has been updated by another transaction, please retry.")

def update_event_pessimistic(event_id, title, description):
    with session.begin():
        event=session.query(Events).filter(Events.id==event_id).with_for_update().one()
        event.title = title
        event.description = description
        print("Event updated")
create_event('Meeting', 'Discuss project', datetime.now(), datetime.now() + timedelta(hours=1))
update_event(1, 'Updated Meeting', 'Discuss updated project')
update_event_pessimistic(1, 'Updated Meeting', 'Discuss updated project')

