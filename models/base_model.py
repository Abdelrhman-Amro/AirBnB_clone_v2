#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))  
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        
        if kwargs:
            # When updating
            if "id" in kwargs:   
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                del kwargs['__class__']
                self.__dict__.update(kwargs)
            else:
                # When using (create ClassName Param_1 Param_2 Param_3 ...)
                from models import storage
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                self.__dict__.update(kwargs)
                storage.new(self)

        else:
            # if there is no kwargs just creat simple obj 
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()


    # Function that called like print(objBaseModel)
    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        # Delete _sa_instance_state if exist
        if dictionary.get('_sa_instance_state'):
            del dictionary['_sa_instance_state']

        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """ delete the current instance from the storage """
        from models.engine.file_storage import FileStorage as fs
        fs.delete(self)
