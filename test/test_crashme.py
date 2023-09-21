from fuzzingbook.MutationFuzzer import FunctionCoverageRunner
from src.crashme import crashme
from src.get_source_lines import get_source_lines

if __name__ == "__main__":
    input = "good"
    crashme_runner = FunctionCoverageRunner(crashme)

    lineas = get_source_lines(crashme)
    print(f"El programa a correr tiene {lineas} lineas.")

    result, outcome = crashme_runner.run(input)
    print(f"El resultado de ejecutar crashme con el input {input} fue {result}")
    print(f"El outcome del Runner fue {outcome}")

    locations = crashme_runner.coverage()
    print(f"Las locations cubiertas durante la ejecución fueron:")
    for loc in locations:
        print(f" -> Función \"{loc[0]}\": línea {loc[1]}")