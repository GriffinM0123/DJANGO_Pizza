#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Pizzeria.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

'''
<p>
    <a href="{% url 'pizzas:index' %}">Joey's Pizzeria</a>
    <a href="{% url 'pizzas:pizzas' %}">Pizzas</a>
</p>

{% block content %} 



{% endblock content %} 


Index

{% block content %}
<p>The Best Pizza in the state!</p>
{% load static %} 
<img src="{% static 'pizzas/images/Home1.jpg' %}">
{% load static %} 
<img src="{% static 'pizzas/images/Home2.jpg' %}">

{% endblock content %} 
'''