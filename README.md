# DJANGO-HTMX-MECHANISM
[link to Git-Hub source files](https://github.com/RobertoRubertelli/Django-HTMX-mechanism)

####
if you know Django but not HTMX or you are a beginner in studying Django, 
the app is useful to understand the mechanism of HTMX.
I've tried to make the code as simple as possible to highlight the mechanism of HTMX.
Install the Django-htmx library in the project is a must.
I've used in the templates the following hx command:
hx-get
hx-post
hx-delete
hx-confirm
hx-patch
hx-target
CRUD in the app is completed with them.
Give a look in the _base.html to:
body hx-headers='{"X-CSRFToken": "{{ csrf_token }}"}'
Without it Django will return an error 403 in every request.POST by HTMX

You can run the code demo here [managepy.it/demo/]()

You can see the tutorial [managepy.it/demo/mechanismtutorial](https://www.managepy.it/homedemo)


My Site [Managepy.it](https://www.managepy.it/)


## Getting started

## Setup

Follow these instructions to try this demo out locally.
I'm using pipenv, you can use pip instead for the virtual environment and install.

```bash

# Install requirements.txt in a new virtual environment
pipenv install -r requirements.txt
# activate the shell
pipenv shell

# Clone Git folders yourself

# Setup database.
./manage.py migrate

# Run the development server.
./manage.py runserver

# Now you can view the project at http://localhost:8000
```
