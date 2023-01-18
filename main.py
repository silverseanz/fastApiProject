from fastapi import FastAPI,Query,Path,Body
from typing import Optional,Union
from pydantic import BaseModel,Field

app = FastAPI()

class Item(BaseModel):
    name:str
    description:Union[str,None] = Field(default=None,title='item介绍',max_length=200)
    price:float = Field(gt=0,title='item价格',)
    tax:Union[float,None]

    class Config:
        schema_extra = {
            "example":{
            "name":"MoDeShan",
            "description":"a player name of Escape From Tarkov",
            "price":100,
            "tax":10.5
            }
        }

@app.put("/items/{item_kid}")
async def update_itemname(item_kid:int,item:Item = Body(...,embed=True)):
    results = {"item_kid":item_kid,"item":item}


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

@app.put("/item/{item_id}")
async def update_item(item_id:int,item:Item = Body(...,embed=True)):
    results = {"item_id":item_id,"item":item}
    return results


@app.get("/items/{item_id}")
async def say_hello(*,item_id: Optional[int] = Path(...,title="物品id"), q: str):
    results = {"item_id":item_id}
    if q :
        results.update({"q":q})
    return results

# @app.get("/items/")
# async def read_item(
#         q:Optional[str] = Query(None,max_length=30)
# ):
#     results = {"items":[{"item_id":"foo"},{"item_id":"bar"}]}
#     if q:
#         results.update({"q":q})
#     return results


# @app.get("/items/1")
# async def read_item(
#         q:Optional[str] = Query(
#             None,
#             title="for example",
#             description="Just have a test of description"
#             )
# ):
#     request_list = {"q":q}
#     return  request_list