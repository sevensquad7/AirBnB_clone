#!/usr/bin/python3
"""
Class AirBnB Command's
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Class AirBnB (hbnb)"""
    prompt= '(hbnb)'
    
    def do_quit(self, args):
        """Command quit"""
        return True
    
    def do_EOF(self, args):
        """Command EOF"""
        return True
    
    def do_help(self, args):
        """Command Help"""
        cmd.Cmd.do_help(self, args)

    def help_quit(self):
        """Help quit"""
        print("Quit command to exit the program")
    
    def help_EOF(self):
        """Help EOF"""
        print("End of File command to exit the program")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
