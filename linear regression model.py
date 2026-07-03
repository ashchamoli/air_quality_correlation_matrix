print("\n Linear Regression for PM2.5")

X = df_seasonal[['Temperature_C', 'Humidity_percent', 'WindSpeed_kmh']]
y_pm25 = df_seasonal['PM2.5']

model_pm25 = LinearRegression()
model_pm25.fit(X, y_pm25)

print(f"PM2.5 Intercept: {model_pm25.intercept_:.2f}")
print(f"PM2.5 Coefficients: Temperature={model_pm25.coef_[0]:.2f}, Humidity={model_pm25.coef_[1]:.2f}, Wind Speed={model_pm25.coef_[2]:.2f}")
print(f"PM2.5 R-squared: {model_pm25.score(X, y_pm25):.2f}")

print("\n Linear Regression for PM10")

y_pm10 = df_seasonal['PM10']

model_pm10 = LinearRegression()
model_pm10.fit(X, y_pm10)

print(f"PM10 Intercept: {model_pm10.intercept_:.2f}")
print(f"PM10 Coefficients: Temperature={model_pm10.coef_[0]:.2f}, Humidity={model_pm10.coef_[1]:.2f}, Wind Speed={model_pm10.coef_[2]:.2f}")
print(f"PM10 R-squared: {model_pm10.score(X, y_pm10):.2f}")
