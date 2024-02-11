#!/usr/bin/python3
""" console"""


import cmd
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """cmd class"""

    prompt = "(hbnb) "
    base = "BaseModel"
    usr = "User"
    clas_list = [base, usr, "State", "City", "Amenity", "Place", "Review"]

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
        elif line == "User":
            x = User()
            print(x.id)
            x.save()
        elif line == "State":
            x = State()
            print(x.id)
            x.save()
        elif line == "City":
            x = City()
            print(x.id)
            x.save()
        elif line == "Amenity":
            x = Amenity()
            print(x.id)
            x.save()
        elif line == "Place":
            x = Place()
            print(x.id)
            x.save()
        elif line == "Review":
            x = Review()
            print(x.id)
            x.save()

    def do_show(self, line):
        """show"""

        if not line:
            print("** class name missing **")
            return
        ls = line.split()
        if ls[0] not in HBNBCommand.clas_list:
            print("** class doesn't exist **")
            return
        if len(ls) < 2:
            print("** instance id missing **")
            return
        all_objects = storage.all()
        for k, v in all_objects.items():
            id_part = k.split('.')[1]
            if id_part == ls[1]:
                print(v)
                return
        print("** no instance found **")

    def do_destroy(self, line):
        """deletes an instance"""

        if not line:
            print("** class name missing **")
            return
        ls = line.split()
        if ls[0] not in HBNBCommand.clas_list:
            print("** class doesn't exist **")
            return
        if len(ls) < 2:
            print("** instance id missing **")
            return
#       all_objects = storage.all()
        for k, v in storage._FileStorage__objects.items():
            id_part = k.split('.')[1]
            if id_part == ls[1]:
                del storage._FileStorage__objects[k]
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, line):
        """print all instances"""

        if not line:
            all_list = []
            for k, v in storage._FileStorage__objects.items():
                all_list.append(str(v))
            print(all_list)
            return
        if line not in HBNBCommand.clas_list:
            print("** class doesn't exist **")
            return

        if line in HBNBCommand.clas_list:
            cls_list = []
            for k, v in storage._FileStorage__objects.items():
                class_part = k.split(".")[0]
                if class_part == line:
                    cls_list.append(str(v))
            print(cls_list)

    def do_update(self, line):
        """updates the values"""

        if not line:
            print("** class name missing **")
            return
        ls = line.split()
        if ls[0] not in HBNBCommand.clas_list:
            print("** class doesn't exist **")
            return
        if len(ls) < 2:
            print("** instance id missing **")
            return
        if len(ls) < 3:
            print("** attribute name missing **")
            return
        if len(ls) < 4:
            print("** value missing **")
            return
        for k, v in storage._FileStorage__objects.items():
            id_part = k.split('.')[1]
            if id_part == ls[1]:
                typ = type(getattr(v, ls[2]))
                if typ == int:
                    setattr(v, ls[2], int(ls[3]))
                elif typ == float:
                    setattr(v, ls[2], float(ls[3]))
                elif typ == str:
                    setattr(v, ls[2], ls[3])
                return
        print("** no instance found **")

    def default(self, line):
        cls_ = line.split('.')
        if cls_[0] not in HBNBCommand.clas_list:
            print("** class doesn't exist **")
            return
        if cls_[1] == 'count()':
            count = 0
            for k, v in storage._FileStorage__objects.items():
                clas_part = k.split('.')[0]
                if clas_part == cls_[0]:
                    count += 1
            print(count)
            return
        if cls_[1].startswith('destroy'):
            idd = cls_[1].split('"')[1]
            ln = f"{cls_[0]} {idd}"
            self.do_destroy(ln)
            return
        if cls_[1].startswith('update'): #and not cls_[1].endswith('}'):
            idd = cls_[1].split('"')[1]
            att = cls_[1].split('"')[3]
            val = cls_[1].split('"')[5]
            ln = f"{cls_[0]} {idd} {att} \"{val}\""
            self.do_update(ln)
            return
        


            


if __name__ == '__main__':
    HBNBCommand().cmdloop()
