#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey, Table
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
import os


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """

    __tablename__ = "places"
    metadata = Base.metadata
    place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60), ForeignKey('places.id'), nullable=False, primary_key=True),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False, primary_key=True))
        
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref='place', cascade='delete')
        amenities = relationship("Amenity",  secondary=place_amenity, back_populates="place_amenities", viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            review = models.storage.all(Review)
            relation = []
            for key in review.values():
                if key.place.id == self.id:
                    relation.append(key)
            return relation

        @property
        def amenities(self):
            amenity = models.storage.all(Amenity)
            relation = []
            for key in amenity.values():
                if key.place.id == self.id:
                    relation.append(key)
            return relation

        @amenities.setter
        def amenities(self, value):
            if value.__class__.__class__ == 'Amenity':
                    amenity_ids.append(amenities.id)
