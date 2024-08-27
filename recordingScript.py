from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import os

# Define database models
Base = declarative_base()

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    job_name = Column(String(100), nullable=True)
    fermi_job_id = Column(String(50), nullable=True)
    user_id = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    main_stats = relationship("MainStats", back_populates="job")
    runtime_analysis = relationship("RuntimeAnalysis", back_populates="job")
    geometric_analysis = relationship("GeometricAnalysis", back_populates="job")
    statistical_analysis = relationship("StatisticalAnalysis", back_populates="job")
    __table_args__ = (
        Index('idx_job_name', 'job_name'),
        Index('idx_fermi_job_id', 'fermi_job_id'),
        Index('idx_user_id', 'user_id'),
    )

class MainStats(Base):
    __tablename__ = 'main_stats'
    id = Column(Integer, primary_key=True, autoincrement=True)
    job_id = Column(Integer, ForeignKey('jobs.id', ondelete='SET NULL'), nullable=True)
    property = Column(String(100), nullable=False)
    value = Column(String(100))
    job = relationship("Job", back_populates="main_stats")

class RuntimeAnalysis(Base):
    __tablename__ = 'runtime_analysis'
    id = Column(Integer, primary_key=True, autoincrement=True)
    job_id = Column(Integer, ForeignKey('jobs.id', ondelete='SET NULL'), nullable=True)
    property = Column(String(100), nullable=False)
    value = Column(String(100))
    job = relationship("Job", back_populates="runtime_analysis")

class GeometricAnalysis(Base):
    __tablename__ = 'geometric_analysis'
    id = Column(Integer, primary_key=True, autoincrement=True)
    job_id = Column(Integer, ForeignKey('jobs.id', ondelete='SET NULL'), nullable=True)
    property = Column(String(100), nullable=False)
    value = Column(String(100))
    job = relationship("Job", back_populates="geometric_analysis")

class StatisticalAnalysis(Base):
    __tablename__ = 'statistical_analysis'
    id = Column(Integer, primary_key=True, autoincrement=True)
    job_id = Column(Integer, ForeignKey('jobs.id', ondelete='SET NULL'), nullable=True)
    set_id = Column(Integer, nullable=False)
    property = Column(String(100), nullable=False)
    value = Column(String(100))
    job = relationship("Job", back_populates="statistical_analysis")

# Database setup
def setup_database():
    engine = None
    try:
        engine = create_engine('mysql+pymysql://d2s:d2s_1234@localhost:3307/emumbaqor')
    except Exception as e:
        print("Couldn't connect to the database. Please check your connection string.", e)
        return
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

# Functions to insert data into the database
def get_session():
    return setup_database()

def insert_main_stats(session, job_id, data):
    # Clear existing entries and insert new data for Main Stats
    session.query(MainStats).filter_by(job_id=job_id).delete()
    for key, value in data.items():
        main_stats = MainStats(job_id=job_id, property=key, value=value)
        session.add(main_stats)
    session.commit()

def insert_runtimeanalysis_stats(session, job_id, data):
    # Clear existing entries and insert new data for Runtime Analysis
    session.query(RuntimeAnalysis).filter_by(job_id=job_id).delete()
    for key, value in data.items():
        rta_stats = RuntimeAnalysis(job_id=job_id, property=key, value=value)
        session.add(rta_stats)
    session.commit()

def insert_geometricanalysis_stats(session, job_id, data):
    # Clear existing entries and insert new data for Geometric Analysis
    session.query(GeometricAnalysis).filter_by(job_id=job_id).delete()
    for key, value in data.items():
        ga_stats = GeometricAnalysis(job_id=job_id, property=key, value=value)
        session.add(ga_stats)
    session.commit()

def insert_statistical_analysis_stats(session, job_id, data):
    # Clear existing entries and insert new data for Statistical Analysis
    session.query(StatisticalAnalysis).filter_by(job_id=job_id).delete()
    set_id = data.pop('set_id')
    for key, value in data.items():
        sa_stats = StatisticalAnalysis(job_id=job_id, set_id=set_id, property=key, value=value)
        session.add(sa_stats)
    session.commit()

# Main function to execute the script
if __name__ == "__main__":
    session = get_session()
    print("Database schema created successfully.")
