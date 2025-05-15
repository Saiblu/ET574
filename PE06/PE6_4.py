"""
Implement the following to simulate how websites ensure that everyone has a unique username.
a) Make a list of five or more usernames called current_users.
b) Request an input of username.
c) Print a message, Sorry XXX, that name is taken and also display the current user list if the input
username has already been used. XXX is the input user name.
d) Print a message, Great, XXX is still available and also display the updated user list if the username has
not been used.
e) Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' or ‘john’ should not be
accepted.
Example Output 1
Enter your user name: TOM
Sorry TOM, that name is taken.
Current users: [‘admin’, ‘tom’, ‘jerry’, ‘Dora’, ‘GEORGE’
"""
current_users = ['admin', 'Tom', 'Jerry', 'Dora', 'GEORGE'] # Since there's a list for the taken username, the user, that type these name exactly, will be listed and send a message, which will be listed down below, that it is taken.

new_username = input("Enter your username: ")# this where the user will input a username.

lower_current_users= [user.lower() for user in current_users] #comparing the lowercase username that the end user have inputed, it will then read the list if the name is taken or not.
new_username_lower = new_username.lower()

if new_username_lower in lower_current_users: #This is where we enter a command for "yes or no" statement, in this case an IF statement.
    print(f"Sorry {new_username}, that name is taken.") #if it is taken, then the end user will receive a message, "sorry.." to let the user know that it has been taken and try again.
    print(f"Current users: {current_users}") #It will list the users based on the list we have created.
else: # Now if the user is able to create a brand new username, that isn't is on the list, it will move forward with the command.
    current_users.append(new_username) #If the user is able to create a new user, what this command do is add the username at the end of the list.
    print(f"Great, {new_username} is still available!") #A message will appear saying "Great..." to show it was succesfull on creating a brand new username.
    print(f"Updated users: {current_users}") #Then another message will appear, showing a brand new list, including a new username, that the user has created.