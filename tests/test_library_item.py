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
        item_id = 1999
        title = "One Piece"
        author = "Eichiro Oda"
        genre = Genre.FICTION
        is_borrowed = False
 
        # Act
        item = LibraryItem(item_id, title, author, genre, is_borrowed)
 
        # Assert
        self.assertEqual(title, item.title)
        self.assertEqual(author, item.author)
        self.assertEqual(genre, item.genre)
        self.assertEqual(item_id, item.item_id)
        self.assertEqual(is_borrowed, item.is_borrowed)

    def test_init_blank_title_raises_value_error(self):
        # Arrange
        item_id = 1999
        title = "   "
        author = "Eichiro Oda"
        genre = Genre.FICTION
        is_borrowed = False
 
        # Act/Assert
        with self.assertRaises(ValueError) as context:
            LibraryItem(item_id, title, author, genre, is_borrowed)
        self.assertEqual("Title cannot be blank.", str(context.exception))
 
    def test_init_blank_author_raises_value_error(self):
        # Arrange
        item_id = 1999
        title = "One Piece"
        author = "   "
        genre = Genre.FICTION
        is_borrowed = False
 
        # Act/Assert
        with self.assertRaises(ValueError) as context:
            LibraryItem(item_id, title, author, genre, is_borrowed)
        self.assertEqual("Author cannot be blank.", str(context.exception))

    def test_init_invalid_genre_raises_value_error(self):
        # Arrange
        item_id = 1999
        title = "One Piece"
        author = "Eichiro Oda"
        genre = "Non_Fiction"
        is_borrowed = False
        
        # Act/Assert
        with self.assertRaises(ValueError) as context:
            LibraryItem(item_id, title, author, genre, is_borrowed)
        self.assertEqual("Invalid Genre.", str(context.exception))

    def test_title_returns_title_attribute(self):
        # Arrange
        item_id = 1999
        title = "One Piece"
        author = "Eichiro Oda"
        genre = Genre.FICTION
        is_borrowed = False
        item = LibraryItem(item_id, title, author, genre, is_borrowed)
 
        # Act
        result = item.title
 
        # Assert
        self.assertEqual(title, result)
 
    def test_author_returns_author_attribute(self):
        # Arrange
        item_id = 1999
        title = "One Piece"
        author = "Eichiro Oda"
        genre = Genre.FICTION
        is_borrowed = False
        item = LibraryItem(item_id, title, author, genre, is_borrowed)
 
        # Act
        result = item.author
 
        # Assert
        self.assertEqual(author, result)
 
    def test_genre_returns_genre_attribute(self):
        # Arrange
        item_id = 1999
        title = "One Piece"
        author = "Eichiro Oda"
        genre = Genre.FICTION
        is_borrowed = False
        item = LibraryItem(item_id, title, author, genre, is_borrowed)
 
        # Act
        result = item.genre
 
        # Assert
        self.assertEqual(genre, result)

    def test_init_invalid_item_id_raises_value_error(self):
        # Arrange
        item_id = "1999"
        title = "One Piece"
        author = "Eichiro Oda"
        genre = Genre.FICTION  
        is_borrowed = False

        # Act/Assert
        with self.assertRaises(ValueError) as context:
            LibraryItem(item_id, title, author, genre, is_borrowed)
        self.assertEqual("Item Id must be numeric.", str(context.exception))

    def test_init_invalid_is_borrowed_raises_value_error(self):
        # Arrange
        item_id = 1999
        title = "One Piece"
        author = "Eichiro Oda"
        genre = Genre.FICTION
        is_borrowed = "None" 

        # Act/Assert
        with self.assertRaises(ValueError) as context:
            LibraryItem(item_id, title, author, genre, is_borrowed)
        self.assertEqual("Is Borrowed must be a boolean value.", str(context.exception))

    def test_item_id_returns_item_id_attribute(self):
        # Arrange
        item_id = 1999
        title = "One Piece"
        author = "Eichiro Oda"
        genre = Genre.FICTION
        is_borrowed = False
        item = LibraryItem(item_id, title, author, genre, is_borrowed)

        # Act
        result = item.item_id

        # Assert
        self.assertEqual(item_id, result)

    def test_is_borrowed_returns_is_borrowed_attribute(self):
        # Arrange
        item_id = 1999
        title = "One Piece"
        author = "Eichiro Oda"
        genre = Genre.FICTION
        is_borrowed = True
        item = LibraryItem(item_id, title, author, genre, is_borrowed)

        # Act
        result = item.is_borrowed

        # Assert
        self.assertTrue(result)

     

    