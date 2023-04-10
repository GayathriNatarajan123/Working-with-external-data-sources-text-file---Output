#  =================Task 15================
# Author: Gayathri
# Created Date: 09/04/2023
# Reference: example.py, W3schools
# This is a Python program, the purpose of this program is to put the data from the text file reg_form.txt and second_reg_form.txt.
# Writng data into the file reg_form.txt as mentioned in the task.
# Writing data into the file second_reg_form.txt as per my creativity.
# Setting the validation to receive only int value to get the number of regristration.
# Setting the validation to receive only 16 digits got the student id.
# Adding validation to check if file exist or not to append the data or to add new data.
# Added defensive programing.
#  ======================================

#Importing os module to check if file exist or not
import os

# Validation to request user to enter only +ve whole number.if user enters -ve integer number converting that to +ve nmber
def validate(variable_to_validate):    
    while(True):
        try:   
            #using abs method to get only +ve whole number
            variable_to_validate = abs(int(variable_to_validate))
            if(variable_to_validate == 0): 
                variable_to_validate = input("The number cannot be 0. Please enter integer number only: ")
            else:
                return variable_to_validate                  
        except ValueError:
            variable_to_validate = input("Please enter integer number only: ")

# Validation to restrict the length of student id to be 10 or less.
def validate_length(variable_to_validate):
    while(True):
        try:
            if(len(variable_to_validate) > 16):
                variable_to_validate = input("Please enter only 16 digits or character: ")
            else:
                return variable_to_validate
        except ValueError:
            variable_to_validate = input("Please enter only 16 digits or character: ")

print("----------------------------------------------------------------------------")
print("-----------Working with external data sources-text file - Output------------")
print("----------------------------------------------------------------------------")

#Start of the program
number_registering = validate(input("Please enter how many students are registering:"))
#Declaring 2 different list for 2 functionality
student_id = []
second_student_id = []
file_name = "reg_form.txt"
second_file_name = "second_reg_form.txt"

try:
    #Get Student id
    for number in range(0,number_registering):
        get_input = validate_length(input("Please enter your ID number to register: "))
        id="Student ID: " + get_input + " ....................\n\n"
        #Appending the inputs into 2 different list for 2 functionality
        student_id.append(id)
        second_student_id.append(get_input)


    #----Check if file and data already exist for display purpose
    is_empty_file = True
    if os.path.exists(file_name):
        with open(file_name, "r") as file_object:
            line = file_object.readline()
            if(line != ""):
                is_empty_file = False

    #---Writing data into file reg_form.txt as instructed in the task-----
    with open(file_name, "a") as file_object:
        # Restrict, adding the heading when we appending data to the existing file with data
        if(is_empty_file):
            file_object.write("Exam Attendance Register\n\n")
        for id in student_id:        
            file_object.write(id)
    
    #--------My style of displaying the data into text file as table----------
    #Formatting to display id's in a table format
    heading = "   Exam Attendance Register\n"
    fulldata = ""
    row_border = "-------------------------------------------"
    student_id_header = "!{:5}Student Id {:5}!".format("","")
    signature_header = "{:5}Signature {:4}!".format("","")
    signature_empty = "{:19}!".format("")
    

    #----Check if file and data already exist for display purpose
    is_empty_file = True
    if os.path.exists(second_file_name):
        with open(second_file_name, "r") as file_object:
            line = file_object.readline()
            if(line != ""):
                is_empty_file = False
    
    if(is_empty_file):
        fulldata = row_border + "\n" + student_id_header + signature_header + "\n"+ row_border +"\n"
    for items in second_student_id:
        id = "{}{}".format("! ", items)
        id_length= len(items)
        id_length = 21-id_length
        for space in range(1,id_length):
            id +=" "
        id += "!"
        fulldata += id + signature_empty + "\n" + row_border + "\n"
    
    #--writing data into the text file Another_reg_form.txt----
    with open(second_file_name, "a") as file_object: 
        # Restrict, adding the heading when we appending data to the existing file with data
        if(is_empty_file):            
            heading = "   Exam Attendance Register\n"
            file_object.write(heading)
            file_object.write(fulldata)
        else:
            file_object.write(fulldata)
    
    print("Thank you for using the application. Successfully added/updated the data.")
    print("----------------------------------------------------------------------------")
except Exception as error_message:
    print(error_message)