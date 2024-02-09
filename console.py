#!/usr/bin/python3
""" console"""


import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """cmd class"""

    prompt = "(hbnb) "
    clas_list = ["BaseModel"]

    def do_EOF(self, line):
        """Exit the program"""
        return True
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """empty line"""
        pass


    def do_create(self, line):
        """creates new instanse"""

        if not line:
            print("** class name missing **")
            return
        if line not in HBNBCommand.clas_list:
            print("** class doesn't exist **")
            return
        if line == "BaseModel":
            x = BaseModel()
            print(x.id)
            x.save()

    def do_show(self, line):
        """show"""

        if not line:
            print("** class name missing **")
            return
        l = line.split()
        if l[0] not in HBNBCommand.clas_list:
            print("** class doesn't exist **")
            return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
