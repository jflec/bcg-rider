import json

def sort_pokemon(input_file: str, output_file: str):
    with open(input_file, "r") as f:
        data = json.load(f)

    sorted_pokemon = dict(sorted(data["pokemonTypes"].items()))

    data["pokemonTypes"] = sorted_pokemon

    with open(output_file, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Sorted data saved to {output_file}")

if __name__ == "__main__":
    sort_pokemon("pokemonRideConfig.json", "sortedPokemonRideConfig.json")
