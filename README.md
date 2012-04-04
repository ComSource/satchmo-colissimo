# Satchmo-Colissimo - Colissimo shipping module for satchmo projects

*satchmo-colissimo* is a custom shipping module for [satchmo](http://www.satchmoproject.com/) [django](https://www.djangoproject.com/) e-commerce solution.

## Dependancies

The only required dependancy is the [django-colissimo](https://github.com/matm/django-colissimo) module up-to-date with LaPoste Colissimo shipping rates. For more informations on how to update django-colissimo to `youryear` rates, please refer to the project page.

## Installation

### Configure django-colissimo

Once dependancies installed, edit your satchmo project `settings.py` and add `colissimo` to your `INSTALLED_APPS`, *e.g.*:

    INSTALLED_APPS = (
        ...
        'colissimo',
    )
	
Now you need to create `colissimo` database scheme with

    python manage.py syncdb

This will also load colissimo rates in the db. If not, fetch initial data:

    mkdir data
    wget https://raw.github.com/matm/django-colissimo/master/colissimo/fixtures/initial_data.json -O data/colissimo_initial_data.json
	python manage.py loaddata data/colissimo_initial_data.json

Now you need to install satchmo-colissimo from github, either by cloning the project of using pip.

### Clone the module from github

    git clone git://github.com/jmaupetit/satchmo-colissimo
    cd satchmo-colissimo
    python setup.py install

### Use pip

    pip install git+git://github.com/jmaupetit/satchmo-colissimo

### Activate satchmo-colissimo

To activate your custom shipping module, add `satchmo-colissimo` to your `CUSTOM_SHIPPING_MODULES` list, *e.g.*:

    SATCHMO_SETTINGS = {
        ....
	    'CUSTOM_SHIPPING_MODULES':['laposte_colissimo'],
	}

Now go to your site settings (once logged in the django admin): in development mode it would be something like `http://localhost:8000/settings/`. Click on `Shipping settings` and select `Colissimo` as an activated shipping module. Then, update settings and a new configuration section will appear for [Colissimo shipping module](/).

## Changelog

* Initial release based on the django-colissimo module to 
* Applies colissimo rates given a package weight, destination and recommanded level

## Roadmap

* Complete support of SoColissimo WS (multiple delivery modes, tracking number, shipping label, etc.)
