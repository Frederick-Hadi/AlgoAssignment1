#
# Demonstration class for linked list.
# Provides command parsing and calling appropriate methods for the linked list.
# DO NOT CHANGE.
#
#  @author Jeffrey Chan, RMIT
#

import sys
from double_linked_list import *
from simple_linked_list import *

def print_help():
    '''
    Print out help menu.
    '''
    print("Available commands:\n"
                + "    help\n"
                + "    add <value>\n"
                + "    insert <index> <value>\n"
                + "    remove <value>\n"
                + "    removeByIndex <index>\n"
                + "    search <value>\n"
                + "    min\n"
                + "    max\n"
                + "    print\n"
                + "    reversePrint\n"
                + "    quit|end\n"
            )

def process_operations(list):
    '''
    Get next command/operation from file.
    @param list Reference to list which the commands will be executed on.
    '''
    while True:

        input_text = input("Enter command: ")
        fields = input_text.split(" ")
        command = fields[0]
        if command == 'help':
            print_help()
        # add operation
        elif command == "add":
            value = int(fields[1])
            list.add(int(value))
        # insert operation
        elif command=="insert":
            index = int(fields[1])
            value = int(fields[2])
            try:
                list.insert(index, value)
            except IndexError as e:
                print(e)

        # remove operation
        elif command=="remove":
            value = int(fields[1])
            list.remove(value)

        # removeByIndex operation
        elif command == "removeByIndex":
            index = int(fields[1])
            try:
                list.remove_by_index(index)
            except IndexError as e:
                print(e)
            
        # search operation
        elif command == "search":
            value = int(fields[1])
            index = list.search(value)
            if index == -1:
                print("Key not found.")
            else:
                print("Key found at index " + str(index))

        # min operation
        elif command=="min":
            minKey = list.min()
            print("Min key = " + str(minKey))
        # max operation
        elif command=="max":
            maxKey = list.max()
            print("Max key = " + str(maxKey))
        # print operation
        elif command=="print":
            print(list.__str__())
        # reversePrint operation
        elif command=="reversePrint":
            list.reverse_print()
        # quit operation
        elif command=="quit" or command=="end" or command=="Quit" or command=="exit" or command=="Exit":
            break
        # unknown command
        else:
            print("Did not recognize command. Enter valid  command.")
            print_help()


def main():
    #if len(sys.argv) != 2:
    #    print_help()
    #    exit()

    # determine which list to construct
    firstArg = sys.argv[1]
    if firstArg == "single":
        mylist = SimpleLinkedList()
    elif firstArg == "double":
        mylist = DoubleLinkedList()
    else:
        print_help()
        exit()

    # process the commands
    process_operations(mylist)

if __name__ == "__main__":
    main()
