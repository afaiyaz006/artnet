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
Alternatively 
# For Docker
Just pull the repo

pull the docker image
```
docker pull faiyaz006/artnet
```

then just run
```
docker run -p 8000:8000 -it faiyaz006/artnet:1.0 /bin/sh
python manage.py runserver 0.0.0.0:8000
```
You can then access the webserver from http://127.0.0.1:8000


