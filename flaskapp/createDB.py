from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

Base = declarative_base()

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    job_name = Column(String(100), nullable=True)  # Nullable
    fermi_job_id = Column(String(50), nullable=True)  # Nullable
    user_id = Column(String(100), nullable=True)  # Nullable
    created_at = Column(DateTime, default=datetime.now)

    # Relationships
    main_stats = relationship("MainStats", back_populates="job")
    runtime_analysis = relationship("RuntimeAnalysis", back_populates="job")
    geometric_analysis = relationship("GeometricAnalysis", back_populates="job")
    statistical_analysis = relationship("StatisticalAnalysis", back_populates="job")

    # Indexes to optimize querying by job_name, fermi_job_id, or user_id
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
    # Replace with your actual MySQL connection details
    engine = create_engine('mysql+pymysql://d2s:d2s_1234@localhost/emumbaqor')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

if __name__ == "__main__":
    session = setup_database()
    print("Database schema created successfully.")
