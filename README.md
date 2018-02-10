# flask-python-practice
Just some practice with Python, Flask, Postgresql, etc. Getting to know the environment. Please edit readme if I missed any steps. Add useful commands. 

# Setup
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

## Other Dependencies
1. read yaml files `pip install pyyaml`
### Run
* `flask run`
* go to http://127.0.0.1:5000/
you should see text on the page. If not, something went wrong. Try rerunning `./createDB.bash` or check permissions to story.
The text on the page is all the entries in the story column of the story table. If you then use postman or something similar, you should be able to add text to the story using a POST request to http://127.0.0.1:5000/publish. If these both work, everything is functioning properly.

# Commands
List of useful commands
### DB
* show table schema: `\d+ tablename`
* list users: `\du`
* list tables: `\dt`
