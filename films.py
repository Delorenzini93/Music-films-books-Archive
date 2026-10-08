from collections import Counter
class films:
    def __init__(self, title, director, genre, country, year):
        self.title = title
        self.director = director
        self.genre = genre
        self.country = country
        self.year = year

lista_de_films = [
films("Edward Scissorhands", "Tim Burton", "Fantasy", "USA",  1990),
films("Fight Club", "David Fincher", "Thriller", "USA", 1999),
films("Sleepy Hollow", "Tim Burton", "Horror", "USA", 1999),
films("Big Fish", "Tim Burton", "Drama", "USA", 2003),
films("Sweeney Todd", "Tim Burton", "Horror", "USA", 2007),
films("Big Eyes", "Tim Burton", "Drama", "USA", 2014),
films("Nightmare Before Christmas", "Tim Burton", "Fantasy", "USA", 1993),
films("Beetlejuice", "Tim Burton", "Comedy", "USA", 1988),
films("8½", "Federico Fellini", "Avant-Garde", "Italy", 1963),
films("Goodfellas", "Martin Scorsese", "Crime", "USA", 1990),
films("For A Fistful Of Dollars", "Sergio Leone", "Western", "Italy", 1964),
films("The Godfather", "Francis Ford Coppola", "Crime", "USA", 1972),
films("The Godfather II", "Francis Ford Coppola", "Crime", "USA", 1974),
films("Once Upon A Time In America", "Sergio Leone", "Crime", "Italy", 1984),
films("Close Encounters of the Third Kind", "Steven Spielberg", "Science Fiction", "USA", 1977),
films("A Series Of Unfortunate Events", "Brad Silberling", "Fantasy", "USA", 2004),
films("Harry Potter & The Sorcerer's Stone", "Chris Columbus", "Fantasy", "England", 2001),
films("Harry Potter & The Chamber Of Secrets", "Chris Columbus", "Fantasy", "England", 2002),
films("Harry Potter & The Prisoner Of Azkaban", "Alfonso Cuaron", "Fantasy", "England", 2004),
films("Se7en", "David Fincher", "Thriller", "USA", 1995),
films("Donnie Darko", "Richard Kelly", "Science Fiction", "USA", 2001),
films("A Single Man", "Tom Ford", "Drama", "USA", 2009),
films("The King's Speech", "Tom Hooper", "Drama", "England", 2010),
films("Notting Hill", "Roger Michell", "Romantic Comedy", "England", 1999),
films("Love Actually", "Richard Curtis", "Comedy", "England", 2003),
films("Mamma Mia!", "Phyllida Lloyd", "Musical Comedy", "USA", 2008),
films("The Cabinet Of Dr Caligari", "Robert Wiene", "Horror", "Germany", 1920),
films("Citizen Kane", "Orson Welles", "Drama", "USA", 1941),
films("Halloween", "John Carpenter", "Horror", "USA", 1978),
films("Maltese Falcon", "John Huston", "Noir", "USA", 1941),
films("Night Of The Comet", "Thom Eberhardt", "Science Fiction", "USA", 1984),
films("About A Boy", "Paul Weitz and Chris Weitz", "Comedy-Drama", "England", 2002),
films("Phantom Of The Opera", "Joel Schumacher", "Musical Drama", "England", 2004),
films("Elizabeth", "Shekhar Kapur", "Drama", "England", 1998),
films("No Country For old men", "Joel and Ethan Coen", "Neo Western", "USA", 2007),
films("The Seventh Seal", "Ingmar Bergman", "Drama", "Sweden", 1957),
films("The Hours", "Stephen Daldry", "Drama", "USA", 2002),
films("Notes on a Scandal", "Richard Eyre", "Thriller", "England", 2006),
films("Metropolis", "Fritz Lang", "Science Fiction", "Germany", 1927),
films("Psycho", "Alfred Hitchcock", "Horror", "USA", 1960),
films("The Night Of The Hunter", "Charles Laughton", "Thriller", "USA", 1955),
films("High Noon", "Fred Zinnemann", "Western", "USA", 1952),
films("Gran Torino", "Clint Eastwood", "Drama", "USA", 2008),
films("The Searchers", "John Ford", "Western", "USA", 1956),
films("2001: A Space Odyssey","Stanley Kubrick","Science Fiction","USA",1968),
films("The Shining","Stanley Kubrick","Horror","USA",1980),
films("Eyes Wide Shut","Stanley Kubrick","Thriller","USA",1999),
films("Requiem for a Dream", "Darren Aronofsky", "Thriller", "USA", 2000),
films("The matador","Richard Shepard","Black Comedy","USA", 2005),
films("Walk The Line","James Mangold","Drama","USA", 2005),
films("Corpse Bride","Tim Burton","Fantasy","England",2005),
films("Charlie & The Chocolate Factory","Tim Burton","Fantasy","USA",2005),
films("Alice In Wonderland","Tim Burton","Fantasy","USA", 2010),
films("Funny Games","Michael Haneke","Thriller","Austria",1997),
films("A History Of Violence","David Cronenberg","Thriller","USA",2005),
films("Eastern Promises","David Cronenberg","Crime","England",2007),
films("100 Candles Games","Victor Catalá","Horror","Argentina",2020),
films("The Blair Witch Project","Daniel Myrick","Horror","USA",1999),
films("Flatliners","Joel Schumacher","Science Fiction","USA",1990),
films("Coherence","James Ward Byrkit","Science Fiction","USA",2013),
films("Inception","Christopher Nolan","Science Fiction","USA",2010),
films("Fargo","Joel and Ethan Coen","Black Comedy","USA",1996),
films("Jurassic Park","Steven Spielberg","Science Fiction","USA",1993),
films("Jumanji","Joe Johnston","Fantasy","USA",1995),
films("12 Angry Men","Sidney Lumet","Drama","USA",1957),
films("9","Shane Acker","Science Fiction","USA",2009),
films("Memento","Christopher Nolan","Thriller","USA",2000),
films("WALL-E","Andrew Stanton","Science Fiction","USA",2008),
films("Shrek","Andrew Adamson","Fantasy","USA",2001),
films("Shrek 2","Andrew Adamson","Fantasy","USA",2004),
films("Toy Story","John Lasseter","Adventure","USA",1995),
films("Toy Story 2","John Lasseter","Adventure","USA",1999),
films("Monsters Inc.","Pete Docter","Adventure","USA",2001),
films("It's A Wonderful Life","Frank Capra","Drama","USA",1946),
films("The Good, The Bad & The Ugly","Sergio Leone","Western","Italy",1966),
films("The Silence Of The Lambs","Jonathan Demme","Thriller","USA",1991),
films("Bram Stoker's Dracula","Francis Ford Coppola","Horror","USA",1992),
films("Interview With the Vampire","Neil Jordan","Horror","USA",1994),
films("The Tree Of Life","Terrence Malick","Drama","USA",2011),
films("American History X","Tony Kaye","Crime","USA",1998),
films("Poltergeist","Tobe Hooper","Horror","USA",1982),
films("Super 8","J.J.Abrams","Science Fiction","USA",2011),
films("We Need to Talk About Kevin","Lynne Ramsay","Thriller","England",2011),
films("Hugo","Martin Scorsese","Adventure","USA",2011),
films("Midnight In Paris","Woody Allen","Comedy","USA",2011),
films("Vicky Cristina Barcelona","Woody Allen","Romantic Comedy","Spain",2008),
films("El Mariachi","Robert Rodriguez","Action","USA",1993),
films("Falling Down","Joel Schumacher","Action","USA",1993),
films("Jennifer's Body","Karyn Kusama","Horror","USA",2009),
films("Reservoir Dogs","Quentin Tarantino","Crime","USA",1992),
films("Moneyball","Bennett Miller","Drama","USA",2011),
films("Argentina, 1985","Santiago Mitre","Drama","Argentina",2022),
films("Le Voyage Dans La Lune","Georges Méliès","Science Fiction","France",1902),
films("The Artist","Michel Hazanavicius","Comedy","France",2011),
films("Terminator","James Cameron","Science Fiction","USA",1984),
films("Terminator 2: Judgment Day","James Cameron","Science Fiction","USA",1991),
films("Titanic","James Cameron","Drama","USA",1997),
films("The Lord of the Rings: The Fellowship of the Ring","Peter Jackson","Fantasy","USA",2001),
films("Moonrise Kingdom","Wes Anderson","Comedy","USA",2012),
films("The Chronicles of Narnia: The Lion, the Witch and the Wardrobe","Andrew Adamson","Fantasy","England",2005),
films("Liar Liar","Tom Shadyac","Comedy","USA",1997),
films("Eternal Sunshine of the Spotless Mind","Michel Gondry","Drama","USA",2004),
films("The Truman Show","Peter Weir","Drama","USA",1998),
]

ranking_directors = Counter(film.director for film in lista_de_films)
ranking_genres = Counter(film.genre for film in lista_de_films)
ranking_countries = Counter(film.country for film in lista_de_films)
ranking_years = Counter(film.year for film in lista_de_films)
ranking_decade = Counter((film.year // 10) * 10 for film in lista_de_films)
ranking_century = Counter((film.year // 100) * 100 for film in lista_de_films)

mas_antiguo = min(lista_de_films, key=lambda film: film.year)
mas_nuevo = max(lista_de_films, key=lambda film: film.year)

#ranking_directors = Counter()
#for film in lista_de_films:
#    ranking_directors[film.director] += 1

#suma = 0
#for film in lista_de_films:
#    suma += film.year
#promedio = suma / len(lista_de_films)

promedio = sum(film.year for film in lista_de_films) / len(lista_de_films)

siglo_XX = ranking_century[1900]
siglo_XXI = ranking_century[2000]

peliculas_yankees = [film for film in lista_de_films if film.country == "USA"]
peliculas_inglesas = [film for film in lista_de_films if film.country == "England"]
peliculas_italianas = [film for film in lista_de_films if film.country == "Italy"]
peliculas_alemanas = [film for film in lista_de_films if film.country == "Germany"]
peliculas_argentinas = [film for film in lista_de_films if film.country == "Argentina"]
peliculas_francesas = [film for film in lista_de_films if film.country == "France"]

promedio_yankee = sum(film.year for film in peliculas_yankees) / len(peliculas_yankees)
promedio_britanico = sum(film.year for film in peliculas_inglesas) / len(peliculas_inglesas)
promedio_italiano = sum(film.year for film in peliculas_italianas) / len(peliculas_italianas)
promedio_aleman = sum(film.year for film in peliculas_alemanas) / len(peliculas_alemanas)
promedio_argentino = sum(film.year for film in peliculas_argentinas) / len(peliculas_argentinas)
promedio_frances = sum(film.year for film in peliculas_francesas) / len(peliculas_francesas)

promedios = {
"USA": promedio_yankee,
"England": promedio_britanico,
"Italy": promedio_italiano,
"Germany": promedio_aleman,
"Argentina": promedio_argentino,
"France": promedio_frances}

promedio_mas_reciente = max(promedios, key=promedios.get,)
#peliculas_inglesas = []
#for film in lista_de_films:
#    if film.country == "England":
#        peliculas_inglesas.append(film)

peliculas_tim_burton = [film for film in lista_de_films if film.director == "Tim Burton"]
decade_tim_burton = Counter((film.year // 10) * 10 for film in peliculas_tim_burton)
newest_tim_burton = max(peliculas_tim_burton, key=lambda film: film.year)
oldest_tim_burton = min(peliculas_tim_burton, key=lambda film: film.year)
#===============================================================================
print("\n=== RANKING DIRECTORS ===")
for i, (director, cantidad) in enumerate(ranking_directors.most_common(), start=1):
    print(f"{i}. {director}: {cantidad}")

print("\n=== RANKING GENRES ===")
for i, (genre, cantidad) in enumerate(ranking_genres.most_common(), start=1):
    print(f"{i}. {genre}: {cantidad}")

print("\n=== RANKING COUNTRIES ===")
for i, (country, cantidad) in enumerate(ranking_countries.most_common(), start=1):
    print(f"{i}. {country}: {cantidad}")

print("\n=== RANKING YEARS ===")
for i, (year, cantidad) in enumerate(ranking_years.most_common(), start=1):
    print(f"{i}. {year}: {cantidad}")

print("\n=== RANKING DECADE ===")
for i, (decade, cantidad) in enumerate(ranking_decade.most_common(), start=1):
    print(f"{i}. {decade}: {cantidad}")

print("\n=== RANKING CENTURY ===")
for i, (century, cantidad) in enumerate(ranking_century.most_common(), start=1):
    print(f"{i}. {century}: {cantidad}")

print(
    f"\nPeliculas del siglo XX: {siglo_XX}"
    f"\nPeliculas del siglo XXI: {siglo_XXI}"
    f"\nTitulo mas antiguo: {mas_antiguo.title} ({mas_antiguo.year})"
    f"\nTitulo mas nuevo: {mas_nuevo.title} ({mas_nuevo.year})"
    f"\nPromedio general del año de lanzamiento: {promedio:.2f}"
    f"\nPromedio USA: {promedio_yankee:.2f}"
    f"\nPromedio Inglaterra: {promedio_britanico:.2f}"
    f"\nPromedio Italia: {promedio_italiano:.2f}"
    f"\nPromedio Alemania: {promedio_aleman:.2f}"
    f"\nPromedio Argentina: {promedio_argentino:.2f}"
    f"\nPromedio Francia: {promedio_frances:.2f}"
    f"\nPromedio mas reciente: {promedio_mas_reciente}")

print("\n=== TIM BURTON DECADES ===")
for i, (decada, cantidad) in enumerate(decade_tim_burton.most_common(), start=1):
    print(f"{i}. {decada}: {cantidad}")

print(
    f"\nPelicula mas reciente de Tim Burton: {newest_tim_burton.title} ({newest_tim_burton.year})"
    f"\nPelicula mas antigua de Tim Burton: {oldest_tim_burton.title} ({oldest_tim_burton.year})")
