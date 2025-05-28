# PD7 6 - Count login time per user

# TASK DESCRIPTION
# Read the contents of the log.txt file and count how much time each user
# spent in the application. File attached under the video

# Import libraries
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Declare function

# Program

with open('logi.txt', 'r', encoding='utf8') as to_read:
    data_list = []
    login_sum_time = {}
    logged_users = {}
    for line in to_read:
        log = line.split(';')
        if log[0] == '\n':
            break
        operation_log_time = datetime.strptime(log[0], '%Y-%m-%d %H:%M:%S')
        if log[2] == 'login\n':
            logged_users[log[1]] = operation_log_time
        elif log[2] == 'logout\n':
            operation_duration = operation_log_time - logged_users[log[1]]
            login_sum_time[log[1]] = login_sum_time.get(log[1], relativedelta(seconds=0)) + operation_duration

# Print output message
    for name in login_sum_time.keys():
        lst = login_sum_time[name]
        print(f'{name} was logged in for {lst.hours} hours, {lst.minutes} minutes and {lst.seconds} seconds.')
