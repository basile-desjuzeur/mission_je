# Mission JE

Points clés :
  
- envoi du [mail](./data/mail.html) (issu de word + signature) publiposté aux 9k clients de la [bdd cleané](./data/241003_cleaned_dataset.csv) (issue de l'excel) avec 
- 2 réponses possibles à ces mails :
  - destinataire n'existe pas : mail supprimé par [clean_not_send_email](./src/clean_inbox_unreachable_emails.py) et on ajoute l'adresse mail à [cette bdd](./data/undelivered_emails.csv) puis on update la [bdd à jour](./data/uptodate_dataset.csv) (pour pas relancer les inexistants et avoir un meilleur bench). Cette tâche s'automatise avec ce [script bash](./scripts/clean_inbox_unreachable_adresses.sh). Pendant toute la durée de l'envoi
  - destinataire a répondu : on supprime le mail avec [python](./src/clean_inbox_answers.py) autoamtisé avec [ce script bash](./scripts/clean_inbox_answers.sh)
  - follow up sur le dataset updaté (total - adresse manquantes - ceux qui ont répondu aux sondages)

Appel Noé :

- réduire les espaces 
- objet mail 
- quelle est le temps 
- espacement random des envois

## TODO

- Envoyer le template publiposté
  - objet
- script pour non recus
- cron pour le cleaning 
  - non recu : toutes les 30 secondes pendant le temps d'exécution de l'envoi 
  - cleaning 
- 2 Follow up    


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


 