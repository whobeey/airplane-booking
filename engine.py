# The most functional file "engine/config/operating", also most important

# Importing essential libraries for various purposes
from random import randint, choice # randint -> generates a random number from a given range, choice -> selects a random item stored in an index of an iterable

# A dictionary to store simple messages that are available to be displayed in terminal output
message = {"welcome": "Welcome to the Apache Airlines booking system!",
           "enter": "Enter your Selection (list number): ",
           "goodbye": "Goodbye valued customer!"}


# A dictionary to store strings that are options/messages to be displayed terminal output
option = {"check": "Check availability of seats",
          "book": "Enter seat booking",
          "free": "Free booked seats",
          "status": "Show seat booking status",
          "note": "Add a note for accessibility",
          "exit": "Exit the program"}

# A dictionary to store strings that are options/messages to be displayed terminal output
error = {"invalid": "ERROR: Invalid user input."}

# A dictionary to indicate what a character stands foR
indicate = ["'F' -> Free to book",
            "'R' -> Reserved",
            "'X' -> Aisle Row",
            "'S' -> Aircraft Storage"]

user_seats = {} # Dictionary that contains the seats the user has booked and location.
user_note = "" # User's custom note for specific reasons and accessibilty support
user = "Place Holder for User Account" # To be overwritten with an object for user account.

booking_database = {} # A Dictionary for the purpose to store booking informatio
booking_references = [] # A list of the booking references that are linked to a Burak Aircraft seats

def generate_reference(): # This function is able to generate new and random reference numbers
    valid_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" # Only upper-case ENG letters and numbers 0-9 for standard practical application

    while True: # Try to generate a unique reference number until possible (Retry if duplicate exists)
        reference = "" # Set the local variable to an empty string variable before inserting characters

        for i in range(8): # 0 - 7, but logically 1st to 8th character, to ensure eight characters
            reference += choice(valid_characters) # Using the random method to select a random character to add to the string

        if reference not in booking_references: # If reference number is unique, then add it to the list and return thr reference
            booking_references.append(reference) # Adds it, if condition is met
            return reference # Returns the Reference if the condition is met

# This function will create a table showing seating plan of the Burak 757 Aircraft, reflects later dictionary content
def create_table(): # Only the dictionary will be changed/edited, the table created only reflects*
    seats_table = [] # The purpose of initializing is for storing seating table rows

    for row in range(1, 80 + 1): # Iterating for 80. We add 1 to the argument of range() to ensure there are 80 because of Python's indexing method
        seats_table.append([row, # The current row, from iteration argument given (range(1, 80 + 1))
                            seats[row]["A"], seats[row]["B"],
                            seats[row]["C"], seats[row]["X"], # Note that what will eventually be marked as 'X' will never be available, just like 'S'/storage
                            seats[row]["D"], seats[row]["E"],
                            seats[row]["F"]])

    return seats_table # Returns an updated table, it should not take any argument since we are dealing with one Burak 757 aircraft at the moment

def status(): # Check status of seats that are free or reserved or aisles or storage spaces
    table_columns = ["  A", "B", "C", "X", "D", "E", "F"] # These are the columns for our aircraft and seating table
    seats_table = create_table() # Calls the function for creating/updating our table that reflects our dictionary (initalized later in code, position follows PEP 8 mostly, so I am sorry about that)

    # Create/Output the seven headers, (A - F) including X -> Aisle
    print("\n", *table_columns, "\n")

    for row in seats_table: # Iterate through each created row of our seating table
        display = lambda v: "R" if len(str(v)) == 8 and str(v) not in ("F", "X", "S") else v # Utilization of a Lambda function for reference
        print(f"{row[0]:02}", display(row[1]), display(row[2]), display(row[3]), row[4], display(row[5]), display(row[6]), display(row[7])) # Creating/Printing the Burak 757 aircraft seating layout plan

    print("\n") # New line, to make sure output is neat in terminal

    for i, indicator in enumerate(indicate, start=1): # Print list of indicators for information about the aircraft's seats
        print(i, indicator) # Prints a character and what it corresponds to.

    if booking_database: # If there are any bookings...
        print("\nBooking References:")
        for ref, details in booking_database.items():
            print(f"  {ref} -> Seats: {', '.join(details['seats'])}")

def book(): # This function will allow users to book a seat that is free 'F', replaced after booking with reference number
    global user # For the purpose of global access (in this program)
    reference_seats = [] # Seats that were booked for Reference.
    while True: # Loop through code below until otherwise when everything goes accordingly right without user error
        seat_location = input("\n" + "Please enter the seat number (1A - 80F) or 'X' to exit: ").strip().upper() # Variable string used for booking a specific seat, it utilizes methods for clean proper neat input

        if seat_location == "X": # Check if the user wishes to exit
            if reference_seats: # If the user has booked any seats
                ref = generate_reference() # For the purpose of generation
                booking_database[ref] = {"passport": user.passport, "name": user.name, "surname": user.surname, "seats": reference_seats} # Method to info managing
                for seat in reference_seats: # Iteration...
                    r_axis, c_axis = user_seats[seat]
                    seats[r_axis][c_axis] = ref
                print(f"\nSeats booked: {', '.join(reference_seats)}\nYour booking reference is: {ref}") # Notify User...
            else:
                print("\nNo seats booked. Returning to menu...") # Notify user...
            break # Breaks out of the while loop

        if len(seat_location) not in (2, 3): # If the string length of the string is less than two characters or more it is un-acceptable
            print("\n" + error["invalid"] + "\n" + " Please enter a seat number like 1A or 80F") # Inform about error
            continue # Continues the while loop / Restarts to allow the user to try again

        row_text = seat_location[:-1] # User input is a string which can be seen as a series or list of characters in an order, this gets every character except the last, just to get row number
        column_text = seat_location[-1] # Which means if we have three characters and the third is the column and last character, we can use -1 to grab the last character needed for this operation

        if not row_text.isdigit(): # If it cannot be used as an integer or float then it is unusable in our operation
            print("\n" + error["invalid"] + " " + "Row input must be a number") # inform user...
            continue # Continues the while loop / Restarts to allow the user to try again

        row_text = int(row_text) # User input of row number is a string, we can turn

        if not (1 <= row_text <= 80): # Check if the seat number entered is valid and can exist in the aircraft.
            print("\n" + error["invalid"] + " " + "Row must be in or between 1 – 80") # inform user...
            continue # Continues the while loop / Restarts to allow the user to try again

        if column_text not in ["A", "B", "C", "X", "D", "E", "F"]: # Check if the column entered is valid and can exist in the aircraft.
            print("\n" + error["invalid"] + " " + "Invalid column input, please try again") # Inform user about error...
            continue # Continues the while loop / Restarts to allow the user to try again

        if seats[row_text][column_text] == "F": # If the seat is free/'F', book only if it is valid (It is, we checked in previous lines/statements)
            seats[row_text][column_text] = "R" # Set as 'R'/Reserved
            user_seats[seat_location] = (row_text, column_text) # Add to the list of seats that the user has booked
            reference_seats.append(seat_location) # Add to the list of seats linked to the reference number
            print(f"\nSeat {row_text}{column_text} booked successfully!") # Inform user about successful booking!
            print("You can book another seat on the same Aircraft!") # Offer another opportunity to book more seats

        else: # Using a match case inside an else statement for better readability
            match seats[row_text][column_text]: # Depending on seat's status / Anything other than 'F'/Free
                case "R": # If the seat is reserved
                    print(f"\nSeat at {row_text}{column_text} is already reserved.") # inform...
                case "X": # If the seat is an aisle, which is logically unbookable in modern aircrafts
                    print(f"\nSeat at {row_text}{column_text} is an aisle, please choose a valid free seat.") # inform...
                case "S": # If the seat is in a storage area
                    print(f"\nSeat at {row_text}{column_text} is storage.") # inform...
                case _: # If the seat cannot be booked for no reason, (This condition will likely never get raised)
                    print(f"\nSeat at {row_text}{column_text} cannot be booked.") # inform...

def user_booked(): # Function to display...
    print("\nYour booked seats:") # Display the user's booked seats

    if not user_seats: # If there aren't any seats booked by the user...
        print("No seats booked yet.") # Then inform them.
    else: # But if there are...
        for seat, (row, column) in user_seats.items(): # Display the seats booked by the user
            print(f"  {seat}  —  Reference: {seats[row][column]}") # Output the ones that are available

def free(): # This function will allow users to free a seat that was booked, marked 'R'
    user.verify() # Verify Identity
    while True: # Loop through code below until otherwise when everything goes accordingly right without user error
        user_booked() # Display the seats that the user has booked
        seat_location = input("\n" + "Enter a seat you booked that you wish to free or enter 'X' to exit: ").strip().upper() # Prompt user to enter, uses methods to format input

        if seat_location == "X": # If user input 'X' then they wish to exit
            print("\n" + "Exiting free page...") # Inform the user of exit
            break # Breaks out of the while loop and enters back into the main main

        if seat_location not in user_seats: # If they tried to free a seat that is not booked by them.
            print("\n" + error["invalid"] + " " + "You have not booked this seat") # Inform...
            continue # Continue...

        row, column = user_seats[seat_location] # "Grab the location*   "

        if seats[row][column] not in ("F", "X", "S"): # If the seat is Reserved...
            ref = seats[row][column]
            seats[row][column] = "F" # Then free it.
            del user_seats[seat_location] # Delete from the dictionary of booked seats
            if ref in booking_database: # Check and do the following if True
                booking_database[ref]["seats"].remove(seat_location) # Removal
                if not booking_database[ref]["seats"]: # Reverses the conditon of the statement to check ("not")
                    del booking_database[ref] # Delete (Deletes from running Memory)
            print(f"\nSeat at {seat_location} has now been freed.") # inform...
            continue # continue to give user another chance to free another seat.
        else: # Else...
            print(f"\nSeat at {seat_location} is not reserved.") # inforn...

def check(): # Simply check status
    status() # Show current seating plan
    user_booked() # Show user's booked seat

def note(): # Abilty to add a note to request accessibility support from Apache Airlines
    global user_note # Global Access for User Note
    print("You can add a note if you require accessibility or support.") # Inform user.
    print("Current Note: " + user_note) # Display the user's note
    user_note = input("Enter a new note: ") # User enters a new note

# Intializing a dictionary to call functions depending on user input
ability = {'1': check, # calls the function check()
           '2': book, # calls the function book()
           '3': free, # calls the function free()
           '4': status, # calls the function status()
           '5': note}  # calls the function note()

# The main function of this module, it manages actions, data and it displays the main menu
def run(): # The run() function does not take any argument or return any value when called
    global user # Global...
    user = Client(None, None, None, None) # Register to access (1/2)
    user.register() # Register to access (2/2)

    while True: # Continue running the code inside the while statement unless commanded otherwise
        print("\n" + "Welcome to the Apache Airlines booking system!") # Display a welcome message

        for i, key in enumerate(option, start=1): # We can use enumerate for easily iterating through a dictionary
            print(str(i) + ' - ' + option[key]) # String Concatenation, turn i/index into a string value in this statement

        choice = input("\n" + message["enter"]).strip() # Strip spaces to ensure input is compatible

        try: # Try converting input into an integer, to make sure it is valid
            choice = int(choice) # Try converting the user input for item choice into an integer
        except ValueError: # If it fails, then allow them to try again and inform them properly
            print("\n" + error["invalid"] + ' ' + "Please enter a number (1 - 6)") # Error and explanation
            continue # Restarts the while loop from the beginning

        # If user input of chosen list item number is 1 to 6, call a function depending on the key value (abilty dictionary)
        if 1 <= choice <= len(ability): # String value must be turned to an integer in the accepted range for this if statement
            ability[str(choice)]() # If true -> call the function based on the key's value, except we need a string value so we used str() to access dictionary indexing. Alternatively, we could remove quotes from the keys
            continue # Go back to the menu, which restarts the current while loop

        elif choice == 6: # If 6 is inputted, then the user wishes to exit
            print("\n" + message["goodbye"]) # Say Goodbye
            break # Exit out of the while loop and end the program
        else: # If input is invalid, let user know and go through the while loop again
            print("\n" + error["invalid"] + ' ' + "Please enter a number (1 - 6)") # Prints error message
            continue # Continues the while True loop statement

# Creating the seating plan for the Burak 757, set all seats to either 'F'/Free or 'X'/Aisle or 'S'/Storage. In this stage, there will be no booked spaces, therefore no 'R'/Reserved
seats = {} # Initializing an empty dictionary for seating

columns = ["A", "B", "C", "X", "D", "E", "F"] # There will be seven columns, except one will be the aisle 'X'.

# Using a 'for' loop to create the seating map for our Burak 757 aircraft
for row in range(1, 80 + 1): # Iterating for 80. We add 1 to the argument of range() to ensure there are 80 because of Python's indexing method
    seats[row] = {}

    # Using a 'for' loop to set certain seats as either 'F'/Free or 'X'/Aisle or 'S'/Storage. In this stage, there will be no booked spaces, therefore no 'R'/Reserved
    for column in columns: # For the column A, B, C... Check and do the following:

        if column == "X": # While iterating through columns, when at 'X' create
            seats[row][column] = "X"  # 'X' -> These are aisle spaces and they are never bookable

        elif 77 <= row <= 78 and column in ["D", "E", "F"]: # rows 77 and 78 in D/E/F are storage
            seats[row][column] = "S"  # 'S' -> These are designated & unbookable storage areas in the aircraft

        else: # If no condition applies, set the rest as free seats available for consumer booking
            seats[row][column] = "F"  # 'F' -> These are going to be free/unbooked seats available

class Client: # Initializing a Class to manage demo user details and booking
    def __init__(self, reference, passport, name, surname): # Initializing object attributes
        self.reference = reference # "Reference" -> Reference number linked to booking
        self.passport = passport # "Passport" -> User Passport for verification
        self.name = name # "Firstname" -> User Name for verification
        self.surname = surname # "Surname" -> User Surname for verification

    def register(self): # Method to register the user for this program
        while True: # While true do the following, until otherwise (until condition is met)
            self.name = input("Enter your first name: ") # Get user's firstname

            if len(self.name) < 2 or len(self.name) > 14: # Check length
                print("Invalid length, please enter a firstname 2-14 characters.") # Inform of error
                continue # Restart the while True loop, until correct input

            if any(char.isdigit() for char in self.name): # Check if the first name input has any numbers
                print("Please enter only valid English letters and no numbers.") # Inform of error
                continue # Restart the while True loop, until correct input

            break # Exit this while loop and move on to the next one

        while True: # While true do the following, until otherwise (until condition is met)
            self.surname = input("Enter your last name: ") # Request the user's surname for registration.

            if len(self.surname) < 2 or len(self.surname) > 14: # Check if surname length in valid to be used
                print("Invalid length, please enter a lastname 2-14 characters.") # Inform of error
                continue # Restart the while True loop, until correct input

            if any(char.isdigit() for char in self.surname): # Check if surname input is valid
                print("Please enter only valid English letters and no numbers.") # Inform of error
                continue # Restart the while True loop, until correct input

            break # Exit this while loop and move on to the next one

        while True: # While true do the following, until otherwise (until condition is met)
            self.passport = input("Enter your passport number (PXXXXXX) (Don't enter 'P'): ") # Get the user's passport number

            if len(self.passport) != 6: # Check if the passport number is invalid, and if it is, do the following:
                print("Invalid length, please enter a passport number of 6 characters.") # Inform of error
                continue # Restart the while True loop, until correct input

            if self.passport.isdigit() != True: # If the input wasn't a valid numbers only input, do the following and inform the user of their invalid input.
                print("Please enter only numbers.") # Inform of error
                continue # Restart the while True loop, until correct input

            break # Exit this while loop and move on to the next stage

        print(f"Your first and last name is {self.name} {self.surname} and your passport number is {self.passport}.") # Confirming details
        print("You have registered!") # Inform of success

    def verify(self): # Method for identity verification
        while True: # Do the following unless otherwise
            detail = input("Enter your surname to proceed: ") # Get input

            if detail != self.surname: # If input is invalid...
                print("Incorrect Info Inputted. Please Try Again") # If input is invalid inform user
                continue

            break # Exit and move on to the next part
        
        while True: # Do the following unless otherwise
            detail = input("Enter your passport number to proceed: ") # Get input

            if detail != self.passport: # If input is invalid...
                print("Incorrect Info Inputted. Please Try Again") # If input is invalid inform user
                continue

            break # Exit and move on to the next part
