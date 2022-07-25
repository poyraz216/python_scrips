import paramiko

command = "df"

# Update the next three lines with your
# server's information

host = "192.168.1.65"
username = "theadmin"
password = "3608355"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
stdin, stdout, stderr = client.exec_command("df -h /")
print(stdout.read().decode())
client.close()