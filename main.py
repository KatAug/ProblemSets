# Make sure to import your problems here to test as you work!

# Example (uncomment lines 4-8 to test):
import problems_one

to_reverse = [1, 2, 3, 4, 5, 6]
result = problems_one.reverse_list(to_reverse)
print(result)

num_list = [1, 2, 3, 4, 5, 6]
i = 4
new_list = []
result = problems_one.list_value_checker(num_list, i)
print(new_list) 

list_one = ["David", "Katrina", "Keisha", "Nick", "Jaxson"]
list_two = ["Matthew", "Brianna", "Samantha", "Catherine", "Nick"]
result = problems_one.list_value_comparison(list_one, list_two)
print(result)

#Do I need to copy the dictionary onto this page? 
person = {
    "name": "Timmy Thomas",
    "age": 5,
    "interests": {
        "favorite_book": "Where The Sidewalk Ends",
        "favorite_movie": "Star Wars",
        "favorite_color": "Red"
    }
}
sample_dictionary = (person['interests']['favorite_color'])
result = problems_one.get_value_of_favorite_color(sample_dictionary)
print(sample_dictionary)

address = {
	"street": "123 Sesame Street",
	"city": "Some Town",
	"state": "Some State",
	"zip_code": 12345
}
dictionary = (address)
result = problems_one.dictionary_printer(dictionary)
#print(dictionary["street"])
#print(dictionary["city"])
#print(dictionary["state"])
#print(dictionary["zip_code"])

