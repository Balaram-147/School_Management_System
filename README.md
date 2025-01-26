School Management System:

This project is a School Management System built using Django, Django Rest Framework, and MongoDB.
The system allows administrators to manage students, teachers, schools, and other school-related data.

Key Features:

Manage Schools: Add and manage school details, including teachers and students.
Teacher Management: Create and manage teacher profiles.
Student Management: Track and manage student details like age, grade, and enrollment.
RESTful APIs: Built with Django REST Framework for efficient data interaction.
MongoDB Integration: Fast and flexible database for seamless data storage.

Technologies Used:

Backend: Django, Django REST Framework
Database: MongoDB
Language: Python

How to Run the Project:

Clone the repository:
git clone https://github.com/Balaram-147/School_Management_System.git
cd School-Management-System

Configure MongoDB in settings.py and apply migrations:
python manage.py makemigrations
python manage.py migrate

Start the server:
python manage.py runserver

Access the application:
API: http://127.0.0.1:8000/api/

API Endpoints:
/api/schools/: Manage schools
/api/students/: Manage students
/api/teachers/: Manage teachers

Future Plans:
Add authentication and authorization.
Build a frontend using ReactJS.
Deploy to cloud services.

Contributing:
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

Acknowledgments:
- Django and Django Rest Framework for providing a robust framework for building web applications.
- MongoDB for providing a scalable and flexible NoSQL database.
- The open-source community for providing valuable resources and support.
