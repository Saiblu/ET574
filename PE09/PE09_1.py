"""
1. Print List
a) Define a function printList() with one parameter p.
1) This function prints all values in the list p.
b) Define a main() function to do the following:
1) Create a list of strings called lst. For example, lst = [“apple”, “banana”, “cherry”].
2) Call the function printList() with lst as an argument.
c) Call main() function to initiate the tasks to be performed.

"""
def printlist(p):
    print(",".join(p))
        
def main():
    lst = ["apple", "banana", "cherry"]
    printlist(lst)

main()


