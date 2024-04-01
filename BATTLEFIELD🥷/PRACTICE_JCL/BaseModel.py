# QUICK OVERVIW

  # BaseModel
    # Methods
      # __init__
      # __str__
      # save
      # to_dict

  # FileStorage
    # Attributes
      # __file_path
      # __objects

    # Methods
      # all
      # new
      # save
      # reload
# ---------------------------

# __str__
  # Return this format
    # this -> [<class name>] (<self.id>) <self.__dict__>
  # How this work?
    # this -> cls = (str(type(self)).split('.')[-1]).split('\'')[0]
      # this -> cls = ClassName😉 Just ClassName🤣😅
  
# to_dict
  # __dict__ of object to dictionary
  # Add '__class__' key with value 'ClassName'
    # That what the next line mean
      # {'__class__': (str(type(self)).split('.')[-1]).split('\'')[0]}
  # Reformat the date

      