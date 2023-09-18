#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from sqlalchemy import Column, String
import models


class State(BaseModel, models.Base):
    """ State class """
    if models.storage_engine == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    @property
    def cities(self):
        """cities list
        """
        result = []
        for city in models.storage.all(models.city.City).values():
            if city.state_id == self.id:
                result.append(city)
        return result
