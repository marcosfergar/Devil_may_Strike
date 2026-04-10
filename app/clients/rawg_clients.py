from collections import OrderedDict
import requests
import time

class RAWGClient:
    URL = "https://api.rawg.io/api/games"
    TTL = 86400

    def __init__(self, api_key):
        self.api_key = api_key
        self._cache = OrderedDict()
        self.max_cache = 10

    def _get_cache(self, key):
        item = self._cache.get(key)
        if item is None:
            return None

        if time.time() > item["tiempo"]:
            del self._cache[key]
            return None
        
        self._cache.move_to_end(key)
        return item["value"]

    def _set_cache(self, key, value):
        if key in self._cache:
            self._cache.move_to_end(key)
        elif len(self._cache) >= self.max_cache:
            self._cache.popitem(last=False)

        self._cache[key] = {
            "value": value,
            "tiempo": time.time() + self.TTL
        }

    def get_saga_dmc(self):
        cache_key = "saga_completa_dmc"
        cached = self._get_cache(cache_key)
        if cached: return cached

        try:
            params = {
                'key': self.api_key,
                'search': 'devil-may-cry',
                'page_size': 20
            }
            resp = requests.get(self.URL, params=params, timeout=10)
            resp.raise_for_status()
            
            data = resp.json()
            juegos = data.get('results', [])
            
            print(f"carga {len(juegos)} juegos.")
            
            self._set_cache(cache_key, juegos)
            return juegos
        except Exception as e:
            print(f"CLIENT ERROR: {e}")
            return []