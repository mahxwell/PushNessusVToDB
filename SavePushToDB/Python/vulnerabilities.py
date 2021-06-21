import strings


def vulnerabilities_nbr_spe_list(data_xls, ip_address):
    vulnerabilities_list = [0, 0, 0, 0]
    critical_nbr = 0
    high_nbr = 0
    medium_nbr = 0
    i = 0
    vulnerabilities_count = 0
    while i < len(data_xls):
        if data_xls[strings.IP_ADDRESS][i] == ip_address:
            vulnerabilities_count += 1
            vulnerabilities_list[0] = vulnerabilities_count
            if data_xls[strings.SEVERITY][i] == 4:
                critical_nbr = critical_nbr + 1
                vulnerabilities_list[1] = critical_nbr
            if data_xls[strings.SEVERITY][i] == 3:
                high_nbr = high_nbr + 1
                vulnerabilities_list[2] = high_nbr
            if data_xls[strings.SEVERITY][i] == 2:
                medium_nbr = medium_nbr + 1
                vulnerabilities_list[3] = medium_nbr
        i = i + 1
    return vulnerabilities_list
