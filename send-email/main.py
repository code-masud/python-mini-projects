from models import Gmail, Outlook

def prompt_user_input(prompt: str, optional: bool = False, ) -> str | None:
    value = input(prompt).strip()
    return value if value or not optional else None

def demonstrated_email():
    print("=== Welcome To Email Service ===")

    sender = prompt_user_input('\nEnter sender email(ex: from@gmail.com): ')
    password = prompt_user_input('Enter app password(ex: asdf quio zxcv uiop): ')
    receiver = prompt_user_input('Enter receiver email(ex.to@gmail.com): ')
    subject = prompt_user_input("Enter email subject: ")
    body = prompt_user_input('Enter email body: ')

    html = prompt_user_input("Enter raw html template: ") if input("Do you have html template? (y/n): ").lower() == 'y' else None
    attachment = prompt_user_input("Enter file path: ") if input("Do you have attachment? (y/n): ").lower() == 'y' else None
    
    if not all([sender, password, receiver, subject, body]):
        print("Missing required fields. Email not sent.")
        return

    print("\nSelect SMTP Server:")
    print("1. Gmail\n2. Outlook")

    smtp_options = {
        1: {'class': Gmail, 'host': "smtp.gmail.com", "port": 465},
        2: {'class': Outlook, 'host': "smtp.office365", "port": 587}
    }
    
    try:
        user_choice = int(input("Enter option number: ").strip())
        if user_choice not in smtp_options:
            print("Invalid option selected")
            return
        
        config = smtp_options[user_choice]
        email_client = config['class'](config['host'], config['port'], sender, password)
        message = email_client.create_message(receiver, subject, body, html, attachment)

        email_client.send_email(message)
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    try:
        demonstrated_email()
    except Exception as e:
        print(f"An error found: {e}")
        return 1
    return 0

if __name__ == "__main__":
    main()
