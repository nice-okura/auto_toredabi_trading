import datetime
import jsm

q = jsm.Quotes()

start_date = datetime.date(2018, 1, 1)

c = jsm.QuotesCsv()
c.save_historical_prices('9972', 9972, jsm.DAILY, start_date)
