import pandas as pd
import paramiko
import schedule
import time

def transfer():
	# Update the next three lines with your
	# server's information
	host = "131.252.223.182"
	username = "hank"
	password = "Jbcasf18"

	# Set up ssh connection with server
	client = paramiko.client.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(host, username=username, password=password)
	print("Connection made.")

	# Read in file with data to be transferred
	file = pd.read_csv('/home/pi/Water_heater_SCADA_system/Water_heater_SCADA_system/Water_heater_SCADA_system/Water_heater_SCADA_system/Water_heater_data.csv', header=None)

	# Copy last 15 lines of data
	row_data = file.tail(15)
	print(row_data)

	# Set remote path directory
	remotepath = str(file)

	# sftp
	#sftp = client.open_sftp()
	#sftp.putfo(file, remotepath, callback=None, confirm=True)
	#sftp.close()
	#print("File transfer complete")
	client.close()

transfer()
schedule.every(15).minutes.do(transfer)

while True:
	schedule.run_pending()
	time.sleep(1)

