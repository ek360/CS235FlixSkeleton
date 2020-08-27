import pytest
from domainmodel.movie import Movie
from domainmodel.watchlist import WatchList

@pytest.fixture()
def watchlist():
    return WatchList()

def test_add_movie(watchlist):
    watchlist.add_movie(Movie("Moana",2016))
    watchlist.add_movie(Movie("something", 2005))
    watchlist.add_movie(Movie("something else", 1994))
    watchlist.add_movie(Movie("title name here", 2011))
    assert watchlist.size()==4
    watchlist.add_movie(Movie("something else", 1994))
    assert watchlist.size() == 4

def test_add_movie_fail(watchlist):
    watchlist.add_movie(Movie("Moana",2016))
    watchlist.add_movie(Movie("something", 2005))
    watchlist.add_movie(Movie("something else", 1994))
    watchlist.add_movie(Movie("title name here", 2011))
    assert watchlist.size()==4
    watchlist.add_movie("Not a movie")
    assert watchlist.size() == 4

def test_remove_movie(watchlist):
    watchlist.add_movie(Movie("Moana",2016))
    watchlist.add_movie(Movie("something", 2005))
    watchlist.add_movie(Movie("something else", 1994))
    watchlist.add_movie(Movie("title name here", 2011))
    assert watchlist.size()==4
    watchlist.remove_movie(Movie("something else", 1994))
    assert watchlist.size() == 3

def test_remove_movie_fail(watchlist):
    watchlist.add_movie(Movie("Moana",2016))
    watchlist.add_movie(Movie("something", 2005))
    watchlist.add_movie(Movie("something else", 1994))
    watchlist.add_movie(Movie("title name here", 2011))
    assert watchlist.size()==4
    watchlist.remove_movie(Movie("not in list", 1969))
    assert watchlist.size() == 4

def test_select_movie(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("something", 2005))
    watchlist.add_movie(Movie("something else", 1994))
    watchlist.add_movie(Movie("title name here", 2011))
    assert watchlist.size() == 4
    assert watchlist.select_movie_to_watch(2) == Movie("something else", 1994)
    assert watchlist.select_movie_to_watch(0) == Movie("Moana", 2016)

def test_select_movie_fail(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("something", 2005))
    watchlist.add_movie(Movie("something else", 1994))
    watchlist.add_movie(Movie("title name here", 2011))
    assert watchlist.size() == 4
    assert watchlist.select_movie_to_watch(2) == Movie("something else", 1994)
    assert watchlist.select_movie_to_watch(0) == Movie("Moana", 2016)
    assert watchlist.select_movie_to_watch(-2) == None
    assert watchlist.select_movie_to_watch(5) == None

def test_select_first(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("something", 2005))
    watchlist.add_movie(Movie("something else", 1994))
    watchlist.add_movie(Movie("title name here", 2011))
    assert watchlist.size() == 4
    assert watchlist.first_movie_in_watchlist() == Movie("Moana", 2016)
    watchlist.remove_movie(Movie("Moana", 2016))
    assert watchlist.first_movie_in_watchlist() == Movie("something", 2005)

def test_select_first_None(watchlist):
    assert watchlist.first_movie_in_watchlist() == None

def test_iter(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("something", 2005))
    watchlist.add_movie(Movie("something else", 1994))
    watchlist.add_movie(Movie("title name here", 2011))
    holder = iter(watchlist)
    assert next(holder) == Movie("Moana", 2016)
    assert next(holder) == Movie("something", 2005)
    assert next(holder) == Movie("something else", 1994)
    assert next(holder) == Movie("title name here", 2011)

def test_iter_range(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("something", 2005))
    watchlist.add_movie(Movie("something else", 1994))
    watchlist.add_movie(Movie("title name here", 2011))
    i = watchlist.size()
    holder = iter(watchlist)
    assert next(holder) == Movie("Moana", 2016)
    s=1
    assert next(holder) == Movie("something", 2005)
    s+=1
    assert next(holder) == Movie("something else", 1994)
    s+=1
    assert next(holder) == Movie("title name here", 2011)
    s+=1
    assert i == s

def test_size(watchlist):
    assert watchlist.size() == 0
