📱 Social Media API

This project is a Social Media API built with Django and Django REST Framework (DRF) as part of the ALX Django Learn Lab program.
It includes a custom user model, token-based authentication, and profile management features.

🚀 Features

Custom User Model with extended fields:

bio → Text field for user biography

profile_picture → Optional image upload

followers → Many-to-many relationship with other users

Authentication:

User registration with token generation

User login with token retrieval

Token-based authentication using DRF

Profile Management:

View user profiles

Update user profiles

🧑‍💻 User Model Overview

The custom user model extends Django’s AbstractUser and adds:

bio → A short text field for a user’s biography or description

profile_picture → An optional image field for profile pictures

followers → A many-to-many field that lets users follow other users