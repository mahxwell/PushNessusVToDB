import strings

## Create a vulnerability nbr list

def vulnerabilities_nbr_spe_list(data_xls, ip_address):
    ### Instead of creating vulnerability obj, fill vulnerability nbr into a list -> vulnerabilities_list
    ### vulnerabilities_list[0] -> total vulnerability nbr
    ### vulnerabilities_list[1] -> info vulnerability nbr
    ### vulnerabilities_list[2] -> low vulnerability nbr
    ### vulnerabilities_list[3] -> medium vulnerability nbr
    ### vulnerabilities_list[4] -> high vulnerability nbr
    ### vulnerabilities_list[5] -> critical vulnerability nbr


    vulnerabilities_list = [0, 0, 0, 0, 0, 0]
    total_nbr = 0
    info_nbr = 0
    low_nbr = 0
    medium_nbr = 0
    high_nbr = 0
    critical_nbr = 0
    i = 0
    while i < len(data_xls):
        if data_xls[strings.IP_ADDRESS][i] == ip_address:
            total_nbr += 1
            vulnerabilities_list[0] = total_nbr
            if data_xls[strings.RISK_FACTOR][i] == strings.INFO:
                info_nbr = info_nbr + 1
                vulnerabilities_list[1] = info_nbr
            if data_xls[strings.RISK_FACTOR][i] == strings.LOW:
                low_nbr = low_nbr + 1
                vulnerabilities_list[2] = low_nbr
            if data_xls[strings.RISK_FACTOR][i] == strings.MEDIUM:
                medium_nbr = medium_nbr + 1
                vulnerabilities_list[3] = medium_nbr
            if data_xls[strings.RISK_FACTOR][i] == strings.HIGH:
                high_nbr = high_nbr + 1
                vulnerabilities_list[4] = high_nbr
            if data_xls[strings.RISK_FACTOR][i] == strings.CRITICAL:
                critical_nbr = critical_nbr + 1
                vulnerabilities_list[5] = critical_nbr
        i = i + 1
    return vulnerabilities_list
