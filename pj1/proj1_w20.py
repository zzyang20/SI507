#########################################
##### Name: Zhengyang Zhao          #####
##### Uniqname: zzyang              #####
#########################################
import requests, json

class Media:

    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", json=None):
        if json:
            try:
                self.title = json["trackName"]
                self.url = json["trackViewUrl"]
            except KeyError:
                self.title = json["collectionName"]
                self.url = json["collectionViewUrl"]
            self.author = json["artistName"]
            self.release_year = json["releaseDate"][:4]
        else:
            self.title = title
            self.author = author
            self.release_year = release_year
            self.url = url



    def info(self):
        return f"{self.title} by {self.author} ({self.release_year})"

    def length(self):
        return 0



# Other classes, functions, etc. should go here
class Song(Media):
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", album="No Album", genre="No Genre", track_length=0, json=None):
        super().__init__(title, author, release_year, url, json)
        if json:
            self.album = json["collectionName"]
            self.genre = json["primaryGenreName"]
            self.track_length = json["trackTimeMillis"]
        else:
            self.album = album
            self.genre = genre
            self.track_length = track_length

    def info(self):
        return super().info() + f" [{self.genre}]"

    def length(self):
        return round(self.track_length/1000)


class Movie(Media):
        def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", rating="No Rating", movie_length=0, json=None):
            super().__init__(title, author, release_year, url, json)
            if json:
                self.rating = json["contentAdvisoryRating"]
                self.movie_length = json["trackTimeMillis"]
            else:
                self.rating = rating
                self.movie_length = movie_length

        def info(self):
            return super().info() + f" [{self.rating}]"

        def length(self):
            return round(self.movie_length/1000/60)


# build two functions used when the file is called
def get_results(endpoint, term, attribute=''):
    """get json results from requested url
    
    Parameters
        endpoint (str): iTunes API base url
        term (str): what user what to search
        attribute (str): song, movie or other
    Returns
        list: a list of dictionary
    """
    url = endpoint + term + attribute
    data = requests.get(url).json()
    return data['results']

def launch_str(media, num):
    """return a string

    Parameters
        media (str): key of print_all dictionary
        num (int): key of key of print_all dictionary
    Returns
        str: launching url string
    """
    return f"\nLaunching\n{print_all[media][num].url}\nin web browser..."



if __name__ == "__main__":
    # your control code for Part 4 (interactive search) should go here
    ENDPOINT = 'https://itunes.apple.com/search?term='
    SONGS = '&meida=song&entity=song'
    MOVIES = '&media=movie&entity=movie'
    OTHER = '&media=podcast&media=musicVideo&media=audiobook&media=shortFilm&media=tvShow&media=software&media=ebook'
    
    first_input = 0
    while True:
        # check whether it's the first input
        if first_input == 0:
            TERM = input("\nEnter a search term, or \"exit\" to quit: ")
            first_input = 1
        else:
            TERM = input("\nEnter a number for more info, or another search term, or exit: ")

        # check whether it's "exit", num, or str
        if TERM == 'exit':
            print('\nBye!')
            break

        elif TERM.isnumeric() is False:
            # n = 0
            separate = {'SONGS':[], 'MOVIES':[], 'OTHER MEDIA':[]}

            # SONGS
            results = get_results(ENDPOINT, TERM, SONGS)
            for result in results:
                song = Song(json=result)
                if song not in separate['SONGS']:
                    separate['SONGS'].append(song)
            
            # MOVIES
            results = get_results(ENDPOINT, TERM, MOVIES)
            for result in results:
                movie = Movie(json=result)
                if movie not in separate['MOVIES']:
                    separate['MOVIES'].append(movie)
            
            # OTHER
            results = get_results(ENDPOINT, TERM, OTHER)
            for result in results:
                other = Media(json=result)
                if other not in separate['OTHER MEDIA']:
                    separate['OTHER MEDIA'].append(other)

            # print out results
            # give each record a number as key 
            n = 0
            print_all = {'SONGS':{}, 'MOVIES':{}, 'OTHER MEDIA':{}}
            for key, value in separate.items():
                print(f"\n{key}")
                if len(value) == 0:
                    print('none')
                else:
                    check_list = []
                    for item in value:
                        if item.info() not in check_list:
                            n += 1
                            print_all[key][n] = item
                            print(f"{n} {item.info()}")
                            check_list.append(item.info())

        elif TERM.isnumeric():
            num = int(TERM)
            if num in print_all['SONGS'].keys():
                print(launch_str('SONGS', num))
            elif num in print_all['MOVIES'].keys():
                print(launch_str('MOVIES', num))
            elif num in print_all['OTHER MEDIA'].keys():
                print(launch_str('OTHER MEDIA', num))
            else:
                print('\nInvalid number. Please try again.')
            
        else:
            print("\nInvalid input. Please try again.")

