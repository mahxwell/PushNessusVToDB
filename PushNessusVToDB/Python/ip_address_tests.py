#Test File for Ip_address parsing


## Show contents of IP address object

def test_profile_content(profile_list):
    ### Get obj Attribute
    for i in range(len(profile_list)):
        ip = getattr(profile_list[i], "ip")
        ip_1 = getattr(profile_list[i], "ip_1")
        ip_2 = getattr(profile_list[i], "ip_2")
        ip_3 = getattr(profile_list[i], "ip_3")
        ip_4 = getattr(profile_list[i], "ip_4")
        vulnerabilities_nbr = getattr(profile_list[i], "nbr_vulnerabilities")
        critical_nbr = getattr(profile_list[i], "nbr_critical")
        high_nbr = getattr(profile_list[i], "nbr_high")
        medium_nbr = getattr(profile_list[i], "nbr_medium")
        fqdn = getattr(profile_list[i], "fqdn")
    ### Print IP obj
        print("ip = " + str(ip))
        print("ip1 = " + str(ip_1))
        print("ip2 = " + str(ip_2))
        print("ip3 = " + str(ip_3))
        print("ip4 = " + str(ip_4))
        print("Nombre total de Vulnerabilités = " + str(vulnerabilities_nbr))
        print("Nombre de Vulnerabilités critiques = " + str(critical_nbr))
        print("Nombre de Vulnerabilités hautes = " + str(high_nbr))
        print("Nombre de Vulnerabilités moyennes = " + str(medium_nbr))
        print("fqdn = " + str(fqdn))