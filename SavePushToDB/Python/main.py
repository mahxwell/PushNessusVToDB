import xls_parser as xls
import ip_address_tests as ip_test
import mariadb_query as query
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(sys.argv[1])
        path_to_file_to_parse = sys.argv[1]
        profile_list = xls.parse_xls(str(path_to_file_to_parse))

        # Fill Data Base with collected data

        query.launch_data_push(profile_list)

        # launch tests

        #ip_test.test_profile_content(profile_list)
    else:
        print("Enter full path to file to parse as parameter 1")
