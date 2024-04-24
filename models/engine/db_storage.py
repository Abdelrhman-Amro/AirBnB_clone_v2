#!/usr/bin/python3
""" new class for sqlAlchemy """
# specific modules
from os import getenv

# sqlalchemy modules and Base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base

# models modules
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """ create tables in environmental"""
    __engine = None
    __session = None

    # DONE
    def __init__(self):
        """Create engine"""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        db_uri = f"mysql://{user}:{passwd}@{host}/{db}"
        self.__engine = create_engine(db_uri, pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    # DONE
    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)

    # DONE
    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    # DONE
    def save(self):
        """save changes"""
        self.__session.commit()

    # DONE
    def delete(self, obj=None):
        """Delete- an element in the table"""
        if obj:
            self.session.delete(obj)

    # DONE
    def reload(self):
        """Create tables and stablish session"""
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()
