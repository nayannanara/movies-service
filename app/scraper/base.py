import requests
from bs4 import BeautifulSoup
from app.application.core.logging import logger


class MovieScraper:
    def __init__(self) -> None:
        self.url = "https://www.adorocinema.com/filmes/criancas/"

    def get_number_of_pages(self, html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        pagination = soup.find(class_="pagination-item-holder")
        return int(pagination.find_all(class_="item")[-1].text)

    def get_directors(self, movie):
        director_infos = movie.find(class_="meta-body-direction")
        if director_infos:
            directors = director_infos.find_all(class_="dark-grey-link")
            names = [item.text for item in directors]
            return ", ".join(names)

    def get_cast(self, movie):
        actor_infos = movie.find(class_="meta-body-actor")

        if actor_infos:
            actors = actor_infos.find_all(class_="dark-grey-link")
            names = [item.text for item in actors]
            return ", ".join(names)

    def get_html_content(self, url):
        response = requests.get(url)
        if not response.status_code == 200:
            logger.info(f"Erro ao acessar a página: {response.status_code}")
        html_content = response.content
        return html_content

    def run(self):
        movies = []
        html_content = self.get_html_content(url=self.url)
        number = self.get_number_of_pages(html_content=html_content)
        logger.info("Iniciando extração de dados")

        if number > 1:
            for i in range(1, number + 1):
                url = f"{self.url}?page={i}"
                html_content = self.get_html_content(url=url)
                data = self.get_movie_data(html_content=html_content)
                movies.extend(data)
        else:
            html_content = self.get_html_content(url=self.url)
            data = self.get_movie_data(html_content=html_content)
            movies.extend(data)

        logger.info("Extração concluída")
        return movies

    def get_movie_data(self, html_content):
        data = []
        soup = BeautifulSoup(html_content, "html.parser")
        movies = soup.find_all(class_="card")
        for movie in movies:
            title = movie.find(class_="meta-title").text.strip()
            infos = movie.find(class_="meta-body-info").text.split("|")
            if len(infos) == 2:
                kinds = infos[1].strip()
                duration = None
            else:
                kinds = infos[2].strip().replace("\n", " ")
                duration = infos[1].strip()
            release_date = infos[0].strip()
            directors = self.get_directors(movie=movie)
            cast = self.get_cast(movie=movie)
            original_title = (
                movie.find(class_="dark-grey").text
                if movie.find(class_="dark-grey")
                else None
            )
            note = (
                float(movie.find(class_="stareval-note").text.replace(",", "."))
                if movie.find(class_="stareval-note")
                else None
            )
            description = movie.find(class_="content-txt").text.strip()
            item = {
                "title": title,
                "release_date": release_date,
                "duration": duration,
                "kinds": kinds,
                "directors": directors,
                "cast": cast,
                "original_title": original_title,
                "note": note,
                "description": description,
            }
            data.append(item)
        return data
