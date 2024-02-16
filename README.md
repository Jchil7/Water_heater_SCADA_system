# Water_heater_SCADA_system
The purpose of this system is to collect data from a client that is connected to a water heater to measure the power and water usage. The water usage is logged via a fluid flow sensor and is logged to a file in the raspberry pi directory /home/pi/josh/Water_heater_SCADA_system/Water_heater_SCADA_system.

The data from the water usage files and the energy usage logs will be combined together in one data file. The combined data file will be stored on the Pi and transferred to the Unraid server once a day.

A network connection must be made to the host server from the client server. 

Edit the code "data_sftp_2.py" to specify the local file path and remote file path. 


Run 'Water_heater_data_tr.py' to perform water draw, log the data, and transfer the data to desired location. This program runs two other python programs in succession to immediately process the data and transfer the file via sftp. 

Test line
