def response_movies():
    return {
        "count": 2,
        "next": "http://localhost:8000/movies?limit=2&offset=2",
        "previous": "http://localhost:8000/movies?limit=2&offset=0",
        "results": [
            {
                "id": "f9f8140b-4fd5-495c-8c75-ba7b55cb45cb",
                "created_at": "2024-06-10T09:49:26.363288",
                "title": "Batman & Robin",
                "release_date": "4 de julho de 1997",
                "duration": "2h 05min",
                "kinds": "Ação, Fantasia, Suspense",
                "directors": "Joel Schumacher",
                "cast": "George Clooney, Arnold Schwarzenegger, Chris O'Donnell",
                "original_title": None,
                "note": 2,
                "description": "A dupla dinâmica enfrenta uma terrível"
                " dupla de vilões: o gélido Mr. Freeze (Arnold Schwarzenegger)"
                "e a delicada botânica que, ao sofrer um acidente, "
                "transforma-se na perigosa e vingativa Hera Venenosa (Uma Thurman). "
                "Mas, para poder livrar Gotham City das garras dos vilões, "
                "Batman (George Clooney) e Robin (Chris O'Donnell) "
                "contam com uma nova ...",
            },
            {
                "id": "58b962d7-ef63-49a8-a6f4-15e71cdd00d6",
                "created_at": "2024-06-10T09:50:35.319993",
                "title": "Monstros Vs. Alienígenas",
                "release_date": "3 de abril de 2009",
                "duration": "1h 33min",
                "kinds": "Animação",
                "directors": "Rob Letterman, Conrad Vernon",
                "cast": "Reese Witherspoon, Seth Rogen, Hugh Laurie",
                "original_title": "Monsters vs. Aliens",
                "note": 3.9,
                "description": "Susan Murphy (Reese Witherspoon) está prestes"
                " a se casar com Derek Dietl (Paul Rudd), um repórter de TV "
                "que sonha em ascender profissionalmente. No dia de seu"
                "casamento ela é atingida por um meteorito, oriundo de um "
                "planeta que explodiu recentemente. A radioatividade do "
                "objeto espacial faz com que ela cresça até"
                "a altura de 15 metros. Sem ...",
            },
        ],
    }
