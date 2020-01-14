test-0
------

The following are simple tests to Shopper Army job posting. Extra details such as folder structure, coding style, and more that's not mentioned here are up to you.

* Fork this repository to your GitHub account - both frontend and backend should be placed in the same repo
* [Python, backend] Create a django project directory (LTS version only)
* Create a `Member` model referencing or extending django's `User` model - add `gender` and `country` field
* Create a command that creates a `Member` object which contains required and/or optional arguments
* [Node.js, frontend] Create a vue project directory
* Create a vue form component for adding a `Member` - use bootstrap or vuetify for UI (added as dependency)
* When done, create a pull request to `submit-0` branch


Optional
--------

* Lock all dependencies
* Implement `django-rest-framework` or `GraphQL` - tie in both frontend and backend using this
* Implement `elasticsearch` - index `Member` objects
* Implement `celery` - `Member` creation to be run by worker
* Implement `docker` / `docker-compose` to simultaneously launch frontend and backend (along with DB, if applicable)
