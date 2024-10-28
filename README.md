# Mission JE

Projet de publipostage de 14K + mails avec envoi de mail en masse et nettoyage de boîte de réception.

## Points clés :

- fonctionne sur une machine Windows avec Outlook, la configuration est conteneurisée avec Docker et les scripts sont en Python.

- pour des questions de confidentialité, les données sont stockées sur un autre serveur et les secrets sont gérés avec Bitwarden.

- envoi du [template de mail](./data/mail_initial.html) avec ce [script python](./src/send_emails.py) qui envoie des mails par paquets de 500 et nettoie régulièrement la boîte de réception. NB : **l'espacement entre deux mails correspond aux nombres de requêtes autorisées par minute par le serveur Outlook.**