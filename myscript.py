import os

# Indique les commits (le bon et le mauvais)
good_hash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"
bad_hash = "c1a4be04b972b6c17db242fc37752ad517c29402"

# Démarre la recherche bisect
os.system(f"git bisect start {bad_hash} {good_hash}")

# Exécute automatiquement les tests à chaque commit intermédiaire
# Remplace `pytest` par ta commande de test réelle (ex: `python -m unittest`, `./test.sh`, etc.)
os.system("git bisect run pytest")

# Réinitialise git bisect à la fin
os.system("git bisect reset")
