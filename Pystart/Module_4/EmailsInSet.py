# Emails collection in set

# Receive 10 email addresses from a user. Check the address
# contains @ and .com or .pl, if so, add the address to the list
# Finally, convert the list to a set to remove all duplicates.
# View the number of entries before and after removing duplicates

#Declare empty list
list_of_emails = []

#Initiate counter of given emails
counter = 0

#Initiate nof emails to give by user
nof_given_emails = 10

#While loop validating emails till nof_given_emails is reached
#Loop also appends valid emails to list
while counter < nof_given_emails:
    email_to_validate = str(input(f'Give me email address no {counter + 1}: '))
    if "@" in email_to_validate and (".com" in email_to_validate or ".pl" in email_to_validate):
        list_of_emails.append(email_to_validate)
    counter += 1
# print(list_of_emails)

#Create set out of list, in order to avoid duplicates
correct_emails_without_duplicates = sorted(set(list_of_emails))
# print(correct_emails_without_duplicates)

#Output
#Firstly summary on number of emails
print(f'\nYou gave me {nof_given_emails} email addresses.\nOnly {len(list_of_emails)} were correct, as they had "@" '
      f'and postfix ".com" or ".pl". \nWhen duplicates were removed, as result we received '
      f'set of {len(correct_emails_without_duplicates)} distinct emails, which you can see below:\n')

#Secondly printing valid emails, without duplicates
for email in correct_emails_without_duplicates:
    print(email)