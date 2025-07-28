import win32com.client as win32


def send_mail_fun():
    try:
        # step 1 - create integration with Outlook
        outlook = win32.Dispatch('outlook.application')

        # step 2 - create an email
        email = outlook.CreateItem(0)

        # step 3 - configure email information
        email.To = "govindakg543@gmail.com"
        email.Subject = "Automatic Email from Python"
        email.body = "Dear all please find"

        # step 4 - attach a file to email
        email.Attachments.Add(r"C:\Hunter\py\telecomHallPython\Sample.txt")

        # step 5 - send an email
        email.Send()
        print("Email Sent!")
    except Exception as e:
        print(e)


send_mail_fun()
