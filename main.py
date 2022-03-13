# fastAPIをインポート
# from enum import Enum
from typing import Optional

from fastapi import FastAPI




# FastAPIのインスタンス作成
# uvicornで呼び出す main:XX
app = FastAPI()

# デコレータ　= 直下の関数を用いて何かをおこなう
# パス / , オペレーション　get , 関数 def XX()
# [直下の関数 の引数 が、 "get を使用した パス /" に対応すること]をFastAPIに通知する
# /items/XX を叩くと、関数が呼び出される

@app.get("/items/{item_id}")
async def read_item(item_id: str, q:Optional[str] = None, short:bool = False):
	item = {"item_id": item_id}
	if q:
		return {"item_id": item_id, "q": q}
	return {"item_id": item_id}

# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
# @app.get("/items/")
# async def read_item(skip: int=0, limit:int=10):
# 	return fake_items_db[skip: skip+limit]

# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
# 	return {"file_path": file_path}

# class ModelName(str, Enum):
# 	alexnet = "alexnet"
# 	resnet = "resnet"
# 	lenet = "lenet"
# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
# 	if model_name == ModelName.alexnet:
# 		return {"model_name": model_name, "message": "Deep Learning FTW!"}

# 	if model_name == "lenet":
# 		return {"model_name": model_name, "message": "LeCCN all the images"}

# 	return {"model_name": model_name, "message": "Have some residuals"}


# @app.get("/users/me")
# async def read_user_me():
# 	return {"user_id": "the current User"}

# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
# 	return {"user_id": user_id}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
# 	return {"item_id": item_id}
# async def root():
# 	return {"message": "Hello World"}
