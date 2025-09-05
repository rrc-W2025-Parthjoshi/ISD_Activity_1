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
        item_id (int): The ID of the LibraryItem.
        title (str): The title of the item.
        author (str): The author the item.
        genre (Genre): The genre of item. 
        is_borrowed (boolean): Tells whether the item is borrowed or not.
    """
    def __init__(self,item_id: int,  title: str, author: str, genre: Genre, is_borrowed: bool):
        """
        Creates a new library item with given title, author, and genre.

        Args:
            item_id (int): Represents the id number of the LibraryItem.
            title (str): The title of the library item. Cannot be blank.
            author (str): The author of the library item. Cannot be blank.
            genre (Genre): The genre classification of the item.
            is_borrowed (boolean): Tells whether the item is borrowed or not.

        Raises:
            ValueError: If title or author is blank, or if genre is not a valid Genre.
        """
        if not isinstance(item_id, int):
            raise ValueError("Item Id must be numeric.")
        if title is None or title.strip() == "":
            raise ValueError("Title cannot be blank.")
        if author is None or author.strip() == "":
            raise ValueError("Author cannot be blank.")
        if not isinstance(genre,Genre):
            raise ValueError("Invalid Genre.")
        if not isinstance(is_borrowed, bool):
            raise ValueError("Is Borrowed must be a boolean value.")
        self.__item_id = item_id
        self.__title = title.strip()
        self.__author = author.strip()
        self.__genre = genre
        self.__is_borrowed = is_borrowed

    @property
    def item_id(self) -> int:
        """
        Returns the unique ID of the library item.

        Returns:
            int: TThe library item's ID.
        """
        return self.__item_id
        
    @property
    def title(self) -> str:
        """
        Returns the title of the library item.

        Returns:
            str: The item's title.
        """
        return self.__title
    
    @property
    def author(self) -> str:
        """
        Returns the author of the library item.

        Returns:
            str: The item's author.
        """
        return self.__author
    
    @property
    def genre(self) -> Genre:
        """
        Returns the genre of the library item.

        Returns:
            Genre: The item's genre.
        """
        return self.__genre
    
    @property
    def is_borrowed(self) -> bool:
        """
        Returns whether the library item is currently borrowed.

        Returns:
            bool: True if the item is borrowed, otherwise False.
        """
        return self.__is_borrowed
    