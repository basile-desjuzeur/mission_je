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

## TODO

Le nombre de requêtes au serveur Outlook est limité :

  -max : 30 message par minute => 2.5 secondes d'espacement par message

  -max : 200 destinataires par message => OK

  -max : 10000 messages par jour => OK

(source : service IT)

- Follow up  : 
  - changer object
  - check rendu (boxes ?)


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

 
