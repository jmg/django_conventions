### Django Convention Over Configuration Urls Routing


Rails-like Convention Over Configuration Urls Routing for your Django Projects. (Yeah, forget about urls.py!)

<br>
#### Installation 

```bash
~$ python setup.py install
```

#### Run test suite

```bash
~$ sh run_tests.sh
```
<br>
### How it works

django_conventions uses **introspection** the infer your views **files and classes** (at this moment it just works with [django class based views](https://docs.djangoproject.com/en/dev/topics/class-based-views/)). In order to start using it you just have to open your urls.py file (this will be the first and last time you open it) and add the following code:

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

In the code above **root** is the directory module of your views. django_conventions will look for all the files inside that directory and search for classes that inherit from **django.views.generic.base.View** or any of its subclasses (django.views.generic.base.TemplateView, django.views.generic.base.RedirectView, etc). This is done when you instantiate the **UrlsManager** class inside urls.py.

<br>
### Usage

#### Convention based routing and rendering

The urls for your views classes will be generated by just using **its name** (without the "View" suffix) and the **name of the file** where they are.
For instance, a view class called **MainView** inside **index.py** will be automatically routed to **^index/main/$**. Magic, uh?, but that's not all.

The **render_to_response** method will automatically render the template 
called **main.html** inside the **index** directory under your templates folder.

Example:

**my_project/my_app/views/index.py**

```python
from django.views.generic import TemplateView

class MainView(TemplateView):
    """
        The url for this view will be ^index/main/$
        The template rendered will be main.html under the index directory.
    """

    pass
```

**my_project/my_app/views/user.py**

```python
from django.views.generic import TemplateView

class LoginView(TemplateView):
    """
        The url for this view will be ^user/login/$
        The template rendered will be login.html under the user directory.
    """

    def render_to_response(self, context):

       # Write your regular view code here

       return MainView.render_to_response(self, context)
```

#### Overriding the defaults

Conventions are amazing! But what's when you need to **override** them
to get a **different url** or to render a **different template**? Are you thinking 
on going back to urls.py? Luckily there's no need to do it!

Just define a **url** class attribute on your classes to route it to the url 
you want (fully django regular expressions for defining urls is supported). 

In the same way, just define a **template_name** class attribute to render the template you need.

Example:

**my_project/my_app/views/customers.py**

```python
from django.views.generic import TemplateView

class GetClientView(TemplateView):

    # Use regular expression just like you used to do in urls.py
    url = r"^client/(?P<client_id>\d)/$"

    template_name = "business/client.html"
    
    """
        The url for this view will be ^client/(?P<client_id>\d)/$ (the default ^/customers/getclient/$ was overwritten by the url attribute)
        The template rendered will be client.html under the business directory (the default customers/getclient.html was overwritten by the template_name attribute).
    """

    pass
```

#### Multiple Urls Mapping

Some times you want **two or more views** to be routed to the **same url**.
In that case you can make the url class attribute a **list of urls**.

Example:

**my_project/my_app/views/sellers.py**

```python
from django.views.generic import TemplateView

class CustomersView(TemplateView):
    
    # You can pass a list of urls to this attribute
    url = [r"^business/customers/$", r"^business/buyers/$", #...]
    
    """
        The urls for this view will be ^business/customers/$, ^business/buyers/$ and all the ones that you add in the url attribute list.
    """

    pass
```