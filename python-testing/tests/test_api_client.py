import unittest, requests
from src.api_client import get_location
from unittest.mock  import patch


class ApiClientTests(unittest.TestCase):

    @patch('src.api_client.requests.get')
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "countryName": "USA",
            "regionName": "FLORIDA",
            "cityName": "MIAMI",
        }
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")

        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8") #Confirma que se llama a la URL correcta
        
    @patch('src.api_client.requests.get')
    def test_get_location_returns_side_effect(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException("Error de conexión"),
            unittest.mock.Mock(status_code=200, json=lambda: {
                "countryName": "USA",
                "regionName": "FLORIDA",
                "cityName": "MIAMI",
            })
        ]

        with self.assertRaises(requests.exceptions.RequestException):
            get_location("8.8.8.8")  # Lanza una excepción de conexión
                         
        result = get_location("8.8.8.8") # Llama a la segunda respuesta simulada
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")
        
        """RETO
        Si envia una validación para una ip inválida,
        debería lanzar una excepción de tipo ValueError.
        
        si envia una ip valida, debería retornar un diccionario con las claves country, region y city.
        """

    def test_get_location_with_invalid_ip_raises_value_error(self):
        """Verifica que se lanza ValueError con una IP inválida."""
        with self.assertRaises(ValueError):
            get_location("invalid_ip")

    def test_get_location_with_empty_ip_raises_value_error(self):
        """Verifica que se lanza ValueError con una IP vacía."""
        with self.assertRaises(ValueError):
            get_location("")