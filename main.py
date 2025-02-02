from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - list-and-dic-coll-304d0c851d7f498fa687a569d0933973',debug=False,docs_url='/festive-sagar-b1c9d954c90511ef920d0242ac1200054/docs',openapi_url='/festive-sagar-b1c9d954c90511ef920d0242ac1200054/openapi.json')

app.include_router(router, prefix='/festive-sagar-b1c9d954c90511ef920d0242ac1200054/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()