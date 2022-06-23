# Project: Movie Rating
# Author: Joe Fraser
# Date: 6/22/2022
# Description: asks the user to input a rating for favorite movie.

movie_choice = "Prometheus"

my_rating = 4

rating = eval(input(f"Rate the following movie - {movie_choice} with a score 1 to 5: "))

rating_difference = my_rating - rating

print(f"Great rating appears our difference is fairly close by {rating_difference} point!")