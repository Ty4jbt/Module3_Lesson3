# Task 1
# Objective: compare two sets of airline destinations

# Sets to compare
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"LAX", "CDG", "LHR", "BKK"}

# Common destinations
destinations_in_both = our_routes.intersection(competitor_routes)
print("Destination in both sets: ", destinations_in_both)

# Destinations unique to us
unique_to_us = our_routes.difference(competitor_routes)
print("Destinations unique to us: ", unique_to_us)

# Destinations that are not shared
not_shared = our_routes.symmetric_difference(competitor_routes)
print("Destinations not shared: ", not_shared)
