# Flight Data Transformation

This project transforms raw flight data into a more readable and user-friendly format using pandas and string manipulation in Python. The transformed data is stored in a pandas DataFrame with relevant columns such as 'Airline Code', 'DelayTimes', 'FlightCodes', 'To', and 'From'. The final dataset is then saved as a CSV file for further analysis.

## Instructions

To run the code, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/prerak77/Flight-Data-Transformation.git
   ```

2. Navigate to the project directory:

   ```bash
   cd flight-data-transformation
   ```

3. Run the main script:

   ```bash
   python main.py
   ```

## Libraries Used

- [pandas](https://pandas.pydata.org/): A powerful data manipulation and analysis library for Python.
- [string](https://docs.python.org/3/library/string.html): Python's built-in string manipulation module.

## Data Transformation

The provided code transforms raw flight data, originally in the form of a semicolon-separated string, into a structured and user-friendly DataFrame. Each row corresponds to a different flight, with columns such as 'Airline Code', 'DelayTimes', 'FlightCodes', 'To', and 'From'. The data is cleaned and formatted for better readability.

Airline Code,DelayTimes,FlightCodes,To,From
Air Canada,"[21, 40]",20015,WATERLOO,NEWYORK
Air France,[],20025,MONTREAL,TORONTO
Porter Airways,"[60, 22, 87]",20035,CALGARY,OTTAWA
Air France,"[78, 66]",20045,OTTAWA,VANCOUVER
Lufthansa,"[12, 33]",20055,LONDON,MONTREAL

## Output

The final transformed data is saved in a CSV file named `transformed_flight_data.csv`. This file contains the organized flight information, making it easier for further analysis and exploration.
