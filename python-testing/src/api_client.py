import requests
import ipaddress

def get_location(ip):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        raise ValueError("Invalid IP address")
        
    url = f"https://freeipapi.com/api/json/{ip}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    #import ipdb; ipdb.set_trace() # Se debe eliminar esta línea en producción
    return {
        "country": data["countryName"],
        "region": data["regionName"],
        "city": data["cityName"],
    }


