from typing import List, Set
from fuzzingbook.Coverage import Location
from fuzzingbook.MutationFuzzer import FunctionCoverageRunner


class MagicFuzzer:
    covered_locations = []
    contributing_inputs = []


    def __init__(self, initial_inputs, function_to_call, function_name_to_call = None) -> None:
        """Ejecuta inputs iniciales, almacenando la cobertura obtenida"""
        # Reset mappings
        self.covered_locations = []
        self.contributing_inputs = []

        # Execute inputs
        function_runner = FunctionCoverageRunner(function_to_call)
        for input in initial_inputs:
            function_runner.run(input)
            locations = function_runner.coverage()
            for loc in locations:
                if (loc[0] == function_name_to_call) and (loc not in self.covered_locations):
                    self.covered_locations.append(loc)
                    if input not in self.contributing_inputs:
                        self.contributing_inputs.append(input)

    def get_contributing_inputs(self) -> List[str]:
        """Retorna la lista de los inputs que aumentaron la cobertura en el orden que fueron ejecutados"""
        return self.contributing_inputs

    def get_covered_locations(self) -> Set[Location]:
        """Retorna el conjunto de locaciones cubiertas de todas las ejecuciones"""
        return set(self.covered_locations)


    def mutate(self, s: str) -> str:
        """Aplica al azar alguna de las tres operaciones de mutacion definidas en el archivo mutation_utils.py"""
        pass

    def fuzz(self):
        """
        Elije aleatoriamente un input s usando seleccion de ruleta sobre e(s),
        muta el input s utilizando la función mutate(s), y ejecuta el s mutado
        """
        pass

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