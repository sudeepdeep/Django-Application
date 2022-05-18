python manage.py migrate
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


Users - http://127.0.0.1:8000/users
    To create Team we can click on "Create Team" or click on this link - http://127.0.0.1:8000/users/createteam/
    To create Task and assign to a team we can click on "Create Task" or click on this link - http://127.0.0.1:8000/users/createtask/



Team Lead - http://127.0.0.1:8000/users/lead

Team Members - http://127.0.0.1:8000/users/member

All the users(user, teamlead, team members has been created in django admin - Create Users table, you can use them or create your own users there)




Database Tables: http://127.0.0.1:8000/admin

Create Tasks - to store Teamname, Task Name, Task Description
Create Users - to store role, name and email
Task Models - to store Name, Team Name, Task Name, Task Description, Status, Start Date, End Date.
Team Models - to store Name, Team Name, Role



Work Flow: 

User create team and it is stored in Team Models
User create task and it is stored in Create Tasks

Team Lead will assign the specific task to the team member or members and is stored in the Task Models.

Team Members can update the status in the Task Models later by going to this link(http://127.0.0.1:8000/users/member) and click on update status and then update.


All the Tasks Given by the User can be viewed in this link - http://127.0.0.1:8000/users/alltasks/ and we can check what is the status of the work.


Note:
To switch between multiple team members/team leads 
we have two variables in the views.py which are lead_name and the member_name.

we can change the values and go to the above mentioned links to see what tasks are assigned to that particular Team Lead/Team Member.


Requirements:

users create task and assign to team, create team - Done <br>
sending mail to team lead after assign to a team - Done <br>
team leader assign to team members - Done <br>
team members can update status - Done<br>
