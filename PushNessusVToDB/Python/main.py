import xls_parser as xls
import ip_address_tests as ip_test
import mariadb_query as query
import sys

## Main Function App

if __name__ == '__main__':
    ### Check existing argv -> path to the xlsx file to parse
    if len(sys.argv) > 1:

        ### Get absolute path to xlsx file

        path_to_file_to_parse = sys.argv[1]

        ### Fill profile_list by parsing xlsx file

        profile_list = xls.parse_xls_profile_list(str(path_to_file_to_parse))

        ### Fill risk_list by parsing xlsx file

        risk_list = xls.parse_xls_risk_list(str(path_to_file_to_parse))

        # Fill Data Base with collected data in profile_list

        query.launch_data_push(profile_list, risk_list)

        # launch tests uncomment

        # ip_test.test_profile_content(profile_list)

        # ip_test.test_risk_content(risk_list)

    else:
        print("Enter full path to file to parse as parameter 1")
