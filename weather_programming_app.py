import requests
from bs4 import BeautifulSoup
import re
# Function to format city and state names for URL (replace spaces and make it lowercase)
def format_location(city, state):
    formatted_city = city.lower().replace(" ", "")
    formatted_state = state.lower().replace(" ", "")
    return formatted_city, formatted_state

# Get user input for city and state
city_input = input("Hello Ewok's, pick a city: ")
state_input = input("Great! Now pick a state (Make sure to abbreviate your state ex: TN(Tennessee) or OH(Ohio)): ")

# Format the input to fit the URL structure
formatted_city, formatted_state = format_location(city_input, state_input)

# Generate the URL for the specified city and state
url = f"https://www.wunderground.com/weather/us/{formatted_state}/{formatted_city}"

# Request the web page content
response = requests.get(url)
if response.status_code == 200:  # Check if the request was successful
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract relevant data from the page (adjust the tag/class based on actual HTML structure)
        # Extract relevant data from the page
    weather_data = soup.find('div', class_='current-temp')  # Example: Adjust to match Wunderground's page structure
    hi_lo = soup.find('div', class_='hi-lo')  # Finding the div containing high and low temperatures
    conditions = soup.find('div', class_='condition-icon')


        # What does r'\d+' do? It's a regular expression pattern. And it tells re.search() to look for one or more (+) digits (\d).'
    #high_temp.text.strip():  This provides the string in which re.search() will look for the pattern. The .strip() method removes any leading or trailing whitespace from the text.
    # In this case, re.search(r'\d+', high_temp.text.strip()) finds the first number (the temperature) in the high_temp text and returns it as part of a match object.
#         if high_temp_value:
#                 print(f"High Temperature: {high_temp_value.group()}")

#     if high_temp_value:
#         # Add the degree symbol (°) and "F" for Fahrenheit
#         print(f"High Temperature: {high_temp_value.group()}°F")
    if weather_data or hi_lo or conditions:
        print(f"Weather data for {city_input}, {state_input}")
        
        if weather_data:
            print(f"Current Temperature: {weather_data.text.strip()}")

        if hi_lo:
            # Use regex to extract all numeric temperature values
            temperatures = re.findall(r'\d+', hi_lo.text.strip())

            if len(temperatures) >= 2:
                # Assign high and low temperatures
                temp1 = int(temperatures[0])
                temp2 = int(temperatures[1])
                high_temp_value = max(temp1, temp2)
                low_temp_value = min(temp1, temp2)
                print(f"High Temperature: {high_temp_value}°F")
                print(f"Low Temperature: {low_temp_value}°F")
    if conditions:
            conditions_clean = re.sub(r'\d+°F', '', conditions.text.strip())  # Remove any numbers with °F from conditions
            print(f"Weather Conditions: {conditions_clean.strip()}")

    else:
        print(f"Couldn't find weather data for {city_input}, {state_input}")
else:
    print(f"Failed to retrieve data for {city_input}, {state_input}")

print(url)