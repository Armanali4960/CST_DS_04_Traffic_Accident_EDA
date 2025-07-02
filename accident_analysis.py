import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("accident_data_sample.csv", parse_dates=['Start_Time'])

# Clean and prepare data
df['Hour'] = df['Start_Time'].dt.hour
df.dropna(subset=['Weather_Condition', 'Severity', 'Temperature(F)', 'Humidity(%)'], inplace=True)

# Set up plots
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Accidents by Hour
sns.countplot(x='Hour', data=df, ax=axs[0, 0])
axs[0, 0].set_title('Accidents by Hour')

# Plot 2: Severity vs Temperature
sns.boxplot(x='Severity', y='Temperature(F)', data=df, ax=axs[0, 1])
axs[0, 1].set_title('Severity vs Temperature')

# Plot 3: Weather Condition count
df['Weather_Condition'].value_counts().nlargest(10).plot(kind='bar', ax=axs[1, 0])
axs[1, 0].set_title('Top 10 Weather Conditions')

# Plot 4: Correlation Heatmap
sns.heatmap(df[['Temperature(F)', 'Humidity(%)', 'Visibility(mi)', 'Wind_Speed(mph)', 'Precipitation(in)']].corr(), annot=True, ax=axs[1, 1])
axs[1, 1].set_title('Weather Feature Correlation')

plt.tight_layout()
plt.savefig("output_charts.png")