# Mission JE

Points clés :
  
- envoi du [mail](./data/mail.html) (issu de word + signature) publiposté aux 9k clients de la [bdd cleané](./data/uptodate_dataset.csv) (issue de l'excel) avec [ce script python](./src/send_emails.py) qui envoie des mails par paquets de 500 et nettoie régilièrement la boîte de réception

- réponses possibles à ces mails 
  
  - destinataire n'existe pas : mail supprimé par [clean_not_send_email](./src/clean_inbox_unreachable_emails.py) et on ajoute l'adresse mail à [cette bdd](./data/undelivered_emails.csv) puis on update la [bdd à jour](./data/uptodate_dataset.csv) (pour pas relancer les inexistants et avoir un meilleur bench). 

  - destinataire a répondu : on supprime le mail avec [python](./src/clean_inbox_answers.py) automatisé avec [ce script bash](./scripts/clean_inbox_answers.sh) qui tourne toutes les 15 minutes pendant 1 mois 

  - confirmation anti spam 
  - le destinataire n'est plus dans la boîte / en vacances "automatic reply"

(en réalité une troisième voix : besoin de reconfirmer)

- follow up sur le dataset updaté (total - adresse manquantes - ceux qui ont répondu aux sondages)
****

## TODO

- check hourly rate https://learn.microsoft.com/fr-fr/office365/servicedescriptions/exchange-online-service-description/exchange-online-limits#receiving-and-sending-limits
- message limit exceeded
- faire analytics et renvoi


- Follow up  : 
  - changer object
  

## DONE

- Réception mail Noé
- Clean dataset 
    - create csv
    - remove analysts ...

- Prepare outlook
  - create junk
  - test send email and test rule
  - if in csv then delete

- Tests
  - avec eux
  - interne

- Follow up  : 
  - faire template mail

 