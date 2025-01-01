# Problem 5

# Initialize an empty dictionary to store the message counts for each domain
message_count = {}

# Add your code below
with open("Email_log.txt", "r") as file:
    for line in file:
        email, count = line.strip().split()
        domain = email.split("@")[1].split()[0]
        if domain in message_count:
            message_count[domain] += int(count)
        else:
            message_count[domain] = int(count)

for domain, count in message_count.items():
    print(f"{domain}: {count}")
