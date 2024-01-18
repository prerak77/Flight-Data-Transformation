"""Libraries"""
import pandas as pd
from helper import remove_punctuation, remove_numbers
"""*********"""

data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'


"""Cleaned final output should look like

Airline Code    ,DelayTimes,    FlightCodes,    To,         From
Air Canada      ,[21, 40],      20015,          WATERLOO,   NEWYORK

"""

# Split the data into a list that stores each individual line
lines = data.split("\n")
# the splits function creats an additional
# blank string at the end and it needs to be removed
lines.pop()


# extract the column headings from the string
column_heading = lines[0]
column_heading = column_heading.split(";")
lines.pop(0)

# need to make to_from into 2 seperate column
destination_column = column_heading.pop()
destination_column = destination_column.split("_")
column_heading.extend(destination_column)


# create a dataframe to store all the transformed data
data_df = pd.DataFrame(columns=column_heading)

# variable to that check if it is the first line of data
# to store the first flight code
first_line = True
# looping through all the data to add it to the dataframe
for line in lines:
    line = line.split(";")
    if first_line:
        first_flight_code = int(float(line[2]))
        first_line = False

    # cleaning the airline codes
    airline_code = line[0]
    airline_code = remove_punctuation(airline_code)
    airline_code = remove_numbers(airline_code)
    airline_code = airline_code.strip()

    delay_time = line[1]

    # cleaning the flight codes
    flight_code = first_flight_code
    first_flight_code += 10

    # extracting the to and from data
    to_from = line[3]
    to_from = to_from.split("_")

    To = to_from[0]
    To = To.upper()

    From = to_from[1]
    From = From.upper()

    transformed_line = [airline_code, delay_time, flight_code, To, From]

    # Add the new row to the DataFrame
    data_df.loc[len(data_df)] = transformed_line

data_df.to_csv("transformed_flight_data.csv", index=False)
