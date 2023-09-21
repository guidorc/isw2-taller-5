import random
from typing import Set
from fuzzingbook.Coverage import Location
from fuzzingbook.GreyboxFuzzer import getPathID


class RouletteInputSelector:
    exponent = 1
    paths = {}

    def __init__(self, exponent: int):
        """Guarda el exponente"""
        self.exponent = exponent

    def add_new_execution(self, s: str, s_path: Set[Location]):
        """Agrega una nueva ejecución del input s y su path"""
        self.paths[s] = getPathID(s_path)

    def get_frequency(self, s: str) -> int:
        """Retorna la cantidad de apariciones del path_id de s. Retorna 0 si el input no fue ejecutado"""
        if s not in self.paths.keys():
            return 0

        path_id = self.paths[s]
        frequency = 0
        for stored_id in self.paths.values():
            if path_id == stored_id:
                frequency += 1
        return frequency

    def get_energy(self, s: str) -> float:
        """Retorna el valor actual de e(s). Levanta una excepción si el input no fue ejecutado"""
        if s not in self.paths.keys():
            raise Exception("Input has not been executed")

        frequency = self.get_frequency(s)
        return 1 / (frequency ** self.exponent)

    def select(self) -> str:
        """Elije aleatoriamente un s usando seleccion de ruleta sobre e(s)"""
        total_energy = 0
        for s in self.paths.keys():
            total_energy += self.get_energy(s)

        fitness_by_individual = {}
        for s in self.paths.keys():
            f = self.get_energy(s) / total_energy
            fitness_by_individual[s] = f

        # roulette wheel selection
        pick = random.uniform(0, 1)
        current = 0
        for s in self.paths.keys():
            current += fitness_by_individual[s]
            if current > pick:
                return s
