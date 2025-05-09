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


## Part 3: Visiting Interesting Places

# create empty attraction lists
attractions = [list() for x in destinations]
print(attractions)

# func: add attraction
def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index].append(attraction)

  except ValueError:
    print('Value_error: Could not retrieve "{}" in list of destinations.'.format(destination))
    pass

# test function
add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
print(attractions)

# add more attractions
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Patio do Colegio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

print(attractions)

# test error handling for destination out of scope
add_attraction("Barcelona, Spain", ["Museu Nacional d'Art de Catalunya", ["museum"]])


## Part 4: Finding the Best Places to Go

# func: find attractions
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]

  attraction_with_interest = []
  for possible_attraction in attractions_in_city:
    attraction_tags = possible_attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attraction_with_interest.append(possible_attraction[0])
  return attraction_with_interest


# test function
la_arts = find_attractions('Los Angeles, USA', ['art'])
print(la_arts)

la_arts = find_attractions('Los Angeles, USA', ['art', 'beach', 'museum'])
print(la_arts)


## Part 5: See The Parts of a City You want to See

# func: get attractions for traveler
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)

  interests_string = "Hi "

  interests_string += "{traveler_name}, we think you'll like these places around {destination}: the ".format(traveler_name=traveler[0], destination=traveler_destination)

  for i in range(len(traveler_attractions)):
    if i == 0:
      interests_string += traveler_attractions[i]
    else:
      interests_string += ', the ' + traveler_attractions[i]

  return interests_string

# test function
attractions_test_traveler = get_attractions_for_traveler(test_traveler)
print(attractions_test_traveler)

attractions_smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(attractions_smills_france)

