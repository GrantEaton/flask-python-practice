# flask-python-practice
Just some practice with Python, Flask, Postgresql, etc. Getting to know the environment. Please edit readme if I missed any steps. Add useful commands. 

# setup
1. install postgresql `brew install postgresql`
### DB
Note: im going to work on automating this setup, but requirements.txt wasnt working with `pip install` for me.

1. start postgres `psql postgres`
2. set default password for postgres `\password postgres`
3. quit postgres `\q`
4. create new user `createuser story --createdb` and superuser`createuser -s -U $USER`
5. log into user `psql postgres -U story`
6. create db and table
  * `chmod +x createDB.bash` `./createDB.bash`
7. grant yo'self priviledges `GRANT ALL PRIVILEGES ON DATABASE storyboard TO storyboard;`
8. grant priviledges to table `GRANT ALL PRIVILEGES ON TABLE story TO storyboard;`
9. install pysycopg2 `pip install pyscopg2`

### Flask
1. install Flask `pip install flask`
2. set default flask file `export FLASK_APP=hello.py`

### Run
`flask run`

# commands
List of useful commands
### DB
* show table schema: `\d+ tablename`
* list users: `\du`
* list tables: `\dt`
