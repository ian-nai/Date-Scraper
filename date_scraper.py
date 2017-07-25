import datefinder
import datetime
import os

def date_scraper():

    filepath1 = raw_input("Please enter the .txt file you'd like to extract dates from: ")

    with open(filepath1, 'r') as file1:
        text1 = file1.read()

    string_with_dates = text1

    matches = datefinder.find_dates(string_with_dates)

    for match in matches:
        print match
   
    
    saving = raw_input("Would you like to save these as 'dates.txt'? Note: this will overwrite previous saves. Type 'y' for yes and 'n' for no.")
    if saving == "y":
        text_file1 = open("dates.txt", "w")
        string_with_dates = text1
        matches = datefinder.find_dates(string_with_dates)
        for match in matches:
            string_dates1 = (str(match))
            text_file1.write(string_dates1 + '\n')
        text_file1.close()
        run_again = raw_input("Scrape another file? Type 'y' for yes and 'n' for no.")
        if run_again == "y":
            date_scraper()
        if run_again == "n":
            print "Bye!"
            exit(0)
    else: 
        run_again = raw_input("Scrape another file? Type 'y' for yes and 'n' for no.")
        if run_again == "y":
            date_scraper()
        if run_again == "n":
            print "Bye!"
            exit(0)
        else:
            print "Please enter a valid input."

date_scraper()
