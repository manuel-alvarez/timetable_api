# Timetable API

Testing new apistar framework (https://github.com/tomchristie/apistar) applied to my school timetable database scheme.

## Installation

In order to test it locally, first you need to have **Python 3.6** and **pip** installed in your computer. We recommend to use **VirtualEnv** too. It's very useful to avoid install all libraries in the main environment.

Then, install all dependencies with

```
pip3 install -r requirements
```

You'll need to create the database too:

```
apistar create_tables
```

## Usage

Once installed and created the database, you can run the project writing:

```
apistar run
```

Now open a browser and go to http://localhost:8080/ url to see it working.

## Heroku

Project is ready to be deployed in an Heroku instance, so you'll find both `runtime.txt` and `Procfile` to be able to properly run it.
