# coding: utf-8
def add(x, y):
    """Додає два числа."""
    return x + y

def subtract(x, y):
    """Віднімає друге число від першого."""
    return x - y

def multiply(x, y):
    """Множить два числа."""
    return x * y

def divide(x, y):
    """Ділить перше число на друге."""
    if y == 0:
        raise ValueError("Ділення на нуль неможливе!")
    return x / y



    # docker run -u root -d --rm --name jenkins -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home -v /var/run/docker.sock jenkins/jenkins:2.440.2