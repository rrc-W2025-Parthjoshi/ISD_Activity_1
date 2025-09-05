""""
Description: A class to manage LibraryItem objects.
"""
__author__ = "Parth Joshi"
__version__ = "1.0.0"

from genre.genre import Genre

class LibraryItem: 
    """
    An item in the library, Like a book.

    Attributes:
        title (str): The title of the item.
        author (str): The author the item.
        genre (Genre): The genre of item. 
    """
    def __init__(self, title: str, author: str, genre: Genre):
        """
        Creates a new library item with given title, author, and genre.

        Args:
            title (str): The title of the library item. Cannot be blank.
            author (str): The author of the library item. Cannot be blank.
            genre (Genre): The genre classification of the item.

        Raises:
            ValueError: If title or author is blank, or if genre is not a valid Genre.
        """
        if title is None or title.strip() == "":
            raise ValueError("Title cannot be blank.")
        if author is None or author.strip() == "":
            raise ValueError("Author cannot be blank.")
        if not isinstance(genre,Genre):
            raise ValueError("Invalid Genre.")
        self.__title = title.strip()
        self.__author = author.strip()
        self.__genre = genre

        
    @property
    def title(self) -> str:
        """
        Gets the title of this library item.
 
        Returns:
            str: The title of the item.
        """
        return self.__title
    
    @property
    def author(self) -> str:
        """
        Gets the author of this library item.
 
        Returns:
            str: The author of the item.
        """
        return self.__author
    
    @property
    def genre(self) -> Genre:
        """
        Gets the genre of this library item.
 
        Returns:
            Genre: The genre of the item.
        """
        return self.__genre
    