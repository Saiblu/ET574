"""Print List
a) Define a function printList() with one parameter p.
 1) This function prints all values in the list p.
b) Define a main() function to do the following:
 1) Create a list of strings called lst. For example, lst = [“apple”, “banana”, “cherry”].
 2) Call the function printList() with lst as an argument.
c) Call main() function to initiate the tasks to be performed.
Example Output
apple banana cherry"""

def printList(p):
    for item in p:
        print(item, end=' ')
    print()  # For a new line after printing all items
    
def main():
    lst = ["apple", "banana", "cherry"]
    printList(lst)

if __name__ == "__main__":
    main()
# The code defines a function to print all items in a list and demonstrates its usage with a sample list of strings.
# The function printList takes a list as an argument and prints each item in the list on the same line, separated by spaces.
