# -*- coding: utf-8 -*-
"""
Built by Beni Saadon.
13-02-2022
"""

import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
students_db = {} # MAIN DATA BASE



# ******************* Print Functions *******************************


# --main_menu()
menu_options = {
    1: 'Insert Student details',
    2: 'Change Student details',
    3: 'Print Class details',
    4: 'failed student details',
    5: 'students mean details',
    6: 'Exit'
}


def print_menu():
  """Print main menu on screen."""
  print("\n")
  for key in menu_options.keys():
    print("--------------------------------------")
    print(key, '--', menu_options[key])
    print("--------------------------------------")


# *******************************************************

post_options = {
    1: 'Delete Student From The Class',
    2: 'Change Student From The Class',
    3: 'Exit'
}


def print_post_menu():
  """Print menu on screen."""
  print("\n")
  for key in post_options.keys():
    print("--------------------------------------")
    print(key, '--', post_options[key])
    print("--------------------------------------")


# *******************************************************

show_data_options = {
    1: 'Partial view',
    2: 'Full view'
}


def print_show_data_menu():
  """Print menu on screen."""
  print("\n")
  for key in show_data_options.keys():
    print("--------------------------------------")
    print(key, '--', show_data_options[key])
    print("--------------------------------------")
  


# *******************************************************

fal_menu_options = {
    1: 'Display details of failed students in Math',
    2: 'Display details of failed students in English',
    3: 'Display details of failed students in Electronics',
    4: 'Display details of students who have failed more than one subject',
    5: 'Exit'
}


def print_fal_menu():
  """Print menu on screen."""
  print("\n")
  for key in fal_menu_options.keys():
    print("-----------------------------------------------------------------------------")
    print(key, '--', fal_menu_options[key])
    print("-----------------------------------------------------------------------------")
  
# *******************************************************


avreg_menu_options = {
    1: 'Student Average',
    2: 'Class Average',
    3: 'Math Class Average',
    4: 'English class Average',
    5: 'Electronics class Average',
    6: 'Outstanding Students',
    7: 'Exit'
}


def print_avreg_menu():
  """Print menu on screen."""
  print("\n")
  for key in avreg_menu_options.keys():
    print("--------------------------------------")
    print(key, '--', avreg_menu_options[key])
    print("--------------------------------------")
  


   
# ***************************************************************
# ***************************************************************




# ***************************************************************

# ******************** Calculate student average ****************


def student_average_alon(student_math_grade, student_eng_grade, student_elect_grade):
  return float((int(student_math_grade) + int(student_eng_grade) + int(student_elect_grade)) / 3)

###
# ******** Calculating the number of failures per student ********
###

def false_amount(student_math_grade, student_eng_grade, student_elect_grade):
  count = 0
  if int(student_math_grade)  <= 54 :
    count += 1
  if int(student_eng_grade)   <= 54 :
    count += 1
  if int(student_elect_grade) <= 54 :
    count += 1
  return str(count)

# *******************************************************
# ***************************************************************



# ******************* Option 1 - Obtain student information ********************

# 1 --main_menu
def option1():

  if len(students_db) == 25: 
    # Check if the number of students has reached 25
    print("The student quota is full")
    return  # Out of the system

  else:
    print("--------------------------------------------------------------------")
    print("Please enter the following details:\n")

    while True:      
      student_id = input("Please insert the student's ID card: ")
      if student_id in students_db:   
          print('A student is already in the system\n')
          continue
      elif (len(student_id) != 9):   
        print("ID must be at least 9 numbers\n")
        continue                     
      else:
          break

# *********** After receiving id continue receiving variables ***********

    while True:
      student_name = input("Please enter the student's first name: ")
      if not student_name:
          print("The student's first name cannot be empty\n")
      else:
          break

    while True:
      student_lastname = input("Please enter the student's last name: ")
      if not student_lastname:
          print("The student's last name cannot be blank\n")
      else:
          break

    while True:
      student_cell = input("Please enter the student's phone number: ")
      if not re.findall(r"[\d]{3}-[\d]{3}-[\d]{4}", student_cell): 
          print("Enter only numbers in the format of 000-000-0000 \n")
          continue
      else:
          break

    while True:
      student_email = input("Please enter the student's email address: ")
      if not re.search(regex, student_email):  
          print("Invalid email address Please try again in the format (xxx@xxx.xxx) \n ")
      else:
          break

    while True: 
      try:
        student_math_grade = int(input("Please enter a student's math grade: "))
        if int(student_math_grade) < 40 or int(student_math_grade) > 100:
          raise ValueError
        break
      except ValueError:
        print("A math grade must be between 40 to 100\n")
           
    while True:
      try:
        student_eng_grade = input("Please enter the student's English grade: ")
        if int(student_eng_grade) < 40 or int(student_eng_grade) > 100:
          raise ValueError
        break 
      except ValueError:
        print("An English grade must be between 40 and 100\n")
          
    while True:
      try:
        student_elect_grade = input("please enter electronics grade:")
        if int(student_elect_grade) < 40 or int(student_elect_grade) > 100:
          raise ValueError
        break
      except ValueError:
        print("Electronics grade should be between 40 to 100")


    student_avg = student_average_alon(student_math_grade, student_eng_grade, student_elect_grade)
    student_avg = "%.2f" % student_avg
    print("Average student: " + student_avg)

    student_false_amount = false_amount(student_math_grade, student_eng_grade, student_elect_grade)
    print("Number of failures: " + student_false_amount)
    print("--------------------------------------------------------------------\n")

    




    student_data = {'name': student_name, 'lastname': student_lastname, 'cell': student_cell, 'email': student_email,
                    'math': student_math_grade, 'eng': student_eng_grade, 'elect': student_elect_grade, 'avg': student_avg, 'false_amount': student_false_amount}

    students_db[student_id] = student_data

    print(" ** Finish absorbing student data and return to the menu **\n")
    return
#******************************************************************************


# **Option 2 - Functions for deleting and changing a student from the list*****

# ******* Function for deleting a student from the list ***********************

# 1 --option2()
def del_student_details():
  if students_db == {}: 
    print("The list is empty. Please enter a student\n")
    print("back to menu\n")
    return
  else:
    print("Deleting student information\n")
    print("List of IDs: ")
    print("-------------")
    for key in students_db.keys():
      print(key) # print id list
    print("-------------")

    while True:
      del_id = str(input("Please enter the thesis of the user you want to delete: "))
      if (len(del_id) != 9):
        print("ID must be at least 9 numbers\n")
        continue
      if del_id not in students_db:  
        print('A student does not exist in the system\n')
        continue                  
      else:    
        for key in students_db.keys():
          if del_id != key:
            continue
          elif del_id == key:
            print("If you're sure you want to delete " + del_id + "?\n")
            yes_no = input("Please indicate 'yes' or 'no': ") 
            if yes_no == "yes":
              del students_db[del_id]
              print(del_id + " Deleted \n")
              break
            else:
              print("Not deleted")
              print('back to menu\n')
              break
          break
      break
    

#*********************************************************

#************** Function for changing student details ****

# 2 --option2()
def updating_student_details():
  if students_db == {}: 
    print("The list is empty. Please enter a student\n")
    print("back to menu\n")
    return
  else:
    print("--------------------------------------------------------------------")
    print("Change student details\n")
    while True:

      print("List of IDs: ")
      print("-------------")
      for key in students_db.keys():
        print(key) # print id list
      print("-------------")

      change_id = str(input("Please enter the the id of the user you want to change: "))
      if (len(change_id) != 9):
        print("ID must be at least 9 numbers\n")
        continue
      if change_id not in students_db:  
        print('A student does not exist in the system\n')
        continue                  
      else:
        for key in students_db.keys(): 
          if change_id != key:
            continue
          elif change_id == key:
            print("Are you sure you want to change your ID " + change_id + "?\n")
            yes_no = input("Please indicate 'yes' or 'no': ") 
            if yes_no == "yes":
              new_id = str(input("Insert a new ID\n"))

              # set the new id instead the old one

              old_key = change_id
              students_db[new_id] = students_db.pop(old_key)

              # start getting new value into the new id.

              while True:
                students_db[new_id]["name"] = input("Please enter the new student's first name: ")
                if not students_db[new_id]["name"]:
                    print("The student's first name cannot be empty\n")
                else:
                    break

              while True:
                students_db[new_id]["lastname"] = input("Please enter the new student's last name: ")
                if not students_db[new_id]["lastname"]:
                  print("The student's last name cannot be blank\n")
                else:
                    break

              while True:
                students_db[new_id]["cell"] = input("Please enter the new student's phone number: ")
                if not re.findall(r"[\d]{3}-[\d]{3}-[\d]{4}", students_db[new_id]["cell"]):
                  print("Enter only numbers in the format of 000-000-0000 \n")
                  continue
                else:
                    break

              while True:
                students_db[new_id]["email"] = input("Please enter the new student email address: ")
                if not re.search(regex, students_db[new_id]["email"]):  
                  print("Invalid email address Please try again in the format (xxx@xxx.xxx) \n ")
                else:
                    break

              while True:
                try:
                  students_db[new_id]["math"] = int(input("Please enter a student new math grade: "))
                  if int(students_db[new_id]["math"]) < 40 or int(students_db[new_id]["math"]) > 100:
                    raise ValueError
                  break
                except ValueError:
                  print("A math grade must be between 40 to 100\n")
                    
                    
              while True:
                try:
                  students_db[new_id]["eng"] = input("Please enter the student English grade: ")
                  if int(students_db[new_id]["eng"]) < 40 or int(students_db[new_id]["eng"]) > 100:
                    raise ValueError
                  break
                    
                except ValueError:
                  print("An English grade must be between 40 and 100\n")
                    

              while True:
                try:
                  students_db[new_id]["elect"] = input("Please enter the student electronics grade: ")
                  if int(students_db[new_id]["elect"]) < 40 or int(students_db[new_id]["elect"]) > 100:
                    raise ValueError
                  break
                except ValueError:
                  print("Electronics grade must be between 40 and 100\n")
                    

              student_avg_new = student_average_alon(students_db[new_id]["math"], students_db[new_id]["eng"], students_db[new_id]["elect"])
              student_avg_new = "%.2f" % student_avg_new
              students_db[new_id]["student_avg"] = student_avg_new
              print("Average student: " + student_avg_new)

              student_false_amount_new = false_amount(students_db[new_id]["math"], students_db[new_id]["eng"], students_db[new_id]["elect"])
              students_db[new_id]["false_amount"] = student_false_amount_new
              print("Number of failures: " + student_false_amount_new)
              print("\n ** Finish absorbing student data and return to the menu **\n")
              print("--------------------------------------------------------------------\n")
              

            else: 
              print(" Not change")
              print('back to menu\n')
              break
          break
      break         
# ***********************************************************


# 2 --main_menu
def option2():

  if students_db == {}: 
    print("The list is empty. Please enter a student\n")
    return
  else:
    while True:
      option = ''
      print_post_menu()

      try:
        option = int(input('Please enter your choice from 1 to 3: '))
        print('\n')
      except ValueError:
        print('Wrong Input, Please enter a number...\n')

      if option == 1:
        del_student_details()

      elif option == 2:
        updating_student_details()

      elif option == 3:
        print('Thank you \nBack to the main menu\n')
        break

      else:
        print('Incorrect value Please enter a value between 1 to 3')

#***********************************************************

#*************************************************************************


# ********* Part 3 - Partial / full printing of the students *************


# 1 --option3()
def part_show(): # Partial printing
  for key, value in students_db.items():
    print("-------------------------------")
    print(key + " " + value["name"] + " " + value["lastname"] ) 
    print("-------------------------------")
  return

# 2 --option3()
def full_show(): # full printing
  for key, value in students_db.items():
    print("----------------------------------")
    print(key)
    print(str(value["name"]) + " " + str(value["lastname"]) + " " + str(value["cell"]))
    print(str(value["email"])) 
    print("Math grade: " + str(value["math"]))
    print("English grade: " + str(value["eng"])) 
    print("Electronics grade: " + str(value["elect"])) 
    print("average: " + str(value["avg"])) 
    print("Number of failures: " + str(value["false_amount"])) 
    print("----------------------------------")
  return



# 3 --main_menu
def option3():
  if students_db == {}: 
    print("The list is empty. Please enter a student\n")
    return
  else:
    while True:
      option = ""
      print_show_data_menu() 

      try:
        option = int(input('Please enter your choice from 1 to 2: '))
        print('\n')
      except ValueError:
        print('Wrong Input, Please enter a number...')
      
      if option == 1:
        part_show()
        print('Thank you \nBack to the main menu\n')
        break
      elif option == 2:
        full_show()
        print('Thank you \nBack to the main menu\n')
        break
      else:
        print('Incorrect value Please enter a value between 1 to 2\n')


# **************************************************************************



# ***************** Part 4 - Viewing Failed Details ************************


# 1 --option4()
def show_false_math():
  count = 0
  for key, value in students_db.items():
    if int(value["math"]) < 54:
      count += 1
      print("---------------------------------------------------")
      print(key + " " + value["name"] + " " + value["lastname"] ) 
      print("Grade in mathematics: " + str(value["math"])) 
      print("---------------------------------------------------")
  print("\n")
  if count == 0:
    print("Not find Failed student in Math\n")

# 2 --option4()
def show_false_eng():
  count = 0
  for key, value in students_db.items():
    if int(value["eng"]) < 54:
      count += 1
      print("---------------------------------------------------")
      print(key + " " + value["name"] + " " + value["lastname"] ) 
      print("Grade in English: " + str(value["eng"])) 
      print("---------------------------------------------------")
  print("\n")
  if count == 0:
    print("Not find Failed student in English\n")

# 3 --option4()
def show_false_elect():
  count = 0
  for key, value in students_db.items():
    if int(value["elect"]) < 54:
      count += 1
      print("----------------------------------")
      print(key + " " + value["name"] + " " + value["lastname"] ) 
      print("Grade in Electronics: " + str(value["elect"])) 
      print("----------------------------------")
  print("\n")
  if count == 0:
    print("Not find Failed student in Electronics\n")

# 4 --option4()
def show_false_more_one():
  count = 0
  for key, value in students_db.items():
    if int(value["false_amount"]) > 0:
      count += 1
      print("---------------------------------------------------")
      print(key + " " + value["name"] + " " + value["lastname"] + "\n")
      print("Number of failures: " + str(value["false_amount"])) 
      if int(value["math"]) < 54:
        print("Failed in math: " + str(value["math"])) 
      if int(value["eng"]) < 54:
        print("Failed in English: " + str(value["eng"])) 
      if int(value["elect"]) < 54:
        print("Failed in electronics: " + str(value["elect"])) 
      print("---------------------------------------------------")
  print("\n")
  if count == 0:
    print("Not find student that have Failed. \n")



#******************** Details fail menu **************************

# 4 --main_menu()
def option4():
  if students_db == {}:  
    print("The list is empty. Please enter a student\n")
    return
  else:
    while True:
      option = ''
      print_fal_menu()

      try:
        option = int(input('Please enter your choice from 1 to 5: '))
        print('\n')
      except ValueError:
        print('Wrong Input, Please enter a number...')

      if option == 1:
        show_false_math() 

      elif option == 2:
        show_false_eng()

      elif option == 3:
        show_false_elect()

      elif option == 4:
        show_false_more_one()

      elif option == 5:
        print('Thank you \nBack to the main menu\n')
        break
      else:
        print('Incorrect value Please enter a value between 1 to 5\n')

# **************************************************************************


# ***************** Part 5 - Viewing Averages Details **********************


# 1 --option5()
def student_average():
  print("List of IDs: ")
  print("-------------")
  for key in students_db.keys():
    print(key) # print id list
  print("-------------")

  while True: 
    avg_id = str(input("Please enter the ID of the user you want to check average: "))
    avg = 0
    for key, value in students_db.items(): 
      if avg_id != key:
        continue
      elif avg_id == key:
        print("---------------------------------------")
        print(key + " " + value["name"] + " " + value["lastname"] + " " + value["avg"])
        print("---------------------------------------\n")
      else:
        print("not find \n")
        break
      break
    break

# 2 --option5()
def class_average():
  while True:
    avg, class_avg = 0, 0
    for key, value in students_db.items(): 
      avg  += float(value["avg"])
    class_avg = (avg / len(students_db))
    class_avg = "%.2f" % class_avg
    print("---------------------------")
    print("Class average: " + str(class_avg))
    print("---------------------------\n")
    break

# 3 --option5()
def math_class_average():
  while True:
    math_avg, class_avg = 0, 0
    for key, value in students_db.items(): 
      math_avg  += float(value["math"])
    class_avg = (math_avg) / len(students_db)
    class_avg = "%.2f" % class_avg
    print("-----------------------------------------")
    print("Class average grade in math: " + str(class_avg))
    print("-----------------------------------------\n")
    break

# 4 --option5()
def english_class_average():
  while True:
    eng_avg, class_avg = 0, 0
    for key, value in students_db.items(): 
      eng_avg += float(value["eng"])
    class_avg = (eng_avg) / len(students_db)
    class_avg = "%.2f" % class_avg
    print("------------------------------------------")
    print("Class average grade in english: " + str(class_avg))
    print("------------------------------------------\n")
    break

# 5 --option5()
def average_class_electronics():
  while True:
    elect_avg, class_avg = 0, 0
    for key, value in students_db.items(): 
      elect_avg += float(value["elect"])
    class_avg = (elect_avg) / len(students_db)
    class_avg = "%.2f" % class_avg
    print("----------------------------------------------")
    print("Class average grade in electronics: " + str(class_avg))
    print("----------------------------------------------\n")
    break

# 6 --option5()
def avg_outstanding():
  print("Details of students whose average is greater than 95: ")
  while True:
    avg = 0
    for key, value in students_db.items(): 
      if float(value["avg"]) >= 95.0:
        avg = float(value["avg"])
        print("-----------------------------------------")
        print(key)
        print("The name of the outstanding: " + value["name"])
        print("Average: " + str(avg))
        print("-----------------------------------------\n")
      else:
        continue
    if avg == 0:
      print("Not find outstanding Students\n")
      break
    break
# ************************************************************

# **************** Average details menu ****************************

# 5 --main_menu() 
def option5():
  if students_db == {}: 
    print("The list is empty. Please enter a student\n")
    return
  else:
    while True:
      option = ''
      print_avreg_menu()

      try:
        option = int(input('Please enter your choice from 1 to 7: '))
        print('\n')
      except ValueError:
        print('Wrong Input, Please enter a number...')

      if option == 1:
        student_average() 

      elif option == 2:
        class_average()

      elif option == 3:
        math_class_average()

      elif option == 4:
        english_class_average()

      elif option == 5:
        average_class_electronics()

      elif option == 6:
        avg_outstanding()

      elif option == 7:
        print('Thank you \nBack to the main menu\n')
        break

      else:
        print('Incorrect value Please enter a value between 1 to 7\n')

# **************************************************************************
# **************************************************************************

# **************** main menu ****************************

def main_menu():
  while True:
    option = ''
    print_menu()  
    try:
      option = int(input('Please enter your choice from 1 to 6: '))
    except ValueError:
        print('Wrong Input, Please enter a number...')

    if option == 1:
      option1()
      
    elif option == 2:
      option2()

    elif option == 3:
      option3()

    elif option == 4:
      option4()

    elif option == 5:
      option5()

    elif option == 6:
      print('Thank you AND good bye.')
      break
    
    else:
      print('Incorrect value Please enter a value between 1 to 6.\n')

# ************************************************************


def main():
  """Application main program."""
  main_menu()

# ***** START *****

if __name__ == "__main__":
  main()

# ************************************************************
# ********************** END *********************************
# ************************************************************