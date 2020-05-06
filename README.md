# GroupProject [![Build Status](https://dev.azure.com/PrizeGenerator/PrizeGenApp/_apis/build/status/PrizeGenApp-Docker%20container-CI?branchName=przgen)](https://dev.azure.com/PrizeGenerator/PrizeGenApp/_build/latest?definitionId=3&branchName=przgen)
# Prize Generator Application
A group project to fulfill the DevOps GMCA Project Specifications
 
## Index
* [Brief](#brief)
* [Solution](#solution)
* [User Stories](#user_stories)
* [Risk Assessment](#risks)
* [Kanban!](#kan)
* [Entity Relationship Diagrams](#erd)
* [Testing](#testing)
* [Deployment](#deployment)
* [User Web Interface](#UWI)
* [Relevant Information and Links](#rel)
 
 
<a name="brief"></a>
## Brief
Our client has a requested that our group create a prize generator application. 
At the click of a button, the user will be presented on screen with a randomly generated code. 
The code must contain three randomly generated letters and six randomly created digits, for example hsy653471.

The generated code will be automatically tested to ensure that it meets the following conditions:

•	If the first letter is an ‘a’ there is a 25% chance of winning £100, and 75% to win £50 otherwise.

The generated codes and their output (prize status) must be stored in a database. 

The application must run as four separate, yet inter-connected services.

For services number 2, number 3 and number 4 we need to create two different implementations. 

We must be able to demonstrate swapping these implementations out for each other seamlessly, without disrupting the user experience. 

This allows the client to make any updates without the application being effected.  


<a name= 'solution'></a>
## Solution
 
To provide a solution for our client we aim to utilise the supporting tools, technologies and methodologies covered during training in the academy. We will approach each area of the project with a DevOps mindset aiming to produce a high-quality application with clear communication and cooperation between the members of the group. For this we have decided the following:
 
* Adopt Agile methods to manage our project
* Perform risk assessments using the outline covered during the training
* Implement Kanban method using Trello (later Projects on Azure DevOps).
* Build database ERD using Draw.io
* Create Git repository to be our VCS (subsequently migrated to Azure DevOps repo).
* Use MySQL server, HTML5, CSS3 , Python, Flask and a few more python modules  to build and test the application (refer to the requirements.txt for more details )
* Host the Application (MySQL Database Server, Linux Web Application Server and Linux server hosting the automated deployment server for continuous integration ‘Jenkins’ ) on Google Cloud Platform ( free tier )
* Build containers for the separate micro-services that are part of the project
* Integrate automation where possible in line with the DevOps mindset 
* Test the application
* Deploy the application using an orchestration tool
* Migrate the application to Azure DevOps CI Pipeline and orchestration tool for seamless rolling updates

<a name="user_stories"></a>
## User Stories

<img src="documentation/user_stories1.png" alt="User Stories" width="90%" height="90%"/>


<a name="risks"></a>
## Risk Assessment

<img src="documentation/Risk_Assessment_1.png" alt="Risk Assessment" width="90%" height="90%"/>

<img src="documentation/Risk_Assessment_2.png" alt="Risk Assessment" width="90%" height="90%"/>

<img src="documentation/Risk_Assessment3.png" alt="Risk Assessment" width="90%" height="90%"/>
 

<a name="kan"></a>
## Kanban Board
A regularly updated Trello board - see https://trello.com/b/EiUrPxd9/group-1-devops -  kept track of sprints, user stories, progress resolving issues and to-do list/task backlog. 

This was extremely useful for planning and managing our work as a geographically separated team as we were completing the project by working remotely.

<img src="documentation/trello1.png" alt="Trello Board" width="90%" height="90%"/>

<img src="documentation/trello2.png" alt="Trello Board" width="90%" height="90%"/>
 
<a name="erd"></a>
## Entity Relationship Diagrams
#### Initial ERD plan
 
<img src="documentation/Grp1-proj-init-ERD.png" alt="Prize Generator ERD" width="60%" height="80%"/>

<a name="testing"></a>
## Testing
The Testing for the application was done using pytest module. It tests the different microservices used for the application:
- the random number generator
- random text generator
- prize generator
- front-end prize generator page

### Number Generator
<img src="documentation/numgen-coverage.PNG" alt="Number Generator Coverage" width="100%" height="100%"/>

### Text Generator
<img src="documentation/txtgen-coveerage.PNG" alt="Text Generator Coverage" width="100%" height="100%"/>

### Prize Generator
<img src="documentation/przgen-coverage.PNG" alt="Prize Generator Coverage" width="100%" height="100%"/>

### Front-end Prize Generator Page
<img src="documentation/prize_frontend-coverage.PNG" alt="Prize Frontend Coverage" width="100%" height="100%"/>

<a name="UWI"></a>
## User Web Interface
 
### Home Page without Login
<img src="documentation/home_page.png" alt="Home Page" width="100%" height="100%"/>
 
### Registration Page
<img src="documentation/reg_page.png" alt="Registration Page" width="100%" height="100%"/>
 
### Login Page
<img src="documentation/login_page.png" alt="Login Page" width="100%" height="100%"/>
 
### Generate Code Page
<img src="documentation/gen_code.png" alt="Generate Code Page" width="100%" height="100%"/>

### Stored Codes Page
<img src="documentation/stored_codes.png" alt="Stored Codes" width="100%" height="100%"/>

### Manage Account Page
<img src="documentation/manage_acc.png" alt="Manage Account Page" width="100%" height="100%"/>
