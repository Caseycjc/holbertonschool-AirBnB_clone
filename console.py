#!/usr/bin/python3
<<<<<<< HEAD
"""Console for HBnB Project"""
import cmd


valid_class = {"BaseModel": BaseModel,
               "User": User,
               "State": State,
               "City": City,
               "Amenity": Amenity,
               "Place": Place,
               "Review": Review
               }
=======
"""command line interpreter"""
import cmd
>>>>>>> main


class HBNBCommand(cmd.Cmd):
    """class for HBNB command interpreter"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """do nothing when an empty line and "enter" is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
