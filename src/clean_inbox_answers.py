##########################################################################
# Script Name  : clean_inbox_answers.py
# Description  : Removes potential emails from clients that have been contacted
# Auteur       : basiledesj@hotmail.fr
# Date : 2024/10/05
##########################################################################

###### PARAMETERS #######

CLIENT_LIST = "./data/241003_cleaned_dataset.csv"


from utils import remove_emails_from_clients

if __name__ == "__main__":
    remove_emails_from_clients(CLIENT_LIST)
