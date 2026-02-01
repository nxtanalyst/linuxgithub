class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self._available = True  # Protected attribute for availability status

    def describe(self):
        """Returns a description of the book"""
        return f"{self.title} by {self.author} ({self.publication_year})"

    def is_available(self):
        """Base availability check"""
        return self._available

    def set_availability(self, status):
        """Set the availability status"""
        self._available = status


class FictionBook(Book):
    def __init__(self, title, author, publication_year, genre):
        super().__init__(title, author, publication_year)
        self.genre = genre
        # Dictionary of genres that are currently popular and likely to be unavailable
        self.popular_genres = {"fantasy", "mystery", "science fiction"}

    def describe(self):
        """Override describe to include genre"""
        base_description = super().describe()
        return f"{base_description} - Genre: {self.genre}"

    def is_available(self):
        """Override availability check based on genre popularity"""
        # Books in popular genres are less likely to be available
        if self.genre.lower() in self.popular_genres:
            return self._available and not self.is_peak_season()
        return self._available

    def is_peak_season(self):
        """Helper method to check if it's peak reading season"""
        # This could be expanded to check actual seasonal demand
        return False


class NonFictionBook(Book):
    def __init__(self, title, author, publication_year, subject):
        super().__init__(title, author, publication_year)
        self.subject = subject
        # Dictionary of subjects with reference-only status
        self.reference_only = {"encyclopedia", "dictionary", "atlas"}

    def describe(self):
        """Override describe to include subject"""
        base_description = super().describe()
        return f"{base_description} - Subject: {self.subject}"

    def is_available(self):
        """Override availability check based on subject restrictions"""
        # Reference books are never available for checkout
        if self.subject.lower() in self.reference_only:
            return False
        return self._available


# Example usage
def main():
    # Create some books
    fiction_book = FictionBook(
        "The Hobbit",
        "J.R.R. Tolkien",
        1937,
        "fantasy"
    )
    
    nonfiction_book = NonFictionBook(
        "A Brief History of Time",
        "Stephen Hawking",
        1988,
        "physics"
    )
    
    reference_book = NonFictionBook(
        "World Atlas",
        "National Geographic",
        2023,
        "atlas"
    )

    # Demonstrate usage
    print("Book Descriptions:")
    print(fiction_book.describe())
    print(nonfiction_book.describe())
    print(reference_book.describe())
    
    print("\nAvailability Status:")
    print(f"Fiction Book Available: {fiction_book.is_available()}")
    print(f"Non-Fiction Book Available: {nonfiction_book.is_available()}")
    print(f"Reference Book Available: {reference_book.is_available()}")

    # Change availability status
    fiction_book.set_availability(False)
    print(f"\nAfter setting fiction book as unavailable: {fiction_book.is_available()}")


if __name__ == "__main__":
    main()
switching to master for new line
otfix line
