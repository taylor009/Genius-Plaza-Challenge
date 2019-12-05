# Genius-Plaza-Challenge

### Project Description:
>- REST APIs using Django REST Framework for creating recipes to a postgres database.
### Project Overview:
- Entire project will run from docker-compose including postgres and pgadmin.
- Simple bash script to freeze pip decencies.
- bash script to run the django sql migration and create the superuser for the admin.

### Running project Instructions:
>Inside of the project directory run
1. `$ docker-compose up` - This build pull and build all docker containers.

1. Server base url: `http://localhost:8000`

1. Server Admin url: `http://localhost:8000/admin`
    >Admin user credentials:
    - username: admin
    - password: pass

### Recipe-Endpoints:
 - INDEX: `recipes`
 - CREATE: `recipes/`
 - READ: `recipes/<int:id>`
 - UPDATE: `recipes/<int:id>`
 - DELETE: `recipes/<int:id>`

 ### Step-Endpoints: 
 - CREATE: `steps/`
 - READ: `steps/<int:id>`
 - UPDATE: `steps/<int:id>`
 - DELETE: `steps/<int:id>`

### Ingredient-Endpoints:
 - CREATE: `ingredients/`
 - READ: `ingredients/<int:id>`
 - UPDATE: `ingredients/<int:id>`
 - DELETE: `ingredients/<int:id>`
 
### High level additions to add in the future:
- Django test cases with code coverage
- CI/CD integration with Jenkins

### High level notes:
- For production purposes remove postgres database from docker container 
and move to dedicated service. As this is really only for development. Running databases
inside of containers will lead to data inconsistencies due to the fact that you have your 
data mounted from a volume.



