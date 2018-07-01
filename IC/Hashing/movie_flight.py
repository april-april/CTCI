#O(n)

def can_two_movies_fill_flight(movie_lengths, flight_length):
    # set for movie lengths you have seen so far
    movie_lengths_seen = set()

    #loop through each movie
    for each_movie_length in movie_lengths:
        second_movie_length = flight_length - each_movie_length
        if second_movie_length in movie_lengths_seen
            return True
        movie_lengths_seen.add(each_movie_length)

    # We never found a match, so return False
    return False

#We will not match the same movie twice because we check
#the set for second movie length before adding it to set