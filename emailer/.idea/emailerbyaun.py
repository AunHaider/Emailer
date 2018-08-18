
import smtplib

def get_emails():
    emails = {'aunhaider.it@gmail.com' : 'Aun Haider lexicon', 'mmj_judy@yahoo.com' : 'Mohammed',
              'tarikdoha80@gmail.com' : 'Tarek Doha', 'shadi21985@gmail.com' : 'Shadi Abo Alnaser',
              'Linus.Goransson@lexicon.se' : 'Linus', 'johan.peyron@gmail.com' : 'Johan Peyron',
              'marcus.gyllencreutz@lexicon.se' : 'Marcus',  'evedat@gmail.com' : 'Vedet'}

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
