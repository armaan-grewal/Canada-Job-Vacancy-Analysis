#!/usr/bin/env python3

import sys
import csv
import matplotlib.pyplot as plt
import numpy as np

def empty_vacancy_dict():
    return {
        'No education required': 0,
        'HS diploma': 0,
        'non-uni certificate': 0,
        "Diploma below bachelor's": 0,
        "Bachelor degree's": 0,
        "Diploma above bachelor's": 0
    }



def parser(namedata_reader, rates, location):
     #this variable is used to check if province is valid
    province_checker= 0

    #parses through the csv file row by row, this is for the FIRST LOCATION
    for row_data_fields in namedata_reader:

        # Give all of the fields better names, and make sure that the numeric field is stored as an integer, for this data we only need
        #GEO, value and job vacancy Job_vacancy_characteristics 
        GEO = row_data_fields[1]
        Job_vacancy_characteristics = row_data_fields[4]
        value = (row_data_fields[12])
        stats = row_data_fields[5]

        #to only include values from the province selected
        if location == GEO:

            #update value to tell us province exists
            province_checker += 1

            if stats == "Job vacancies":
                #check if the string is empty
                if not value:  
                    continue

                else:
                    #cast as int
                    value = int(row_data_fields[12])
                
                #now check for each education level and add to dictonary according to which level it is, this dict will be used to graph
                if Job_vacancy_characteristics == "No minimum level of education required":
                    rates['No education required'] += value
                

                elif Job_vacancy_characteristics == "High school diploma or equivalent":
                    rates['HS diploma'] += value

                
                elif Job_vacancy_characteristics == "Non-university certificate or diploma":
                    rates['non-uni certificate'] += value

                elif Job_vacancy_characteristics == "University certificate or diploma below bachelor's level":      
                    rates["Diploma below bachelor's"] += value

                elif Job_vacancy_characteristics == "Bachelor's degree": 
                    rates["Bachelor degree's"] += value

                elif Job_vacancy_characteristics == "University certificate, diploma or degree above the bachelor's level": 
                    rates["Diploma above bachelor's"] += value


    #province does not exist
    if province_checker == 0:  
        return -1
    
    return rates
    


def education_vacancy(location_1, location_2):

     #these two dictionaries will hold the values for education level and their vacancy number for both provinces
    vacancy_rates_1 = empty_vacancy_dict()
    vacancy_rates_2 = empty_vacancy_dict() 

    #name of file for education vacancy
    namedata_filename = "educationLevel.csv"


    #check for error
    try:
        namedata_fh = open(namedata_filename, encoding="utf-8-sig")

    except IOError as err:
        print("Unable to open names file '{}' : {}".format(
                namedata_filename, err), file=sys.stderr)
        sys.exit(1)

    #as csv
    namedata_reader = csv.reader(namedata_fh)
    next(namedata_reader)   #skip header

    #call helper function to parse and get the needed info into variables
    vacancy_rates_1 = parser(namedata_reader, vacancy_rates_1, location_1)

    if (vacancy_rates_1 == -1):
        print("First province is not valid, please input a valid province")
        return -1    

    #close file
    namedata_fh.close()

 

    #open agin and check for error
    try:
        namedata_fh = open(namedata_filename, encoding="utf-8-sig")

    except IOError as err:
        print("Unable to open names file '{}' : {}".format(
                namedata_filename, err), file=sys.stderr)
        sys.exit(1)

    namedata_reader = csv.reader(namedata_fh)
    next(namedata_reader)   #skip header

    #call helper function to parse and get the needed info into variables
    vacancy_rates_2 = parser(namedata_reader, vacancy_rates_2, location_2)
    if (vacancy_rates_2 == -1):
        print("Second province is not valid, please input a valid province")
        return -1
    
    #close file
    namedata_fh.close()



    #now its time to plot the values of the two locations
    #for height value, this puts value of each education level, into custom_height
    custom_height_1 = [int(i[1]) for i in vacancy_rates_1.items()]
    custom_height_2 = [int(k[1]) for k in vacancy_rates_2.items()]

 
    #using numpy library, use np.arange which rearragnes and creates array within a range 
    #in this case it generates an array from 0 to the number of (key,value) pairs there are minus 1
    x_position = np.arange(len(vacancy_rates_1.items()))

    #set values to specifications for the graph
    plt.bar(x_position,height = custom_height_1, width=0.2, color = 'royalBlue', label = location_1)     #for first province

    #move x_position over 0.2 so bars get displayed right beside the first province
    plt.bar(x_position + 0.2,height = custom_height_2, width=0.2 , color = 'red', label = location_2)           #for second province

    plt.xticks(range(len(vacancy_rates_1)), vacancy_rates_1.keys())

    #for fonts for title and x,y-axis
    header_Font = {'fontname':'Comic Sans MS'}
    axis_Font = {'fontname':'Helvetica'}

    #give titles
    plt.xlabel('Education Level', axis_Font)
    plt.ylabel('Total Job Vacancies', axis_Font)
    plt.title(f"2023 Comparation of {location_1} and {location_2}'s Job Vacancies by Education Level", header_Font)

    #create legend, it will create it based on the labels given in plt.bar
    plt.legend()

    plt.show()

    return 1



def main():

    return_val = 0
    #function only returns 1 when valid province is inputted, if return is not 1, keep looping until it is 
    while(return_val != 1):

        #ask users for locations they would like to compare
        location_1 = input("Input first province: ").strip().title()
        location_2 = input("Input second province: ").strip().title()

        #if it returns -1, this means location invalid, so it will loop again
        return_val = education_vacancy(location_1, location_2)

    
            
if __name__ == "__main__":
    main()
