import os.path
import sys

#checking IP address file and content validity
def ip_file_valid():
    #prompt user input
    ip_file = input("\n# Enter the IP file path :")
    #check if file exists
    if os.path.isfile(ip_file) == True:
        print("\n* IP file is valid :) \n")

    else:
        print("\n* Invalid".format(ip_file))
        sys.exit()

    #open the selected file
    selected_ip_file = open(ip_file, 'r')

    #starting from the beggining of the file
    selected_ip_file.seek(0)

    #reading each line
    ip_list = selected_ip_file.readlines()

    #closing file
    selected_ip_file.close()

    return ip_list