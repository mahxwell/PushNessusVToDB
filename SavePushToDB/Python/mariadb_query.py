import strings
import mariadb
import sys


def mariadb_queries(profile_list):
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
    connection.close()
    return cur


def fill_ip_spilt_table_rows(cur, connection):
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


def push_ip_address_to_db(cur,connection, profile_list):

    for i in range(len(profile_list)):
        ip1 = getattr(profile_list[i], "ip_1")
        ip2 = getattr(profile_list[i], "ip_2")
        ip3 = getattr(profile_list[i], "ip_3")
        ip4 = getattr(profile_list[i], "ip_4")

        ip_address = str(ip1) + '.' + str(ip2) + '.' + str(ip3) + '.' + str(ip4)

        try:
            cur.execute(
                "INSERT INTO ip (idip, ip_description, ip1_idip1, ip2_idip2, ip3_idip3, ip4_idip4)"
                " VALUES (?,?,?,?,?,?)", (0, ip_address, str(ip1), str(ip2), str(ip3), str(ip4)))
        except mariadb.Error as e:
            print(f"Error: {e}")
    connection.commit()


def push_vulnerabilities_nbr_to_db(cur, connection, profile_list):

    for i in range(len(profile_list)):
        ip1 = getattr(profile_list[i], "ip_1")
        ip2 = getattr(profile_list[i], "ip_2")
        ip3 = getattr(profile_list[i], "ip_3")
        ip4 = getattr(profile_list[i], "ip_4")
        vulnerabilities_nbr = getattr(profile_list[i], "nbr_vulnerabilities")
        critical_nbr = getattr(profile_list[i], "nbr_critical")
        high_nbr = getattr(profile_list[i], "nbr_high")
        medium_nbr = getattr(profile_list[i], "nbr_medium")

        try:
            cur.execute(
                "INSERT INTO vulnerabilities (idvulnerabilities_nbr, total_vulnerabilities, medium_vulnerabilities,"
                " high_vulnerabilities, critical_vulnerabilities, ip_idip, ip_ip1_idip1, ip_ip2_idip2, ip_ip3_idip3,"
                " ip_ip4_idip4) VALUES (?,?,?,?,?,?,?,?,?,?)",
                (0, int(vulnerabilities_nbr),
                 int(medium_nbr), int(high_nbr), int(critical_nbr), i+1, int(ip1), int(ip2), int(ip3), int(ip4)))
        except mariadb.Error as e:
            print(f"Error: {e}")

    connection.commit()


def launch_data_push(profile_list):
    mariadb_queries(profile_list)
