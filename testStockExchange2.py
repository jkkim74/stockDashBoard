import FinanceDataReader as fdr
import matplotlib.pyplot as plt

# Set the start and end dates for the data
start_date = '2000-01-01'
end_date = '2023-02-16'

# Retrieve the Kospi index data with a monthly frequency
kospi = fdr.DataReader('KS11', start_date, end_date).resample('M').last()

# Retrieve the exchange rate data (KRW/USD) with a monthly frequency
exchange_rate = fdr.DataReader('USD/KRW', start_date, end_date).resample('M').last()

# Retrieve the cyclical component of the leading index data with a monthly frequency
cyclical = fdr.DataReader('ECI', start_date, end_date).resample('M').last()
print(cyclical)
# Create a figure and an axis object
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the Kospi index data on the axis object
ax.plot(kospi.index, kospi['Close'], label='KOSPI')

# Plot the exchange rate data on the axis object
ax.plot(exchange_rate.index, exchange_rate['Close'], label='USD/KRW')

# Plot the cyclical component of the leading index data on the axis object
ax.plot(cyclical.index, cyclical['Close'], label='ECI')

# Set the title and legend of the plot
ax.set_title('KOSPI, USD/KRW, and ECI')
ax.legend()

# Show the plot
plt.show()