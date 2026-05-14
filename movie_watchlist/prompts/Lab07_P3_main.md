I am building a Movie Watchlist CLI app.



src/models.py already exists with:

\- Movie (@dataclass): title, genre, rating, watched, date\_added

&#x20; method: mark\_watched(self)

\- Watchlist: add(), get\_all(), get\_unwatched(), get\_top\_rated(n),

&#x20; get\_by\_index(), \_\_len\_\_()



src/storage.py already exists with:

\- load\_movies() -> Watchlist

\- save\_movies(collection: Watchlist) -> None

&#x20; (saves to data/movies.json using dataclasses.asdict())



Read src/models.py first, then create src/main.py with:



1\. Load collection with load\_movies() at startup

2\. A while True menu loop displaying:

&#x20;  \[1] Add a movie

&#x20;  \[2] View all movies

&#x20;  \[3] View unwatched

&#x20;  \[4] Mark as watched

&#x20;  \[5] Quit



3\. \[1] Add: input title, genre, rating (float) -> create Movie -> add -> save

4\. \[2] View all: print numbered list with title, genre, rating, watched status

5\. \[3] Unwatched: print list of unwatched movies

6\. \[4] Mark watched: print numbered list -> input number -> mark\_watched() -> save

7\. \[5] Quit: print "Goodbye!" and exit

8\. Handle invalid input with: print("Invalid option, try again.")



Use only input() and print(). No external libraries.

Write the file directly to src/main.py.



