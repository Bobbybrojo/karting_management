import PySimpleGUI as sg
import pymysql
import datetime



sign_up_layout = [[sg.Text("Register a Racer                         ", font=("Calibri", 24))],
                  [sg.HorizontalSeparator(color='white')],
                  [sg.Text("Username")],
                  [sg.Input(key='Username')],
                  [sg.Text("First Name")],
                  [sg.Input(key='FirstName')],
                  [sg.Text("Last Name")],
                  [sg.Input(key='LastName')],
                  [sg.Button("Sign Up", key="SignUpButton")]]

racer_layout = [[sg.Text("View Racers                                ", font=("Calibri", 24))],
                [sg.HorizontalSeparator(color='white')],
                [sg.Input(key='-SearchInput-'), sg.Button("Search", key="SearchButton")],
                [sg.Table([], headings=['username', 'first name', 'last_name'], key="RacerTable", enable_events=True, expand_x=True),
                  sg.Column([[sg.Button("Update", key=("UpdateRacers"))], 
                             [sg.Button("Delete", key=("DeleteRacers"))]])]]

stints_layout = [[sg.Text("View Stints                                 ", font=("Calibri", 24))],
                [sg.HorizontalSeparator(color='white')],
                [sg.Text("Search By Username"), sg.Input(key="SearchUsername", size=15, enable_events=True), sg.VerticalSeparator(),
                 sg.Text("Search By Race Id"), sg.Input(key="SearchRaceId", size=15, enable_events=True)],
                [sg.Table([], headings=['Date', 'racer', 'race_id', 'position', 'best lap time'], expand_x=True, key="StintTable")]]

races_layout = [[sg.Text("View Races                                 ", font=("Calibri", 24))],
                [sg.HorizontalSeparator(color='white')],
                [sg.Table([], headings=['race id', 'race date'], key="RaceTable"),
                 sg.Column([[sg.Button("Create", key=("CreateRace"))], 
                             [sg.Button("Delete", key=("DeleteRace"))]])]]

employees_layout = [[sg.Text("View Emplloyees                           ", font=("Calibri", 24))],
                    [sg.HorizontalSeparator(color='white')],
                    [sg.Table([], headings=['id', 'first name', 'last name'], key="EmployeeTable")]]

shop_layout = [[sg.Text("Energy Drink Shop", font=("Calibri", 24))],
               [sg.HorizontalSeparator(color='white')],
               [sg.Text("Red Energy Drink"), sg.Spin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], initial_value=5, readonly=True, text_color='White', key="RedSpin")],
               [sg.Text("Blue Energy Drink"), sg.Spin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], initial_value=5, readonly=True, text_color='White', key="BlueSpin")],
               [sg.Text("Yellow Energy Drink"), sg.Spin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], initial_value=5, readonly=True, text_color='White', key="YellowSpin")],
               [sg.Text("Green Energy Drink"), sg.Spin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], initial_value=5, readonly=True, text_color='White', key="GreenSpin")],
               [sg.Button("Complete Transaction", key="BuyButton")]]


# All the stuff inside your window.
layout = [[sg.TabGroup([[sg.Tab("Sign Up", sign_up_layout, key="SignUp"),
                         sg.Tab("Racers", racer_layout), 
                         sg.Tab("Stints", stints_layout),
                         sg.Tab("Races", races_layout),
                         sg.Tab("Shop", shop_layout),
                         sg.Tab("Employees", employees_layout)
                         ]], enable_events=True, key='tabs')]]

# Create the Window
sg.theme("Reddit")
font = ("Arial", 15)
window = sg.Window('GoKart Racing Management System', layout, font=font)

# Connect to database

try:
  username = input("Enter your database username: ")
  password = input("Enter your database password: " )
  connection = pymysql.connect(host='localhost',
                                user=username,
                                password=password,
                                database='GoKarting',
                                cursorclass=pymysql.cursors.DictCursor)

except:
  print("Connection Unsuccessful - Incorrect username or password entered for database.")
  exit()

cursor = connection.cursor()

# Format a dictionary from MySql to fit PySimpleGUI Table format
def format_table(tables_dict):
  table = []
  for row in tables_dict:
    values = []
    for val in row.values():
      if type(val) == datetime.date:
        values.append(val.strftime("%m/%d/%Y"))
      else:
        values.append(val)
    table.append(values)
  return table

# Returns the username of racer given the index of appearance in the table
def get_username_from_table_index(idx):
  cursor.execute("SELECT * FROM racer")
  table_json = cursor.fetchall()
  return format_table(table_json)[idx][0]

# Returns the username of racer given the index of appearance in the table
def get_race_id_from_table_index(idx):
  cursor.execute("SELECT * FROM race ORDER BY race_date DESC")
  table_json = cursor.fetchall()
  return format_table(table_json)[idx][0]

# Updates the GUI view of a table to the latest versions of a MySQL table
def update_table_from(sql_table, table_key):
  cursor.execute(f"SELECT * FROM {sql_table}")
  table_json = cursor.fetchall()
  window[table_key].update(values=format_table(table_json))

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'tabs':
      
      if values['tabs'] == 'Races':
        cursor.execute("SELECT * FROM race ORDER BY race_date DESC")
        table_json = cursor.fetchall()
        window["RaceTable"].update(values=format_table(table_json))
        
      if values['tabs'] == 'Racers':
        update_table_from("racer", "RacerTable")
        
      if values['tabs'] == 'Stints':
        cursor.callproc("get_stints");
        table_json = cursor.fetchall()
        window["StintTable"].update(values=format_table(table_json))
        
      if values['tabs'] == 'Shop':
        cursor.execute("SELECT * FROM energy_drink")
        edrink_quantities = cursor.fetchall()
        for row in edrink_quantities:
          if row['color'] == "RED":
            window["RedSpin"].update(value=row['quantity'])
          if row['color'] == "BLUE":
            window["BlueSpin"].update(value=row['quantity'])
          if row['color'] == "YELLOW":
            window["YellowSpin"].update(value=row['quantity'])
          if row['color'] == "GREEN":
            window["GreenSpin"].update(value=row['quantity'])
        
      if values['tabs'] == 'Employees':
        update_table_from("employee", "EmployeeTable")
    
    # Create new racers    
    if event == 'SignUpButton':
      if len(values['Username']) > 0 and len(values['FirstName']) > 0 and len(values['LastName']) > 0:
        try:
          cursor.callproc("create_racer", [values['Username'], values['FirstName'], values['LastName']])
          connection.commit()
        except:
          print("That username was already used")
    
    # Racers view features
    if event == "SearchButton":
      username = values['-SearchInput-']
      if len(username) > 0:
        print(f"Search pushed{username}")
        cursor.execute(f"SELECT * FROM racer WHERE username = '{username}'")
        table_json = cursor.fetchall()
        window["RacerTable"].update(values=format_table(table_json))
      else:
        update_table_from("racer", "RacerTable")
          
    if event == 'UpdateRacers':
      print("Update Pressed")
      try:
        username = get_username_from_table_index(values["RacerTable"][0])        
        new_username = sg.popup_get_text("Enter new username", title="Update Username")
        if new_username != "None":
          cursor.execute(f"UPDATE racer SET username = '{new_username}' WHERE username = '{username}'")
          connection.commit()
          update_table_from("racer", "RacerTable")
      except: 
        continue
      
    if event == 'DeleteRacers':
      try:
        username = get_username_from_table_index(values["RacerTable"][0])
      except: continue
      try:
        cursor.execute(f"DELETE FROM RACER WHERE username = '{username}'")
        connection.commit()
        update_table_from("racer", "RacerTable")
        print(f"Deleted row where username = {username}")
      except:
        print("Username to delete not found in database")
    
    if event == 'CreateRace':
      print("Create Pressed")
      try:
        tuple_list = sg.popup_get_text("Enter race tuple in format 'int race_id, Date YYYY-mm-dd'").split(", ")
        insert_query = f"INSERT INTO race VALUES ({int(tuple_list[0])}, {tuple_list[1]})"
        print(insert_query)
        cursor.callproc("create_race", tuple_list)
        connection.commit()
        
        cursor.execute("SELECT * FROM race ORDER BY race_date DESC")
        table_json = cursor.fetchall()
        window["RaceTable"].update(values=format_table(table_json))
      except:
        print("Create formatting was wrong and not committed.")
    
    if event == 'DeleteRace':
      try:
        race_id = get_race_id_from_table_index(values["RaceTable"][0])
      except: continue
      try:
        cursor.execute(f"DELETE FROM race WHERE race_id = '{race_id}'")
        connection.commit()
        
        cursor.execute("SELECT * FROM race ORDER BY race_date DESC")
        table_json = cursor.fetchall()
        window["RaceTable"].update(values=format_table(table_json))
        print(f"Deleted row where race_id = {race_id}")
      except:
          print("Race_id to delete not found in database")
    
    
    # Searching Features for Stints
    if event == "SearchUsername":
      if len(values["SearchUsername"]) > 0:
        cursor.callproc("get_stints_by_racer", [values["SearchUsername"]])
        print("Search queried")
        window["StintTable"].update(values=format_table(cursor.fetchall()))
      else:
        cursor.callproc("get_stints");
        table_json = cursor.fetchall()
        window["StintTable"].update(values=format_table(table_json))
        
    if event == "SearchRaceId":
      if len(values["SearchRaceId"]) > 0 and str.isdigit(values["SearchRaceId"]):
        cursor.callproc("get_stints_by_race_id", [values["SearchRaceId"]])
        print("Search queried")
        window["StintTable"].update(values=format_table(cursor.fetchall()))
      else:
        cursor.callproc("get_stints");
        table_json = cursor.fetchall()
        window["StintTable"].update(values=format_table(table_json))
      
    if event == "BuyButton":
      red_quantity = values["RedSpin"]
      blue_quantity = values["BlueSpin"]
      yellow_quantity = values["YellowSpin"]
      green_quantity = values["GreenSpin"]
      try:
        cursor.execute(f"UPDATE energy_drink SET quantity = {red_quantity} WHERE color = 'RED'")
        cursor.execute(f"UPDATE energy_drink SET quantity = {blue_quantity} WHERE color = 'BLUE'")
        cursor.execute(f"UPDATE energy_drink SET quantity = {yellow_quantity} WHERE color = 'YELLOW'")
        cursor.execute(f"UPDATE energy_drink SET quantity = {green_quantity} WHERE color = 'GREEN'")
        connection.commit()
        sg.popup_ok("Transaction Comitted")
      except:
        print("Error occured during update")

window.close()
connection.commit()
connection.close()
exit()