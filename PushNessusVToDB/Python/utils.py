## Utilitary Functions

## Check if a string is already in a list

def check_already_in_list(list_to_check, string_to_check):
    i = 0
    while i < len(list_to_check):
        if list_to_check[i] == string_to_check:
            return True
        i += 1
    return False


### Split an Ip address into 4 parts -> use '.' char as separator

def split_ip_address(ip_address):
    split_ip_address_list = ip_address.split(".")
    return split_ip_address_list
