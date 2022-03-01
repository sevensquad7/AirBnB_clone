#!/usr/bin/python3
"""AirBnB BaseModel"""
import uuid
import models
from datetime import datetime
"""date = date format"""
date = %Y-%m-%dT%H:%M:%S.%f


class BaseModel:
    """BaseModel"""
    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel"""
        if kwargs:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key == "created_at" and k == "updated_at":
                        setattr(self, key, datetime.strptime(val, date))
                    else:
                        setattr(self,key,val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.update_at = self.created_at
            models.storage.new(self)
    
    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        return ("[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Instance to_dictionary"""
        dictionary = self.__dict__.copy()
        if "created_at" in dictionary:
            dictionary["created_at"] = dictionary["created_at"].strftime(date)
        if "updated_at" in dictionary:
            dictionary["updated_at"] = dictionary["updated_at"].strftime(date)
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
