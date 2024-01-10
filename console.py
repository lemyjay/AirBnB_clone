#!/usr/bin/python3
"""
Command interpreter module
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    
    Attributes:
    - prompt (str): The custom prompt for the command interpreter.

    Methods:
    - do_quit(arg): Implements the 'quit' command to exit the program.
    - do_EOF(arg): Implements the 'EOF' command to exit the program.
    - emptyline(): Does nothing on an empty line.
    """
    
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
