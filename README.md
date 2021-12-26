# BriteCore-Insurance-System
Welcome to BriteCore Insurance System. The project's goal is to build in one week a system that enables Insurers to define their own data model, and for that, was provided a fully tested API to allow interaction by any frontend system, such as VueJS.

In summary, this project was created using MySQL to create a dynamic data model, Django Restful framework for the backend API, and the frontend was built using the modern javascript framework VueJS.

For that, was created two internal projects, one called by backend and another called by frontend, and the communication between them was done through the REST pattern. The DevOps base was built using Docker, Docker-compose, and Amazon AWS to deploy it.

## What was done

###  Data
Two data models were created, one that was implemented as an MVP ( Minimum Viable Product) and another to be the best approach, but consequently, would spend more time.

Here are (The MVP and the best approach): ***(My personal bonus)**
* https://github.com/geovanecomp/BriteCore-Insurance-System/blob/master/docs/model/Implemented%20MVP.jpeg
* https://github.com/geovanecomp/BriteCore-Insurance-System/blob/master/docs/model/Best%20approach%20model.jpeg

### Backend
* The backend was built using the community best practices and TDD oriented, with that, the API was fully tested (around 50 tests!). The API was created using the framework Django 2.0 and python 3.6.

* The API is prepared for all HTTP verbs / REST. It means anyone is able to request a full CRUD of risk types, risk, field types, fields, and fields by risk. ***(My personal bonus)**

Here are a few localhost API screens:
* https://github.com/geovanecomp/BriteCore-Insurance-System/blob/master/docs/api/api_root_page.jpeg
* https://github.com/geovanecomp/BriteCore-Insurance-System/blob/master/docs/api/fields_by_risk_list.jpeg
* https://github.com/geovanecomp/BriteCore-Insurance-System/blob/master/docs/api/structure_documentation.jpeg
* https://github.com/geovanecomp/BriteCore-Insurance-System/blob/master/docs/api/api_interaction.jpeg

### Frontend
* The frontend was built using the modern javascript framework Vuejs, HTML5, CSS3 / Sass. 

* Three pages were created, one to make all CRUD API requests for Risk Types, one to simulate how to create the riks and their fields (_almost finished_), and finally the main page, which gets all risk fields and shows them in an appropriate way.  ***(My personal bonus)**

Here are a few frontend screens:
* https://github.com/geovanecomp/BriteCore-Insurance-System/blob/master/docs/system/welcome_page.jpeg
* https://github.com/geovanecomp/BriteCore-Insurance-System/blob/master/docs/system/risk_type_crud.jpeg
* https://github.com/geovanecomp/BriteCore-Insurance-System/blob/master/docs/system/manage_risks.jpeg
* https://github.com/geovanecomp/BriteCore-Insurance-System/blob/master/docs/system/main_screen.jpeg

### Devops ***(My personal mega bonus)**
* The project was built using Docker and Docker-compose, with that anyone can make an easy and faster installation using these containers. With that, for example, was really easy to deploy the application to the AWS (Amazon Web Services).


## How to execute a developer version
1. Download and install Docker (Version 3);
2. Download and install Docker-compose;
3. Clone this project;
5. From the project root folder execute to build and up the containers: `docker-compose -f docker-compose.yml -f docker-compose.development.yml up --build`;
6. Access the backend container and execute the script *db_initialize.sh* to populate the database: `docker-compose -f docker-compose.yml -f docker-compose.development.yml exec backend bash -c "sh db_initialize.sh"`;
7. Access `http://localhost:8080` to open the software or `http://localhost:8000` to open the API documentation.
8. Finally, have fun =).

## How to execute the production version (Temporary Off)
 1. Just access: http://ec2-54-198-232-208.compute-1.amazonaws.com/


##

For questions, critiques or compliments, send me an email: geovane.pacheco99@gmail.com
