# !/bin/bash
python3 -m update_ens_calendar
git add .
git commit -m "$(date +'Update %d %B %Y, %H:%M')"
git push