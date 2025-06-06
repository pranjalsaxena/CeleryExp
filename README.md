# My Celery Experiments

This repo consists basic Celery Experimentation Rig.
I have also written a Medium article for this, please read it here.
Follow these steps to setup this rig in your machine.

a. Run setup.ps1
<br>b. Install Docker and Redis Image
<br>c. Start required processes
<br>d. Happy Experimenting

## a. Run setup.ps1
This will:
<br>i. Create a python virtual environment in your local.
<br>ii. Activate the virtual environment.
<br>iii. Install required python packages in your virtual environment.

```
(base) PS C:\code\CeleryExp>.\setup.ps1

# Once the above script completes the PS prompt will change to below
(venv) (base) PS C:\code\CeleryExp>
```

## b. Install Docker and Redis Image
Go to this [link](https://medium.com/r/?url=https%3A%2F%2Fdocs.docker.com%2Fdesktop%2Fsetup%2Finstall%2Fwindows-install%2F) to find docker installation steps. Once installed, run below command to install Redis Image.

```
(venv) (base) PS C:\code\CeleryExp>docker pull redis
```

## c. Start required processes
Before we run any of the cells in the celery.ipynb notebook. We need to start redis process for message broker and result backend and also we must start a Celery worker process for running Celery tasks.
Therefore, open a new powershell windows and do the following to start the redis process inside a docker container: 

```
# First Time Run
# Creating and starting a new docker container 
# using Redis Image with 6379 port
docker run --name redis -p 6379:6379 -d redis

# Subsequent Runs 
# Once a container with name 'redis' is created, 
# using above command will raise error
# Hence using below command to run the already created container
docker start redis
```

Then open another powershell window, cd to the local clone and do the following to start the Celery worker process:

```# First we need to activate the virtual environment
venv\Scripts\Activate.ps1

# Then we need to start celery worker
# Notice we are using the 'my_app' celery app name to start worker
celery -A my_app worker --loglevel=info -P solo
```

## e. Happy Experimenting

We are now set to start experimenting with Celery. 
In the celery.ipynb, run the first cell to import required modules. Make sure to choose the virtual environment setup under your CeleryExp cloned directory while running any cell in the Jupyter Notebook.

```
# importing the 'app' from my_app module
from my_app import app

# importing the tasks from tasks.py
from tasks import adder, multiply
```

Then, we will call a task asynchronously with required parameters using delay() method.

```
res = adder.delay(53,5)
# Saving the AsyncResult object in res for further tracking
```

Then we will wait for the task to finish using ready()

```
while not res.ready():
    pass
```

Finally, we can get the result using get()
```
res.get()
```


