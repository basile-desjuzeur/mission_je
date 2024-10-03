import pandas as pd 
import win32com.client as win32
import re
import os

def get_undeliverable_email_adress_from_error_mail(error_email):
    # extract the first email address from the error message
    undelivered_email_address = re.search(r'[\w\.-]+@[\w\.-]+', error_email)
    return undelivered_email_address.group(0)

def check_undelivered_emails():
    outlook = win32.Dispatch('outlook.application')
    inbox = outlook.GetNamespace("MAPI").GetDefaultFolder(6)
    messages = inbox.Items
    undelivered_emails = []
    for message in messages:
        if "Non remis" in message.Subject or "Undelivered" in message.Subject:
            # get the email address of the undelivered email
            undelivered_email_address = get_undeliverable_email_adress_from_error_mail(message.Body)
            undelivered_emails.append(undelivered_email_address)

            # remove the undelivered email from the inbox
            message.Delete()

    # append the undelivered email addresses to a csv file
    undelivered_emails_df = pd.DataFrame(undelivered_emails)
    undelivered_emails_df.to_csv("../data/undelivered_emails.csv", mode='a', header=False)

def remove_emails_from_clients_list():
    # check unread emails
    outlook = win32.Dispatch('outlook.application')
    inbox = outlook.GetNamespace("MAPI").GetDefaultFolder(6)
    messages = inbox.Items

    # read the clients list
    clients_list = pd.read_csv("../data/241003_cleaned_dataset.csv")["EMAIL"]

    for message in messages:

        # get sender email address
        sender_email_address = message.SenderEmailAddress

        # check if the sender email address is in the clients list
        if sender_email_address in clients_list:
            
            # delete the email
            message.Delete()


def get_html_content(html_file_path):
    with open(html_file_path, "r") as file:
        content = file.read()
    return content

# replace [Recipient's Name] with the recipient's name

def send_email_with_html(email_recipient,
                         email_subject,
                         html_content,
                         client_name,
                         client_surname,
                        attachment_location = ""):

    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = email_recipient
    mail.Subject = email_subject

    # add client name and surname to the html content
    html_content = html_content.replace("[Recipient's Name]", client_name + " " + client_surname)

    # add html content to the email
    mail.HTMLBody = html_content

    image_path1 = "../data/photo_armen.png"
    image_cid1 = "image1"    

    image_path2 = "../data/photo_signature.png"
    image_cid2 = "image2"

    # Ajout de la première image en tant que pièce jointe avec Content-ID
    attachment1 = mail.Attachments.Add(os.path.abspath(image_path1))
    attachment1.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F", image_cid1)

    # Ajout de la deuxième image en tant que pièce jointe avec Content-ID
    attachment2 = mail.Attachments.Add(os.path.abspath(image_path2))
    attachment2.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F", image_cid2)

    # send the email
    try:
        mail.Send()
        print("Email successfully sent to " + email_recipient)
    except Exception as e:
        print(e)
        print("Email not sent to " + email_recipient) 