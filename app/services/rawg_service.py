from app.clients.rawg_clients import RAWGClient
from app.models.juegoDMC import JuegoDMC

def listar_saga_dmc():
    juegos_raw = RAWGClient(api_key="381a942d4ead4fa089ded136a5153827").get_saga_dmc()
    
    if juegos_raw is None:
        print("error: El cliente devolvió None")
        return []
    
    print(f"Cargando {len(juegos_raw)} juegos.")

    lista_objetos = []

    for item in juegos_raw:
        nombre_juego = item.get('name', '')
        
        if "devil may cry" in nombre_juego.lower() or "dmc" in nombre_juego.lower():
            
            try:
                raw_platforms = item.get('platforms') or []
                
                nombres_plataformas = [
                    p.get('platform', {}).get('name', 'N/A') 
                    for p in raw_platforms 
                    if isinstance(p, dict)
                ]

                juego_obj = JuegoDMC(
                    id=item.get('id'),
                    name=nombre_juego,
                    released=item.get('released', 'Sin fecha'),
                    background_image=item.get('background_image', ''),
                    rating=item.get('rating', 0),
                    platforms=nombres_plataformas
                )
                
                lista_objetos.append(juego_obj)
                
            except Exception as e:
                print(f"Error con: {nombre_juego}: {e}")
                continue

    return lista_objetos