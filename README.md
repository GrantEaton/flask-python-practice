# flask-python-practice
Just some practice with Python, Flask, Postgresql, etc. Getting to know the environment. Please edit readme if I missed any steps. Add useful commands. 

# Setup


### Dependencies
1. install postgresql `brew install postgresql`
2. install Flask `pip install flask`
3. read yaml files `pip install pyyaml`

### DB
Our database is setup through AWS. If you need to make your own, follow [these instructions](http://duspviz.mit.edu/tutorials/intro-postgis.php) to learn how to set up postgis on AWS. Also check out "DB Setup" below. 

In order to connect to the AWS db, you need to provide four things in a file named `.creds.yml`. 
The file should be formatted like:
```
 AWS:
      HOST:       '<host aka endpoint>'
      PORT:       '<port>'
      USER:       '<username>'
      PASSWORD:   '<password>'
```
Assuming you have an AWS hen run the app, you should be automatically connected.

### Other
1. set default flask file `export FLASK_APP=hello.py`

### Run
* `flask run`
* go to http://127.0.0.1:5000/
You should see text on the page. If not, something went wrong. Try rerunning `./createDB.bash` or check permissions to story.
The text on the page is all the entries in the story column of the story table. If you then use postman or something similar, you should be able to add text to the story using a POST request to http://127.0.0.1:5000/publish. If these both work, everything is functioning properly.

# Commands
List of useful commands
### DB
* show table schema: `\d+ tablename`
* list users: `\du`
* list tables: `\dt`

### DB Setup
Note: the database is already setup on AWS, however I'm saving these commands in case it needs to be redone.

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
