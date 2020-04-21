#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine, MetaData
from models.base_model import Base
import os


class DBStorage():
    """manager of mysql database"""
    __engine = None
    __session = None

    def __init__(self):

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                           os.environ.get("HBNB_MYSQL_USER"),
                           os.environ.get("HBNB_MYSQL_PWD"),
                           os.environ.get("HBNB_MYSQL_HOST"),
                           os.environ.get("HBNB_MYSQL_DB")),
                           pool_pre_ping=True)
        if (os.environ.get("HBNB_MYSQL_USER") == "test"):
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ doc """
        lists = {}
        classes = {'Place': Place, 'City': City, 'Amenity': Amenity,
                   'Review': Review, 'State': State, 'User': User}
        if cls:
            if cls not in classes:
                for row in self.__session.query(cls):
                    key = "{}.{}".format(row.__class__.__name__, row.id)
                    lists[key] = row
            else:
                for row in self.__session.query(classes[cls]):
                    key = "{}.{}".format(row.__class__.__name__, row.id)
                    lists[key] = row
        else:
            for rows in classes:
                for row in self.__session.query(classes[rows]):
                    key = "{}.{}".format(row.__class__.__name__, row.id)
                lists[key] = row
        return lists

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """

        self.__session.add(obj)
        self.save()

    def save(self):
        """serialize the file path to JSON file path
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ doc """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """serialize the file path to JSON file path
        """
        Base.metadata.create_all(bind=self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                 expire_on_commit=False))
        self.__session = Session()

    def close(self):
        self.__session.close()
