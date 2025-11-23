from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from RRP_MCP.database import Base


class Manager(Base):
    __tablename__ = "managers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=True)
    role = Column(String, default="manager")

    companies = relationship("Company", back_populates="manager")
    projects = relationship("Project", back_populates="manager")
    interviews = relationship("Interview", back_populates="manager")


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    industry = Column(String, nullable=True)

    manager_id = Column(Integer, ForeignKey("managers.id"), nullable=False)

    manager = relationship("Manager", back_populates="companies")
    projects = relationship("Project", back_populates="company")


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    manager_id = Column(Integer, ForeignKey("managers.id"), nullable=False)

    status = Column(String, default="ongoing")
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=True)

    total_payment_amount = Column(Float, default=0.0)

    manager = relationship("Manager", back_populates="projects")
    company = relationship("Company", back_populates="projects")
    payments = relationship("Payment", back_populates="project")
    interviews = relationship("Interview", back_populates="project")


class Interview(Base):
    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True)
    manager_id = Column(Integer, ForeignKey("managers.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))

    candidate_name = Column(String, nullable=False)
    candidate_role = Column(String, nullable=False)
    schedule_time = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="scheduled")

    manager = relationship("Manager", back_populates="interviews")
    project = relationship("Project", back_populates="interviews")


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"))

    amount = Column(Float, nullable=False)
    payment_date = Column(DateTime, default=datetime.utcnow)
    payment_week = Column(String, nullable=True)

    project = relationship("Project", back_populates="payments")
