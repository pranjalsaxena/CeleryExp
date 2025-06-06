# First import the Celery app instance from the mycelerymodule
from my_app import app

# Use this app instance to register tasks
@app.task
def adder(x, y):
    """
    A simple task that adds two numbers.
    """
    return x + y

@app.task
def multiply(x, y):
    """
    A simple task that multiplies two numbers.
    """
    return x * y


