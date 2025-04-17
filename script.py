## PROJECT: The Boredless Tourist

## Part 1: setup the project on Git

# destinations data
destinations = ['Paris, France', 
                'Shanghai, China', 
                'Los Angeles, USA', 
                'Sao Paulo, Brazil', 
                'Cairo, Egypt']

# test traveler data
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


## Part 2: Travelling To Faraway Lands

# func: get destination
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

# test function
print(get_destination_index('Los Angeles, USA'))
print(get_destination_index('Paris, France'))
# print(get_destination_index('Hyderabad, India')) ValueError, value does not exist.

# func: get traveler location
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

# test function
test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

