import json
from typing import List, Dict

def get_file_content(file_path: str) -> str:
    """Lee el contenido de un archivo y lo retorna como texto."""
    with open(file_path, 'r') as file:
        return file.read()

def parse_input(file_content: str) -> (List[List[str]], List[str]):
    """Parsea el contenido del archivo en la sopa de letras y las palabras."""
    lines = file_content.strip().split("\n")
    soup = [list(line.replace(" ", "")) for line in lines if not line.startswith("---")]
    words = lines[len(soup) + 1:]
    return soup, words

def find_word(letter_soup: List[List[str]], word: str) -> bool:
    """Verifica si una palabra está en la sopa de letras."""
    n, m = len(letter_soup), len(letter_soup[0])
    directions = [(0, 1), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1), (0, -1), (-1, 0)]
    
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m
    
    def search(x, y, index):
        if index == len(word):
            return True
        if not is_valid(x, y) or letter_soup[x][y] != word[index]:
            return False
        temp = letter_soup[x][y]
        letter_soup[x][y] = None  # Marca la celda como visitada
        for dx, dy in directions:
            if search(x + dx, y + dy, index + 1):
                return True
        letter_soup[x][y] = temp
        return False

    for i in range(n):
        for j in range(m):
            if letter_soup[i][j] == word[0] and search(i, j, 0):
                return True
    return False

def find_words(letter_soup: List[List[str]], words: List[str]) -> Dict[str, bool]:
    """Retorna un diccionario indicando si las palabras están en la sopa de letras."""
    results = {}
    for word in words:
        results[word] = find_word([row[:] for row in letter_soup], word.upper())
    return results

if __name__ == "__main__":
    # Asegúrate de ingresar la ruta correctamente o usar la ruta relativa si el archivo está en el mismo directorio.
    input_path = input("Ingrese la ruta del archivo de entrada: ").strip("'\"")  # Eliminar comillas si el usuario las pone
    file_content = get_file_content(input_path)
    soup, words = parse_input(file_content)
    results = find_words(soup, words)
    print(results)
