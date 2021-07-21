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
        total_v = getattr(profile_list[i], "total_v")
        info_nbr = getattr(profile_list[i], "info_nbr")
        low_nbr = getattr(profile_list[i], "low_nbr")
        medium_nbr = getattr(profile_list[i], "medium_nbr")
        high_nbr = getattr(profile_list[i], "high_nbr")
        critical_nbr = getattr(profile_list[i], "critical_nbr")
        fqdn = getattr(profile_list[i], "fqdn")
    ### Print IP obj
        print("ip = " + str(ip))
        print("ip1 = " + str(ip_1))
        print("ip2 = " + str(ip_2))
        print("ip3 = " + str(ip_3))
        print("ip4 = " + str(ip_4))
        print("Nombre total de Vulnerabilités = " + str(total_v))
        print("Nombre total de Vulnerabilités Info = " + str(info_nbr))
        print("Nombre total de Vulnerabilités basses = " + str(low_nbr))
        print("Nombre de Vulnerabilités critiques = " + str(critical_nbr))
        print("Nombre de Vulnerabilités hautes = " + str(high_nbr))
        print("Nombre de Vulnerabilités moyennes = " + str(medium_nbr))
        print("fqdn = " + str(fqdn))


def test_risk_content(risk_list):
    for i in range(len(risk_list)):
        risk_description = getattr(risk_list[i], "risk_description")
        severity = getattr(risk_list[i], "severity")
        solutions = getattr(risk_list[i], "solutions")
        cve = getattr(risk_list[i], "cve")
        ip_id = getattr(risk_list[i], "ip_id")
        ip1_id = getattr(risk_list[i], "ip1_id")
        ip2_id = getattr(risk_list[i], "ip2_id")
        ip3_id = getattr(risk_list[i], "ip3_id")
        ip4_id = getattr(risk_list[i], "ip4_id")

        print("description = " + str(risk_description))
        print("severity = " + str(severity))
        print("solutions = " + str(solutions))
        print("cve = " + str(cve))
        print("ip_id = " + str(ip_id))
        print("ip_id1 = " + str(ip1_id))
        print("ip_id2 = " + str(ip2_id))
        print("ip_id3 = " + str(ip3_id))
        print("ip_id4 = " + str(ip4_id))

