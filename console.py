#!/usr/bin/python3
""" console"""


import cmd


class HBNBCommand(cmd.Cmd):
    """cmd class"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit the program"""
        return True
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
