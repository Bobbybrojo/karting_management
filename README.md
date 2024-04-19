# karting_management
A Go-Karting establishment management GUI application with a MySql backend.

# Preview
![SignUp Page](https://i.postimg.cc/LsDkS6Km/Sign-Up-Screen.png)
![Racers Page](https://i.postimg.cc/Y9S6CKMY/Racers-Screen.png)
![Races Page](https://i.postimg.cc/wBg5nRrW/Races-Screen.png)

# Running the project
Dependencies: Python 3.11+
PySimpleGUI: https://pypi.org/project/PySimpleGUI/
Pymysql: https://pypi.org/project/pymysql/
MySqlWorkbench
Make sure to have the above dependencies installed before beginning.
After downloading the project zip file. Unzip the file.
Run the provided SQL file which will generate the necessary project data.
Run the main.py python file and enter the database username and password. The project will try to connect to the localhost.
User: root
Password: password
Enter the application that looks like the following.

Technical Specifications:
I will be using Python to develop the GUI application. I will use the PySimpleGUI package to develop this and use the pymysql library to make requests to the database for data. The database will use MySQL.

Data Description:
The racing database contains a profile for each racer. It tracks the racer’s username {PK}, their first and last name, and a list of the races they’ve taken place in. The racing database represents a race with a raceid{PK}, the date of the race, a list of racers in the race. Multiple racers can take place in multiple races. This relationship is represented as a stint: Per race a racer’s stats (position and best laptime) are stored in the stint with raceid and racer username. The is an object for Employee which is for tracking the employee_id, first_name, and last_name of all employees. Additionally there is an energy_drink product object. This has a primary_id as one of “RED”, “BLUE”, “YELLOW”, “GREEN” which is unique and the primary key of each object. It additionally tracks the “quantity” of energy drinks left in inventory.
UML Diagram for conceptual design:
Logical Design:
  
User Flow and Interaction:
The entire functionality of the application is available through buttons and text input bars once the GUI is open.
User interactions:
Tabs:
- Sign Up
- Enter username, firstname, and last name to CREATE a new racer
- Race
- Read racers in the racer table of database
- Search for racer in search bar and click “Search”
- Click on row to select it
- Click UPDATE or DELETE when a row is selected to update/delete the username
- Stints
- View all stints contained in the database
- Search By Username to view stints raced by a specific username
- Search By Race ID to view stints by a specific race id
- Races
- View all races and the date they took place
- Click CREATE to add a race
- Click Delete while a row is selected to delete it from the database
- Shop
- Track the quantity of energy drinks by increasing or decreasing the scrollbox
- Click complete transaction to update the quantities of items in the shop
- Employees - click to view current employees

Bugs Encountered:
The main bug still contained in the code happens when updating a racer username and the user clicks cancel. This will update the racer name to None and I was unable to fix this bug so far even though an attempted fix is included in the code.

Lessons Learned:
1. Technical Expertise Gained:
I learned how to connect a Python program to a MySQL database and use stored
procedures and API calls to interact with the database. Additionally, I learned to create a tikinter GUI application front end using pysimplegui and design an application that appropriately responds to user input to update the database to meet the application specification requirements.

3. My main insight and takeaway from the project is to prepare more in advance in
research on the technologies I am using so I can achieve the result I expect. I was a bit disappointed by pysimplegui because the window size was extremely small and control of it was restrictive within the package. I would prefer to do more research and pick a different GUI application building package such as Flet.

4. Released or contemplated alternative design / approaches to the project
Learning the language Flutter or the python package Flet to create a nice looking GUI
application would be my goal if I were to revisit this project. I would have liked a bit more freedom in design and sizing options of the application. The GUI would also look more modern with this alternative approach.

Future work:

1. A possible planned use of the database for me would be to track my own race times at different tracks when I go gokarting and use the application as a visualizer of my data and progress go karting.
2. Added functionality would be to add the ability to create a stint from within the application as it is currently a feature that is missing. This would require a significantly deeper knowledge level understanding of the GUI package to build.
3. My justification for using the database as a personal tracker would be my personal growth as a racer at go karting tracks to use as motivation.
