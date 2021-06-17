import pandas as pd
import utils as ut
from Profile import Profile as pr


def read_xls():
    data_xls = pd.read_excel("C:\\Users\\msoro\\Desktop\\toto.xlsx", "Full Report", header=1)
    profile_list = []
    for i in range(len(data_xls)):
        print(len(profile_list))
        if len(profile_list) <= 0:
            ip_to_check = getattr(profile_list[i], "ip")
            print(ip_to_check)
        is_in_the_list = ut.check_ip_address_list(str(data_xls["IP Address"])[i], profile_list)
        if is_in_the_list is False:
            profile_list.append(pr(str(data_xls["IP Address"][i]), str(data_xls["FQDN"][i]),
                                   int(data_xls["Severity"][i]), 0, 0, 0))

        else:
             print("error")
