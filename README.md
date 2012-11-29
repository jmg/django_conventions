## Django Convention Over Configuration Routing Plugin


Do you hate to configurate your django applications routing? Do you think **urls.py** is the painfull django file ever? Do you like **rails convention based routing**?

Then why not to apply **convention over configuration** on the django routing?

This library aims to bring the good parts from convention based routing to an amazing framework such as django!

### Installation 

```bash
~$ python setup.py install
```

### Usage

**my_project/urls.py**
```python
from django.conf.urls import patterns, include, url
from django_conventions import UrlsManager

# You have to specify your views module
import my_app.views as root

urlpatterns = patterns('',

    # Write your regular urls here. django_conventions enables you to work with both your regular urls.py kind of routing and the convention over configuration routing.
)

# Here is where the magic flows
UrlsManager(urlpatterns, root)
```

**my_project/my_app/views/index.py**

```python
from django.views.generic import TemplateView


# The url for this view will be ^index/main/$
class MainView(TemplateView):

    # This view will render the template called main.html under the index directory
    pass


# The url for this view will be ^index/amazing/$
class AmazingView(MainView):

   def render_to_response(self, context):

       # Write your regular view code here
       # This view will render the template called amazing.html under the index directory
       return MainView.render_to_response(self, context)

```