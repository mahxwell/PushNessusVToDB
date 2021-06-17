def check_ip_address_list(ip_add_to_check, ip_list):
    if ip_list:
        for i in range(len(ip_list)):
            if ip_add_to_check in ip_list: # or ip_list is None:
                return True
    return False
