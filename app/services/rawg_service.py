from app.clients.rawg_clients import RAWGClient
from app.models.juegoDMC import JuegoDMC

def listar_saga_dmc():
    cliente_instancia = RAWGClient(api_key="381a942d4ead4fa089ded136a5153827")
    juegos_raw = cliente_instancia.get_saga_dmc()
    
    if not juegos_raw:
        return []

    entregas_añadidas = set()
    lista_objetos = []

    for item in juegos_raw:
        nombre = item.get('name', '')
        nombre_low = nombre.lower()
        
        identificador = None
        if "hd collection" in nombre_low: identificador = "HDC"
        elif "5" in nombre_low: identificador = "DMC5"
        elif "dmc: devil may cry" in nombre_low: identificador = "REBOOT"
        elif "4" in nombre_low: identificador = "DMC4"
        elif "3" in nombre_low: identificador = "DMC3"
        elif "2" in nombre_low: identificador = "DMC2"
        elif "devil may cry" in nombre_low: identificador = "DMC1"

        if identificador and identificador not in entregas_añadidas:
            try:
                platforms = [p.get('platform', {}).get('name') for p in item.get('platforms', [])]
                fecha = item.get('released')

                nuevo_juego = JuegoDMC(
                    id=item.get('id'),
                    name=nombre,
                    released=fecha,
                    background_image=item.get('background_image', ''),
                    rating=item.get('rating', 0),
                    platforms=platforms
                )
                
                lista_objetos.append(nuevo_juego)
                entregas_añadidas.add(identificador)
                print(f"Agregado: {nombre}")
            except Exception as e:
                print(f"Error: {nombre}: {e}")

    lista_objetos.sort(key=lambda x: x.released)
    
    return lista_objetos