# Water_heater_SCADA_system
The purpose of this system is to collect data from a client that is connected to a water heater to measure the power and water usage. The water usage is logged via a fluid flow sensor and can be logged to a file in a specific raspberry pi directory. Example: /home/pi/josh/Water_heater_SCADA_system/

The files in this repository perform different functions, but ultimately can be put together in one file that can perform part or all of the task of transferring data from the client back to the database server. There are ways to change how often the data gets logged and transferred back to the server. 

The data from the water usage files and the energy usage logs will be combined together in one data file. The combined data file will be stored on the Pi and transferred to the Unraid server once a day.

A network connection must be made to the host server from the client server. 

Edit the code "data_sftp_2.py" to specify the local file path and remote file path. 


Run 'Water_heater_data_tr.py' to perform water draw, log the data, and transfer the data to desired location. This program runs two other python programs in succession to immediately process the data and transfer the file via sftp. 


