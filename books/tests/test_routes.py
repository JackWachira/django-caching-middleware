from django.conf import settings
from django.core.cache import caches
from django.test import Client, TestCase
from django.urls import reverse

from ..models import Book, Author


class ViewBooksTestCase(TestCase):
    """Tests view books route."""

    def setUp(self):
        self.client = Client()
        self.cache = caches[settings.CACHE_KEY]
        self.author = Author(first_name="Richard", last_name='Dawkins')
        self.author.save()
        self.book = Book(title="God Delusion", author=self.author)
        self.book.save()

    def test_get_books(self):
        books_response = self.client.get(reverse('books-list'))
        self.assertEqual(books_response.status_code, 200)
        self.assertEqual(len(books_response.data), 1)

    def test_url_in_cache(self):
        """Tests that the urls in the cache are indeed cached by
        showing that a second entry made to the table is not contained in the
        response.
        """
        books_response = self.client.get(reverse('books-list'))
        book1_title = books_response.data[0]['title']
        self.assertEqual(len(books_response.data), 1)
        self.assertEqual(book1_title, 'God Delusion')

        book2 = Book(title="Harry Potter")
        book2.save()
        books_response = self.client.get(reverse('books-list'))
        self.assertEqual(len(books_response.data), 1)

    def tearDown(self):
        del self.client
        self.cache.clear()
