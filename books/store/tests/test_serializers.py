from django.test import TestCase
from store.models import Book
from store.serializers import BooksSerializer


class BooksSerializerTestCase(TestCase):
    def test_serializer_ok(self):
        book_1 = Book.objects.create(name='The test book 1', price=25)
        book_2 = Book.objects.create(name='The test book 2', price=55)
        data = BooksSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'The test book 1',
                'price': '25.00'
            },
            {
                'id': book_2.id,
                'name': 'The test book 2',
                'price': '55.00'
            }
        ]
        print('data:')
        print(data)
        print()
        print('expected_data:')
        print(expected_data)
        self.assertEqual(expected_data, data)
