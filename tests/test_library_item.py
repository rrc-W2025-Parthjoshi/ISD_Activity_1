"""
Description: Unit tests for the Book class.
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_book.py

"""
__author__ = "Parth Joshi"
__version__ = "1.0.0"

import unittest
from genre.genre import Genre
from library_item.library_item import LibraryItem
class TestLibraryItem(unittest.TestCase):
    """
    A suite of tests for the LibraryItem class.
    """
    
    def test_init_sets_attributes_to_input_values(self):
        # Arrange
        title = "One Piece"
        author = "Eichiro Oda"
        genre = Genre.FICTION
 
        # Act
        item = LibraryItem(title, author, genre)
 
        # Assert
        self.assertEqual(title, item.title)
        self.assertEqual(author, item.author)
        self.assertEqual(genre, item.genre)

    def test_init_blank_title_raises_value_error(self):
        # Arrange
        title = "   "
        author = "Eichiro Oda"
        genre = Genre.FICTION
 
        # Act/Assert
        with self.assertRaises(ValueError) as context:
            LibraryItem(title, author, genre)
        self.assertEqual("Title cannot be blank.", str(context.exception))
 
    def test_init_blank_author_raises_value_error(self):
        # Arrange
        title = "One Piece"
        author = "   "
        genre = Genre.FICTION
 
        # Act/Assert
        with self.assertRaises(ValueError) as context:
            LibraryItem(title, author, genre)
        self.assertEqual("Author cannot be blank.", str(context.exception))
 
    def test_init_when_title_missing_raises_value_error(self):
        # Arrange
        title = None
        author = "Eichiro Oda"
        genre = Genre.FICTION
 
        # Act/Assert
        with self.assertRaises(ValueError) as context:
            LibraryItem(title, author, genre)
        self.assertEqual("Title cannot be blank.", str(context.exception))

    def test_init_author_raises_value_error(self):
        # Arrange
        title = "One Piece"
        author = None
        genre = Genre.FICTION
 
        # Act/Assert
        with self.assertRaises(ValueError) as context:
            LibraryItem(title, author, genre)
        self.assertEqual("Author cannot be blank.", str(context.exception))
 
    def test_title_returns_title_attribute(self):
        # Arrange
        title = "One Piece"
        author = "Eichiro Oda"
        genre = Genre.FICTION
        item = LibraryItem(title, author, genre)
 
        # Act
        result = item.title
 
        # Assert
        self.assertEqual(title, result)
 
    def test_author_returns_author_attribute(self):
        # Arrange
        title = "One Piece"
        author = "Eichiro Oda"
        genre = Genre.FICTION
        item = LibraryItem(title, author, genre)
 
        # Act
        result = item.author
 
        # Assert
        self.assertEqual(author, result)
 
    def test_genre_returns_genre_attribute(self):
        # Arrange
        title = "One Piece"
        author = "Eichiro Oda"
        genre = Genre.FICTION
        item = LibraryItem(title, author, genre)
 
        # Act
        result = item.genre
 
        # Assert
        self.assertEqual(genre, result)