from model.tag import TagIn, Tag, TagOut
import service.tag as service

@app.post('/'):
def create(tag_in: TagIn) -> TagIn:
    tag: Tag = Tag(tag=tag_str, created=datetime.utcnow(),
        secret="shhhh")
    service.create(tag)
    return tag_in

@app.get('/{tag_str}', response_model=TagOut)
def get_one(tag_str: str) -> TagOut:
    tag: Tag = service.get(tag_str)
    return tag

