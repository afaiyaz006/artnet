# artnet
Artnet is a photo sharing social network with a simple twist: it transforms photos into artwork based on user given style and also styles from famous artwork.User can like or comment on certain artpost.It is a group project for our cse-322 software engineering course.

# Installation
First clone the repository
```
git clone https://github.com/afaiyaz006/artnet
```
Change directory to artnet
```
cd artnet
```
Activate pipenv virtual enviroment
```
pipenv shell --python 3.10
```
Install necessary packages needed for the project
```
pipenv sync
```
This will take time depending on the bandwith.

# Run
cd the directory
```
cd artnet
```
Make necessary migrations
```
python manage.py makemigrations
```
Migrate the databases
```
python manage.py migrate
```
Runserver by typing
```
python manage.py runserver
```
