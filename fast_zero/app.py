from fastapi import FastAPI
from fast_zero.schemas import UserSchema, UserPublic

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'ola mundo'}

@app.post('/users/', status_code = 201, response_model=UserPublic)
def create_user(user: UserSchema):
    return UserPublic(**user.model_dump())
