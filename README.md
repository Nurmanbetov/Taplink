# Setup

The first thing to do is to clone the repository:

$ git clone https://gitlab.com/intern_jobs/taplink_group_2.git

Create a virtual environment to install dependencies in and activate it:

After you need to create new file called "firebaseConfig.js" 
in "assets/js" folder like it was written in firebaseConfig.example.js

$ virtualenv2 --no-site-packages env
$ source env/bin/activate

Then install the dependencies:

(env)$ pip install -r requirements.txt

And run the server:
(env)$ python manage.py runserver
