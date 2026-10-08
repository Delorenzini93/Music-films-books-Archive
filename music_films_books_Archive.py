from collections import Counter
import json
class Album:
    def __init__(self, album, artist, genre, country, year, rating):
        self.album = album
        self.artist = artist
        self.genre = genre
        self.country = country
        self.year = year
        self.rating = rating

album_list = [
Album("Please Please Me","The Beatles","Pop","UK",1963,6),
Album("Help!","The Beatles","Pop","UK",1965, 7),
Album("Rubber Soul","The Beatles","Pop","UK",1965,8.5),
Album("Revolver","The Beatles","Psychedelic Pop","UK",1966,10),
Album("Sgt. Pepper's Lonely Hearts Club Band","The Beatles","Psychedelic Pop","UK",1967,9),
Album("White Album","The Beatles","Pop","UK",1968,8.5),
Album("Abbey Road","The Beatles","Pop","UK",1969,9.5),
Album("Magical Mystery Tour","The Beatles","Psychedelic Pop","UK",1967,9),
Album("Yellow Submarine","The Beatles","OST","UK",1969,2),
Album("Let It Be","The Beatles","Pop","UK",1970,6),
Album("Aftermath","The Rolling Stones","Rock","UK",1966,8.5),
Album("Their Satanic Majesties Request","The Rolling Stones","Psychedelic Pop","UK",1967,5),
Album("Exile on Main St.","The Rolling Stones","Rock","UK",1972,8),
Album("Power Windows","Rush","Prog Rock","Canada",1985,8),
Album("Moving Pictures","Rush","Prog Rock","Canada",1981,9.5),
Album("Permanent Waves","Rush","Prog Rock","Canada",1980,8.5),
Album("Trash","Alice Cooper","Glam Metal","USA",1989,7.5),
Album("Hey Stoopid","Alice Cooper","Pop Metal","USA",1991,7),
Album("Raise Your Fist and Yell","Alice Cooper","Glam Metal","USA",1987,6),
Album("Constrictor","Alice Cooper","Glam Metal","USA",1986,5),
Album("Images and Words","Dream Theater","Prog Metal","USA",1992,9),
Album("Electric Ladyland","Jimi Hendrix","Psychedelic Rock","USA",1968,8.5),
Album("Are You Experienced?","Jimi Hendrix","Psychedelic Rock","USA",1967,9),
Album("Axis: Bold as Love","Jimi Hendrix","Psychedelic Rock","USA",1967,8),
Album("Cheap Thrills","Big Brother and the Holding Company","Blues Rock","USA",1968,7),
Album("Surrealistic Pillow","Jefferson Airplane","Psychedelic Rock","USA",1967,7),
Album("After Bathing at Baxter's","Jefferson Airplane","Psychedelic Rock","USA",1967,6),
Album("OK Computer","Radiohead","Alternative Rock","UK",1997,10),
Album("Pablo Honey","Radiohead","Alternative Rock","UK",1993,5),
Album("Happy Trails","Quicksilver Messenger Service","Psychedelic Rock","USA",1968,8.5),
Album("Aoxomoxoa","Grateful Dead","Psychedelic Rock","USA",1969,8.5),
Album("Anthem Of The Sun","Grateful Dead","Psychedelic Rock","USA",1967,7),
Album("The Man Who Sold the World","David Bowie","Hard Rock","UK",1970,7),
Album("Hunky Dory","David Bowie","Art Pop","UK",1971,9),
Album("Ziggy Stardust","David Bowie","Glam Rock","UK",1972,8.5),
Album("Aladdin Sane","David Bowie","Glam Rock","UK",1973,7),
Album("Pin Ups","David Bowie","Glam Rock","UK",1973,4),
Album("Diamond Dogs","David Bowie","Glam Rock","UK",1974,7),
Album("Young Americans","David Bowie","Soul","UK",1975,6),
Album("Station to Station","David Bowie","Art Rock","UK",1976,9),
Album("Low","David Bowie","Art Rock","UK",1977,9.5),
Album("Heroes","David Bowie","Art Rock","UK",1977,8),
Album("Lodger","David Bowie","Art Rock","UK",1979,7),
Album("Scary Monsters","David Bowie","Art Rock","UK",1980,9),
Album("Let's Dance","David Bowie","Pop","UK",1983,6),
Album("Tonight","David Bowie","Pop","UK",1984,2),
Album("Never Let Me Down","David Bowie","Pop","UK",1987,4),
Album("Outside","David Bowie","Experimental","UK",1995,5),
Album("Earthling","David Bowie","Drum & Bass","UK",1997,7.5),
Album("The Next Day","David Bowie","Art Rock","UK",2013,7),
Album("Blackstar","David Bowie","Experimental","UK",2016,7.5),
Album("Appetite For Destruction","Guns N' Roses","Hard Rock","USA",1987,8.5),
Album("Marry Me","St Vincent","Art Pop","USA",2007,6),
Album("Actor","St Vincent","Art Pop","USA",2009,9),
Album("Strange Mercy","St Vincent","Art Pop","USA",2011,8),
Album("Love This Giant","St Vincent/David Byrne","Art Pop","USA",2012,6),
Album("St Vincent","St Vincent","Art Rock","USA",2014,10),
Album("Masseduction","St Vincent","Art Pop","USA",2017,7),
Album("Unknown Pleasures","Joy Division","Post Punk","UK",1979,9),
Album("Closer","Joy Division","Post Punk","UK",1980,9),
Album("Strange Days","The Doors","Psychedelic Rock","USA",1967,8),
Album("The Doors","The Doors","Psychedelic Rock","USA",1967,8.5),
Album("Waiting for the Sun","The Doors","Psychedelic Rock","USA",1968,7),
Album("L.A. Woman","The Doors","Blues Rock","USA",1971,6),
Album("Morrison Hotel","The Doors","Blues Rock","USA",1970,8),
Album("The Piper At The Gates Of Dawn","Pink Floyd","Psychedelic Rock","UK",1967,9.5),
Album("A Saucerful of Secrets","Pink Floyd","Psychedelic Rock","UK",1968,6),
Album("Dark Side Of The Moon","Pink Floyd","Prog Rock","UK",1973,10),
Album("Pet Sounds","The Beach Boys","Psychedelic Pop","USA",1966,10),
Album("Smiley Smile","The Beach Boys","Psychedelic Pop","USA",1967,5),
Album("Today!","The Beach Boys","Pop","USA",1965,7.5),
Album("Summer Days (And Summer Nights!!)","The Beach Boys","Pop","USA",1965,8),
Album("Surf's Up","The Beach Boys","Psychedelic Pop","USA",1971,9),
Album("Friends","The Beach Boys","Pop","USA",1968,5.5),
Album("Love You","The Beach Boys","Pop","USA",1977,7),
Album("Brian Wilson Presents Smile","Brian Wilson","Psychedelic Pop","USA",2004,9.5),
Album("Younger Than Yesterday","The Byrds","Psychedelic Rock","USA",1967,8.5),
Album("Fifth Dimension","The Byrds","Psychedelic Rock","USA",1966,7),
Album("Arthur","The Kinks","Psychedelic Rock","UK",1969,7),
Album("Van Halen","Van Halen","Hard Rock","USA",1978,8),
Album("Hounds of Love","Kate Bush","Art Pop","UK",1985,10),
Album("So","Peter Gabriel","Art Pop","UK",1986,9),
Album("Melt","Peter Gabriel","Art Rock","UK",1980,8),
Album("Rust In Peace","Megadeth","Thrash Metal","USA",1990,8.5),
Album("Youthanasia","Megadeth","Thrash Metal","USA",1994,8),
Album("Cryptic Writings","Megadeth","Thrash Metal","USA",1997,5),
Album("Final Fantasy IX OST","Nobuo Uematsu","VG OST","Japan",2000,9),
Album("A Single Man","Abel Korzeniowski","OST","Poland",2009,9),
Album("Edward Scissorhands","Danny Elfman","OST","USA",1990,8),
Album("Sleepy Hollow","Danny Elfman","OST","USA",1999,8),
Album("Big Fish","Danny Elfman","OST","USA",2003,7),
Album("Corpse Bride","Danny Elfman","OST","USA",2005,6),
Album("Charlie and the Chocolate Factory","Danny Elfman","OST","USA",2005,5),
Album("Alice in Wonderland","Danny Elfman","OST","USA",2010,7),
Album("Sweeney Todd: The Demon Barber of Fleet Street","Stephen Sondheim","Musical","USA",2007,8),
Album("Forever Changes","Love","Psychedelic Pop","USA",1967,9),
Album("The Psychedelic Sounds of the 13th Floor Elevators","13th Floor Elevators","Psychedelic Rock","USA",1966,7),
Album("Easter Everywhere","13th Floor Elevators","Psychedelic Rock","USA",1967,4.5),
Album("Definitely Maybe","Oasis","Britpop","UK",1994,8.5),
Album("(What's the Story) Morning Glory?","Oasis","Britpop","UK",1995,8),
Album("Sing When You're Winning","Robbie Williams","Pop","UK",2000,6.5),
Album("Noel Gallagher's High Flying Birds","Noel Gallagher's High Flying Birds","Rock Pop","UK",2011,7.5),
Album("Lost Horizons","Abney Park","Industrial Rock","USA",2008,5),
Album("Æther Shanties","Abney Park","Steampunk","USA",2009,6.5),
Album("The End of Days","Abney Park","Steampunk","USA",2010,8),
Album("Off The Grid","Abney Park","Folk","USA",2011,5),
Album("Ancient World","Abney Park","Steampunk","USA",2012,6),
Album("The Circus At The End Of The World","Abney Park","Swing","USA",2013,4),
Album("Nevermind","Nirvana","Alternative Rock","USA",1991,8),
Album("In Utero","Nirvana","Alternative Rock","USA",1993,8.5),
Album("Dirt","Alice In Chains","Alternative Metal","USA",1992,8.5),
Album("Ten","Pearl Jam","Alternative Rock","USA",1991,9),
Album("Core","Stone Temple Pilots","Alternative Rock","USA",1992,7),
Album("The Man-Machine","Kraftwerk","Synthpop","Germany",1978,8.5),
Album("Phaedra","Tangerine Dream","Krautrock","Germany",1974,7),
Album("Californication","Red Hot Chili Peppers","Alternative Rock","USA",1999,8),
Album("Black Album","Metallica","Thrash Metal","USA",1991,8.5),
Album("Transilvanian Hunger","Darkthrone","Black Metal","Norway",1994,6),
Album("Reign in Blood","Slayer","Thrash Metal","USA",1986,5.5),
Album("Keeper of the Seven Keys: Part I","Helloween","Power Metal","Germany",1987,8),
Album("Episode","Stratovarius","Power Metal","Finland",1996,6),
Album("Visions","Stratovarius","Power Metal","Finland",1997,8),
Album("Destiny","Stratovarius","Power Metal","Finland",1998,7),
Album("Infinite","Stratovarius","Power Metal","Finland",2000, 7),
Album("Get A Grip","Aerosmith","Hard Rock","USA",1993,8),
Album("Pump","Aerosmith","Hard Rock","USA",1989,7),
Album("Permanent Vacation","Aerosmith","Hard Rock","USA",1987,6),
Album("Toys in the Attic","Aerosmith","Hard Rock","USA",1975,7.5),
Album("Time Out","Dave Brubeck Quartet","Cool Jazz","USA",1959,8.5),
Album("Illmatic","Nas","Gangsta Rap","USA",1994,7),
Album("Straight Outta Compton","N.W.A.","Gangsta Rap","USA",1989,7.5),
Album("The Chronic","Dr. Dre","Gangsta Rap","USA",1992,7),
Album("Vain Glory Opera","Edguy","Power Metal","Germany",1998,5.5),
Album("Theater of Salvation","Edguy","Power Metal","Germany",1999,7),
Album("Mandrake","Edguy","Power Metal","Germany",2001,8),
Album("Hellfire Club","Edguy","Heavy Metal","Germany",2004,7),
Album("Rocket Ride","Edguy","Hard Rock","Germany",2006,6),
Album("The Scarecrow","Avantasia","Power Metal","Germany",2008,8),
Album("Filosofem","Burzum","Ambient","Norway",1996,6),
Album("Aske","Burzum","Black Metal","Norway",1993, 4.5),
Album("Burzum","Burzum","Black Metal","Norway",1992, 4),
Album("Hvis lyset tar oss","Burzum","Black Metal","Norway",1994, 3),
Album("Pentagram","Gorgoroth","Black Metal","Norway",1994, 2),
Album("Metal Machine Music","Lou Reed","Noise","USA",1975,1),
Album("Sons of Northern Darkness","Immortal","Black Metal","Norway",2002,7.5),
Album("Diabolical Fullmoon Mysticism","Immortal","Black Metal","Norway",1992,4),
Album("Pure Holocaust","Immortal","Black Metal","Norway",1993,5),
Album("Kind of Blue","Miles Davis","Modal Jazz","USA",1959,9.5),
Album("In a Silent Way","Miles Davis","Jazz Fusion","USA",1969,7),
Album("Bitches Brew","Miles Davis","Jazz Fusion","USA",1970,8),
Album("The Incredible Jazz Guitar of Wes Montgomery","Wes Montgomery","Jazz","USA",1960,7.5),
Album("Ascension","John Coltrane","Free Jazz","USA",1966,6),
Album("A Love Supreme","John Coltrane","Modal Jazz","USA",1965,8),
Album("Om","John Coltrane","Free Jazz","USA",1968,3),
Album("Giant Steps","John Coltrane","Jazz","USA",1960,9),
Album("Lush Life","John Coltrane","Jazz","USA",1961,5),
Album("Silent Hill OST","Akira Yamaoka","Experimental","Japan",1999,6),
Album("Clics modernos","Charly Garcia","Art Pop","Argentina",1983,9),
Album("After chabon","Sumo","Post Punk","Argentina",1987,8.5),
Album("Soda Stereo", "Soda Stereo", "New Wave", "Argentina", 1984, 4.5),
Album("Doble Vida", "Soda Stereo", "New Wave", "Argentina", 1988, 6),
Album("Signos", "Soda Stereo", "New Wave", "Argentina", 1986, 7.5),
Album("Canción Animal","Soda Stereo","Alternative Rock","Argentina",1990,8.5),
Album("Dynamo", "Soda Stereo", "Shoegaze", "Argentina", 1992, 9),
Album("Fuerza Natural","Gustavo Cerati","Folk Rock","Argentina",2009,8.5),
Album("Dawn of the Deli Creeps","Deli Creeps","Alternative Metal","USA",2005,6.5),
Album("Colma","Buckethead","Ambient","USA",1998,9),
Album("Monsters and Robots","Buckethead","Experimental","USA",1999,6),
Album("The Cuckoo Clocks of Hell","Buckethead","Experimental Metal","USA",2004,4),
Album("Population Override","Buckethead","Blues Rock","USA",2004,5),
Album("Enter the Chicken","Buckethead","Alternative Metal","USA",2005,7.5),
Album("Crime Slunk Scene","Buckethead","Alternative Metal","USA",2006,7),
Album("Electric Tears","Buckethead","Ambient","USA",2002,7),
Album("The Day of the Robot","Buckethead","Experimental","USA",1996,4),
Album("Giant Robot","Buckethead","Experimental","USA",1994,6),
Album("Bucketheadland","Buckethead","Experimental","USA",1992,3),
Album("Slaughterhouse On The Prairie","Buckethead","Alternative Rock","USA",2009,7),
Album("Cyborg Slunks","Buckethead","Experimental","USA",2007,1.5),
Album("Ah Via Musicom","Eric Johnson","Instrumental Rock","USA",1990,7),
Album("Passion and Warfare","Steve Vai","Instrumental Rock","USA",1990,8.5),
Album("Cowboys from Hell","Pantera","Alternative Metal","USA",1990,7),
Album("Shadows Between the Sky","Buckethead","Ambient","USA",2010,7),
Album("Electric Sea","Buckethead","Ambient","USA",2012,5),
Album("A Real Diamond in the Rough","Buckethead","Ambient","USA",2009,8),
Album("Albino Slug","Buckethead","Alternative Rock","USA",2008,6),
Album("The Elephant Man's Alarm Clock","Buckethead","Experimental Metal","USA",2006,4),
Album("Hours...","David Bowie","Art Pop","UK",1999,4),
Album("Hybrid Theory","Linkin Park","Nu Metal","USA",2000,8),
Album("Meteora","Linkin Park","Nu Metal","USA",2003,7),
Album("Minutes To Midnight","Linkin Park","Alternative Rock","USA",2007,6),
Album("American Idiot","Green Day","Alternative Rock","USA",2004,9),
Album("Milo Goes To College","Descendants","Pop Punk","USA",1982,8),
Album("Walk Among Us","Misfits","Punk Rock","USA",1982,6),
Album("Entertainment!","Gang Of Four","Post Punk","UK",1979,8.5),
Album("Juju","Siouxsie and the Banshees","Post Punk","UK",1981,8),
Album("Blizzard Of Ozz","Ozzy Osbourne","Heavy Metal","UK",1980,9),
Album("Diary Of A Madman","Ozzy Osbourne","Heavy Metal","UK",1981,8.5),
Album("Bark At The Moon","Ozzy Osbourne","Heavy Metal","UK",1983,5),
Album("Black Rain","Ozzy Osbourne","Heavy Metal","UK",2007,4),
Album("Metal Health","Quiet Riot","Hard Rock","USA",1983,6),
Album("Imaginations from the Other Side","Blind Guardian","Power Metal","Germany",1995,9),
Album("Películas","La Máquina de Hacer Pájaros","Prog Rock","Argentina",1977,7.5),
Album("El jardín de los presentes","Invisible","Prog Rock","Argentina",1976,8),
Album("Los Delirios Del Mariscal","Crucis","Prog Rock","Argentina",1976,8.5),
Album("Anabella","BuBu","Prog Rock","Argentina",1978,7),
Album("American Football","American Football","Midwest Emo","USA",1999,8),
Album("Nothing Feels Good","The Promise Ring","Midwest Emo","USA",1997,7.5),
Album("Karma","Pharoah Sanders","Free Jazz","USA",1969,7),
Album("Born to Die","Lana Del Rey","Indie Pop","USA",2012,8),
Album("Remain in Light","Talking Heads","New Wave","USA",1980,7),
Album("Little Creatures","Talking Heads","New Wave","USA",1985,7),
Album("The United States of America","The United States of America","Psychedelic Rock","USA",1968,5),
Album("Zentropy","Frankie Cosmos","Indie Pop","USA",2014,6),
Album("Hopes and Fears","Keane","Alternative Pop","UK",2004,7),
Album("X&Y","Coldplay","Alternative Pop","UK",2005,6),
Album("Whatever People Say I Am, That's What I'm Not","Arctic Monkeys","Alternative Rock","UK",2006,8),
Album("Our Endless Numbered Days","Iron & Wine","Indie Folk","USA",2004,4.5),
Album("Sunshine Superman","Donovan","Psychedelic Folk","USA",1966,5.5),
Album("Disraeli Gears","Cream","Psychedelic Rock","UK",1967,7),
Album("Salad Days","Mac DeMarco","Indie Pop","Canada",2014,5),
Album("Odyssey and Oracle","The Zombies","Psychedelic Pop","UK",1968,8.5),
Album("No Boundaries","Michael Angelo Batio","Instrumental Rock","USA",1994,4),
Album("Demon Days","Gorillaz","Alternative Pop","UK",2005,8),
Album("Plastic Beach","Gorillaz","Alternative Pop","UK",2010,7.5),
Album("Audioslave","Audioslave","Alternative Rock","USA",2002,6),
Album("In the Aeroplane Over the Sea","Neutral Milk Hotel","Psychedelic Folk","USA",1998,7.5),
Album("Dive","Tycho","Post Rock","USA",2011,7),
Album("Loveless", "My Bloody Valentine", "Shoegaze", "Ireland", 1991, 9),
Album("Souvlaki", "Slowdive", "Shoegaze", "UK", 1993, 8),
Album("Nowhere", "Ride", "Shoegaze", "UK", 1990,7),
Album("Selling England by the Pound", "Genesis", "Prog Rock", "UK", 1973, 8),
Album("Another Green World", "Brian Eno", "Ambient", "UK", 1975,8),
Album("Spirit of Eden", "Talk Talk", "Post Rock", "UK", 1988,7),
Album("Mezzanine", "Massive Attack", "Trip Hop", "UK", 1998, 8.5),
Album("Purple Rain", "Prince", "Pop", "USA", 1984, 8),
Album("Pink Moon", "Nick Drake", "Folk", "UK", 1972, 7.5),
Album("Trans-Europe Express", "Kraftwerk", "Synthpop", "Germany", 1977, 9),
Album("Alturas de Macchu Picchu", "Los Jaivas", "Prog Rock", "Chile", 1981, 8.5),
Album("Tango", "Tanguito", "Folk", "Argentina", 1973, 7.5),
Album("Spinettalandia y Sus Amigos", "Luis Alberto Spinetta", "Psychedelic Rock", "Argentina", 1971, 3.5),
Album("Pelusón Of Milk", "Luis Alberto Spinetta", "Alternative Rock", "Argentina", 1991, 6.5),
Album("Blue Hawaii", "Elvis Presley", "Pop", "USA", 1961, 1),
Album("Rising Force", "Yngwie Malmsteen", "Heavy Metal", "Sweden", 1984, 7),
Album("Out to Lunch!", "Eric Dolphy", "Avant-Garde Jazz", "USA", 1964, 4.5),
Album("Hot Rats", "Frank Zappa", "Jazz Fusion", "USA", 1969, 8),
Album("Minecraft – Volume Alpha", "C418", "Ambient", "Germany", 2011, 8),
Album("The Velvet Underground & Nico", "The Velvet Underground", "Art Rock", "USA", 1967, 6),
Album("Disintegration", "The Cure", "Post Punk",  "UK", 1989, 8),
Album("Kid A", "Radiohead", "Experimental", "UK", 2000, 9),
Album("Amnesiac", "Radiohead", "Experimental", "UK", 2001, 6.5),
Album("Scott 4", "Scott Walker", "Pop", "UK", 1969, 6),
Album("We're Only in It for the Money", "Mothers Of Invention", "Psychedelic Rock", "USA", 1968, 4),
Album("Crash Bandicoot 3","Josh Mancell","VG OST","USA",1998,7),
Album("Crash Team Racing","Josh Mancell","VG OST","USA",1999,8),
Album("Final Fantasy XII","Hitoshi Sakimoto","VG OST","Japan",2006,8),
Album("Final Fantasy X-2","Noriko Matsued","VG OST","Japan",2003,5.5),
Album("Katamari Damacy","Yuu Miyake","VG OST","Japan",2004,6.5),
Album("Okami","Masami Ueda","VG OST","Japan",2006,7),
Album("Resident Evil 2","Masami Ueda","VG OST","Japan",1998,6.5),
Album("A Series of Unfortunate Events","Thomas Newman","OST","USA",2004,6),
Album("Harry Potter and the Philosopher's Stone","John Williams","OST","UK",2001,9),
Album("Luzbelito","Patricio Rey y Sus Redonditos de Ricota","Alternative Rock","Argentina",1996,8),
Album("Oktubre","Patricio Rey y Sus Redonditos de Ricota","Post Punk","Argentina",1986,8.5),
Album("Artaud", "Pescado Rabioso", "Art Rock", "Argentina", 1973, 7),
Album("In the Court of the Crimson King", "King Crimson", "Prog Rock", "UK", 1969, 9),
Album("Vespertine", "Björk", "Art Pop", "Iceland", 2001, 6.5),
Album("Almendra", "Almendra", "Psychedelic Pop", "Argentina", 1970, 7.5),
Album("La Grasa De Las Capitales", "Serú Girán", "PRog Rock", "Argentina", 1979, 8.5),
]

ranking_artists = Counter(album.artist for album in album_list)
ranking_genres = Counter(album.genre for album in album_list)
ranking_countries = Counter(album.country for album in album_list)
ranking_years = Counter(album.year for album in album_list)
ranking_ratings = Counter(album.rating for album in album_list)

ranking_decade = Counter((album.year // 10) * 10 for album in album_list)
ranking_century = Counter((album.year // 100) * 100 for album in album_list)

top_rank = max(album_list, key=lambda album: album.rating)

print("\n=== RANKING ARTISTS ===")
for i, (artist, cantidad) in enumerate(ranking_artists.most_common(), start=1):
    print(f"{i}. {artist}: {cantidad}")

print("\n=== RANKING GENRES ===")
for i, (genre, cantidad) in enumerate(ranking_genres.most_common(), start=1):
    print(f"{i}. {genre}: {cantidad}")

print("\n=== RANKING COUNTRIES ===")
for i, (country, cantidad) in enumerate(ranking_countries.most_common(), start=1):
    print(f"{i}. {country}: {cantidad}")

print("\n=== RANKING YEARS ===")
for i, (year, cantidad) in enumerate(ranking_years.most_common(), start=1):
    print(f"{i}. {year}: {cantidad}")

print("\n=== RANKING BY RATING ===")
sorted_albums = sorted(album_list, key=lambda album: album.rating, reverse=True)
for i, album in enumerate(sorted_albums, start=1):
    print(f"{i}. [{album.rating}] {album.album} - {album.artist} ({album.year})")

print("\n=== RANKING DECADE ===")
for i, (decade, cantidad) in enumerate(ranking_decade.most_common(), start=1):
    print(f"{i}. {decade}: {cantidad}")

print("\n=== RANKING CENTURY ===")
for i, (century, cantidad) in enumerate(ranking_century.most_common(), start=1):
    print(f"{i}. {century}: {cantidad}")


################################################
# def load_from_json(filename="albums.json"):
#     with open(filename, "r", encoding="utf-8") as f:
#         data = json.load(f)
#     return [Album(
#         d["album"],
#         d["artist"],
#         d["genre"],
#         d["country"],
#         d["year"],
#         d["rating"]
#     ) for d in data]
#
# album_list = load_from_json()
# print(f"{len(album_list)} albums loaded.")
#
# def export_to_json(album_list, filename="albums.json"):
#     data = []
#     for a in album_list:
#         data.append({
#             "album": a.album,
#             "artist": a.artist,
#             "genre": a.genre,
#             "country": a.country,
#             "year": a.year,
#             "rating": a.rating
#         })
#     with open(filename, "w", encoding="utf-8") as f:
#         json.dump(data, f, indent=2, ensure_ascii=False)
#     print(f"{len(data)} albums exported to {filename}")
#
# export_to_json(album_list)