from typing import Optional


class BaseException(Exception):
    def __init__(
        self,
        *args: object,
        message: Optional[str] = None,
    ) -> None:
        super().__init__(*args)

        if message:
            self.message = message


class RequestError(BaseException):
    message = "Ocorreu um erro na chamada da API"
