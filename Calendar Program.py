"""
A calendar program. Will allow the user to add events, delete events, update, view the calendar and exit
"""
from time import sleep, strftime
import os

calendar = {}
def welcome():#welcomes the user to the program
  user = input("Enter name")
  print ("Welcome "+user)
  print ("Calendar starting...")
  sleep(1)
  print ("Today is "+strftime("%A %d %B, %Y"))#lets us know the date today, weekday, date, month as word, year
  print ("Time is "+strftime("%H:%M:%S"))#shows us the current time.

def display_calendar():#allows us to view the calendar
    print("")
    if len(calendar.keys())==0:
        print ("Calendar is empty.")
    else:
        for i in calendar.keys():#displays events showing the date and then the event
            print("Date: "+i+". Event "+str(calendar[i])+"\n")

    
def start_calendar():
  welcome()
  start=True
  while start==True:
    print ("Select a task...\nA to Add an event \nU to Update an existing event \nV to View the calendar \nD to Delete an event \nX to Exit")
    user_choice = input("")
    user_choice = user_choice.upper()
    if user_choice == "V":#Views the calendar
      os.system('cls')
      display_calendar()
    elif user_choice=="U":#Updates the calendar
      date = input("What date to update?: ")#asks for the date
      update = input("What event do we want to change this date to")#asks what the update is
      calendar[date] = update#changes the values
      os.system('cls')
      print ("Successful")
      display_calendar()
    elif user_choice == "A":#Adds new events to the calendar
      event = input("Enter event")#asks for the event
      date = input("Enter date, (DD/MM/YYYY): ")#Asks for the date
      month=int(date[3:5])
      day = int(date[:2])
      if len(date)>10 or int(date[6:])<int(strftime("%Y"))or month>12 or day>31:#checks to see if the date format is too long or if the year is less than this year.
        print ("Invalid date selected.")
        try_again = input("Try again? N or Y")
        try_again=try_again.upper()
        if try_again=="Y":
          continue#continues back from the start of the main loop
        else:
          start=False
      else:
        calendar[date]=event
        os.system('cls')
        print ("Successfully added.")
        display_calendar()
    elif user_choice =="D":#deletes an entry in the calendar
      if len(calendar.keys())==0:
        print ("Calendar is already empty")
      else:
        date = input("What date does the event take place? ")
        del calendar[date]

    elif user_choice == "X":#exits the program
      start=False
    else:
      print ("Invalid option.")#also exists the program
start_calendar()#runs the main function.
