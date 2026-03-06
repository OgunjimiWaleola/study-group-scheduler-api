# Study Group Scheduler API

This is a backend REST API that helps students create and manage study groups.

Students can:
- Create study groups
- Join or leave groups
- View upcoming study sessions
-Filtering by subject or date
- Pagination for group listings
Built with Django and Django REST Framework.


Installation & Setup

1. Clone the repo:
git clone https://github.com/OgunjimiWaleola/study-group-scheduler-api.git
   cd study-group-scheduler-api

2. Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate 

3. Install dependencies:
pip install -r requirements.txt

4. Run migrations:
python manage.py migrate

5. Start the server:
python manage.py runserver
Server runs at: http://127.0.0.1:8000/




API Endpoints
Authentication
Method	           Endpoint	                        Description
POST	        /api/register/	                  Register new user
POST	       /api/login/	                  Login user
GET	          /api/profile/	                 View profile
PUT	         /api/profile/	                 Update profile



Study Groups
Method	           Endpoint	                           Description
GET	              /api/groups/	                     List all groups
POST	         /api/groups/	                     Create a new group
GET	            /api/groups/<id>/	                 View a single group
PUT	           /api/groups/<id>/	                 Update group (creator only)
DELETE	      /api/groups/<id>/	                     Delete group (creator only)



Participation
Method	-               Endpoint	                  Description
POST	           /api/groups/<id>/join/	         Join a group
POST	          /api/groups/<id>/leave/	         Leave a group
GET	             /api/my-groups/	                 List groups user joined



Filtering & Pagination
Filter by subject:
/api/groups/?subject=Math


Filter by upcoming date:
/api/groups/?upcoming=true


Pagination:
/api/groups/?page=2


Notes:
All endpoints require authentication except registration and login.
Only group creators can update or delete groups.
Users cannot join past groups or join the same group twice.


API DOCUMENTATION

Base URL:
http://study-group-scheduler-api-production.up.railway.app/api/


Authentication
This API uses Token Authentication.
After login, the server returns a token which must be included in every request.

Header Format
Authorization: Token your_token_here


1. Register User

Create a new account.

Endpoint
POST /api/register/

Request Body
{
  "username": "waleola",
  "email": "waleola55@gmail.com",
  "password": "54190"
}

Response
{
  "message": "User created successfully",
}


2. Login User

Authenticate an existing user.

Endpoint
POST /api/login/
Request Body
{
  "username": "waleola",
  "password": "54190"
}


Response
{
  "message": "Login successful",
  "token": "your_generated_token"
}


3. POST /api/group/
Headers
Authorization: Token your_token
Request Body

body

{
  "title": "indicies",
  "description": "Deep dive into indicies",
  "subject": "mathematics",
  "location": "Zoom Meeting",
  "scheduled_date": "2026-05-10T18:00:00Z"
}


resonse

{
    "id": 9,
    "participants_count": 0,
    "title": "indicies",
    "subject": "mathematics",
    "description": "Deep dive into indicies",
    "location": "Zoom Meeting",
    "scheduled_date": "2026-05-10T18:00:00Z",
    "max_participants": 10,
    "created_at": "2026-03-06T18:29:16.046901Z",
    "created_by": 1,
    "participants": []
}


4. Get All Study Groups

Retrieve all available study groups.

Endpoint
GET /api/group/
Headers
Authorization: Token your_token

response

{
    "id": 9,
    "participants_count": 0,
    "title": "indicies",
    "subject": "mathematics",
    "description": "Deep dive into indicies",
    "location": "Zoom Meeting",
    "scheduled_date": "2026-05-10T18:00:00Z",
    "max_participants": 10,
    "created_at": "2026-03-06T18:29:16.046901Z",
    "created_by": 1,
    "participants": []
}


5. Join Study Group

Join an existing study group.
Endpoint
POST /api/group/{1}/join/

Example
POST /api/group/1/join/
Headers
Authorization: Token your_token
Response
{
  "message": "Successfully joined the study group"
}


6. Leave Study Group

Leave a study group.
Endpoint
POST /api/group/{1}/leave/

Example
POST /api/group/1/leave/
Headers
Authorization: Token your_token
Response
{
  "message": "You have left the study group"
}



7. Delete Study Group

Delete a study group (only the creator can delete).

Endpoint
DELETE /api/group/{1}/delete/

Example
DELETE /api/group/1/delete/
Headers
Authorization: Token your_token
Response
{
  "message": "Study group deleted successfully"
}


Status  Codes
Code	             Meaning
200	           Successful request
201	           Resource created
400	           Bad request
401	           Unauthorized
404	           Resource not found


