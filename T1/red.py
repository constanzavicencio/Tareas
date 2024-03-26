import dcciudad
from collections import deque

class RedMetro:
    def __init__(self, red: list, estaciones: list) -> None:
        self.red = red
        self.estaciones = estaciones

    def informacion_red(self) -> list:
        largo = len(self.estaciones)
        self.lista = []
        for i in range(largo):
            suma = 0
            for j in range(largo):
                suma += self.red[i][j]
            self.lista.append(suma)
        return [largo, self.lista]

    def agregar_tunel(self, inicio: str, destino: str) -> int:
        largo = len(self.estaciones)
        inicio_index = self.estaciones.index(inicio)
        destino_index = self.estaciones.index(destino)
        if self.red[inicio_index][destino_index] == 1:
            return -1
        else:
            self.red[inicio_index][destino_index] = 1
            suma = 0
            for j in range(largo):
                suma += self.red[inicio_index][j]
            return suma

    def tapar_tunel(self, inicio: str, destino: str) -> int:
        largo = len(self.estaciones)
        inicio_index = self.estaciones.index(inicio)
        destino_index = self.estaciones.index(destino)
        if self.red[inicio_index][destino_index] == 0:
            return -1
        else:
            self.red[inicio_index][destino_index] = 0
            suma = 0
            for j in range(largo):
                suma += self.red[inicio_index][j]
            return suma

    def invertir_tunel(self, estacion_1: str, estacion_2: str) -> bool:
        est_1_index = self.estaciones.index(estacion_1)
        est_2_index = self.estaciones.index(estacion_2)
        if self.red[est_1_index][est_2_index] == 1:
            if self.red[est_2_index][est_1_index] == 1:
                return True
            else:
                self.red[est_1_index][est_2_index] = 0
                self.red[est_2_index][est_1_index] = 1
                return True
        else:
            if self.red[est_2_index][est_1_index] == 0:
                return False
            else:
                self.red[est_1_index][est_2_index] = 1
                self.red[est_2_index][est_1_index] = 0
                return True

    def nivel_conexiones(self, inicio: str, destino: str) -> str:
        inicio_index = self.estaciones.index(inicio)
        destino_index = self.estaciones.index(destino)
        largo = len(self.estaciones)
        def conec_directa(inicio, destino):
            if self.red[inicio][destino] == 1:
                return True
            return False
        if conec_directa(inicio_index, destino_index):
            return 'túnel directo'
        else:
            suma = 0
            for i in range(largo):
                if self.red[inicio_index][i] == 1 and self.red[i][destino_index] == 1:
                    suma = 1
            if suma == 1:
                return 'estación intermedia'
            else:
                if dcciudad.alcanzable(self.red, inicio_index, destino_index):
                    return 'muy lejos'
                else:
                    return 'no hay ruta'
                
    def rutas_posibles(self, inicio: str, destino: str, p_intermedias: int) -> int:
        inicio_index = self.estaciones.index(inicio)
        destino_index = self.estaciones.index(destino)
        largo = len(self.estaciones)
        cola = deque([(inicio_index, 0)])
        contador_rutas = 0

        while cola:
            nodo, intermedias = cola.popleft()
            if nodo == destino_index and intermedias == p_intermedias:
                contador_rutas += 1
            if intermedias < p_intermedias:
                for i in range(largo):
                    if self.red[nodo][i] == 1:
                        cola.append((i, intermedias + 1))

        return contador_rutas
       

    def ciclo_mas_corto(self, estacion: str) -> int:
        pass

    def estaciones_intermedias(self, inicio: str, destino: str) -> list:
        pass

    def estaciones_intermedias_avanzado(self, inicio: str, destino: str) -> list:
        pass

    def cambiar_planos(self, nombre_archivo: str) -> bool:
        pass

    def asegurar_ruta(self, inicio: str, destino: str, p_intermedias: int) -> list:
        pass