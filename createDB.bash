psql -U $USER -d postgres -c "CREATE DATABASE storyboard";
psql -U $USER -d storyboard -c "CREATE TABLE story( id SERIAL UNIQUE, story varchar(10000));"
psql -U $USER -d storyboard -c "INSERT into story(story) values('hey Sridhar this is Grant testing.');"

