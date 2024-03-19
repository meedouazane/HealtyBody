#!/usr/bin/python3
"""
This module defines a base class for all models
"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class User(Base):
    """ table for users """
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True)
    username = Column(String(128), unique=True, nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    sex = Column(String(36))
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    date_of_birth = Column(DateTime, nullable=True)
    bmi_records = relationship("BMI", back_populates="user")


class BMI(Base):
    """ table for bmi """
    __tablename__ = "bmi_records"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True)
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False)
    height = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    bmi = Column(Integer, server_default="0")
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    user = relationship("User", back_populates="bmi_records")
