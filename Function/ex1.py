#  8.1 try it yourself
def display_message(name):
    """Heir print the message about what someone learnig"""
    print(f"Hello {name.title()} , I am learning Python function")


display_message("henok")

# 8.2 try it yourself


def favorite_book(book_title):
    print(f"One of my favorite books is {book_title.title()}")


favorite_book("Alice in wonderland")

# 8.3 try it yourself


def make_shirt(size, message):
    print(f"{message} {size.title()}")


make_shirt("XL", "I Love Python")
make_shirt(size="XL", message="I Love Python")

# 8.4 modifying the shirt
make_shirt("L", "I lOve Python")
make_shirt("M", "I love Python")
make_shirt("S", "The size of the shirt is")

# 8.5 try it by yourself


def describe_city(city, country="Eritrea"):
    print(f"{city.title()} is in {country.title()}")


describe_city("Asmara")
describe_city("Cape town", "South Africa")
describe_city("Bern", "Swizerland")
# 8.6 try it yourself


def city_country(city, country):
    print(f"'{city}, {country}'")


city_country("santiago", "chile")
city_country("Zurich", "Switzerland")
city_country("Berlin", "Germany")

# 8.7 try it yourself
def make_album()
