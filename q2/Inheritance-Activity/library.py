class Publication:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author

    def display_info(self):
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")


class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.number_of_pages = number_of_pages

    @property
    def number_of_pages(self):
        return self._number_of_pages

    @number_of_pages.setter
    def number_of_pages(self, value):
        if value <= 0:
            print("Number of pages must be positive.")
            return
        self._number_of_pages = value

    def get_number_of_pages(self):
        return self._number_of_pages

    def set_number_of_pages(self, value):
        self.number_of_pages = value

    def display_info(self):
        super().display_info()
        print(f"Number of pages: {self._number_of_pages}")


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number

    @property
    def issue_number(self):
        return self._issue_number

    @issue_number.setter
    def issue_number(self, value):
        if value <= 0:
            print("Issue number must be positive.")
            return
        self._issue_number = value

    def get_issue_number(self):
        return self._issue_number

    def set_issue_number(self, value):
        self.issue_number = value

    def display_info(self):
        super().display_info()
        print(f"Issue number:{self._issue_number}")


pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)


print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)  
book1.display_info()
print(book1.get_number_of_pages())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number()) 