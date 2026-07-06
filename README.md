# TweetApp

TweetApp is a Django project for creating, editing, deleting, and viewing user posts with optional image uploads.

## Stack

- Django 6.0.6
- SQLite
- Tailwind CSS
- django-browser-reload
- Pillow for image uploads

## Features

- User registration, login, and logout
- Create, edit, and delete tweets
- Tweet feed ordered by newest first
- Optional photo upload for each tweet
- Ownership checks so only the author can edit or delete a tweet
- Public site pages: home, about, contact, and privacy

## Project Structure

- `secondProject/` project settings, URLs, and public page views
- `tweets/` tweet model, forms, views, URLs, and templates
- `theme/` Tailwind app and base layout
- `templates/` shared site templates and auth pages
- `static/` static assets
- `media/` uploaded images

## Main Routes

- `/` home page
- `/tweets/` tweet feed
- `/tweets/create/` create tweet
- `/tweets/<id>/edit/` edit tweet
- `/tweets/<id>/delete/` delete tweet
- `/tweets/register/` register account
- `/accounts/login/` login
- `/accounts/logout/` logout
- `/about/` about page
- `/contact/` contact page
- `/privacy/` privacy page

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run migrations:

```bash
python manage.py migrate
```

4. Start the development server:

```bash
python manage.py runserver
```

## Notes

- Media uploads are stored in `media/photos/`.
- Tailwind is loaded through the `theme` app.
- Login is required for creating, editing, and deleting tweets.

# tweets app (part of project)

The `tweets` app provides the core post management feature set for TweetApp.

## Responsibilities

- Store tweet content and optional images
- Expose CRUD views for tweets
- Restrict edit and delete actions to the tweet owner
- Provide the registration form used by the auth flow

## Model

- `Tweets`
  - `user`: foreign key to `auth.User`
  - `text`: tweet body
  - `photo`: optional image upload
  - `created_at`: auto-created timestamp
  - `updated_at`: auto-updated timestamp

## Forms

- `tweet_form` for creating and editing tweets
- `UserRegistrationForm` for new user sign-up

## Views

- `tweet_read`: lists tweets newest first
- `tweet_create`: creates a tweet for the current user
- `tweet_edit`: updates the current user’s tweet
- `tweet_delete`: deletes the current user’s tweet
- `register`: creates a user account and logs the user in

## URLs

- `/tweets/`
- `/tweets/create/`
- `/tweets/<id>/edit/`
- `/tweets/<id>/delete/`
- `/tweets/register/`