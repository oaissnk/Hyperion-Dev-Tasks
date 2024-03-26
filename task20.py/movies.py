import spacy
import os

nlp = spacy.load('en_core_web_md')

def find_most_similar_movie(description, filename):
    model_description = nlp(description)

    # giving variables start points for the loop
    most_similar_movie = None
    max_similarity_score = -1  

    
    filepath = os.path.join(os.path.dirname(__file__), filename)

    '''with open(filepath, 'r') as file:
        for line in file:
            movie_title, movie_description = line.strip().split(':', 1)  # just checking this works properly 
            print("Movie Title:", movie_title)
            print("Movie Description:", movie_description)
            print("----")'''

   
    with open(filepath, 'r') as file:
        for line in file:
            movie_title, movie_description = line.strip().split(':', 1)  # splitting the movie from the text
            similarity_score = model_description.similarity(nlp(movie_description))
            if similarity_score > max_similarity_score:
                max_similarity_score = similarity_score
                most_similar_movie = movie_title

    return most_similar_movie

# Using our function to get the answer

description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

most_similar_movie = find_most_similar_movie(description, 'movies.txt')
print("The most similar movie is:", most_similar_movie)

