import paramiko

#command = "df"

# Update the next three lines with your
# server's information

host = "131.252.223.182"
username = "hank"
password = "Jbcasf18"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
#_stdin, _stdout,_stderr = client.exec_command("df")
sftp = client.open_sftp()
sftp.put("pi/home/josh/'Hello World!'", "home/hank/Downloads/'Hello World!'")
sftp.close()
print("File transfer complete")
client.close()



