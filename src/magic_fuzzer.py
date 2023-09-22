import random
from typing import List, Set
from fuzzingbook.Coverage import Location
from fuzzingbook.MutationFuzzer import FunctionCoverageRunner

from mutation_utils import insert_random_character, delete_random_character, change_random_character
from roulette_input_selector import RouletteInputSelector

INSERT = 0
DELETE = 1
CHANGE = 2


class MagicFuzzer:
    covered_locations = []
    locations_per_input = {}
    contributing_inputs = []

    def __init__(self, initial_inputs, function_to_call, function_name_to_call = None) -> None:
        """Ejecuta inputs iniciales, almacenando la cobertura obtenida"""
        # Reset mappings
        self.covered_locations = []
        self.contributing_inputs = []
        self.locations_per_input = {}

        # Execute inputs
        function_runner = FunctionCoverageRunner(function_to_call)
        for current_input in initial_inputs:
            function_runner.run(current_input)
            locations = function_runner.coverage()
            for loc in locations:
                if (loc[0] == function_name_to_call) and (loc not in self.covered_locations):
                    self.covered_locations.append(loc)
                    if input not in self.locations_per_input:
                        self.contributing_inputs.append(input)
                        self.locations_per_input[input] = [loc]
                    else:
                        self.locations_per_input[input].append(loc)

    def get_contributing_inputs(self) -> List[str]:
        """Retorna la lista de los inputs que aumentaron la cobertura en el orden que fueron ejecutados"""
        return self.contributing_inputs

    def get_covered_locations(self) -> Set[Location]:
        """Retorna el conjunto de locaciones cubiertas de todas las ejecuciones"""
        return set(self.covered_locations)

    def mutate(self, s: str) -> str:
        """Aplica al azar alguna de las tres operaciones de mutacion definidas en el archivo mutation_utils.py"""
        choice = random.randint(0, 2)
        if choice == INSERT:
            return insert_random_character(s)
        if choice == DELETE:
            return delete_random_character(s)
        if choice == CHANGE:
            return change_random_character(s)

    def fuzz(self):
        """
        Elije aleatoriamente un input s usando seleccion de ruleta sobre e(s),
        muta el input s utilizando la función mutate(s), y ejecuta el s mutado
        """
        roulette = RouletteInputSelector()
        for s, locations in self.locations_per_input.items():
            s_path = set(locations)
            roulette.add_new_execution(s, s_path)

        selection = roulette.select()
        mutated_selection = self.mutate(selection)

    def run_until_covered(self, n = None) -> int:
        """
        Corre una campania del MagicFuzzer hasta cubrir todas las lineas del programa.
        Retorna la cantidad de iteraciones realizadas.
        """
        pass

    def run(self, n = None) -> int:
        """
        Corre una campaña del MagicFuzzer.
        La campaña debe ser ejecutada por n iteraciones (si n no es None), o hasta cubrir todas las líneas del programa.
        Retorna la cantidad de iteraciones realizadas.
        """
        pass