##########################################################################
# Script Name  : send_emails.py
# Description  : Sends emails to the clients and remove error messages
# Auteur       : basiledesj@hotmail.fr
# Date : 2024/10/05
##########################################################################


import pandas as pd
import time
from utils import send_email_with_html, check_undelivered_emails, get_html_content
import tqdm
from pathlib import Path

##### PARAMETERS ######

MAIL_FILE = Path("./data/mail_initial.html")
DATASET_FILE = Path("./test/test_client_answers_bdd.csv")
MAIL_OBJECT = "Armen HEC Value Sharing Index Second Edition – Please take part in our survey"
UNDELIVERED_EMAILS_FILE = Path("./test/test_undelivered_emails.csv")
IMAGE_1 = Path("./data/photo_armen.png")
IMAGE_2 = Path("./data/photo_signature.png")
CHUNKSIZE = 3

##### MAIN ####


def emailing_and_clean_by_chunk(
        mail_file=get_html_content(MAIL_FILE),
        dataset_file=DATASET_FILE,
        chunksize=CHUNKSIZE,
        image_path_1=IMAGE_1,
        image_path_2=IMAGE_2,
        mail_object=MAIL_OBJECT,
        undelivered_emails_file=UNDELIVERED_EMAILS_FILE,
        ):
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
    data_temp = data[data["SENT"] == 0].head(chunksize)

    # we check the inbox and delete undelivered emails each 50 emails sent
    counter_inbox_cleaner = 0

    # send emails
    for i in range(len(data_temp)):

        # check inbox and delete undelivered emails
        if counter_inbox_cleaner == 50:
            check_undelivered_emails(undelivered_emails_file, mail_object)
            counter_inbox_cleaner = 0

        # send email
        email_recipient = data_temp["EMAIL"].iloc[i]
        name = data_temp["NAME"].iloc[i]
        send_email_with_html(
            email_recipient,
            MAIL_OBJECT,
            mail_file,
            name,
            image_path_1=image_path_1,
            image_path_2=image_path_2,
            random_time_spacing=True)


    # modify the original dataset only for the chunksize adresses that have been contacted
    # only for the SENT column and the corresponding adresses
    data.loc[data["EMAIL"].isin(data_temp["EMAIL"]), "SENT"] = 1
    data.to_csv(dataset_file, index=False)

    # wait 4 minutes before sending the next chunk, cleans inbox meanwhile
    #time.sleep(2 * 60)
    check_undelivered_emails(undelivered_emails_file, mail_object)
    #time.sleep(2 * 60)




def main():
    """
    Continuously send emails to the first chunksize adresses that have not been contacted yet.
    Until all adresses have been contacted.


    Parameters:
    - None
    """

    # add a progress bar
    data = pd.read_csv(DATASET_FILE)
    size = len(data)

    del data
    
    for i in tqdm.tqdm(range(0, size, CHUNKSIZE)):
        emailing_and_clean_by_chunk()



if __name__ == "__main__":
    main()
    print("Last check of undelivered emails")
    time.sleep(30)
    check_undelivered_emails(UNDELIVERED_EMAILS_FILE, MAIL_OBJECT)
    print("End of the emailing process")
    check_undelivered_emails(UNDELIVERED_EMAILS_FILE, MAIL_OBJECT)