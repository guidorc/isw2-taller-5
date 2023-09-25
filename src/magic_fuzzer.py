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
    function_name = None
    function = ""

    def __init__(self, initial_inputs, function_to_call, function_name_to_call=None) -> None:
        """Ejecuta inputs iniciales, almacenando la cobertura obtenida"""
        # Reset mappings
        self.covered_locations = []
        self.contributing_inputs = []
        self.locations_per_input = {}
        self.function = function_to_call
        self.function_name = function_name_to_call

        # Execute inputs
        function_runner = FunctionCoverageRunner(function_to_call)
        for current_input in initial_inputs:
            self.run_with_coverage(function_runner, current_input)

    def run_with_coverage(self, runner, input_to_run):
        runner.run(input_to_run)
        locations = runner.coverage()
        for loc in locations:
            if ((loc[0] == self.function_name) or (self.function_name is None)) and (loc not in self.covered_locations):
                self.covered_locations.append(loc)
                if input_to_run not in self.locations_per_input:
                    self.contributing_inputs.append(input_to_run)
                    self.locations_per_input[input_to_run] = [loc]
                else:
                    self.locations_per_input[input_to_run].append(loc)

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
        roulette = RouletteInputSelector(2)
        for s, locations in self.locations_per_input.items():
            s_path = set(locations)
            roulette.add_new_execution(s, s_path)

        selection = roulette.select()
        mutated_selection = self.mutate(selection)
        function_runner = FunctionCoverageRunner(self.function)
        self.run_with_coverage(function_runner, mutated_selection)

    def run_until_covered(self) -> int:
        """
        Corre una campania del MagicFuzzer hasta cubrir todas las lineas del programa.
        Retorna la cantidad de iteraciones realizadas.
        """
        lines_covered = set()
        for loc in self.covered_locations:
            line = loc[1]
            lines_covered.add(line)

        iterations = 0
        while lines_covered != {2, 3, 4, 5, 6}:
            self.fuzz()
            # Update covered lines
            for loc in self.covered_locations:
                line = loc[1]
                lines_covered.add(line)
            iterations += 1

        return lines_covered, iterations

    def run_iterations(self, n=None) -> int:
        """
        Corre una campaña del MagicFuzzer.
        La campaña debe ser ejecutada por n iteraciones (si n no es None), o hasta cubrir todas las líneas del programa.
        Retorna la cantidad de iteraciones realizadas.
        """
        lines_covered = set()
        for loc in self.covered_locations:
            line = loc[1]
            lines_covered.add(line)

        iterations = 0
        while (lines_covered != {2, 3, 4, 5, 6}) and (iterations < n):
            self.fuzz()
            # Update covered lines
            for loc in self.covered_locations:
                line = loc[1]
                lines_covered.add(line)
            iterations += 1

        return lines_covered, iterations
