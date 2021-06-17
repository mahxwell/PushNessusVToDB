class Profile:
  def __init__(self, ip, nbr_vulnerabilties, nbr_critical, nbr_high, nbr_medium, fqdn):
    self.ip = ip
    self.nbr_vulnerabilties = nbr_vulnerabilties
    self.nbr_critical = nbr_critical
    self.nbr_high = nbr_high
    self.nbr_medium = nbr_medium
    self.fqdn = fqdn



p1 = Profile("192.168.1.1" , 3, 2, 2 , 2, "toto")
