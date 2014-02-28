imagebase
=========

Simple image database application which is a companion to a talk about hybrid web applications.

Slides are on slideshare: http://www.slideshare.net/jamesdac/hybrid-web-applications

Each branch builds on the next to improve the functionality / UX:

* initial: no JavaScript, simulation of traditional web app
* basic_pjax: adds master-detail view to dashboard
* modal: adds modal popup for editing image details
* discover: decouples urls from server using json
* animation: nicer transistions from master to master-detail
* replace_state: uses replaceState instead of pushState
* sync: adds updates for multiple areas of the page to keep them in sync
* master: adds 3D transforms for editing/viewing an image

Setting up
----------
This is a Django application so setup involves the typical steps.

* create a virtualenv
* pip install -r requirements.txt
* setup a database and run python ./manage.py syncdb
* run python ./manage.py runserver


