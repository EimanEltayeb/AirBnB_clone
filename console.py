#!/usr/bin/python3
""" console"""


import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


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
        if len(l) < 2:
            print("** instance id missing **")
            return
        all_objects = storage.all()
        for k, v in all_objects.items():
            id_part = k.split('.')[1]
            if id_part == l[1]:
                print(v)
                return
        print("** no instance found **")

    def do_destroy(self, line):
        """deletes an instance"""

        if not line:
            print("** class name missing **")
            return
        l = line.split()
        if l[0] not in HBNBCommand.clas_list:
            print("** class doesn't exist **")
            return
        if len(l) < 2:
            print("** instance id missing **")
            return
        all_objects = storage.all()
        for k, v in storage._FileStorage__objects.items():
            id_part = k.split('.')[1]
            if id_part == l[1]:
                del storage._FileStorage__objects[k]
                print("id_part")
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, line):
        """print all instances"""

        l = line.split()
        if len(l) = 2 and l[1] not in HBNBCommand.clas_list:
            print("** class doesn't exist **")
            return
        if len(l) = 1:
            print(f'["{storage.all}"]')
            return
        if len(l) < 2 and l[1] in HBNBCommand.clas_list:
            all_objects = storage.all()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
