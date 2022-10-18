# 3X03-Team39-2022
## Healthcaretether web application
This web application requires the use of Docker to build. Refer to https://docs.docker.com/engine/install/ for installation instructions
## How to run
Navigate to root of project folder in the terminal.
```
docker-compose -f docker-compose.yml up -d --build
```
This builds and runs the 3 containers required, django, postgres, and nginx.

```
docker-compose -f docker-compose.yml exec web python manage.py migrate --noinput
```
This command migrates the django models into the database.
```
docker-compose -f docker-compose.yml exec web python manage.py collectstatic --no-input --clear
```
This command allows the web application to find static files through nginx.

Web application should be live at http://localhost:1337. To run commands for django, use 
```
docker-compose -f docker-compose.yml exec web python manage.py <command>
