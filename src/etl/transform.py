from typing import Any

def transform_users(
    records: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    transformed: list[dict[str, Any]] = []

    for user in records:
        transformed.append({
            "id": user["id"],
            "first_name": user["firstName"],
            "last_name": user["lastName"],
            "email": user["email"],
            "gender": user["gender"],
        })

    return transformed

def transform_products(
    records: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    transformed: list[dict[str, Any]] = []

    for product in records:
        transformed.append({
            "id": product["id"],
            "title": product["title"],
            "description": product["description"],
            "price": product["price"],
            "stock": product["stock"],
        })

    return transformed