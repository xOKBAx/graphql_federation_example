"""Graphql Example"""
import strawberry


# Every GraphQL server uses a schema to define the structure of the data that clients can query.
# In this example, we will create a server for querying a collection of books by title and author.

@strawberry.type
class Book: # pylint: disable=too-few-public-methods
    """Book Type"""
    title: str
    author: str


# Database
database = [
    Book(title="The Great Gatsby", author="F. Scott Fitzgerald"),
    Book(title="Gatsby 2", author="F. Scott Fitzgerald"),
]


# Strawberry can work with any data source
# (for example a database, a REST API, files, etc).
# For this tutorial we will be using hard-coded data.

def get_books():
    """Simulation of a data getter (Like database for example)"""
    return database


# Strawberry doesn’t know it should use "get_books" when executing a query.
# We need to update our query to specify the resolver for our books.
# A resolver tells Strawberry how to fetch the data associated with a particular field.

@strawberry.type
class Query: # pylint: disable=too-few-public-methods
    """Query Type"""
    books: list[Book] = strawberry.field(resolver=get_books)


@strawberry.type
class Mutation: # pylint: disable=too-few-public-methods
    """Mutation Type"""
    @strawberry.mutation
    def add_book(self, title: str, author: str) -> Book:
        """Add more books"""
        book = Book(title=title, author=author)
        database.append(book)
        return book


# We have defined our data and query,
# now what we need to do is create a GraphQL schema and start the server.
# Command: strawberry server main
# http://localhost:8000/graphql

schema = strawberry.Schema(query=Query, mutation=Mutation)


# Now we can run the next query to retrieve all books
"""
query books {
  books {
    title
  	author
  }
}
"""
# Or this to create a new book
"""

"""
