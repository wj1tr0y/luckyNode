import subprocess
import time
import os
if __name__ == '__main__':
    cmd = 'nohup python3 -u luckyNode.py>luckyNode.log 2>&1 &'
    if not os.path.exists('.config_luckynode'):
        Authorization = input("请输入你的Authorization值：")
        with open('.config_luckynode', 'w') as f:
            f.write(Authorization)
    
    print('Starting backgroung servive...')
    print(cmd)
    subprocess.call(cmd, shell=True)
    print('Done')
