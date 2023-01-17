class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
command = input()

while command != "Stop":
    split_command = command.split()
    email = Email(split_command[0], split_command[1], split_command[2])
    emails.append(email)

    command = input()

indexes = [int(i) for i in input().split(", ")]

for index in indexes:
    emails[index].send()

for mail in emails:
    print(mail.get_info())
