from paramiko import SSHClient

ssh = SSHClient()
ssh.load_system_host_keys()
# more options found at https://docs.paramiko.org/en/stable/api/client.html
# ssh.connect(ip,port,username,password)
ssh.connect('192.168.1.65', username='theadmin', password='3608355')  # using ssh keys
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('df -h /')
outlines = ssh_stdout.readlines()
resp = ''.join(outlines)
print(resp)