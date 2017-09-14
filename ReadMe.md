Run the following commands before commiting:

These commands will delete all the .pyc files and db.sqlite3 from local as well as remote repo.
```cd path/to/hackocracy
git rm *.pyc
git rm db.sqlite3
git commit -a -m "removed .pyc files and db.sqlite3"
git push origin master```

#Using this we can ignore .pyc and db.sqlite3 for further commits
```touch .gitignore
echo 'db.sqlite3' >> .gitignore 
echo '*.pyc' >> .gitignore```
