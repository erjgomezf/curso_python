# Apuntes de asserts en Python con unittest

```python
import unittest
SERVER = "production"

class AllAssertsTest(unittest.TestCase):
    # Test para verificar que se lanza una excepción específica
    def test_assert_raises(self):
        with self.assertRaises(ValueError, msg="Se esperaba un ValueError"):
            raise ValueError("Este es un error de prueba")
        
    # test para casos iguales y no iguales
    def test_assert_equal(self):
        self.assertEqual(1+1, 2, "1 + 1 suma es igual a 2")
        
    def test_assert_not_equal(self):
        self.assertNotEqual(1+1, 3, "1 + 1 suma no es igual a 3")
    
    # test para casos de mayor, menor, mayor o igual, menor o igual
    def test_assert_greater(self):
        self.assertGreater(2, 1, "2 es mayor que 1")
        
    def test_assert_less(self):
        self.assertLess(1, 2, "1 es menor que 2")
        
    def test_assert_greater_equal(self):
        self.assertGreaterEqual(2, 2, "2 es mayor o igual a 2")
        
    def test_assert_less_equal(self):
        self.assertLessEqual(1, 2, "1 es menor o igual a 2")
    
    # test para casos de pertenencia, identidad y excepciones
    def test_assert_in(self):
        self.assertIn(1, [1, 2, 3], "1 está en la lista [1, 2, 3]")
        
    def test_assert_not_in(self):
        self.assertNotIn(4, [1, 2, 3], "4 no está en la lista [1, 2, 3]")
    
    def test_assert_is(self):
        self.assertIs("hello", "hello", "Las dos cadenas son la misma instancia")
        
    def test_assert_is_not(self):
        self.assertIsNot("hello", "world", "Las dos cadenas son instancias diferentes")
    
    # Test para casos de igualdad y desigualdad con tolerancia
    def test_assert_almost_equal(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=7, msg="0.1 + 0.2 debe ser aproximadamente igual a 0.3") # tolerancia de 7 lugares decimales
        
    def test_assert_not_almost_equal_with_places(self):
        self.assertNotAlmostEqual(0.1 + 0.2, 0.4, places=7, msg="0.1 + 0.2 no debe ser aproximadamente igual a 0.4") # tolerancia de 7 lugares decimales
        
    # Test para casos de igualdad y desigualdad con tolerancia
    def test_assert_true(self):
        self.assertTrue(1 < 2, "1 es menor que 2")
        
    def test_assert_false(self):
        self.assertFalse(1 > 2, "1 no es mayor que 2")
        
    # Test para casos de cadenas, listas, conjuntos y diccionarios
    def test_assert_is_none(self):
        self.assertIsNone(None, "El valor es None")
        
    def test_assert_is_not_none(self):
        self.assertIsNotNone(1, "El valor no es None")
        
    def test_assert_count(self):
        self.assertCountEqual([1, 2, 3], [3, 2, 1], "Las listas tienen los mismos elementos sin importar el orden")
    
    def test_assert_multi_line(self):
        self.assertMultiLineEqual("line1\nline2", "line1\nline2", "Las dos cadenas multilinea son iguales")
        
    def test_assert_regex(self):
        import re
        self.assertRegex("abc123", r"\d+", "La cadena contiene números")
        
    def test_assert_not_regex(self):
        import re
        self.assertNotRegex("abc", r"\d+", "La cadena no contiene números")
        
    def test_assert_dict_equal(self):
        self.assertDictEqual({"a": 1, "b": 2}, {"b": 2, "a": 1}, "Los diccionarios son iguales sin importar el orden de las claves")
    
    def test_assert_list_equal(self):
        self.assertListEqual([1, 2, 3], [1, 2, 3], "Las listas son iguales, importando el orden")
        
    def test_assert_set_equal(self):
        self.assertSetEqual({1, 2, 3}, {3, 2, 1}, "Los conjuntos son iguales sin importar el orden")
        
    def test_assert_sequence_equal(self):
        self.assertSequenceEqual((1, 2, 3), (1, 2, 3), "Las secuencias son iguales, importando el orden")
        
    # Test para casos de excepciones
    def test_assert_is_instance(self):
        self.assertIsInstance("hello", str, "La cadena 'hello' es una instancia de str")
        
    def test_assert_not_is_instance(self):
        self.assertNotIsInstance(1, str, "El entero 1 no es una instancia de str")
        
    @unittest.skip("Trabajo en progreso, sera habilitada nuevamente en el futuro")
    def test_skip(self):
        self.assertEqual("hola", "chao", "comparación entre cadenas no es correcta")
        
    @unittest.skipIf(SERVER=="production", "No se ejecuta en producción")
    def test_skip_if(self):
        self.assertEqual(100, 100, "comparación entre enteros es correcta")
        
    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(1, 2, "Esta prueba debería fallar intencionalmente")
        
    @unittest.skipUnless(SERVER=="production", "Solo se ejecuta en producción")
    def test_skip_unless(self):
        self.assertEqual("test", "test", "Esta prueba solo se ejecuta en producción")
```

---

## Resumen de asserts útiles en unittest

- `assertEqual(a, b)`: Verifica que `a == b`.
- `assertNotEqual(a, b)`: Verifica que `a != b`.
- `assertTrue(x)`: Verifica que `x` es verdadero.
- `assertFalse(x)`: Verifica que `x` es falso.
- `assertIs(a, b)`: Verifica que `a` y `b` son la misma instancia.
- `assertIsNot(a, b)`: Verifica que `a` y `b` no son la misma instancia.
- `assertIsNone(x)`: Verifica que `x` es `None`.
- `assertIsNotNone(x)`: Verifica que `x` no es `None`.
- `assertIn(a, b)`: Verifica que `a` está en `b`.
- `assertNotIn(a, b)`: Verifica que `a` no está en `b`.
- `assertGreater(a, b)`: Verifica que `a > b`.
- `assertLess(a, b)`: Verifica que `a < b`.
- `assertGreaterEqual(a, b)`: Verifica que `a >= b`.
- `assertLessEqual(a, b)`: Verifica que `a <= b`.
- `assertAlmostEqual(a, b, places)`: Verifica que `a` y `b` son aproximadamente iguales.
- `assertNotAlmostEqual(a, b, places)`: Verifica que `a` y `b` no son aproximadamente iguales.
- `assertCountEqual(a, b)`: Verifica que las listas tienen los mismos elementos, sin importar el orden.
- `assertMultiLineEqual(a, b)`: Verifica que dos cadenas multilinea son iguales.
- `assertRegex(a, r)`: Verifica que la cadena `a` coincide con el regex `r`.
- `assertNotRegex(a, r)`: Verifica que la cadena `a` no coincide con el regex `r`.
- `assertDictEqual(a, b)`: Verifica que dos diccionarios son iguales.
- `assertListEqual(a, b)`: Verifica que dos listas son iguales.
- `assertSetEqual(a, b)`: Verifica que dos conjuntos son iguales.
- `assertSequenceEqual(a, b)`: Verifica que dos secuencias son iguales.
- `assertIsInstance(a, tipo)`: Verifica que `a` es instancia de `tipo`.
- `assertNotIsInstance(a, tipo)`: Verifica que `a` no es instancia de `tipo`.
- `assertRaises(error)`: Verifica que se lanza una excepción.
- Decoradores:  
  - `@unittest.skip("razón")`
  - `@unittest.skipIf(condición, "razón")`
  - `@unittest.skipUnless(condición, "razón")`
  - `@unittest.expectedFailure`

---

Puedes copiar este contenido a tu archivo `.md` para tus apuntes.






