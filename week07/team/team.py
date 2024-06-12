"""
Course: CSE 251
Lesson Week: Week 07
File: team.py
Purpose: Week 07 Team Activity

Instructions:

1) Make a copy of your assignment 2 program.  Since you are 
   working in a team, you can decide which assignment 2 program 
   that you will use for the team activity.

2) Convert the program to use a process pool and use 
   apply_async() with a callback function to retrieve data 
   from the Star Wars website.  Each request for data must 
   be a apply_async() call.

3) You can continue to use the Request_Thread() class from 
   assignment 02 that makes the call to the server.

"""
"""
Course: CSE 251 
Lesson Week: 02
File: assignment.py 
Author: Brother Comeau

Purpose: Retrieve Star Wars details from a server

Instructions:

- Each API call must only retrieve one piece of information
- You are not allowed to use any other modules/packages except for the ones used
  in this assignment.
- Run the server.py program from a terminal/console program.  Simply type
  "python server.py"
- The only "fixed" or hard coded URL that you can use is TOP_API_URL.  Use this
  URL to retrieve other URLs that you can use to retrieve information from the
  server.
- You need to match the output outlined in the decription of the assignment.
  Note that the names are sorted.
- You are requied to use a threaded class (inherited from threading.Thread) for
  this assignment.  This object will make the API calls to the server. You can
  define your class within this Python file (ie., no need to have a seperate
  file for the class)
- Do not add any global variables except for the ones included in this program.

The call to TOP_API_URL will return the following Dictionary(JSON).  Do NOT have
this dictionary hard coded - use the API call to get this.  Then you can use
this dictionary to make other API calls for data.

{
   "people": "http://127.0.0.1:8790/people/", 
   "planets": "http://127.0.0.1:8790/planets/", 
   "films": "http://127.0.0.1:8790/films/",
   "species": "http://127.0.0.1:8790/species/", 
   "vehicles": "http://127.0.0.1:8790/vehicles/", 
   "starships": "http://127.0.0.1:8790/starships/"
}
"""

"""
Course: CSE 251 
Lesson Week: 02
File: assignment.py 
Author: Brother Comeau

Purpose: Retrieve Star Wars details from a server

Instructions:

- Each API call must only retrieve one piece of information
- You are not allowed to use any other modules/packages except for the ones used
  in this assignment.
- Run the server.py program from a terminal/console program.  Simply type
  "python server.py"
- The only "fixed" or hard coded URL that you can use is TOP_API_URL.  Use this
  URL to retrieve other URLs that you can use to retrieve information from the
  server.
- You need to match the output outlined in the decription of the assignment.
  Note that the names are sorted.
- You are requied to use a threaded class (inherited from threading.Thread) for
  this assignment.  This object will make the API calls to the server. You can
  define your class within this Python file (ie., no need to have a seperate
  file for the class)
- Do not add any global variables except for the ones included in this program.

The call to TOP_API_URL will return the following Dictionary(JSON).  Do NOT have
this dictionary hard coded - use the API call to get this.  Then you can use
this dictionary to make other API calls for data.

{
   "people": "http://127.0.0.1:8790/people/", 
   "planets": "http://127.0.0.1:8790/planets/", 
   "films": "http://127.0.0.1:8790/films/",
   "species": "http://127.0.0.1:8790/species/", 
   "vehicles": "http://127.0.0.1:8790/vehicles/", 
   "starships": "http://127.0.0.1:8790/starships/"
}
"""

from datetime import datetime, timedelta
import requests
import json
import threading
import multiprocessing as mp

# Include cse 251 common Python files
from cse251 import *

# Const Values
TOP_API_URL = 'http://127.0.0.1:8790'

# Global Variables
call_count = 0

def listToString(list):
    str1 = ', '
    return str1.join(list)

# TODO Add your threaded class definition here
class Request_Thread(threading.Thread):
    def __init__(self, URL):
        super().__init__()
        self.URL = URL
        self.response = {}
    
    def run(self):
        global call_count
        call_count += 1
        response = requests.get(self.URL)
        self.response = response.json()
        

# TODO Add any functions you need here
class Film:
    def __init__(self, id):
        self.film_id = id
        self.film_url = ''
        self.film_data = {}
        self.title = ''
        self.director = ''
        self.producer = ''
        self.release_date = ''
        self.character_count = 0
        self.characters = []
        self.planet_count = 0
        self.planets = []
        self.starship_count = 0
        self.starships = [] 
        self.vehicle_count = 0
        self.vehicles = []
        self.species_count = 0
        self.species = []
      
    
    def get_top_urls(self):
        t = Request_Thread(TOP_API_URL)
        t.start()
        t.join()
        self.film_url = t.response['films'] + self.film_id
    
    def get_film_data(self, url):
        t = Request_Thread(url)
        t.start()
        t.join()
        self.film_data  = t.response
        self.title = t.response['title']
        self.director = t.response['director']
        self.producer = t.response['producer']
        self.release_date = t.response['release_date']
        
def get_character(self,url):
    name = get_name(url)
    return name

# def get_characters(self, list):
#     threads = []
#     for url in list:
#         t = threading.Thread(get_character,args=(url,))
#         threads.append(t)
#         t.start()
#     for t in threads:
#         t.join()

# def get_planet(self,url):
#     name = self.get_name(url)
#     self.planet_count +=1
#     self.planets.append(name)

# def get_planets(self, list):
#     threads = []
#     for url in list:
#         t = threading.Thread(target=self.get_planet, args= (url,))
#         threads.append(t)
#         t.start()
#     for t in threads:
#         t.join()

# def get_starship(self,url):
#     name = self.get_name(url)
#     self.starship_count +=1
#     self.starships.append(name)

# def get_starships(self, list):
#     threads = []
#     for url in list:
#         t = threading.Thread(target=self.get_starship,args=(url,))
#         threads.append(t)
#         t.start()
#     for t in threads:
#         t.join()

# def get_vehicle(self,url):
#     name = self.get_name(url)
#     self.vehicle_count +=1
#     self.vehicles.append(name)

# def get_vehicles(self, list):
#     threads = []
#     for url in list:
#         t = threading.Thread(target=self.get_vehicle, args=( url,))
#         threads.append(t)
#         t.start()
#     for t in threads:
#         t.join()

# def get_specie(self,url):
#     name = self.get_name(url)
#     self.species_count +=1
#     self.species.append(name)

# def get_species(self, list):
#     threads = []
#     for url in list:
#         t = threading.Thread(target=self.get_specie,args=(url,))
#         threads.append(t)
#         t.start()
#     for t in threads:
#         t.join()




        
def get_name(self, url):
    t = Request_Thread(url)
    t.start()
    t.join()
    return t.response['name']
        
        
        

def main():
    log = Log(show_terminal=True)
    log.start_timer('Starting to retrieve data from the server')

    # TODO Retrieve Top API urls
    film = Film('6')
    film.get_top_urls()

    # TODO Retrieve Details on film 6
    film.get_film_data(film.film_url)

    pool = mp.Pool(6)

    pool.apply_async(get_name, args=film.film_data['characters'])
    # pool.apply_async(film.get_planets, args=(film.film_data['planets'],))
    # pool.apply_async(film.get_starships, args=(film.film_data['starships'],))
    # pool.apply_async(film.get_vehicles, args=(film.film_data['vehicles'],))
    # pool.apply_async(film.get_species, args=(film.film_data['species'],))
    
    film.characters = pool.get()
    
    # film.get_characters(film.film_data['characters'])
    # film.get_planets(film.film_data['planets'])
    # film.get_starships(film.film_data['starships'])
    # film.get_vehicles(film.film_data['vehicles'])
    # film.get_species(film.film_data['species'])
    

    # TODO Display results
    log.write('-------------------------------------')
    log.write(f"Title   : {film.title}")
    log.write(f"Director: {film.director}")
    log.write(f"Producer: {film.producer}")
    log.write(f"Released: {film.release_date}")
    log.write()
    log.write(f"Characters: {film.character_count}")
    log.write(listToString((sorted(film.characters))))
    log.write()
    log.write(f"Planets: {film.planet_count}")
    log.write(listToString(sorted(film.planets)))
    log.write()
    log.write(f"Starships: {film.starship_count}")
    log.write(listToString(sorted(film.starships)))
    log.write()
    log.write(f"Vehicles: {film.vehicle_count}")
    log.write(listToString(sorted(film.vehicles)))
    log.write()
    log.write(f"Species: {film.species_count}")
    log.write(listToString(sorted(film.species)))
    log.write()
    
    log.stop_timer('Total Time To complete')
    log.write(f'There were {call_count} calls to the server')
    

if __name__ == "__main__":
    main()
