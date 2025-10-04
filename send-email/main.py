from models import Gmail, Outlook

def demonstrated_email():
    print("=== Welcome Email Sender ===")

    sender = input('Enter sender email(ex: from@gmail.com): ')
    password = input('Enter app password(ex: asdf quio zxcv uiop): ')
    receiver = input('Enter receiver email(ex.to@gmail.com): ')
    sub = input("Enter subject: ")
    body = input('Enter body: ')
    html = input("Enter html template: ")

    if sender and password and receiver and sub and body:
        print("Select SMTP Server")
        print("1.Gmail\n2.Outlook")

        try:
            user_choice = int(input("Enter option number: "))

            match user_choice:
                case 1:
                    host = "smtp.gmail.com"
                    port = 465
                    
                    gmail = Gmail(host, port, sender, password)
                    message = gmail.create_email(receiver, sub, body, html)
                    gmail.send_email(message)
                case 2:
                    host = "smtp.office365.com"
                    port = 587

                    outlook = Outlook(host, port, sender, password)
                    message = outlook.create_email(receiver, sub, body, html)
                    outlook.send_email(message)
                case _:
                    print("Invalid option selected")
        except Exception as e:
            raise ValueError(e)

def main():
    try:
        demonstrated_function()
    except Exception as e:
        print(f"An error found: {e}")
        return 1
    return 0

if __name__ == "__main__":
    main()
