import paramiko

# Update the next three lines with your
# server's information

host = "131.252.223.182"
username = "hank"
password = "Jbcasf18"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
print("Connection made.")

localpath = "/home/pi/sample.txt"
remotepath = "/home/hank/sample.txt"
sftp = client.open_sftp()
sftp.put(localpath, remotepath, callback=None, confirm=True)
sftp.close()
print("File transfer complete")
client.close()



