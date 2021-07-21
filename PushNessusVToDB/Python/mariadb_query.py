import strings
import mariadb
import sys

## Maria DB connection and queries functions


def mariadb_queries(profile_list, risk_list):
    # Connect to MariaDB Platform
    try:
        connection = mariadb.connect(
            user=strings.USER,
            password=strings.PASSWORD,
            host=strings.HOST,
            port=strings.PORT,
            database=strings.DATABASE
        )
        print("Connected to " + strings.DATABASE + " Database with User " + strings.USER)

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = connection.cursor()

    fill_ip_spilt_table_rows(cur, connection)
    push_ip_address_to_db(cur, connection, profile_list)
    push_vulnerabilities_nbr_to_db(cur, connection, profile_list)
    push_risks_to_db(connection, cur, risk_list)
    connection.close()
    #return cur

### Fill spilt ip rows ip1, ip2, ip3, ip4 with contents from 1 to 255
### Beware 0 is at index 256


def fill_ip_spilt_table_rows(cur, connection):
    ## ip_table_list -> prepare split ip tables from 1 to 4
    ip_table_list = ["1", "2", "3", "4"]
    for i in range(len(ip_table_list)):
        mask = 1
        while mask < 256:
            try:
                cur.execute(
                    "INSERT INTO ip" + ip_table_list[i] + " (idip" + ip_table_list[i] + ", ip" + ip_table_list[i]
                    + "_content) VALUES (?,?)", (0, mask))
                mask = mask + 1
            except mariadb.Error as e:
                print(f"Error: {e}")
        cur.execute(
                "INSERT INTO ip" + ip_table_list[i] + " (idip" + ip_table_list[i] + ", ip" + ip_table_list[i]
                + "_content) VALUES (?,?)", (0, 0))
    connection.commit()


## Push Ip obj to DB

def push_ip_address_to_db(cur, connection, profile_list):

### Get attributes from Ip Obj
    for i in range(len(profile_list)):
        ip1 = getattr(profile_list[i], "ip_1")
        ip2 = getattr(profile_list[i], "ip_2")
        ip3 = getattr(profile_list[i], "ip_3")
        ip4 = getattr(profile_list[i], "ip_4")

### Concat ip1, ip2, ip3 and ip4 attribute to create ip address

        ip_address = str(ip1) + '.' + str(ip2) + '.' + str(ip3) + '.' + str(ip4)

### Push all informations into DB
        try:
            cur.execute(
                "INSERT INTO ip (idip, ip_description, ip1_idip1, ip2_idip2, ip3_idip3, ip4_idip4)"
                " VALUES (?,?,?,?,?,?)", (0, ip_address, str(ip1), str(ip2), str(ip3), str(ip4)))
        except mariadb.Error as e:
            print(f"Error: {e}")
    connection.commit()


## Push vulnerabilities nbr to db

def push_vulnerabilities_nbr_to_db(cur, connection, profile_list):

    ### Get vulnerabilities nbr informations from IP address
    for i in range(len(profile_list)):
        ip1 = getattr(profile_list[i], "ip_1")
        ip2 = getattr(profile_list[i], "ip_2")
        ip3 = getattr(profile_list[i], "ip_3")
        ip4 = getattr(profile_list[i], "ip_4")
        total_v = getattr(profile_list[i], "total_v")
        info_nbr = getattr(profile_list[i], "info_nbr")
        low_nbr = getattr(profile_list[i], "low_nbr")
        medium_nbr = getattr(profile_list[i], "medium_nbr")
        high_nbr = getattr(profile_list[i], "high_nbr")
        critical_nbr = getattr(profile_list[i], "critical_nbr")

        ### Push vulnerabilities informations to DB
        try:
            cur.execute(
                "INSERT INTO vulnerabilities (idvulnerabilities_nbr, total_vulnerabilities, info_vulnerabilities, low_vulnerabilities,"
                " medium_vulnerabilities,"
                " high_vulnerabilities, critical_vulnerabilities, ip_idip, ip_ip1_idip1, ip_ip2_idip2, ip_ip3_idip3,"
                " ip_ip4_idip4) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                (0, int(total_v),
                 int(info_nbr), int(low_nbr), int(medium_nbr), int(high_nbr), int(critical_nbr), i+1, int(ip1), int(ip2), int(ip3), int(ip4)))
        except mariadb.Error as e:
            print(f"Error: {e}")

    connection.commit()


def push_risks_to_db(connection, cur, risk_list):
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

        ### Push vulnerabilities informations to DB
        try:
            cur.execute(
                "INSERT INTO risk (idrisk,risk_description, severity, solutions, cve,"
                " ip_idip, ip_ip1_idip1, ip_ip2_idip2, ip_ip3_idip3, ip_ip4_idip4) VALUES (?,?,?,?,?,?,?,?,?,?)",
                (0, risk_description, severity, solutions, cve, ip_id, ip1_id, ip2_id, ip3_id, ip4_id))
        except mariadb.Error as e:
            print(f"Error: {e}")
    connection.commit()



## Maria DB query launcher


def launch_data_push(profile_list, risk_list):
    if profile_list is not None and risk_list is not None:
        mariadb_queries(profile_list, risk_list)
    else:
        print("Error : Profile list or Risk list empty")
