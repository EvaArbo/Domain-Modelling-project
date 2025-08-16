from author import Author
from magazine import Magazine
from article import Article

# Create authors
a1 = Author("Alice")
a2 = Author("Bob")

# Create magazines
m1 = Magazine("TechWorld", "Technology")
m2 = Magazine("Foodie", "Cooking")

# Create articles
a1.add_article(m1, "The Future of AI")
a1.add_article(m2, "10 Best Pasta Recipes")
a2.add_article(m1, "Quantum Computing Explained")
a1.add_article(m1, "Cybersecurity Trends 2025")

# Test methods
print("Alice's Articles:", [a.title for a in a1.articles()])
print("Alice's Magazines:", [m.name for m in a1.magazines()])
print("Alice's Topic Areas:", a1.topic_areas())

print("TechWorld Articles:", [a.title for a in m1.articles()])
print("TechWorld Contributors:", [a.name for a in m1.contributors()])
print("TechWorld Article Titles:", m1.article_titles())
print("TechWorld Contributing Authors (>2 articles):", [a.name for a in (m1.contributing_authors() or [])])

print("Top Publisher:", Magazine.top_publisher().name)
