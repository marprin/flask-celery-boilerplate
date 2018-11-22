How to Setup?
-------------

A. Setup using virtual environment
----------------------------------

1. Install virtualenv for encapsulate the environment
2. Create the virtual environment
   `virtualenv -p python3 venv`
3. Activate the virtualenv
   `. venv/bin/activate`
4. Install the requirements
   `pip3 install -r requirements/local.txt`
5. Run the server
   `./runserver`
   The app will run on port 5000

B. Setup using Docker
---------------------
Just run 
```sh
$ docker-compose up
```

And the application will run on port 9300 for http, 9400 for flower (background task monitoring)


Running Test
------------

```sh
$ ./runtest
```

Shell
-----

```sh
$ ./shell
```

The purpose of putting the tasks inside registered_tasks.py file is because easier to register the task and prevent us to add more worker later.
To setup the schedule of background tasks, just register on settings.py file.