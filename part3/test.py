
import unittest  # Importamos la librería para hacer pruebas
from app import create_app  # Importamos la app Flask

class TestUserEndpoints(unittest.TestCase):  # Creamos nuestra clase de pruebas
    def setUp(self):  # Esto se ejecuta ANTES de cada prueba
        self.app = create_app()  # Creamos la app de Flask
        self.client = self.app.test_client()  # Cliente para hacer peticiones

    def test_create_user(self):  
        """Prueba que se pueda crear un usuario"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Juan", 
            "last_name": "Dieguito", 
            "email": "juan.Dieguito@example.com"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_user_invalid_data(self):
        """Prueba que un usuario  no se pueda crear con datos invalidos"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "", 
            "last_name": "", 
            "email": "invalid-email"
        })
        self.assertEqual(response.status_code, 400)

    def test_create_amenity(self):
        """Prueba que se pueda crear un amenity"""
        response = self.client.post('/api/v1/amenities/', json={"name": "Balcon"})
        self.assertEqual(response.status_code, 201)

    def test_create_place(self):
        """Prueba que se pueda crear un lugar"""
        user_response = self.client.post('/api/v1/users/', json={
            "first_name": "Lu", 
            "last_name": "Rios", 
            "email": "lu.rios@example.com"
        })
        user_id = user_response.json["id"]

        place_response = self.client.post('/api/v1/places/', json={
            "title": "Departamento pequeño",
            "description": "Un pequeño departamento en el centro de la ciudad", 
            "price": 50,
            "latitude": 40.0, 
            "longitude": -74.0,
            "owner_id": user_id
        })
        self.assertEqual(place_response.status_code, 201)

    def test_get_all(self):
        """Prueba que se puedan obtener todos los elementos"""
        users = self.client.get('/api/v1/users/')
        amenities = self.client.get('/api/v1/amenities/')
        places = self.client.get('/api/v1/places/')
        
        self.assertEqual(users.status_code, 200)
        self.assertEqual(amenities.status_code, 200)
        self.assertEqual(places.status_code, 200)

    def test_get_user_by_id(self):
        """Prueba que se pueda obtener un usuario por su ID"""
        user_response = self.client.post('/api/v1/users/', json={
            "first_name": "Test", 
            "last_name": "User", 
            "email": "test@example.com"
        })
        user_id = user_response.json["id"]
        fetched_user = self.client.get(f'/api/v1/users/{user_id}')
        self.assertEqual(fetched_user.status_code, 200)
        self.assertEqual(fetched_user.json["email"], "test@example.com")

    def test_update_user(self):
        """Prueba que se pueda actualizar un usuario"""
        user_response = self.client.post('/api/v1/users/', json={
            "first_name": "Luis", 
            "last_name": "Gómez", 
            "email": "luis.gomez@example.com"
        })
        user_id = user_response.json["id"]
        
        updated_user = self.client.put(f'/api/v1/users/{user_id}', json={"first_name": "Carlos"})
        self.assertEqual(updated_user.status_code, 200)
        self.assertEqual(updated_user.json["first_name"], "Carlos")

if __name__ == '__main__':
    unittest.main()
