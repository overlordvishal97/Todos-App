import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a pandas dataframe
data = pd.read_csv('data.csv.txt')

# Create a dictionary to map month names to their numerical values
month_map = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}

# Convert the month column to numerical values
data['month_num'] = data['index'].apply(lambda x: month_map[x.split(',')[0]])

# Filter out data that is not within the limit
current_month = 5
current_year = 2023
data = data[data['month_num'] >= current_month]
data = data[data['final'] <= 1]
data = data[data.apply(lambda x: x['month_num'] - current_month + 12 * (x['within_month'] == 0) <= x['final'], axis=1)]

# Melt the data to create a month column and a value column
melted = pd.melt(data, id_vars=['index', 'final'], value_vars=['within_month', 'within_2month', 'within_3month', 'within_4month', 'within_5month', 'within_6month', 'within_7month'], var_name='months', value_name='value')

# Convert the months column to numerical values
melted['months'] = melted['months'].apply(lambda x: int(x.split('_')[1].replace('month', '')))

# Calculate the year for each data point
melted['year'] = current_year + (melted['months'] - current_month) // 12

# Calculate the month for each data point
melted['month'] = ((melted['months'] - current_month) % 12) + current_month

# Calculate the months difference from May 2023
melted['months_diff'] = (melted['year'] - current_year) * 12 + (melted['month'] - current_month)

# Sort the data by month and year
melted.sort_values(['year', 'month'], inplace=True)

# Save the transformed data to a CSV file
melted.to_csv('transformed_data.csv', index=False)

# Read the transformed data
df = pd.read_csv("transformed_data.csv")

# Plot the line graph
plt.plot(df["months_diff"], df["value"])
plt.xlabel("Months Difference from May 2023")
plt.ylabel("Final Value")
plt.title("Final Value over Time")
plt.show()
