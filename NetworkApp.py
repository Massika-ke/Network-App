import sys
import time

from ip_file_valid import ip_file_valid
from ip_addr_valid import ip_addr_valid
from ip_reach import ip_reach
from ssh_connection import ssh_connection
from create_threads import create_threads

#save the list of ip addresses in ip.txt to a variable
ip_list = ip_file_valid()
#verify the validity of each IP address in the list
try:
    ip_addr_valid(ip_list)

except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()

#verify reachability of each IP address in the list
try:
    ip_reach(ip_list)

except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()

#calling threads creation for one/ multiple SSH connections
create_threads(ip_list, ssh_connection)