uvicorn web:app

http :8000/creature

- validate data in model.py
    conint: gt, lt, ge, le, multiple_of
    constr: min_length, max_length, to_upper, to_lower, regex
    tuple, list, or set: min_items, max_items