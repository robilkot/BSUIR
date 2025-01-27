import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_squared_error, r2_score, root_mean_squared_error

filename = 'Electric_Production.csv'
date_column = 'DATE'
result_column = 'Value'

df = pd.read_csv(filename, parse_dates=[date_column])

data = df[result_column].tolist()
data = pd.Series(np.asarray(data), index=pd.date_range(start='1/1/1985', periods=len(data), freq='ME'))

separator = int(len(df) * 0.93)
train_data = data[:separator]
test_data = data[separator:]

train_series = train_data
test_series = test_data

hw_model = statsmodels.tsa.holtwinters.ExponentialSmoothing(
    train_series,
    trend='add',
    seasonal='add',
    seasonal_periods=12
).fit()
forecast = hw_model.forecast(len(test_series))

mse = mean_squared_error(test_series, forecast)
rmse = root_mean_squared_error(test_series, forecast)
r2 = r2_score(test_series, forecast)

print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared (R²): {r2:.3f}")

plt.figure(figsize=(12, 6))
plt.plot(train_series, label="Train Data", color='blue')
plt.plot(test_series, label="Test Data", color='orange')
plt.plot(forecast, label="Forecast", color='green', linestyle='--')
plt.title("Electric consumption graph")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.show()

residuals = test_series - forecast

plt.figure(figsize=(12, 6))
plt.plot(residuals, label="Residuals", color='purple')
plt.axhline(0, color='red', linestyle='--', label="Zero Line")
plt.title("Residuals graph")
plt.xlabel("Date")
plt.ylabel("Residuals")
plt.legend()
plt.show()
