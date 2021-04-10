import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure(figsize=(6,4))
name = ['date', 'open', 'high', 'low', 'close', 'volume', 'adj_close']
df = pd.read_csv('9972', names=name, parse_dates=['date'], index_col='date')
df.head()
df['adj_close'].plot()
plt.title("stock price (アルテック)")
plt.tight_layout()
plt.show()
