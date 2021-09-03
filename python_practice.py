# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])
    
# ## What is the score?
# score = int(input("What is your test score? "))

## Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >= 60:
#     print('Your grade is a D.')
# else:
#     print('Your grade is an F.')
    
##----------
##Membership Operaters -- in, not in

counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")
##Output: El Paso is not the list of counties

##----------
##Logical Operartors -- and, or, not

# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties.")
##Output: Arapahoe or El Paso is not in the list of counties.

##---------- 
##LOOPING

##for loop, as long as value is in list
#for county in counties:
#    print(county)

##while loop, set to a value threshold
#x = 0
#while x <= 5:
#    print(x)
#       x = x + 1

# #using "range" for looping inside the list
# for i in range(len(counties)):
#    print(counties[i])
# # i is used in the index here, the value inside range is the length count of items in counties (number of items in counties)

##---- PRACTICE
#libraries, data comes in key:value pairs
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# 2 Ways to get KEYS
# for county in counties_dict:
#     print(county)
# same as keys() - example
# for county in counties_dict.keys():
#     print(county)

# # Way to get VALUES
# for voters in counties_dict.values():
#     print(voters)

# # Way to get BOTH KEYS AND VALUES
# for county, voters in counties_dict.items():
#     print(f"The county of {county} has {voters} registered voters.")

# Pull Dictionaries out of list of dictionaries using for loops 
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_d in voting_data:
    print(county_d)
# try doing the same using RANGE

for i in range(len(voting_data)):
    print (i)

# using nested for loop just to get values or keys or both
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#getting the values of specific keys
for county_dict in voting_data:
    print(county_dict["registered_voters"])
