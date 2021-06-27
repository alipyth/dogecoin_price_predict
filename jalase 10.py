import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
bitcoin = pd.read_csv('DOGE-USD.csv')
plt.figure(figsize = (12, 7))
plt.plot(bitcoin["Date"], bitcoin["Close"], color='goldenrod', lw=2)
plt.title("Dogecoin Price over time", size=25)
plt.xlabel("Time", size=20)
plt.ylabel("$ Price", size=20)
bitcoin.isnull().sum()
bitcoin.dropna(inplace=True)
required_features = ['Open', 'High', 'Low', 'Volume']
output_label = 'Close'
x_train, x_test, y_train, y_test = train_test_split(bitcoin[required_features],bitcoin[output_label],test_size = 0.3)
model = LinearRegression()
model.fit(x_train, y_train)
model.score(x_test, y_test)
future_set = bitcoin.shift(periods=30).tail(30)
prediction = model.predict(future_set[required_features])
plt.figure(figsize = (12, 7))
plt.plot(bitcoin["Date"][-400:-60], bitcoin["Open"][-400:-60], color='goldenrod', lw=2)
plt.plot(future_set["Date"], prediction, color='deeppink', lw=2)
plt.title("Doge Price", size=25)
plt.xlabel("Time", size=20)
plt.ylabel("$ Price", size=20)
plt.show()
