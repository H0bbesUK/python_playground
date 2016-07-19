# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Franciso',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']
print "CA State has: ", cities['CA']

print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print '{0} is abbreviated {1}' .format(state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print '{0} is has the city {1}' .format(abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print '{0} state is abbreviated {1} and has city {2}' .format(state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
var = 'Texas'
state = states.get(var)
if not state:
    print 'Sorry, not {0}' .format(var)

# get a city with a default value
city = cities.get('TX', 'totaly made up')
print 'The city for the state \'TX\' is {poo}' .format(poo = city)


