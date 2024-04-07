#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.engine.file_storage import FileStorage as fs
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    state = relationship("City", back_populates="cities",
                         cascade='all, delete, delete-orphan')

    @property
    def cities(self):
        """Return city"""
        c_lists = []
        c_obj = fs.all(City)
        for c in c_obj:
            if c.state_id == self.state_id:
                c_lists.append(c)
        return (c_lists)
                
        
        