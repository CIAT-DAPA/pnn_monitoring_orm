import unittest
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
orm_dir_path = os.path.abspath(os.path.join(dir_path, '..'))
sys.path.append(orm_dir_path)

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from src.pnn_monitoring_orm import *

class DatabaseConnection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:', echo=True)
        Session = sessionmaker(bind=cls.engine)
        cls.session = Session()

    def setUp(self):
        print('hola mundo')
        Base.metadata.bind = self.engine
        Base.metadata.create_all(self.engine)

    def test_conexion_base_de_datos(self):
        table = Base.metadata.tables.get('Action') 
        self.assertIsNotNone(table, "La tabla no existe en la base de datos")


    def tearDown(self):
        # Limpiar la sesión y eliminar las tablas después de la prueba
        self.session.close()
        Base.metadata.drop_all(self.engine)

if __name__ == '__main__':
    unittest.main()