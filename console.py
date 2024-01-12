#!/usr/bin/python3
"""
Command interpreter module
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
from shlex import split


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class

    Attributes:
    - prompt (str): The custom prompt for the command interpreter.

    Methods:
    - do_quit(arg): Implements the 'quit' command to exit the program.
    - do_EOF(arg): Implements the 'EOF' command to exit the program.
    - emptyline(): Does nothing on an empty line.
    - do_create(arg): Creates a new instance of BaseModel or User, saves
      it (to the JSON file) and prints the id.
    - do_show(arg): Prints the string representation of an instance based
      on the class name and id.
    - do_destroy(arg): Deletes an instance based on the class name and id
      (saves the change into the JSON file)
    - do_all(arg): Prints all string representation of all instances based or
      not on the class name.
    - do_update(arg): Updates an instance based on the class name and id by adding
      or updating attribute (save the change into the JSON file).
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        if arg.strip() == "":
            return True
        print("** Invalid command for quit. Type 'quit' to exit.")
        return False

    def do_EOF(self, _):
        """
        EOF command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on empty line
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, User, Place, State, City, Amenity, or Review,
        saves it (to the JSON file) and prints the id.
        """
        args = split(arg)
        if not args or args[0] == "":
            print("** class name missing **")
            return
        class_mapping = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }
        try:
            class_name = args[0]
            new_instance = class_mapping[class_name]()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")
        except Exception as e:
            print("** {}".format(e))

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the class name and id.
        """
        args = split(arg)
        if not args or args[0] == "":
            print("** class name missing **")
            return
        try:
            class_name = args[0]

            if len(args) < 2:
                print("** instance id missing **")
                return

            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            obj = storage.all().get(key)

            class_mapping = {
                "BaseModel": BaseModel,
                "User": User,
                "Place": Place,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Review": Review,
            }

            if class_name in class_mapping:
                class_type = class_mapping[class_name]
                instance_objects = [obj for obj in storage.all().values() if isinstance(obj, class_type)]
                if instance_objects:
                    print(instance_objects[0])
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

        except Exception as e:
            print("** {}".format(e))

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (saves the change into the JSON file)
        """
        args = split(arg)
        if not args or args[0] == "":
            print("** class name missing **")
            return
        try:
            class_name = args[0]

            if len(args) < 2:
                print("** instance id missing **")
                return

            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            obj = storage.all().get(key)
            if not obj:
                print("** no instance found **")
                return
            del storage.all()[key]
            storage.save()
        except Exception as e:
            print("** {}".format(e))

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or
        not on the class name
        """
        args = split(arg)
        obj_list = []
        if not args or arg[0] == "":
            for obj in storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
            return
        try:
            class_name = args[0]
            for obj in storage.all().values():
                if class_name == obj.__class__.__name__:
                    obj_list.append(str(obj))
            if not obj_list:
                print("** class doesn't exist **")
                return
            print(obj_list)
        except Exception as e:
            print("** {}".format(e))

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        args = split(arg)
        if not args or args[0] == "":
            print("** class name missing **")
            return
        try:
            class_name = args[0]

            if len(args) < 2:
                print("** instance id missing **")
                return

            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            obj = storage.all().get(key)
            if not obj:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            attribute_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return
            value = args[3]
            setattr(obj, attribute_name, value)
            obj.save()
        except Exception as e:
            print("** {}".format(e))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
