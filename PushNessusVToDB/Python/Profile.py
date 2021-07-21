class Profile:
    def __init__(self, ip, ip_1, ip_2, ip_3, ip_4,
                 total_v, info_nbr, low_nbr, medium_nbr, high_nbr, critical_nbr, fqdn):
        self.ip = ip
        self.ip_1 = ip_1
        self.ip_2 = ip_2
        self.ip_3 = ip_3
        self.ip_4 = ip_4
        self.total_v = total_v
        self.info_nbr = info_nbr
        self.low_nbr = low_nbr
        self.medium_nbr = medium_nbr
        self.high_nbr = high_nbr
        self.critical_nbr = critical_nbr
        self.fqdn = fqdn
## Profile Class : can be considered as IP obj and vulnerabilities nbr associated

class Vulnerabilities:
    def __init__(self, total_v, info_v, low_v, medium_v, high_v,
                 critical_v, ip_id, ip1_id, ip2_id, ip3_id, ip4_id):
        self.total_v = total_v
        self.info_v = info_v
        self.low_v = low_v
        self.medium_v = medium_v
        self.high_v = high_v
        self.critical_v = critical_v
        self.ip_id = ip_id
        self.ip1_id = ip1_id
        self.ip2_id = ip2_id
        self.ip3_id = ip3_id
        self.ip4_id = ip4_id

## Vulnerabilities Class


class Risk:
    def __init__(self, risk_description, severity, solutions, cve,
                 ip_id, ip1_id, ip2_id, ip3_id, ip4_id):
        self.risk_description = risk_description
        self.severity = severity
        self.solutions = solutions
        self.cve = cve
        self.ip_id = ip_id
        self.ip1_id = ip1_id
        self.ip2_id = ip2_id
        self.ip3_id = ip3_id
        self.ip4_id = ip4_id

## Risks Class