import json
from pathlib import Path

from neat_html import h, render
from neat_html.types import Element


"""
Example:
  {
    "name": "Bulbasaur",
    "type": ["Grass", "Poison"],
    "total": 318,
    "hp": 45,
    "attack": 49
  }
"""
pokemon_data = json.loads(Path("examples/pokemon.json").read_text())


def neat_html() -> str:
    headings = ["Name", "Type", "Total", "HP", "Attack"]
    columns = ["name", "type", "total", "hp", "attack"]

    thead = h("thead", h("tr", [h("th", heading) for heading in headings]))

    rows = []
    for pokemon in pokemon_data:
        rows.append(h("tr", [h("td", str(pokemon[key])) for key in columns]))

    tbody = h("tbody", rows)
    table = h("table", [thead, tbody])

    return render(table)
