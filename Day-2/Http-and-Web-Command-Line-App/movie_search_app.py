import requests


class Movie(object):
	"""A Command line Movie application that consumes a Public Movie API.
	https://www.omdbapi.com
	"""

	def __init__(self):
		self.movie_title = input("Enter the name for a movie to search for: ")
		self.prefix_url = "http://www.omdbapi.com/?t="
		self.suffix_url = "&y=&plot=short&r=json"				
		self.my_request = requests.get(self.prefix_url + self.movie_title + self.suffix_url)
		self.my_response = self.my_request.json()
		
	def search_movie_by_title(self):
		return self.my_response

		
search_movie = Movie()

print(search_movie.search_movie_by_title())


