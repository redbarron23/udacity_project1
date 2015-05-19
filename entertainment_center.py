import media
import fresh_tomatoes

dr_strangeLove = media.Movie("Dr. Strangelove or: How I Learned to Stop "
                             "Worrying and Love the Bomb",
                             "The story concerns an unhinged United States \
                              Air Force general who orders a first strike \
                              nuclear attack on "the Soviet Union.",
                              # how to deal w/ long urls
                             "http://upload.wikimedia.org/wikipedia/commons/b/"
                             "bb/Dr._Strangelove.png",
                             "https://youtu.be/1gXY3kuDvSU")

godfather_2 = media.Movie("The Godfather Part_II",
                          "American epic crime film",
                          "http://www.deniro-fans.com/the-godfather-2_poster.jpg",
                          "https://www.youtube.com/watch?v=wPmTp9up26w")

the_hours = media.Movie("The Hours",
                        "The plot focuses on three women of different generations whose lives are interconnected by the novel Mrs Dalloway by Virginia Woolf.",
                        "http://upload.wikimedia.org/wikipedia/en/e/e6/The_Hours_poster.jpg",
                        "https://www.youtube.com/watch?v=gbc7jtmuOJM")

citizen_kane = media.Movie("Citizen Kane",
                           "The story is a film that examines the life and \
                            legacy of Charles Foster Kane, played by Welles, \
                            a character based in part upon the American \
                            newspaper magnate William Randolph Hearst",
                           "http://www.haywiremag.com/wp-content/uploads/2013/09/CitizenKane3.jpg",
                           "https://www.youtube.com/watch?v=zyv19bg0scg")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                "http://goinswriter.com/wp-content/uploads/2011/06/midnight-in-paris.png",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

schindlers_list = media.Movie("Schindler's List",
                              "The film is based on the life of Oskar \
                               Schindler, a German businessman who saved the \
                               lives of more than a thousand mostly \
                               Polish-Jewish refugees during the Holocaust by \
                               employing them in his factories",
                              "http://upload.wikimedia.org/wikipedia/en/3/38/Schindler%27s_List_movie.jpg",
                              "https://www.youtube.com/watch?v=dwfIf1WMhgc"

movies = [godfather_2, the_hours, citizen_kane, midnight_in_paris,
          schindlers_list, dr_strangeLove]
fresh_tomatoes.open_movies_page(movies)
