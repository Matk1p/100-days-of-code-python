# Dictionaries
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

# Nesting a list in a Dictionary
travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a Dictionary in a Dictionary
travel_log_nested = {
    "France" : {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germnay" : {"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits" : 5},
}

# Nesting Dictionaries inside a list
travel_log_nested = [
    {
        "country" : "France", "cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits": 12
    }, # total 3 dictionaries inside
    {
        "country" : "Germnay", "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits" : 5
    },
]