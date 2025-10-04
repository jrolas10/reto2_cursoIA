from backend.database import Base, engine
from backend.models import User, IoTDevice

def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas creadas en la base de datos.")
