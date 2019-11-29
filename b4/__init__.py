"""
b4 - Our Opal Application
"""
from django.urls import reverse_lazy
from opal.core import application
from opal.core import menus


class Application(application.OpalApplication):

    menuitems = [
        menus.MenuItem(
            href=reverse_lazy('add-patient'),
            display='Add Patient',
            icon='fa fa-plus',
            activepattern=reverse_lazy('add-patient')
        )
    ]
