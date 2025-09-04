""""
Description: A client program written to verify correctness of 
the activity classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Parth Joshi"

from genre.genre import Genre
from library_item.library_item import LibraryItem

def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # 1. Code a statement which creates an instance of the LibraryItem class with valid inputs.
    # Use your own unique valid values for the inputs to the class.
    try:
        item1 = LibraryItem("The Great Gatsby", "F. Scott Fitzgerald", Genre.FICTION)
        print("LibraryItem created successfully!")
    except ValueError as e:
        print(f"Error creating LibraryItem: {e}")


    # 2. Using the instance defined above, and the class Accessors, print 
    # each of the attributes of the LibraryItem instance.
    try:
        print(f"Title: {item1.title}")
        print(f"Author: {item1.author}")
        print(f"Genre: {item1.genre.name}")  # .name prints the enum value as string
    except Exception as e:
        print(f"Error accessing attributes: {e}")
    

    # 3. Code a statement which creates an instance of the LibraryItem class with one or more invalid inputs.
    # Use your own unique valid values for the inputs to the class.
    try:
        # Invalid: blank title and invalid genre
        item2 = LibraryItem("   ", "Unknown Author", "InvalidGenre")
    except ValueError as e:
        print(f"Error creating LibraryItem: {e}")

if __name__ == "__main__":
    main()