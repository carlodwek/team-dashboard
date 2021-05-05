# Team Dashboard App

Hello user!

This app allows you to check the latest scores and standings of your favorite football team. You will have the option to choose both the league and team that you wish to check out.

Follow the instructions below to get started!

## Installation

Fork [this repo](https://github.com/carlodwek/team-dashboard), then clone or download the forked repo onto your local computer. Then, navigate there from the command-line:

```sh
cd ~/Desktop/team-dashboard
```

Go ahead and use Anaconda to create and activate a new virtual environment, perhaps called "dashboard-env":

```sh
conda create -n dashboard-env python=3.8
conda activate dashboard-env
```

Then, within an active virtual environment, install the required packages:

```sh
pip install -r requirements.txt
```

## Usage
Code to run the app:

```sh
export FLASK_APP=web_app
flask run
```

## Testing
If you wish to run tests, please write this code in your command-line:
```sh
pytest
```
## Deploying
Please follow the deployment instructions to deploy the app to a remote server.

Please, go ahead and [sign up for a Heroku account](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/heroku.md#prerequisites) and [install the Heroku CLI](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/heroku.md#installation), and make sure you can login and list your applications.

```sh
heroku login # just a one-time thing when you use heroku for the first time

heroku apps #to check your apps
```

## Server Setup

> IMPORTANT: run the following commands from the root directory of your repository!

Use the online [Heroku Dashboard](https://dashboard.heroku.com/) or the command-line (instructions below) to [create a new application server](https://dashboard.heroku.com/new-app), specifying a unique name (e.g. "dashboard-app-123", but yours will need to be different):

```sh
heroku create dashboard-app-123  #remember to choose your unique name
```

Verify the app has been created:

```sh
heroku apps
```

Also verify this step has associated the local repo with a remote address called "heroku":

```sh
git remote -v
```

## Deploying

You are now ready to deploy the application's source code to the Heroku server:

```sh
git push heroku main
```
> NOTE: If you wish to update your code, you can repeat this easy step to upload your new code onto the server.

## Running the Script in Production

Once you have deployed the source code to the Heroku server, login to the server to see the files there, and test your ability to run the script that now lives on the server:

```sh
heroku run bash #login to the server

# alternatively you can run it from your computer in "detached" mode:

heroku run "python -m app.team_dashboard"
```
Now, you are all set. Enjoy our app!

## Future DEVELOPMENT
Time Zone
Local Database for more efficient API calls
Tournament full compatability
