'''
Copyright (c) 2022 Juan Carlos Bindez
This project is licensed under the MIT License.
'''

'''
Author: www.github.com/JuanBindez
Description: Loop In Command Natstat Linux
Python Version: 3.10
Local: Brazil
OS: Linux
'''

import os
import time


def tcp_udp_loop():
    while 1 < 2:
        time.sleep(1)
        os.system("netstat -tu")
        os.system("clear")



if __name__ == "__main__":
    tcp_udp_loop()
