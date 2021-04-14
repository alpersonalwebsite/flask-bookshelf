import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Book

BOOKS_PER_SHELF = 8

def paginate_and_parse(request, data_list):
  page = request.args.get('page', 1, type=int)
  start = (page - 1) * BOOKS_PER_SHELF
  end = start + BOOKS_PER_SHELF
  print(start)
  print(end)

  formatted_books = [book.format() for book in data_list]
  books_in_page = formatted_books[start:end]
  return books_in_page

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  # CORS Headers 
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

  @app.route('/books')
  def get_books():
    books = Book.query.order_by(Book.id).all()
    formatted_books = paginate_and_parse(request, books)

    if len(formatted_books) == 0:
      abort(404)

    return jsonify({
      'success': True,
      'books': formatted_books,
      'total_books': len(books)
    })

  @app.route('/books/<int:book_id>', methods=['PATCH'])
  def update_book_rating(book_id):

    body = request.get_json()

    try:  
      book = Book.query.filter(Book.id == book_id).one_or_none()
      
      if book is None:
        abort(404)

      if 'rating' in body:
        book.rating = int(body.get('rating'))
      
      book.update()

      return jsonify({
        'success': True,
        'id': book.id
      })
    except:
      abort(404)

  @app.route('/books/<int:book_id>', methods=['DELETE'])
  def delete_book(book_id):

    try:
      book = Book.query.filter(Book.id == book_id).one_or_none()

      if book is None:
        abort(404)

      book.delete()

      books = Book.query.order_by(Book.id).all()
      formatted_books = paginate_and_parse(request, books)

      return jsonify({
        'success': True,
        'deleted': book_id,
        'books': formatted_books,
        'total_books': len(Book.query.all())
      })

    except:
      abort(422)

  @app.route('/books', methods=['POST'])
  def add_book():

    body = request.get_json() 
    title = body.get('title', None)
    author = body.get('author', None)
    rating = body.get('rating', None)

    try:
      book = Book(title=title, author=author, rating=rating)
      book.insert()

      books = Book.query.order_by(Book.id).all()
      formatted_books = paginate_and_parse(request, books)

      return jsonify({
        'success': True,
        'created': book.id,
        'books': formatted_books,
        'total_books': len(Book.query.all())
      })
    except:
      abort(422)
  
  return app