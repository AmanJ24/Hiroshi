from random import choice
from string import ascii_lowercase as letters

list_of_domains = ['gmail.com', 'yahoomail.com', 'protonmail.com']

quotes = [ 
    'Luck is what happens when preparation meets opportunity',
    'Begin at once to live, and count each seperate day as a seperate stage',
    'Throw me to the wolves and I will return leading the pack'
]

def generate_name(length_of_name):
    return ''.join(choice(letters) for i in range(length_of_name))

def get_domain(list_of_domains):
    return choice(list_of_domains)

def get_quote(list_of_quotes):
    return choice(list_of_quotes)

def generate_emails(length_of_emails, list_of_domains, total_emails, quotes):
    with open("data.txt", "w") as to_write:
        for num in range(total_emails):
            key = generate_name(length_of_emails) + "@" + get_domain(list_of_domains)
            value = get_quote(quotes)
            to_write.write(key + ":" + value + "\n")

        to_write.write("aman@gmail.com:I Don't Believe in second chances\n")
        to_write.write("Rohan@yahoomail.com:My name is lakhan\n")
    return "Successful..."
    
generate_emails(10, list_of_domains, 100, quotes)

