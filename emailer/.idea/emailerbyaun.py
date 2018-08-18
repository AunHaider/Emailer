
import smtplib

def get_emails():
    emails = {'aunhaider.it@gmail.com' : 'Aun Haider'}

    return emails

def get_comments():

    comments = 'Subject: My Python First Simple Program!\n\n'

    return comments

def get_programs():
    program = {}

    program_file = open('prog.txt', 'r')
    program = program_file.read()

    return program


def get_messages():
    message = ()

    message_file = open('mess.txt', 'r')
    message = message_file.read()

    return message


def send_emails(emails, program, message, comments):
    # Connect to the smtp server
    server = smtplib.SMTP('smtp.gmail.com', '587')

    # Start TLS encryption
    server.starttls()

    # Login
    password = input('Enter Password')
    from_email = 'aunhaider.it@gmail.com'
    server.login(from_email, password)

    for to_email in emails.items():
        copy = comments
        copy += message + '\n\n\n'
        copy += program
        server.sendmail(from_email, to_email, copy)

    server.quit()

# define main function
def main():
    emails = get_emails()
    print(emails)

    program = get_programs()
    print(program)

    message = get_messages()
    print(message)

    comments = get_comments()
    print(comments)


    # call send_emails function
    send_emails(emails, program, message, comments)

main()
