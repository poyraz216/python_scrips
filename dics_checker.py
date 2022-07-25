

import os
stream = os.popen('ssh theadmin@192.168.1.65, "df -h /"')

output = stream.read()
print(output)