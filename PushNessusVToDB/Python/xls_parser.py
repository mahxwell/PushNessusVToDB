import pandas as pd
import utils as ut
import strings
import vulnerabilities as vul
from Profile import Profile as pr
from Profile import Risk as risk

## Parse xlsx file here


def profile_core_parser(data_xls, profile_list, ip_list, i):
    st = str((data_xls[strings.IP_ADDRESS][i]))
    split_ip_address_list = ut.split_ip_address(st)
    ip_list.append(st)
    vulnerabilities_list = vul.vulnerabilities_nbr_spe_list(data_xls, data_xls[strings.IP_ADDRESS][i])
    profile_list.append(pr(str(data_xls[strings.IP_ADDRESS][i]),
                           split_ip_address_list[0],
                           split_ip_address_list[1],
                           split_ip_address_list[2],
                           split_ip_address_list[3],
                           vulnerabilities_list[0],
                           vulnerabilities_list[1],
                           vulnerabilities_list[2],
                           vulnerabilities_list[3],
                           vulnerabilities_list[4],
                           vulnerabilities_list[5],
                           str(data_xls[strings.FQDN][i])))


def parse_xls_profile_list(path_to_file_to_parse):
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
            profile_core_parser(data_xls, profile_list, ip_list, i)
        else:
            ip_to_check = data_xls[strings.IP_ADDRESS][i]
            in_the_list = ut.check_already_in_list(ip_list, ip_to_check)

            ### Check if the current obj is already in the list
            if not in_the_list:
                profile_core_parser(data_xls, profile_list, ip_list, i)
    return profile_list


def parse_xls_risk_list(path_to_file_to_parse):
    data_xls = pd.read_excel(path_to_file_to_parse, strings.FULL_REPORT, header=1)
    risk_list = []
    already_risk_list = []
    ip_id = 0
    for i in range(len(data_xls)):

        st = str((data_xls[strings.IP_ADDRESS][i]))
        split_ip_address_list = ut.split_ip_address(st)
        if not ut.check_already_in_list(already_risk_list, st):
            already_risk_list.append(st)
            ip_id = ip_id + 1;

        risk_list.append(risk(
            str(data_xls[strings.DESCRIPTION][i]) + str(data_xls[strings.SYNOPSIS][i]),
            data_xls[strings.RISK_FACTOR][i],
            data_xls[strings.SOLUTION][i],
            data_xls[strings.CVE][i],
            ip_id,
            split_ip_address_list[0],
            split_ip_address_list[1],
            split_ip_address_list[2],
            split_ip_address_list[3]))
    return risk_list
