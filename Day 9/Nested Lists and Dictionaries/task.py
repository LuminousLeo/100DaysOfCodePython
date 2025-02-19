travel_log1 = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

nested_list = ["A", "B", ["C", "D"]]

travel_log2 = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

#pause 1
print(travel_log1['France'][1])

#pause 2
print(nested_list[2][1])

#pause 3
print(travel_log2['Germany']['cities_visited'][2])
