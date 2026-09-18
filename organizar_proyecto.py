"""
Script de organización del proyecto forecasting-trm
Corre esto UNA VEZ desde la carpeta donde tienes los notebooks.
Mueve los archivos a la estructura correcta para GitHub.
"""

import os
import shutil
from pathlib import Path

# ── Estructura objetivo ──────────────────────────────────────────────
# forecasting-trm/
# ├── README.md
# ├── .gitignore
# ├── requirements.txt
# ├── forecasting_trm_fase1.ipynb
# ├── forecasting_trm_fase2.ipynb
# ├── forecasting_trm_fase3.ipynb
# └── outputs/
#     └── (todos los .png que generaron los notebooks)

def organizar():
    carpeta_base = Path(".")
    carpeta_outputs = carpeta_base / "outputs"
    carpeta_outputs.mkdir(exist_ok=True)

    # Mover todos los .png a outputs/
    pngs = list(carpeta_base.glob("*.png"))
    if pngs:
        print(f"📁 Moviendo {len(pngs)} gráficas a outputs/...")
        for png in pngs:
            destino = carpeta_outputs / png.name
            shutil.move(str(png), str(destino))
            print(f"   ✅ {png.name}")
    else:
        print("ℹ️  No se encontraron .png en la carpeta actual (pueden ya estar en outputs/)")

    # Mover CSVs de datos a outputs/ también
    csvs = list(carpeta_base.glob("*.csv"))
    if csvs:
        print(f"\n📁 Moviendo {len(csvs)} archivos CSV a outputs/...")
        for csv in csvs:
            destino = carpeta_outputs / csv.name
            shutil.move(str(csv), str(destino))
            print(f"   ✅ {csv.name}")

    print("\n✅ Estructura lista para GitHub")
    print("\n📋 Archivos en la raíz del proyecto:")
    for f in sorted(carpeta_base.iterdir()):
        if f.is_file() and f.suffix in ['.ipynb', '.md', '.txt', '.py', '']:
            print(f"   {f.name}")
    print("\n📋 Archivos en outputs/:")
    for f in sorted(carpeta_outputs.iterdir()):
        print(f"   outputs/{f.name}")

if __name__ == "__main__":
    organizar()
