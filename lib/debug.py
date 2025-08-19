from classes.many_to_many import Author, Magazine, Article

author1 = Author("Alice")
mag1 = Magazine("TechLife", "Technology")
mag2 = Magazine("HealthPlus", "Health")

# valid article
a1 = author1.add_article(mag1, "The Future of AI")
a2 = author1.add_article(mag1, "Quantum Computing Breakthrough")

print(author1.articles())        # list of Alice's articles
print(author1.magazines())       # magazines Alice has written for
print(author1.topic_areas())     # categories Alice has written in
print(mag1.articles())           # articles in TechLife
print(mag1.article_titles())     # titles in TechLife
print(mag1.contributors())       # contributors in TechLife
