I am building a Movie Watchlist CLI app.

Project structure:
movie\_watchlist/
├── src/
│   ├── models.py
│   ├── storage.py
│   └── main.py
├── data/
│   └── movies.json
└── prompts/

Create src/models.py with two classes:

1. Movie (@dataclass)
Fields:

   * title: str
   * genre: str
   * rating: float
   * watched: bool = False
   * date\_added: str (auto-set to today using date.today().isoformat())
Use field(default\_factory=...) for date\_added.
Method: mark\_watched(self) -> None sets watched to True
2. Watchlist
Internal storage: \_movies: list\[Movie] = \[]
Methods:

   * add(movie: Movie) -> None
   * get\_all() -> list\[Movie]
   * get\_unwatched() -> list\[Movie] (where watched is False)
   * get\_top\_rated(n: int) -> list\[Movie] (top n by rating, descending)
   * get\_by\_index(index: int) -> Movie
   * **len**() -> int

Do not add an if **name** == "**main**" block.
Write the file directly to src/models.py.

