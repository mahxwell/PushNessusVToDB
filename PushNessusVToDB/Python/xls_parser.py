import pandas as pd
import utils as ut
import strings
import vulnerabilities as vul
from Profile import Profile as pr


## Parse xlsx file here


def parse_xls(path_to_file_to_parse):
    ### Store all parsed informations as a kind of resultset in data_xls

    data_xls = pd.read_excel(path_to_file_to_parse, strings.FULL_REPORT, header=1)
    profile_list = []
    ip_list = []

    ### Parse data_xls

    for i in range(len(data_xls)):
        split_ip_address_list = []

        ### Create here a list of Profile obj -> list of Ip Obj

        ### Check if profile_list is empty
        if len(profile_list) <= 0:
            st = str((data_xls[strings.IP_ADDRESS][i]))
            split_ip_address_list = ut.split_ip_address(st)
            ip_list.append(st)
            vulnerabilities_list = vul.vulnerabilities_nbr_spe_list(data_xls, data_xls[strings.IP_ADDRESS][i])
            profile_list.append(pr(str(data_xls[strings.IP_ADDRESS][i]), split_ip_address_list[0], split_ip_address_list[1],
                                   split_ip_address_list[2], split_ip_address_list[3], vulnerabilities_list[0],
                                   vulnerabilities_list[1], vulnerabilities_list[2], vulnerabilities_list[3],
                                   str(data_xls[strings.FQDN][i])))
        else:
            ip_to_check = data_xls[strings.IP_ADDRESS][i]
            in_the_list = ut.check_already_in_list(ip_list, ip_to_check)

            ### Check if the current obj is already in the list
            if not in_the_list:
                st = str((data_xls[strings.IP_ADDRESS][i]))
                split_ip_address_list = ut.split_ip_address(st)
                ip_list.append(st)

                vulnerabilities_list = vul.vulnerabilities_nbr_spe_list(data_xls, data_xls[strings.IP_ADDRESS][i])

                ### Fill profile_list with new Profile obj

                profile_list.append(
                    pr(str(data_xls[strings.IP_ADDRESS][i]), split_ip_address_list[0], split_ip_address_list[1],
                       split_ip_address_list[2], split_ip_address_list[3], vulnerabilities_list[0],
                       vulnerabilities_list[1], vulnerabilities_list[2], vulnerabilities_list[3],
                       str(data_xls[strings.FQDN][i])))
    return profile_list
