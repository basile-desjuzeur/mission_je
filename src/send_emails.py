##########################################################################
# Script Name  : send_emails.py
# Description  : Sends emails to the clients and remove error messages
# Auteur       : basiledesj@hotmail.fr
# Date : 2024/10/05
##########################################################################


import pandas as pd
import time
from utils import send_email_with_html, check_undelivered_emails


##### PARAMETERS ######

MAIL_FILE = "./data/mail_initial.html"
DATASET_FILE = "./data/test.csv"
MAIL_OBJECT = "Armen HEC Value Sharing Index Second Edition – Please take part in our survey"
UNDELIVERED_EMAILS_FILE = "./data/undelivered_emails.csv"
IMAGE_1 = "../data/photo_armen.png"
IMAGE_2 = "../data/photo_signature.png"


##### MAIN ####


def emailing_and_clean_by_chunk(
        mail_file=MAIL_FILE,
        dataset_file=DATASET_FILE,
        chunksize=500):
    """
    Send email to the first chunksize adresses that have not been contacted yet (to prevent error).
    Check the inbox and delete undelivered emails each 50 emails sent.

    Parameters:
    - mail_file (str) : the path to the html file containing the email content
    - dataset_file (str) : the path to the dataset containing the adresses
    - chunksize (int) : the number of emails to send

    Returns:
    - None
    """

    # keep only first chunksize adresses that have not been contacted
    data = pd.read_csv(dataset_file)
    data = data[data["SENT"] == 0].head(chunksize)

    # we check the inbox and delete undelivered emails each 50 emails sent
    counter_inbox_cleaner = 0

    # send emails
    for i in range(len(data)):

        # check inbox and delete undelivered emails
        if counter_inbox_cleaner == 50:
            check_undelivered_emails(UNDELIVERED_EMAILS_FILE)
            counter_inbox_cleaner = 0

        # send email
        email_recipient = data["EMAIL"].iloc[i]
        name = data["NAME"].iloc[i]
        send_email_with_html(
            email_recipient,
            MAIL_OBJECT,
            mail_file,
            name,
            image_path_1=IMAGE_1,
            image_path_2=IMAGE_2,
            random_time_spacing=True)

        # set SENT to 1 in original dataset
        data.loc[i, "SENT"] = 1

    # wait 4 minutes before sending the next chunk, cleans inbox meanwhile
    time.sleep(2 * 60)
    check_undelivered_emails(UNDELIVERED_EMAILS_FILE)
    time.sleep(2 * 60)


def main():
    """
    Continuously send emails to the first chunksize adresses that have not been contacted yet.
    Until all adresses have been contacted.


    Parameters:
    - None
    """

    while pd.read_csv(DATASET_FILE)["SENT"].sum(
    ) < pd.read_csv(DATASET_FILE).shape[0]:
        emailing_and_clean_by_chunk()


if __name__ == "__main__":
    main()
