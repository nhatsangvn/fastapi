from fastapi import APIRouter
from model.creature import Creature
import service.creature as service

router = APIRouter(prefix = "/creature")

@router.get("")
@router.get("/")
def get_all() -> list[Creature]:
    return service.get_all()

@router.get("/{name}")
def get_one(name) -> Creature | None:
    return service.get_one(name)

@router.post("")
@router.post("/")
def create(creature: Creature) -> Creature:
    try:
        return service.create(explorer)
    except Duplicate as exc:
        raise HTTPException(status_code=409, detail=exc.msg)

@router.patch("")
def modify(creature: Creature) -> Creature:
    try:
        return service.modify(name, explorer)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.put("")
def replace(creature: Creature) -> Creature:
    return service.replace(creature)

@router.delete("/{name}")
def delete(name: str):
    try:
        return service.delete(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)