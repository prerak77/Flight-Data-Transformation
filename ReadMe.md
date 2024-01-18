# Flight Data Transformation

This project transforms raw flight data into a more readable and user-friendly format using pandas and string manipulation in Python. The transformed data is stored in a pandas DataFrame with relevant columns such as 'Airline Code', 'DelayTimes', 'FlightCodes', 'To', and 'From'. The final dataset is then saved as a CSV file for further analysis.

## Instructions

To run the code, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/flight-data-transformation.git
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

## Output

The final transformed data is saved in a CSV file named `transformed_flight_data.csv`. This file contains the organized flight information, making it easier for further analysis and exploration.

Feel free to reach out if you have any questions or suggestions!

---

Make sure to replace "your-username" with your actual GitHub username in the clone URL. Additionally, you may want to update the README with more specific details about the project or instructions if needed.