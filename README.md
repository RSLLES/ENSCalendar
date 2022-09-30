# ENSCalendar
## Introductions
Ce repo est simplement un script `run.sh` qui :
- va récupérer le programme complet du MVA de l'ENS Paris - Saclay, supprime tous les cours que je ne suis pas (voir la liste dans le fichier `update_ens_calendar.py`) et enregistre le calendrier elagué sous le nom `calendar.ics`
- push les modifications

J'ai fait le choix dans `update_ens_calendar.py` de **supprimer les cours que je ne suis pas** plutôt que de **garder uniquement les cours que je suis**.
De cette façon, si un événement que je n'ai pas explicitement choisi de supprimer venait à apparaitre (ex : un seminaire, un partiel, ...) il resterait affiché.

## Quickstart
### Set up
- clone le projet
- selectionner les cours à supprimer dans `update_ens_calendar.py`
- rendre éxécutable `run.sh`: `chmod u+x run.sh`
- ajouter une éxecution périodique avec crontab

### Ajout dans un calendar
Il suffit de recupérer l'url de `calendar.ics` en raw et de l'interfacer avec un calendrier.
Par ex, dans mon cas, j'utilise : `https://raw.githubusercontent.com/RSLLES/ENSCalendar/main/calendar.ics`
