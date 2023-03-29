# Understanding the CLI:

The CLI file holds the data that the user will be interacting with. To begin with we have an __init__ dunder method. This method is 
functioning to break each group within our ProjectGroup class into individual elements so that if the user wishes to access one element 
within that class they can do so. The same goes for the Student class. Here we are also creating a user_input attribute that is given 
the name of name. This allows for any user to input their name and they will be met with the ensuing text that has been written to 
greet them and to begin their journey through our CLI. We lastly invoke the start method within our dunder method in order to kick off 
the CLI.

* start():
Start initiates the conversation between the user and the written code. To begin with we welcome the user. The user is prompted to type 
"list", "search", or "add" at this point in order to see a full list of the projects and students, search through the list, or add to 
the list. Once one of these three options is selected the user will be brought on a short but delightful journey through our CLI. Once 
this is complete the user will be prompted to press either "N" or "Y". If the user presses "N" for "no" the experience will continue 
and the user can once again decide between adding a group or student and searching through a list of them. If the user presses "Y" for 
"yes" the user will be kindly escorted off the CLI premises. 

* add_data():
This function serves as a way for the user to add relevent information to the database. If they wish to add either a project group or a student they can do so. 

* make_student():
Here we are allowing the user to create a new student that will be added to the student list. This includes the students name as well 
as the students linkedin account.

* if __main__ == '__main__':
What this does is it allows for the schema, aka the blueprint of the code, the thing that makes everything relate to one another in a
coherent way within the code, to persist.

* printer():
Once the user has decided to finish their journey the printer waves them off with a print of "Goodbye" plus the user's name.



# project_group

* print_project_groups():
This function allows the user to access individual projects within the list of projects.

* print_project_group():
This function prints up the various printed lines of code seen in the command line after querying a particular project.



# start_ups

* show_data():
This function serves to allow the user to input either upper or lower case spelling when inputting the requested "s" or "pg" in order 
to access the students or projects. It also serves to show the data once the list has been selected.

* search_data():
This allows the user to search through the students and projects to select an individual element within the list.



# Students

* print_students():
This function allows the user to access individual students within the list of students.

* print_student():
This function prints up the various printed lines of code seen in the command line after querying a particular student.

* print_student_details():
This prints up the group id, student name, and student linkedin.



# h1 Seed

The seed file functions to populate the database with realistic data when testing out new features within the database. This is why you'll see the fake function method utilized in our code. This method will give random data that fits the content of the database, such as random names, random colors, random urls, etc. You can, of course, also input data of your own. We have done both in our seed file.

* if __name__ == '__main__':
In our first line of code we are connecting to a sqlite database which we have named "pg-to-students.db". In lines two and three we are setting up our code so we can add content to the database. These lines of code are akin to a class and an instance in python respectively. If we continue down we'll see that we are calling a delete method on the session.query. This is done so when we seed our database it is always done with a fresh slate. If we didn't delete the previous data after leaving the database and getting back into it the data would stack. We would go from seeding the data with 10 names to suddenly having 20 names, to 30, 40, and so on. This method makes sure to always clear the database of that particular data after every exit from the database.

* fake = Fake():
This is attaching the fake function to a variable for later use.

linkedIn and groupnames are creating lists for the database to use.

* projectgroups:
This list is holding the randomly placed groupnames that will be displayed in the CLI. 

* students:
This list is holding the randomly generated fake names of the students as well as the randomly distributed linkedin accounts associated with those students and lastly the project groups id.



# h1 debug
This file is used to enter a debugger within the terminal in order to debug the code, whether that be for playing with the code to better understand it or maybe to try and figure out an error.



# Models 
Firstly we have this crazy line called "convention" full of weird characters and just bellow that we have something called "metadata". Convention is present because SQLite requires names for changes to foreign keys and several other fields in models. The "convention" provides a template for naming these changes, and the metadata saves them to a sqlalchemy.Metadata object. Passing all of this to the declarative_base object allows for Alembic to generate these names automatically when we autogenerate migrations. 

* ProjectGroup:
This class is creating the table for the project groups and is connecting to the class Students via the relationship() method. The inclusion of a foreign key in the Student class completes this relationship. Meaning there are many students to one Project Group

* Student:
This class is creating the table for the students. They each have a name as well as a linkedin account. The Student class has a foreign key in order to connect it with the project group. The __repr__ is used to set a default output value when you print out an instance of the class in the terminal.  