#importamos módulos
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from database import Session, Base, engine
from models import Movie
from schemas import MovieModel

Base.metadata.create_all(bind=engine)


#instanciamos el objeto
app = FastAPI()

#El decorador indica el comportamiento de la función que continua
@app.get("/")
def index():
    return {"Hi from fastApi"}

'''
Este también funciona. Lógica de query:
creación de instancia de la session.
variable res = session.query(ModeloORM).petición
'''

@app.get("/movies")
def get_movies():
    db = Session()
    res = db.query(Movie).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(res))
    

'''
Este método post funciona. Errores que sucedieron en el camino:
No estaba trabajando correctamente con el Modelo_pydantic. Es decir, se creaba la instancia
del modelo y se pasaba al método post de la web, pero al trabajar la inserción en la BD no 
estaba creando la instancia del modelo del ORM, por eso daba error en un principio.
Otro error fue el de dejar la id como parámetro. Lo borré del modelo pydantic pero
quedó como autoincremental en el ORM
'''

@app.post("/movies", response_model=dict)
def add_movie(new_mov:MovieModel):
    db = Session()
    print(f"Aca: {new_mov.title}")
    new_movie = Movie(**new_mov.dict())
    db.add(new_movie)
    db.commit()
    return JSONResponse(status_code=201, content={'mensaje':f'Se agregó correctamente el registro'})
