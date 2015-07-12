__author__ = "PtGaming"

###########
# CLASSES #
###########

class PtGamingError(Exception):
    pass

class CoreError(Exception):
    pass

while True:
    try:
        import imp #Import imp module
        print("imp imported") #Tell user that pygame was imported successfully
        break #break the loop

    except ImportError: #If there was a fault
        error = "module: imp could not be imported" #Declare the error
        raise PtGamingError(error) #Raise the error

while True:
    try:
        import time #Import time module
        print("time imported") #Tell user that time was imported
        break #Break the loop

    except ImportError: #If it failed to import
        error = "module: time could not be imported" #Declare the error
        raise PtGamingError(error) #Raise the error

while True:
    try:
        import random #Import random module
        print("random imported") #Tell user that the module was imported
        break #Break the loop

    except ImportError: #If it failed
        error = "module: random could not be imported" #Declare the error
        raise PtGamingError(error) #Raise the error

while True:
    try:
        import os #Import os module
        print("os imported") #Tell user that the module was imported
        break #Break the loop

    except ImportError: #If it failed
        error = "module: os could not be imported" #Declare the error
        raise PtGamingError(error) #Raise the error

while True:
    try:
        import shutil #Import shutil module
        print("shutil imported") #Tell user that the module was imported
        break #Break the loop

    except ImportError: #If it failed
        error = "module: shutil could not be imported" #Declare the error
        raise PtGamingError(error) #Raise the error

##############
# PROCEDURES #
##############

# LOGGING #
def log(event):
    """ Logs an event to a file. Event = the data/event to record to the file
    """
    temp_dir = os.getcwd() #Get the current directory
    os.chdir(log_dir) #Change the directory to the defined log directory
    date = time.strftime("%x") #Retrieve the date
    date_split = date.split("/") #Split the date into a list
    file_name = date_split[1] + "_" + date_split[0] + "_" + date_split[2] + ".txt" #File name is DD_MM_YY
    data = "[" + time.strftime("%X") + "]" + " " + event + "\n" #The event that is getting logged [TIME]: EVENT
    log_file = open(file_name, "a") #Open the file in append mode
    log_file.write(data) #Write the data to the file
    log_file.close() #Close the file
    os.chdir(temp_dir) #Change the directory back to the previous directory

# LOGIN #
def login():
    """ Logs the user into the Python Command Line. Used to find out who is doing what (for logging)
    """
    print("ID CODE:")
    code = input() #The user's ID code
    if code == "": #If no code entered
        print("NEW USERNAME:") #Create a new ID
        new_username = input() #Their username
        print("NEW ID CODE:")
        file = open("users.txt", "r") #Open users.txt in read mode
        new_code = "_"
        while new_code == "_": #While new_code is nothing
            lines = file.readlines() #Read the codes 
            new_code = random.randint(1000,9999) #Generate a new 4-digit code
            for i in lines: #For every code in the file
                line = i.split(":") #Split the code into [code, username]
                if new_code == int(line[0]): #If the code has already been used
                    new_code = "_" #Continue the loop

        print(new_code) #Print the new code
        file.close() #Close the file
        file = open("users.txt", "a") #Open users.txt in append mode
        value = str(new_code) + ":" + new_username.upper() + "\n" #CODE:USERNAME
        file.write(value) #Append the data to the file
        file.close() #Close the file
        print("REMEMBER YOUR ID CODE!") #Warn the user
        time.sleep(5) #Sleep (pause) for 5 seconds
        print("\n"*80) #Clear the screen
        login() #Call login again
        
    else: #If the user entered a code
        file = open("users.txt", "r") #Open users.txt in read mode
        lines = file.readlines() #Read the data, line for line.
        count = 0
        counter = 0
        for i in lines: #For each line, add one to counter
            counter = counter + 1
            
        for i in lines: #For each line
            line = i.split(":") #Split the data into [CODE, Username]
            if line[0] == code: #If the data is equal to the code the user entered
                user = line[1].split("\n")[0] #Log the user in
                print("[LOGIN] Welcome:", user)
                file.close() #Close the file
                file = open("user.txt", "w") #Open user.txt in write mode
                value = "user:" + user
                file.write(value) #Write the user to the file
                file.close() #Close the file
                #User.txt is a hard copy of the currently logged in user. It allows other modules to easily access who
                #the current user is; without the need for classes.

            else: #If the data isn't equal
                count = count + 1 #Add 1 to the count

        if counter == count: #If list has been exhausted
            print("[LOGIN] ERROR: ID not recognised") #Alert that their ID was not recognised
            event = "[LOGIN] Error ID: {0} not recognised".format(code)
            log(event) #Log the event
            raise PtGamingError(event) #Raise an error

        else:
            event = user + " logged in"
            log(event) #Log that the user logged in
        

def dir_back():
    """ Goes back a directory. Requires os
    """
    x_dir = os.getcwd().split("\\") #Get the current working directory and split directory into folders
    x_dir = x_dir[1:-1] #The new directory is from C to one before the end.
    new_dir = "C:"
    for i in x_dir: #For how ever many folders between C and new destination
        new_dir = new_dir + "\\" + i #Add \\ between the folders

    os.chdir(new_dir) #Change the directory

def direct_dir(x):
    """ Travels directly to a defined location
    """
    try:
        os.chdir(x[0]) #Try to change the directory

    except PermissionError: #If user has no access, deny access.
        print("[CORE] Error: Access is denied: {0}".format(x[0]))
        print("[CORE] Error: You do not have permission to access that directory")

    except FileNotFoundError: #If directory doesn't exist, alert user.
        print("[CORE] Error: File not found: {0}".format(x[0]))
        print("[CORE] Error: The system cannot find the specified directory")

    except NotADirectoryError: #If directory is a file, alert user.
        print("[CORE] Error: Invalid Directory: {0}".format(x[0]))
        print("[CORE] Error: The specified path is not a directory")

def new_dir(x):
    """ Changes the directory to x
    """
    x_dir = os.getcwd().split("\\") #Get the current working directory and split into folders
    for i in x: #For how ever many folders ahead new destination is
        x_dir.append(i) #Add the new folders to the new directory
        
    new_dir = "C:"
    for i in x_dir[1:]: #From 1 to the end of the list
        new_dir = new_dir + "\\" + i #Add \\ between each folder

    try:
        os.chdir(new_dir) #Try to change directory to the newly stated one

    except PermissionError: #If user has no access, deny access.
        print("[CORE] Error: Access is denied: {0}".format(new_dir))
        print("[CORE] Error: You do not have permission to access that directory")

    except FileNotFoundError: #If directory does not exist, alert user.
        print("[CORE] Error: File not found: {0}".format(new_dir))
        print("[CORE] Error: The system cannot find the specified directory")

    except NotADirectoryError: #If directory is not a folder - but a file, alert user.
        print("[CORE] Error: Invalid Directory: {0}".format(new_dir))
        print("[CORE] Error: The specified path is not a directory")

def copy(source, destination):
    """ Copies one folder to another folder
    """
    try:
        shutil.copytree(source, destination) #Try to copy the folder across

    except FileNotFoundError: #If directory/file does not exist, alert user
        print("[CORE] Error: File not found: {0}".format(source))
        print("[CORE] Error: The system cannot find the specified directory")

###############
# PRE-LOADING #
###############

if __name__ != "__main__": #If user is trying to import the file.
    exception = "[CORE] Error: Importing has been disabled for this file." 
    raise CoreError(exception)

else: #If program has been run fairly
    if not os.path.exists("users.txt"): #If users.txt does not exist
        file = open("users.txt", "w") #Make the file
        file.write("007:ADMIN\n")
        file.close()

    if not os.path.exists("user.txt"): #If user.txt does not exist
        file = open("user.txt", "w") #Make the file
        file.close()

    if not os.path.isdir("logs"): #If \logs does not exist
        os.makedirs("logs") #Make the directory

################
# MAIN PROGRAM #
################

print("\nPYTHON CORE")
log_dir = os.getcwd() + "\\logs" #Log directory is the current location + logs
login() #Call the login procedure
while True: #Loop forever
    print("\n" + os.getcwd() + "\n") #Print the current directory
    uinput = input() #Wait for user action
    print()
    InputList = uinput.split(" ")
    if InputList[0] == "cd": #If a directory command is used
        try:
            if InputList[1] == "..": #If the user wants to go back
                dir_back() #Call the dir_back procedure

            elif InputList[1] == "-d": #If the user wants to directly go to a directory
                direct_dir(InputList[2:]) #Call the direct_dir procedure

            else: #Else
                new_dir(InputList[1:]) #Call the new_dir procedure

        except IndexError: #If the user didn't enter a valid command
            print("[CORE] Error: NUL parameter in directory function")
            print("[CORE] Error: Please input a correct parameter for the cd function!")

    elif InputList[0] == "dir": #If the dir command is used
        folders,alphabetic = False,False
        for i in InputList[1:]:
            if i == "-f": #If the -f parameter is used
                folders = True #Only display folders

            elif i == "-a": #If the -a parameter is used
                alphabetic = True #Display files alphabetically

            else:
                print("[CORE] Error: Unknown parameter: {0}".format(i))

        dir_list = []
        for i in os.listdir(): #For each folder/file in the directory
            dir_list.append(i) #Add them to the list
            
        if alphabetic == True: #If alphabetic
            dir_list.sort() #Sort them alphabetically

        if folders == True: #If folders
            for i in dir_list: #For each file/folder in the list
                if os.path.isdir(i) == True: #If directory
                    print(i) #Print the folders

        else: #If not folders
            for i in dir_list: #Print each file/folder
                print(i)

    elif InputList[0] == "run": #If the user wants to run/import a module
        directory = os.getcwd() + "\\" + InputList[1] #Get the current working directory
        if InputList[1][-3:] != ".py": #If the input does not end in .py
            directory = os.getcwd() + "\\" + InputList[1] + ".py" #Make it end in .py 

        try:
            module = imp.load_source("", directory) #Try to run the module
            print("\n"*80, end="[CORE] Session Closed\n") #When the file closes, alert the user

        except FileNotFoundError: #If file doesn't exist, alert user
            print("[CORE] Error: File not found: {0}".format(directory))
            print("[CORE] Error: Target is not valid Python module.")

    elif InputList[0] == "test": #Testing
        print("▒#") #Testing
