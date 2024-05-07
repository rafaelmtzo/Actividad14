from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Nota(BaseModel):
    id: Optional[str] = None
    titulo: str
    autor: str
    fecha_hora: Optional[datetime] = None
    cuerpo: str
    clasificacion: Optional[str] = None
