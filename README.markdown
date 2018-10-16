# Example for Responsive Web Design in Django

This is an example package for my blog post on building a responsive web design
in Django without the need of JavaScript.

## Technical Details

This uses the [spectre](https://picturepan2.github.io/spectre) engine for
SCSS, which is compiled using the 
[django-sass-processor](https://github.com/jrief/django-sass-processor).

## Installation

As with any Python project, it's recommended to use a virtual environment. In
any case, clone this repository:

    $ git clone https://github.com/src-r-r/SassExample

Now install the required packages

    $ pip install -r requirements.txt

Compile the SCSS, collect the static files, and run the server.

    $ python manage.py compilescss
    $ python manage.py collectstatic --noinput
    $ python manage.py runserver

Now navigate to [http://localhost:8000](http://localhost:8000) and experience
a responsive Django site in all it's glory!
