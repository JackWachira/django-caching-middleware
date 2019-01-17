# django-caching-middleware
Django middleware that takes a list of urls from settings file and caches them


1. Install memcached. If you run Linux, you can install it using apt-get install memcached or yum install memcached. This will install memcached from a pre-built package but you can alse build memcached from source, as explained here.
For macOS, using Homebrew is the simplest option. Just run brew install memcached after you’ve installed the Homebrew package manager.
On Windows, you would have to compile memcached yourself or find pre-compiled binaries.

2.