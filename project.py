import csv

def write_into_csv(info_list):
    with open("std_info.csv", "a", newline="") as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(["Name","Age", "Contact_Number", "Email_ID"])

        writer.writerow(info_list)

condition = True
while(condition):
    std_info = input("Enter student information in the following format (Name Age Contact_Number Email_ID):")
    print("Entered Information:"+ std_info)

    std_info_list = std_info.split(' ')
    print("entered split up informatin is: " + str(std_info_list))

    write_into_csv(std_info_list)

    cond_check = input("Enter (yes/no) if you want to input information of another student:")
    if cond_check == "yes":
        condition = True
    elif cond_check == "no":
        condition = False
