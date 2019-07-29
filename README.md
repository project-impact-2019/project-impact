# Project Impact
The goal of Project Impact is to provide an online platform for mentors to connect with foster children aging out of the system in order to help them navigate through life.

## Creating a Github Repository
- On Github, click "New" to create a repository
- Name the repository and click "Create Repository"
- On created repository, click "Clone or Download"
- Copy the repository URL 
- Create a directory in your terminal
- Clone your repository as follows:
```bash
git clone https://github.com/<username>/<repo-name>.git
```

## Setting up a Django Development Environment
- ```cd``` into your repository directory
- Run 
```bash
pipenv --three
```
- Run the following to install Django:
```bash
pipenv install django
```
- Run the following to enter your virtual environment:
```bash
pipenv shell
```

## Start Django Project
- Run 
```bash
django-admin startproject <project_name> .
```
**Note:** Your name for the project replaces project_name.  
**Important**: Remember to insert a "space" and a "." after project_name to avoid creating an extra directory.
- Create a .gitignore file by doing the following:
```bash
touch .gitignore
```  
```bash
open .gitignore
```  
- Copy content from [https://gitignore.io/api/python,visualstudiocode](https://gitignore.io/api/python,visualstudiocode) and paste into .gitignore file
- Create app for project:
```bash
python3 manage.py startapp <app_name>
```  
**Note:** Your name for the app replaces app_name. A common app_name is "core".

## Register the app
- Open **settings.py** and find ```INSTALLED_APPS```
- Add <app_name> to the bottom as follows:
```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_name', 
]
``` 

## Working in group projects
If you are working in a group project, you can create a branch from the origin/master branch to make a contribution to the project as follows:
```bash
git checkout -b <branch_name>
```  
**Note:** Your name for the branch replaces branch_name.  

Once you have finished your branch, you can push your branch to the repository as follows:
```bash
git push origin <branch_name>
```  

Create a pull request to merge the code from your branch with the master branch. After the merge, you can pull the updated master branch into your local master branch as follows:
```bash
git checkout master
git fetch upstream
git merge upstream/master
```  

To delete your branch, you can run the following:
```bash
git branch -d <branch_name>
```  

## Installing Debug Toolbar
Debug Toolbar is a helpful tool for debugging. Follow the directions at the following site:
[https://django-debug-toolbar.readthedocs.io/en/latest/installation.html](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)

## NPM and Django
1. Create a ```package.json``` file with contents ```{"private": true}```
2. Make sure ```node_modules/``` is in your ```.gitignore``` file.
3. Install ```browserify``` and ```watchify```: ```npm install browserify watchify```
4. Try using ```browserify``` on your current JS: ```npx browserify -o <output_file.js> <input_file.js>```
5. Add a ```scripts``` section to ```package.json```:
*content_copy*
```bash
{
  "scripts": {
      "start": "npm-run-all -p django start:js",
      "django": "python3 manage.py runserver",
      "start:js": "watchify -o core/static/compiled.js core/static/main.js",
      "compile:js": "browserify -o core/static/compiled.js core/static/main.js",
      "compile": "browserify -o core/static/compiled.js core/static/main.js"
  }
}
```  
6. Run the following to be have proper setup for using npm-run-all:
```bash
npm install -g npm-run-all
```
7. Use ```npm run start``` to start watching your input file for changes.

## Django Registration Redux
Django Registration Redux is a login/logout setup provided by Django. To set up, follow the directions at the following site: [https://django-registration-redux.readthedocs.io/en/latest/](https://django-registration-redux.readthedocs.io/en/latest/)

## Deploying to Heroku
- Create new app at [https://dashboard.heroku.com/new-app](https://dashboard.heroku.com/new-app)
- Log into the Heroku CLI: ```heroku login```. If you have not installed the CLI, go to [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli) to install it.
- Add ```heroku``` remote to your Git repository: ```heroku git:remote -a <app-name>```
- Install ```django-heroku``` in your Django app: ```pipenv install django-heroku```
- Add ```django-heroku``` to your ```settings.py``` At the bottom of ```settings.py```, add
```bash
# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())
```
- Commit your code after adding django-heroku.
- Install gunicorn in your Django app: ```pipenv install gunicorn.```
- Add a new file called Procfile: 
web: gunicorn <project_dir>.wsgi
- Commit your code after adding gunicorn and a Procfile.
- Push to Heroku: ```git push heroku master```. You will likely have a failure the first time. Debug.
- Run migrations on Heroku: ```heroku run python3 manage.py migrate```
- Create a superuser on Heroku: ```heroku run python3 manage.py createsuperuser```
- Set a secret key just for Heroku: ```heroku config:set SECRET_KEY=$(date | md5)```
- Once you are sure your app works, turn off ```DEBUG``` on Heroku.
- To turn off DEBUG, replace "DEBUG = True" in your settings.py with:
```bash
in_production = bool(os.getenv('PRODUCTION'))
DEBUG = not in_production
```
- And then run ```"heroku config:set PRODUCTION=True"```
