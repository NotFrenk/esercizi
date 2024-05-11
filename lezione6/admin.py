#9-11. Imported Admin: 
#Start with your work from Exercise 9-8. Store the classes User, Privileges, and Admin in one module. 
#Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.
from lezione6 import Admin
ciao1= Admin ("pippo", "baudo", 4, 20, ["add user"])
ciao1.privileges.show_privileges()
