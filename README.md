# Meetup-Planner-using-Django

👋 Welcome to Meetup Planner! This is a web application built with Django that helps you plan your meetups with ease.

Table of Contents
Features
Installation
Usage
Contributing
License
Features
Users can sign up and log in to the application.
Users can create, view, update and delete meetups.
Users can join and leave meetups.
Users can view a list of all upcoming meetups.
Users can search for meetups by keyword and filter by category.
Users can view the profiles of other users and their upcoming meetups.
Installation
To get started with Meetup Planner, you need to have Python and pip installed on your system. Then, follow these steps:

Clone this repository:
bash
Copy code
git clone https://github.com/your-username/meetup-planner.git
Navigate to the project directory:
bash
Copy code
cd meetup-planner
Install the required packages:
bash
Copy code
pip install -r requirements.txt
Apply the database migrations:
bash
Copy code
python manage.py migrate
Create a superuser account:
bash
Copy code
python manage.py createsuperuser
Run the development server:
bash
Copy code
python manage.py runserver
The application will now be available at http://localhost:8000.

Usage
To use Meetup Planner, open your web browser and go to http://localhost:8000. From there, you can sign up or log in to your account, create and join meetups, and search for meetups by keyword or category.

Contributing
If you would like to contribute to Meetup Planner, you can follow these steps:

Fork this repository.
Create a new branch for your feature or bug fix.
Write your code and add tests if possible.
Submit a pull request.
License
Meetup Planner is licensed under the MIT License. See LICENSE for more information.
