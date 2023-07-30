import requests
import pandas as pd
import matplotlib.pyplot as plt

params = {
    'access_key': '836da367eee2299450ab26e2784cd900',  # Replace with your actual API key
    'query': 'New York',
    'historical_date': '2015-01-21',
    'hourly': '1'
}

api_result = requests.get('https://api.weatherstack.com/historical', params)
response = api_result.json()

try:
    # Extract hourly temperature data
    temperature_data = response['historical']['2015-01-21']['hourly']

    # Convert the data into a pandas DataFrame for easier manipulation
    df = pd.DataFrame(temperature_data)

    # Convert the 'time' column to numeric format
    df['time'] = df['time'].astype(int) // 100  # Convert time to hours for plotting

    # Plot the hourly temperature data using matplotlib
    plt.figure(figsize=(10, 6))
    plt.plot(df['time'], df['temperature'], marker='o')
    plt.xlabel('Time (Hours)')
    plt.ylabel('Temperature (°C)')
    plt.title('Hourly Temperature in New York on 2015-01-21')
    plt.grid(True)
    plt.xticks(df['time'])
    plt.tight_layout()

    # Display the chart
    plt.show()

except KeyError:
    print("Hourly temperature data not available for the specified date and location.")
