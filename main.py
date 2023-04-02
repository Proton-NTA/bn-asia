from os import getcwd
from glob import glob
from sys import argv
from re import findall
from pgmpy.readwrite import BIFReader
from pgmpy.inference import VariableElimination


def get_evidence(i: str, states: dict[list]) -> dict | None:
    if not i.strip():
        return None
    evidence = {}
    matches = findall(r"(\w+)\s*=\s*(\w+)", i)
    if not matches:
        print("Fehler: Eingabeformat nicht erkannt")
    for match in matches:
        try:
            evidence_states: list = states[match[0]]
        except KeyError:
            print("Fehler: " + match[0] + " ist nicht Teil des Netzwerks")
            return {}
        if match[1] not in evidence_states:
            print("Fehler: Für " + match[0] + " sind folgende Werte definiert " + evidence_states.__str__() + " nicht "
                  + match[1])
            return {}
        evidence[match[0]] = match[1]
    return evidence


if __name__ == '__main__':
    file = "asia.bif"
    if len(argv) > 1:
        file = argv[1]
        if len(glob(file)) == 0:
            print("Fehler: Datei " + file + " existiert nicht im Ordner " + getcwd())
            exit(1)
    print("Datei wird eingelesen...")
    reader = BIFReader(file)
    print("Folgende Variablen sind im Netzwerk vorhanden: " + ", ".join(reader.get_variables()))
    while True:
        variablesIn = input("Für welche Variablen soll eine Verteilung berechnet werden?\n")
        variables = findall(r"(\w+)", variablesIn)
        wrong_variables = set(variables) - set(reader.get_variables())
        if len(wrong_variables) != 0:
            print("Fehler: " + wrong_variables.__str__() + " nicht Teil von " + reader.get_variables().__str__())
        else:
            break
    evidence = {}
    while evidence == {}:
        evidenceIn = input("Welche optionale Evidenz soll beachtet werden? "
                           "(Liste aus [key]=[value] Paaren oder Leer)\n")
        evidence = get_evidence(evidenceIn, reader.get_states())
    print("Verteilung wird berechnet...")
    model = reader.get_model()
    infer = VariableElimination(model)
    if model.check_model():
        print(infer.query(variables, evidence))
    else:
        print("Fehler: Eingeladenes Modell ist fehlerhaft")
