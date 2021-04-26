# nathandias.com

A website displaying my web developer and programmer portfolio, resume and contact info.

# dreamhost setup
1. enable Passenger on the dreamhost domain
2. install asdf, poetry and direnv locally
3. login to domain via ssh
4. `mkdir -p /home/<username>/<domain>/public/`
5. `cd /home/<username>/<domain>/public/`
6. `git clone git@github.com:nathandias/nathandias.com.git`
7. `cd nathandias.com`
8. `cp passenger_wsgi.py.template /home/<username>/passenger_wsgi.py`
9. customize passenger_wsgi.py (i.e. fill out SECRET_KEY, MYSQL_* settings, etc.) with domain/site specific values
10. poetry install
11. direnv allow
12. `python manage.py collectstatic`
13. `mkdir -p ~/<domain>/public/media/images`

# if restarting site from scratch
1. `python manage.py makemigrations`
2. `python manage.py migrate`
3. `python manage.py collectstatic`

# if rebuilding site using existing dumped data
0. on a different host running the site: `python manage.py dumpdata --indent=4 > dumpeddata.json`
1. `python manage.py loaddata dumpeddata.json`


