# Django Token Authentication

This application demonstrates Django REST API authentication using tokens.

## Django-Rest-Knox

We are relying on **django-rest-knox** library. Knox provides easy to use authentication for 
Django REST Framework. Knox authentication is similar to TokenAuthentication built in DRF,
however it overcomes some problems in the default implementation:

1) DRF tokens are limited one per user, this does not facilitate secure sign in from multiple devices,
as the token is shared. There is also an issue with logout procedure: all devices are logged out all at once. 
Knox allows each client to have its own token, when the client log out the token related to the device is deleted.

2) DRF tokens are stored unencrypted in the database, Knox tokens are only stored in a secure hash form.

3) DRF tokens do not implement token expiry functionality. Knox tokens expiry is configured in the apps settings.

## Useful Links

- django-rest-knox GitHub Repository: https://github.com/James1345/django-rest-knox/

- django-rest-knox Documentation: https://james1345.github.io/django-rest-knox/


## Running the app

1) Install project dependencies:

```
    pip install requirements.txt
```

2) Create superuser account

```
    python manage.py createsuperuser
```

3) Start application server:

```
    python manage.py runserver
```

4) Open the API schema page, and try accessing API ping endpoints, one of the endpoints requires authentication, 
and another does not require authentication, and can be accessed by everyone.

**API Schema Documentation**

- http://127.0.0.1:8000/schema/swagger/

Please note that in order to access the restricted endpoints, you need to authenticate first. This can be done
using the login endpoint: **/auth/login/**


## Project Structure

### config

Project configuration settings are located there.

### apischema app

This app integrates **drf-yasg** urls into the project. **drf-yasg** module is responsible for the generation
of Django REST API schema specification in accordance with Swagger/OpenAPI standards.

### authentication app

This app integrates **django-knox** into the project. **django-rest-knox** module provides token authentication for
Django REST Framework APIs, it offers more advanced token authentication options than built into DRF 
TokenAuthentication module.
 
### pingapi app

Provides demo endpoints to test the implemented token authentication procedure. 

The first endpoints is protected and requires user authentication: 

- https://127.0.0.1:8000/

The second endpoint is not protected, and can be accessed anonymously:

- https://127.0.0.1:8000/ping/









