import pandas as pd
from datetime import datetime
import pytz
import numpy as np
import schedule
import time

def log_entry():

	# Method to read a specific (last) row and grab specific element from a .csv file using pandas
	file = pd.read_csv('/home/pi/josh/CTA_EWH/build/debug/log.csv',header=None)

	# grab instantaneous power reading
	power_read = file.iat[-1,10]
	print(power_read)

	# timestamp
	time = datetime.now(pytz.timezone('America/Los_Angeles'))
	formatted_time = time.strftime('%Y-%m-%d %H:%M:%S %Z')

	# sum of power used for the last 15 min
	#power_15 = (file.iloc[-15:,10])
	#pf = pd.DataFrame(power_15)
	#for i, row in pf.iterrows():
		#value = pf/60
	#print(value)
	#sum_power_15 = np.sum(value)
	#print(sum_power_15.dtypes)

	# write row data
	row_data = [{
		'Time' : str(formatted_time),
		'Water volume last 15 min (gal)' : 0,
		'Water volume current day (gal)' : 0,
		'Water volume consumed total life (gal)' : 0,
		'Instantaneous Power (W)' : str(power_read),
		'Energy consumed last 15 min (Wh)' : 0,
		'Energy consumed current day (wh)' : 0,
		'Energy consumed total life (kWh)' : 0
	}]

	# write row data to data frame
	df = pd.DataFrame(row_data)
	# append data frame to .csv file
	df.to_csv("Water_heater_data.csv", mode='a', header=False, index=False)

	print("Data successfully logged")

schedule.every(5/60).minutes.do(log_entry)

while True:
	schedule.run_pending()
	time.sleep(1)

