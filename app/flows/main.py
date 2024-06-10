import pandas as pd
from prefect import flow, task
import httpx
from app.application.core.exceptions import RequestError


@task(retries=3, retry_delay_seconds=10, timeout_seconds=10, log_prints=True)
def fetch_all_data():
    url = "http://localhost:8000/movies?offset=0&limit=100"
    movies = []

    try:
        while True:
            with httpx.Client(timeout=10) as client:
                response = client.get(url)
            response.raise_for_status()
            result = response.json()["results"]
            movies.extend(result)
            if not result:
                break

            url = response.json().get("next")
        return movies
    except httpx.RequestError as e:
        raise RequestError(f"Failed to fetch data: {e}")


@task
def create_csv(data):
    df = pd.DataFrame(data)
    df.to_csv("movies_output.csv", index=False)


@flow(name="Criar CSV FILE")
def start():
    try:
        data = fetch_all_data()
        create_csv(data=data)
    except RequestError as exc:
        print(exc.message)


if __name__ == "__main__":
    start()
