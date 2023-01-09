import spacy

nlp = spacy.load('en_core_web_md')

movie_file = open("movies.txt", "r+")

movie_list = []
for lines in movie_file:
    movie_list.append(lines)

print(movie_list)


def next_movie(movie_desc):
    model_sent = nlp(movie_desc)
    similarity_list = []
    for sentence in movie_list:  # for loop captures similarity values in a list
        similarity = nlp(sentence).similarity(model_sent)
        print(f"{sentence} similarity is: {similarity}")
        similarity_list.append(similarity)
    largest_sim = sorted(similarity_list)[-1]
    for num, sentence in enumerate(movie_list):  # for loop used to ID corresponding movie.
        similarity = nlp(sentence).similarity(model_sent)
        if similarity == largest_sim:  # this function checks each simliarity value against the largest.
            sim_movie = movie_list[num]  # If true it assigns the movie string to variable "sim_movie"
            sim_movie_str_list = sim_movie.split(" :")  # This formats the string to only return that before the ":"
    print(f" Most similar movie is: '{sim_movie_str_list[0]}', similarity score is: '{largest_sim}'")


planet_hulk: str = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the " \
                   "Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a " \
                   "planet where the Hulk can live in peace. Unfortunately, Hulk land on the " \
                   "planet Sakaar where he is sold into slavery and trained as a gladiator."

next_movie(planet_hulk)

movie_file.close
