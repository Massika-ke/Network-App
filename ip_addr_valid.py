# Iterates over a list of IP addres and verifys validy

import sys

#checking octects
def ip_addr_valid(list):

    for ip in list:
        ip = ip.rstrip("\n")
        octect_list = ip.split('.')

        if (len(octect_list) == 4) and (1 <= int(octect_list[0]) <= 223) and (int(octect_list[0]) != 127) and (int(octect_list[0]) != 169 or int(octect_list[1]) != 254) and (0 <= int(octect_list[1]) <= 255 and
            0 <= int(octect_list[2]) <= 255 and 0 <= int(octect_list[3]) <= 255):
                continue

        else:
            print('\n* There was an invalid IP address: {} :(\n'.format(ip))
            sys.exit()