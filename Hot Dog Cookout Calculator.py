
#math module needed for calucluations

import math

print("""                           
      
      
      
                          Welcome To The Hot Dog Cookout Calculator
      
      
                                 Created By: Geoffrey Chambers
                                 Intro to Python MDC COP1047C
                                 
                                                 
                                 
                                 
                                 """)
                                                 
print("""Let's Start Calculating!
      
      
      
      """)

#Assume hot dogs which we will call, sausages, come in packages of 10, and hot dog buns come in packages of 8

sausages_in_package = 10
buns_in_package = 8

#Ask the user to input the number of people attending the cookout and the number of hot dogs each person will be given.


people = int(input("    How Many People Are Attending Your Cookout?: "))

hotdogs_per_person = int(input("    How Many Hot Dogs Will Each Person Get: "))

input("""            
              
                        Cooking up your numbers!  
                  Press Enter to Take Them Off The Grill!
              
                
              """)

print("""Here Are Your Numbers, Hot Off the Grill:
      
      """)

# Multiply the number of hot dogs per person by how many are attending to get total number of hot dogs required for cook out. 

# Divide Total number of hot dogs required for cook out by number of buns and dogs in each package to give total number of dogs and buns required.

required_hotdogs = people * hotdogs_per_person
packages_sausage = required_hotdogs / sausages_in_package
packages_buns = required_hotdogs / buns_in_package

print(f"    You will need {math.ceil(packages_sausage)} packs of sausages.")
print(f"    You will need {math.ceil(packages_buns)} packs of buns.")

#Calculate remainder of dogs after allotment fulfilled

remaining_hotdogs = (math.ceil(packages_sausage) * sausages_in_package) - required_hotdogs

if remaining_hotdogs > 1:
    print(f'    You will have {remaining_hotdogs} left over sausages.')
elif remaining_hotdogs == 1:
    print("    You will have 1 left over sausage.")
elif remaining_hotdogs ==0:
    print("    You will have 0 left over sausages.")
    
#Calculate remainder of buns after allotment fulfilled    

remaining_buns = (math.ceil(packages_buns) * buns_in_package) - required_hotdogs

if remaining_buns > 1:
    print(f'    You will have {remaining_buns} left over buns.')
elif remaining_buns == 1:
    print("    You will have 1 left over bun.")
elif remaining_buns == 0:
    print("    You will have 0 left over buns.")


input("""              
                  Thanks for Using The Hot Dog Cookout Calculator
      
                              Press Enter to Exit """)