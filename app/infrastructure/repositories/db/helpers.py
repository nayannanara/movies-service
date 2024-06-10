from typing import Any

from sqlalchemy.future import select
from sqlalchemy.sql.elements import BinaryExpression
from sqlalchemy.sql.selectable import Select


def apply_operator(model: Any, field: str, value: Any) -> BinaryExpression:
    if isinstance(value, dict):
        if "in" in value.keys():
            return getattr(model, field).in_(value["in"])

    return getattr(model, field) == value


def build_query(
    model: Any,
    filter: dict[str, Any] | None = None,
) -> Select:
    filter_ = filter or {}
    criteria = tuple(
        apply_operator(model, key, value) for key, value in filter_.items()
    )
    query = select(model).filter(*criteria)

    return query
