import unittest  # Importamos la librería para hacer pruebas
from app import create_app  # Importamos la app Flask
from app.services.facade import HBnBFacade  # Importamos la Facade

class TestHBnBFacade(unittest.TestCase):  # Creamos nuestra clase de pruebas
    test_user = 0
    def setUp(self):  # Esto se ejecuta ANTES de cada prueba
        self.app = create_app()  # Creamos la app de Flask
        self.client = self.app.test_client()  # Cliente para hacer peticiones
        self.facade = HBnBFacade()  # Creamos la Facade que maneja los datos


    def test_create_user(self):  
        """Prueba que se pueda crear un usuario"""
        user_data = {
            "first_name": "Juan", 
            "last_name": "Pérez", 
            "email": "juan.perez@example.com"
        }
        
        user = self.facade.create_user(user_data)  # Creamos un usuario
        test_user =user
        # Comprobamos que se haya creado bien
        self.assertIsNotNone(user)  # Verifica que el usuario no sea None
        self.assertEqual(user.first_name, "Juan")  # Verifica que el nombre sea correcto

    def test_create_amenity(self):
        """Prueba que se pueda crear un amenity"""
        amenity_data = {"name": "WiFi"}  # Amenity de ejemplo
        
        amenity = self.facade.create_amenity(amenity_data)  # Creamos un amenity
        
        self.assertIsNotNone(amenity)  # Verificamos que se creó bien
        self.assertEqual(amenity.name, "WiFi")  # Verificamos que el nombre sea correcto

    def test_create_place(self):
        """Prueba que se pueda crear un lugar"""
        place_data = {
            "title": "Departamento pequeño",
            "description": "Un pequeño departamento en el centro de la ciudad", 
            "price": 50,
            "latitude": 40.0, 
            "longitude": -74.0,
            
        }
        
        place = self.facade.create_place(place_data)  # Creamos un lugar
        
        self.assertIsNotNone(place)  # Verificamos que se creó bien
        self.assertEqual(place.title, "Departamento pequeño")  # Verificamos el título

    def test_get_all(self):
        """Prueba que se puedan obtener todos los elementos"""
        
        users = self.facade.get_all_users()  # Obtenemos todos los usuarios
        amenities = self.facade.get_all_amenities()  # Obtenemos todos los amenities
        places = self.facade.get_all_places()  # Obtenemos todos los lugares
        
        # Verificamos que cada uno sea una lista (aunque esté vacía)
        self.assertIsInstance(users, list)
        self.assertIsInstance(amenities, list)
        self.assertIsInstance(places, list)

    def test_get_by_id(self):
        """Prueba que se pueda obtener un usuario por su ID"""
        
        # Creamos un usuario de prueba
        user_data = {
            "first_name": "Test", 
            "last_name": "User", 
            "email": "test@example.com"
        }
        user = self.facade.create_user(user_data)
        
        # Lo buscamos por su ID
        fetched_user = self.facade.get_user(user.id)
        
        # Comprobamos que es el mismo usuario
        self.assertIsNotNone(fetched_user)
        self.assertEqual(fetched_user.email, "test@example.com")

    def test_update_user(self):
        """Prueba que se pueda actualizar un usuario"""
        
        # Creamos un usuario
        user_data = {
            "first_name": "Luis", 
            "last_name": "Gómez", 
            "email": "luis.gomez@example.com"
        }
        user = self.facade.create_user(user_data)
        
        # Actualizamos el nombre
        updated_user = self.facade.update_user(user.id, {"first_name": "Carlos"})
        
        # Comprobamos que el nombre cambió
        self.assertEqual(updated_user.first_name, "Carlos")

# Esto ejecuta las pruebas cuando corremos el archivo
if __name__ == '__main__':
    unittest.main()