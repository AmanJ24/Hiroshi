from demo import calculate_time, generate_emails, binary_iter


#List of domains for additional email extensions
list_of_domains = ['gmail.com', 'yahoomail.com', 'google+mail.com']

#Generate emails
emails = generate_emails(10, list_of_domains, 10000)

#Testing emails to add to the list
email = 'aman@gmail.com'
emails.append(email)

#s Sorting list of generated emails
sorted_emails = sorted(emails)
index, found = binary_iter(email, sorted_emails)

#printing result from function
print(found)

#Printing index returned from the function on the list of sorted emails
if index: print(f"Element at index: {index} is {sorted_emails[index]}")

#Run analysis of function
print(calculate_time(binary_iter, email, sorted_emails))
print(calculate_time(generate_emails, 10, list_of_domains, 1000))