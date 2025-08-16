📰 Article Management System (Python OOP)

This project is a Python Object-Oriented Programming (OOP) practice app that models a simple publishing system with three main classes:

Author ✍️ — represents a writer who creates articles.

Magazine 📚 — represents a magazine that contains articles.

Article 📝 — represents an article written by an author and published in a magazine.

It demonstrates beginner-to-intermediate OOP concepts in Python such as:

Classes & Objects

Instance & Class Methods

self and variables

Properties (Getters & Setters) using @property decorators

Validation and immutability rules

Relationships between multiple classes

🚀 Features

Create Authors, Magazines, and Articles

Prevent invalid data using validation rules

Immutable article title (cannot be changed after creation)

Relationships between classes:

An Author can have many Articles

A Magazine can have many Articles

An Article always belongs to one Author and one Magazine

📂 Project Structure
📦 article_management
 ┣ 📜 author.py        # Author class
 ┣ 📜 magazine.py      # Magazine class
 ┣ 📜 article.py       # Article class
 ┣ 📜 main.py          # Example usage (run this file)
 ┣ 📜 README.md        # Documentation

📝 Example Usage
from author import Author
from magazine import Magazine
from article import Article

# Create an Author
author1 = Author("John Doe")

# Create a Magazine
magazine1 = Magazine("Tech Weekly", "Technology")

# Create an Article
article1 = Article(author1, magazine1, "The Future of AI")

# Access data
print(article1.title)             # "The Future of AI"
print(article1.author.name)       # "John Doe"
print(article1.magazine.name)     # "Tech Weekly"

# Author can list all their articles
print(author1.articles())         # [article1]

# Magazine can list all its articles
print(magazine1.articles())       # [article1]

# Attempting to change the article title raises an error
article1.title = "New Title"      # ❌ AttributeError

🔑 Key Concepts in This Project
1. Classes and Objects

Used to represent real-world entities (Author, Magazine, Article).

2. self and Variables

self is used inside methods to refer to the current object instance.

3. Properties & Decorators

Used with @property to control access to variables.
Example:

@property
def title(self):
    return self._title

4. Validation

Ensures only correct data is accepted (e.g., article title must be at least 5 characters).

5. Relationships

An Author is linked to their Articles.

A Magazine can hold many Articles.

An Article belongs to exactly one Author and one Magazine.

⚡ How to Run

Clone the repository:

git clone https://github.com/EvaArbo/Domain-Modelling-project
cd article-management


Run the example file:

python3 main.py

📖 Future Improvements

Add database or JSON storage for persistence.

Add search/filter features for magazines and articles.

Add a CLI (Command-Line Interface) for user interaction.

👩‍💻 Author

Made with ❤️ by EvaArbo
Beginner Python developer practicing OOP fundamentals.