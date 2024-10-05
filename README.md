# Mission JE

Points clés :
  
- envoi du [mail](./data/mail.html) (issu de word + signature) publiposté aux 9k clients de la [bdd cleané](./data/241003_cleaned_dataset.csv) (issue de l'excel) avec [ce script python](./src/send_emails.py)


- 2 réponses possibles à ces mails :
  - destinataire n'existe pas : mail supprimé par [clean_not_send_email](./src/clean_inbox_unreachable_emails.py) et on ajoute l'adresse mail à [cette bdd](./data/undelivered_emails.csv) puis on update la [bdd à jour](./data/uptodate_dataset.csv) (pour pas relancer les inexistants et avoir un meilleur bench). 

  - destinataire a répondu : on supprime le mail avec [python](./src/clean_inbox_answers.py) automatisé avec [ce script bash](./scripts/clean_inbox_answers.sh) qui tourne toutes les 15 minutes pendant 1 mois 


  - follow up sur le dataset updaté (total - adresse manquantes - ceux qui ont répondu aux sondages)


## TODO

- remove sapcing
- cron pour le cleaning 
  - non recu : toutes les 30 secondes pendant le temps d'exécution de l'envoi 
  - cleaning 
- 2 Follow up  : faire template mail


## DONE

- Réception mail Noé
- Clean dataset 
    - create csv
    - remove analysts ...

- Prepare outlook
  - create junk
  - test send email and test rule
  - if in csv then delete

- test avec eux


 