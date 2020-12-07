#Protected

import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
Wifi_List = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]

for wifi in Wifi_List:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
    results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line]
    try:
        print(f'Name: {wifi} \t\t\t Password: {results[0]}')
    except IndexError:
        print(f'Name: {wifi} \t\t\t Password: Not Available')

#End
