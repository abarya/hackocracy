Run the following commands before commiting:

cd path/to/hackocracy

git rm *.pyc

git rm db.sqlite3

git commit -a -m "removed .pyc files and db.sqlite3"

git push origin master