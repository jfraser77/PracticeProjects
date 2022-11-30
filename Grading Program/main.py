"""
Name: Joe Fraser
Date: 11/20/22
Description: Grading Program
"""
#TODO: Write the function that will allow new countries
#to be added to the travel_log.


travel_log = [
    {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
    },
    {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
    ]


def add_new_country(country, num_visited, city_list):
    my_dict = {}
    my_dict["country"] = country
    my_dict["visits"] = num_visited
    my_dict["cities"] = city_list
    travel_log.append(my_dict)

def main():

#🚨 Do NOT change the code above

 





#🚨 Do not change the code below
    add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
    print(travel_log)


if __name__ == "__main__":
    main()