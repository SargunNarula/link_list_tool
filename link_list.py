from os import system, name
from time import sleep
class Node:
    num_nodes = 0

    def __init__(self, name, next_element=None):
        self.name = name
        self.next = next_element
        Node.num_nodes += 1

    def getname(self):
        return self.name

    def getnext(self):
        return self.next

    def setname(self, name):
        self.name = name

    def setnext(self, link):
        self.next = link
        
class Linked_List:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.choice = {"1": self.print_list,
                       "2": self.length,
                       "3": self.add_operations,
                       "4": self.del_operations,
                       "5": self.find,
                       "6": self.change_data
                       }

    @staticmethod
    def menu():
        print("\n")
        print("1. Print List")
        print("2. Length of List")
        print("3. Insert node")
        print("4. Delete node")
        print("5. Find Node")
        print("6. Change data")

    def list_operations(self):
        self.menu()
        ans = input("\nChoose an Option :")
        action = self.choice.get(ans)
        if action:
            print()
            if ans == '2':
                cal_length = action()
                print("Length -> ", cal_length)
                sleep(5)
            else:
                action()
        else:
            print("Choose valid option ..!!")

    @staticmethod
    def create_node():
        name = input("Enter Data :")
        val = Node(name)
        return val

    @staticmethod
    def delete_node(node):
        del node

    def add_node_at_front(self, node):
        node.next = self.head
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head = node

    def add_node_at_end(self, node):
        if self.head is None:
            node.next = None
            self.head = node
            self.tail = node

        elif self.head is not None:
            node.next = None
            self.tail.next = node
            self.tail = node

    def add_node_at_middle(self, node, position):
        count = 1
        current = self.head
        while count < position - 1:
            current = current.next
            count += 1
        node.next = current.next
        current.next = node

    def del_node_at_front(self, node):
        tmp = self.head
        self.head = self.head.next
        list.delete_node(tmp)

    def del_node_at_end(self, node):
        count = 1
        current = self.head
        loop_var = list.length()
        while count < (loop_var - 1):
            current = current.next
            count += 1
        if count == 1 and loop_var == 1:
            list.del_node_at_front(node)
        else:
            self.tail = current.next
            current.next = None
            list.delete_node(node)

    def del_node_at_middle(self, position):
        count = 1
        current = self.head
        while count < position - 1:
            current = current.next
            count += 1
        tmp = current.next.next
        list.delete_node(current.next)
        current.next = tmp

    def print_list(self):
        if self.head is None:
            print("List is Empty")
        current = self.head
        count = 1
        while current is not None:
            try:
                print("node - {}\t\t\tdata -> {}\t\t\taddress -> {}\t\t\tnext_node -> {} ".format(count,
                                                                                                  current.name, current,
                                                                                                  current.next.name))
                count += 1
            except:
                print("node - {}\t\t\tdata -> {}\t\t\taddress -> {}\t\t\tnext_node -> {} ".format(count,
                                                                                                  current.name, current,
                                                                                                  current.next))
            current = current.next
        sleep(10)
    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        # print("Length -> ",count)
        return count

    def add_operations(self):
        while True:
            print("\nAdd Operations :->")
            print(" 1 - At Front ")
            print(" 2 - At End   ")
            print(" 3 - In the Middle")
            option = int(input("\nOption :"))

            if option == 3:
                position = int(input("At Which position :"))
                value = list.create_node()
                list.add_node_at_middle(value, position)
            else:
                value = list.create_node()
                if option == 1:
                    list.add_node_at_front(value)
                if option == 2:
                    list.add_node_at_end(value)

            extra = input("Do you want to add another node? (Y/N) :")
            if extra == 'N' or extra == 'n':
                break

    def del_operations(self):
        while True:
            print("\nDelete Operations :->")
            print(" 1 - At Front ")
            print(" 2 - At End   ")
            print(" 3 - In the Middle")
            option = int(input("\nOption :"))

            if self.head is None:
                print("List is already empty")
                break
            if option == 3:
                position = int(input("At Which position :"))
                list.del_node_at_middle(position)
            else:
                if option == 1:
                    list.del_node_at_front(self.head)
                if option == 2:
                    list.del_node_at_end(self.head)

            extra = input("Do you want to delete another node? (Y/N) :")
            if extra == 'N' or extra == 'n':
                break

    def find(self):
        position = int(input("Node index: "))
        count = 1
        current = self.head
        while count < position:
            current = current.next
            count += 1
        try:
            print("data -> {}\t\t\taddress -> {}\t\t\tnext_node -> {} ".format(current.name, current, current.next.name))
        except:
            print("data -> {}\t\t\taddress -> {}\t\t\tnext_node -> {} ".format(current.name, current, current.next))
        sleep(5)


    def change_data(self):
        index = int(input("Node index :"))
        count = 1
        current = self.head
        while count < index:
            current = current.next
            count += 1

        print("Current data ->", current.name)
        data = input("Set new data -> ")
        current.setname(data)
        print("New data -> {} \t\t Correction Done".format(current.name))

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Driver Code
list = Linked_List()
print("\n\t\t\t\t\t\t\t\tWelcome to Linked List Tool \t (Singly linked list)")
print()
while True:
    clear()
    check = input("\nDo you want to continue (Y/N) :")
    if check == 'N' or check == 'n':
        break
    else:
        list.list_operations()
print("\n\t\t\t\t\t\t\t\tThank You")

