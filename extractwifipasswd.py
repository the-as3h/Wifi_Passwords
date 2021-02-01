import subprocess
wifi_list=subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
wifi_name=[list.split(':')[1][1:-1] for list in wifi_list if "All User Profile" in list]
user_pass={}
for list in wifi_name:
    wifi_pass=subprocess.check_output(['netsh','wlan','show','profile',list,'key=clear']).decode('utf-8').split('\n')
    result=[res.split(':')[1][1:-1] for res in wifi_pass if "Key Content" in res]
    print(f'Name: {list} : {result}')
    user_pass[list]=result
print(user_pass)