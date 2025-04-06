![Screenshot (316)](https://github.com/user-attachments/assets/ce52f628-1e34-4fe3-8c69-2347bc0046d0)# Quiz Platform (Backend)

A simple REST API for a quiz platform using Django REST Framework.
User Roles and Features
1. Admin
- Can register and login
- Can create categories
- Can create quizzes
- Can add questions with 4 options and mark the correct answer
- Can activate or deactivate quizzes and questions
- Can view all user submissions with their scores
2. Normal User
- Can register and login
- Can view all active quizzes
- Can submit answers for a quiz
- Can view their own quiz history and scores

Core Functionalities
Admin
- Add/edit categories
- Add/edit quizzes
- Add questions to a quiz (4 options, one correct)
- Activate/deactivate quizzes and questions
- View quiz submissions from all users
User
- View all active quizzes
- Attempt quizzes by submitting answers
- Automatically get scored based on correct answers
- View past quiz submissions and scores
Authentication
- JWT-based authentication using `SimpleJWT`
- Role-based permissions (Admin or Normal User)
Project Structure
- Models: Custom user, Quiz, Question, Option, Submissions
- Serializers: For all models and quiz submission handling
- Views: Functionality for admin and user actions
- URLs: Organized routes for all features

  ![Screenshot (321)](https://github.com/user-attachments/assets/be0e811f-2de5-40de-93ad-fdc983879fc3)
![Screenshot (320)](https://github.com/user-attachments/assets/fb3a8442-01df-4188-94f6-99806901e4ea)
![Screenshot (319)](https://github.com/user-attachments/assets/ae4f970b-2f26-482a-8286-2baf3cf08d2c)

![Screenshot (316)](https://github.com/user-attachments/assets/9f3872d0-534a-4850-a92d-76912d3200da)
![Screenshot (317)](https://github.com/user-attachments/assets/f133ef91-af26-40c6-87b4-dbf848332cdb)
![Screenshot (318)](https://github.com/user-attachments/assets/ff58ba13-1883-4ed8-9c0c-2d3d2ede9192)
