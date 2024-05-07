from fastapi import FastAPI, HTTPException
from .models import Nota
from typing import List
from uuid import uuid4, UUID

app = FastAPI()

# Simulación de base de datos en memoria
db: List[Nota] = []

@app.post("/notas/", response_model=Nota)
def crear_nota(nota: Nota):
    nota.id = uuid4()  # Asignar un ID único a la nota
    db.append(nota)
    return nota

@app.get("/notas/", response_model=List[Nota])
def leer_notas():
    return db

@app.put("/notas/{nota_id}", response_model=Nota)
def actualizar_nota(nota_id: UUID, nota: Nota):
    for n in db:
        if n.id == nota_id:
            n.titulo = nota.titulo
            n.autor = nota.autor
            n.fecha_hora = nota.fecha_hora
            n.cuerpo = nota.cuerpo
            n.clasificacion = nota.clasificacion
            return n
    raise HTTPException(status_code=404, detail="Nota no encontrada")

@app.delete("/notas/{nota_id}", response_model=dict)
def eliminar_nota(nota_id: UUID):
    for index, n in enumerate(db):
        if n.id == nota_id:
            db.pop(index)
            return {"mensaje": "Nota eliminada"}
    raise HTTPException(status_code=404, detail="Nota no encontrada")

