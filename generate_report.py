import json
from sopa_de_letras import get_file_content, parse_input, find_words

def generate_report(input_path: str, output_path: str) -> None:
    """Genera un reporte en formato JSON con las palabras encontradas y no encontradas."""
    file_content = get_file_content(input_path)
    soup, words = parse_input(file_content)
    results = find_words(soup, words)
    with open(output_path, 'w') as file:
        json.dump(results, file, indent=4)
    print(f"Reporte generado en: {output_path}")

if __name__ == "__main__":
    input_path = input("Ingrese la ruta del archivo de entrada: ")
    output_path = "reporte.json"
    generate_report(input_path, output_path)
