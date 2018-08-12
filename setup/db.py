from datetime import datetime

from sqlalchemy import create_engine, MetaData, Table, Column,\
                        Integer, String, Float, VARBINARY, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import configparser

config = configparser.ConfigParser()
config.read('../config.ini')
DATABSE_URI = config['LOCAL']['DATABASE_URI']
PASSWORD = config['LOCAL']['DATABASE_PASSWORD']
USER = config['LOCAL']['DATABASE_USER']

engine = create_engine(f'mysql+pymysql://{USER}:{PASSWORD}@{DATABSE_URI}/giveaway',
                        echo=True)
Base = declarative_base()


class Result(Base):
    __tablename__ = 'prize_result'
    id = Column('result_id', Integer, primary_key=True)
    result = Column('result', String(255))
    count = Column('result_count', Integer, default=0)

    def __repr__(self):
        return f'<Result(result={self.result}), count={self.count}>'

class Entry_Requirement(Base):
    __tablename__ = 'entry_requirement'
    id = Column('requirement_id', Integer, primary_key=True)
    giveaway_type = Column('giveaway_type', String(255))
    query_selector = Column('query_selector', String(255))
    count = Column('requirement_count', Integer, default=0)

    def __repr__(self):
        return f'<Entry_Requirement(giveaway_type={self.giveaway_type}, \
                query_selector={self.query_selector}), count={self.count}>'

class Entry(Base):
    __tablename__ = 'entry'
    id = Column('entry_id', Integer, primary_key=True)
    date_entered = Column('date_entered', Date(),
                            default=datetime.today())
    date_results = Column('date_results', Date(),
                            default=datetime.today())
    prize = Column('prize', String(255))
    prize_value = Column('prize_value', Float(precision=2))
    prize_image = Column('prize_image', VARBINARY(length=255))
    entry_requirements_id = Column('requirement_id', Integer,
                                ForeignKey('entry_requirement.requirement_id'))
    results_id = Column('result_id', Integer,
                        ForeignKey('prize_result.result_id'))

    def __repr__(self):
        return f'<entry(entry_requirement={self.entry_requirement_id}, \
                result={self.result_id})>'

Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)
session = session()
