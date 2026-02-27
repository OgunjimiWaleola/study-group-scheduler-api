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