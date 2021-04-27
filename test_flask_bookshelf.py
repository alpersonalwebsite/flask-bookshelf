import os
import unittest
import json
from THE_NAME_OF_YOUR_APP import create_app
from models import setup_db, Book

class BookTestCase(unittest.TestCase):
    """This class represents the Book test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "bookshelf_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_book = {
            'title': 'Title of Test Book',
            'author': 'Author of Test Book',
            'rating': 5
        }
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_books(self):
      res = self.client().get('/books')
      data = json.loads(res.data)

      self.assertEqual(res.status_code, 200)
      self.assertEqual(data['success'], True)
      self.assertTrue(data['total_books'])
      self.assertTrue(data['books'])

    def test_get_books_error_with_pager_out_of_range(self):
      res = self.client().get('/books?page=111')
      data = json.loads(res.data)

      self.assertEqual(res.status_code, 404)
      self.assertEqual(data['success'], False)
      self.assertEqual(data['message'], 'resource not found')

    def test_update_book_rating(self):
      res = self.client().patch('/books/7', json={ 'rating': 1 })
      data = json.loads(res.data)

      book = Book.query.filter(Book.id == 7).one_or_none()

      self.assertEqual(res.status_code, 200)
      self.assertEqual(data['success'], True)

      self.assertEqual(book.format()['rating'], 1)

    def test_update_book_rating_error_with_no_payload(self):
      res = self.client().patch('/books/7')
      data = json.loads(res.data)
      
      self.assertEqual(res.status_code, 404)
      self.assertEqual(data['success'], False)
      self.assertEqual(data['message'], 'resource not found')

    def test_update_book_rating_error_with_non_existing_book(self):
      res = self.client().patch('/books/111', json={ 'rating': 1 })
      data = json.loads(res.data)
      
      self.assertEqual(res.status_code, 404)
      self.assertEqual(data['success'], False)
      self.assertEqual(data['message'], 'resource not found')

    def test_delete_book(self):
      res = self.client().delete('/books/4')
      data = json.loads(res.data)

      book = Book.query.filter(Book.id == 4).one_or_none()

      self.assertEqual(res.status_code, 200)
      self.assertEqual(data['success'], True)
      self.assertEqual(data['deleted'], 4)
      self.assertTrue(data['total_books'])
      self.assertTrue(len(data['books']))
      self.assertEqual(book, None)

    def test_delete_non_existing_book(self):
      res = self.client().delete('/books/111')
      data = json.loads(res.data)      

      self.assertEqual(data['success'], False)
      self.assertEqual(data['message'], 'unprocessable')

    def test_create_book(self):
      res = self.client().post('/books', json=self.new_book)
      data = json.loads(res.data)

      self.assertEqual(res.status_code, 200)
      self.assertEqual(data['success'], True)
      self.assertTrue(data['created'])
      self.assertTrue(len(data['books']))

    def test_create_book_with_id(self):
      res = self.client().post('/books/111', json=self.new_book)
      data = json.loads(res.data)

      self.assertEqual(res.status_code, 405)
      self.assertEqual(data['success'], False)
      self.assertEqual(data['message'], 'method not allowed')

    def test_search_book(self):
      res = self.client().post('/books', json={'search': 'novel'})
      data = json.loads(res.data)

      self.assertEqual(res.status_code, 200)
      self.assertEqual(data['success'], True)
      self.assertTrue(data['total_books'])
      self.assertEqual(len(data['books']), 2)

    def test_search_non_existing_book(self):
      res = self.client().post('/books', json={'search': 'apples'})
      data = json.loads(res.data)

      self.assertEqual(res.status_code, 200)
      self.assertEqual(data['success'], True)
      self.assertEqual(data['total_books'], 0)
      self.assertEqual(len(data['books']), 0)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()