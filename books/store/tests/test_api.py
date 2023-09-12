from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from store.models import Book
from store.serializers import BooksSerializer


class BooksApiTestCase(APITestCase):
    def setUp(self):
        self.book_1 = Book.objects.create(name='The test book 1', price=20,
                                          author_name='Author 1')
        self.book_2 = Book.objects.create(name='The test book 2 Author 1', price=50,
                                          author_name='Author 2')
        self.book_3 = Book.objects.create(name='The test book 3', price=70,
                                          author_name='Author 3')
        self.books = [self.book_1, self.book_2, self.book_3]

    def test_get_list(self):
        url = reverse('book-list')
        response = self.client.get(url)
        serializer = BooksSerializer(self.books, many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)

    def test_get_filter(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'price': 50})
        serializer = BooksSerializer([self.book_2], many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)

    def test_get_search(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'search': 'Author 1'})
        serializer = BooksSerializer([self.book_1, self.book_2], many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)

    def test_get_sort(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'ordering': '-price'})
        serializer = BooksSerializer([self.book_3, self.book_2, self.book_1], many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)

    # def test_get_detail(self):
    #     url = reverse('book-detail')
    #     print(url)
    #     response = self.client.get(url)
    #     print(response)
