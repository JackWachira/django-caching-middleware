[![Coverage Status](https://coveralls.io/repos/github/JackWachira/django-caching-middleware/badge.svg?branch=master)](https://coveralls.io/github/JackWachira/django-caching-middleware?branch=master)
[![Build Status](https://travis-ci.org/JackWachira/django-caching-middleware.svg?branch=master)](https://travis-ci.org/JackWachira/django-caching-middleware)
# django-caching-middleware
Django middleware that takes a list of urls from settings file and caches them

# Running locally
1. Install memcached.
    - If you run Linux, you can install it using `apt-get install memcached` or `yum install memcached`. This will install memcached from a pre-built package but you can alse build memcached from source
    - For macOS, using Homebrew is the simplest option. Just run `brew install memcached` after you’ve installed the Homebrew package manager.
    - On Windows, you would have to compile memcached yourself or find pre-compiled binaries.

2. Install the dependancies by running `pip install -r requirements.txt` from your virtual environment
3. Start memchached by simply running `memchached`.
4. Start the app `python manage.py runserver --settings=django_caching.settings.dev`.

# Testing
 - Tests are run by nose. To run them, simply run `python manage.py test --settings=django_caching.settings.test`
