from time import sleep

from django.conf import settings
from django.core.cache import caches
from django.test import Client, TestCase
from django.urls import reverse

from ..models import Author, Book, Publisher


class ViewBooksTestCase(TestCase):
    """Tests view books route."""

    def setUp(self):
        self.client = Client()
        self.cache = caches[settings.CACHE_KEY]
        self.author = Author(first_name="Toni", last_name='Morrison')
        self.author.save()
        self.publisher = Publisher(title="Alfred Knopf")
        self.publisher.save()
        self.book = Book(title="Beloved",
                         author=self.author, publisher=self.publisher)
        self.book.save()

    def test_get_books(self):
        books_response = self.client.get(reverse('books-list'))
        self.assertEqual(books_response.status_code, 200)
        self.assertEqual(len(books_response.data), 1)

    def test_url_in_cache(self):
        """Tests that the urls in the cache are indeed cached by
        showing that a second insert to the table is not contained in the
        response.
        """
        books_response = self.client.get(reverse('books-list'))
        book1_title = books_response.data[0]['title']
        self.assertEqual(len(books_response.data), 1)
        self.assertEqual(book1_title, self.book.title)

        book2 = Book(title="Harry Potter")
        book2.save()
        books_response = self.client.get(reverse('books-list'))
        self.assertEqual(len(books_response.data), 1)

    def test_url_not_in_cache(self):
        """Tests that the urls not in the cache are not cached by showing
        that a second insert to the table is contained in the response
        """
        authors_response = self.client.get(reverse('authors-list'))
        author1_name = authors_response.data[0]['first_name']
        self.assertEqual(len(authors_response.data), 1)
        self.assertEqual(author1_name, self.author.first_name)

        author2 = Author(first_name="Rowling")
        author2.save()
        authors_response = self.client.get(reverse('authors-list'))
        author1_name = authors_response.data[0]['first_name']
        author2_name = authors_response.data[1]['first_name']

        self.assertEqual(len(authors_response.data), 2)
        self.assertEqual(author1_name, self.author.first_name)
        self.assertEqual(author2_name, author2.first_name)

    def test_cache_timeout(self):
        """Tests that the urls in the cache are cached for the time specified.
        """
        publishers_response = self.client.get(reverse('publishers-list'))
        publisher_title = publishers_response.data[0]['title']
        self.assertEqual(len(publishers_response.data), 1)
        self.assertEqual(publisher_title, self.publisher.title)

        publisher2 = Publisher(title="Bantam Books")
        publisher2.save()
        publishers_response = self.client.get(reverse('publishers-list'))
        self.assertEqual(len(publishers_response.data), 1)

        sleep(3)

        publishers_response = self.client.get(reverse('publishers-list'))
        publisher1_name = publishers_response.data[0]['title']
        publisher2_name = publishers_response.data[1]['title']
        self.assertEqual(len(publishers_response.data), 2)
        self.assertEqual(publisher1_name, self.publisher.title)
        self.assertEqual(publisher2_name, publisher2.title)

    def tearDown(self):
        del self.client
        self.cache.clear()
