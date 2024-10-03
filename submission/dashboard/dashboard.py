import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load data
day_data = pd.read_csv('day.csv')
hour_data = pd.read_csv('hour.csv')

# Fill missing data
day_data.fillna(method='ffill', inplace=True)
hour_data.fillna(method='ffill', inplace=True)

# Add weekend indicator (1 for weekend, 0 for weekday)
day_data['weekend'] = day_data['weekday'].apply(lambda x: 1 if x >= 5 else 0)

# Business Question 1: Bike rentals on weekdays vs. weekends
usage_by_weekend = day_data.groupby('weekend')['cnt'].sum()

# Plot for Total Bike Rentals: Weekday vs Weekend
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x='weekend', y='cnt', data=day_data, estimator=sum, ax=ax1)
ax1.set_title('Total Penyewaan Sepeda: Hari Kerja vs Akhir Pekan')
ax1.set_xlabel('Akhir Pekan (1) vs Hari Kerja (0)')
ax1.set_ylabel('Total Penyewaan Sepeda')
ax1.set_xticks([0, 1])
ax1.set_xticklabels(['Hari Kerja', 'Akhir Pekan'])

# Business Question 2: Bike rentals by hour
hourly_usage = hour_data.groupby('hr')['cnt'].sum()

# Plot for Bike Rentals by Hour
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.lineplot(x='hr', y='cnt', data=hour_data, estimator=sum, ax=ax2)
ax2.set_title('Penyewaan Sepeda Berdasarkan Jam')
ax2.set_xlabel('Jam')
ax2.set_ylabel('Jumlah Penyewaan')
ax2.set_xticks(range(0, 24))

# Streamlit dashboard
st.title('Dashboard Penyewaan Sepeda')

st.subheader('1. Total Penyewaan Sepeda: Hari Kerja vs Akhir Pekan')
st.pyplot(fig1)

st.subheader('2. Penyewaan Sepeda Berdasarkan Jam')
st.pyplot(fig2)

st.write("Data Summary:")
st.write(day_data.describe())
st.write(hour_data.describe())
