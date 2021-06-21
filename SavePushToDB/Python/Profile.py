class Profile:
  def __init__(self, ip, ip_1, ip_2, ip_3, ip_4,
               nbr_vulnerabilities, nbr_critical, nbr_high, nbr_medium, fqdn):
    self.ip = ip
    self.ip_1 = ip_1
    self.ip_2 = ip_2
    self.ip_3 = ip_3
    self.ip_4 = ip_4
    self.nbr_vulnerabilities = nbr_vulnerabilities
    self.nbr_critical = nbr_critical
    self.nbr_high = nbr_high
    self.nbr_medium = nbr_medium
    self.fqdn = fqdn

