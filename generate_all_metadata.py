import json
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SUBMODULES_DIR = os.path.join(ROOT_DIR, "datasets")
OUTPUT_FILE = os.path.join(ROOT_DIR, "all_metadata.json")

all_metadata = {}

for submodule_name in os.listdir(SUBMODULES_DIR):
    if submodule_name.startswith("."):
        continue  # Skip hidden/system folders

    submodule_path = os.path.join(SUBMODULES_DIR, submodule_name)
    metadata_path = os.path.join(submodule_path, "metadata.json")

    if os.path.isdir(submodule_path) and os.path.isfile(metadata_path):
        with open(metadata_path, "r") as f:
            try:
                data = json.load(f)
                all_metadata[submodule_name] = data
                print(f"✅ Loaded metadata from: {submodule_name}")
            except json.JSONDecodeError as e:
                print(f"⚠️ Invalid JSON in {metadata_path}: {e}")
            except Exception as e:
                print(f"⚠️ Error reading {metadata_path}: {e}")

with open(OUTPUT_FILE, "w") as f:
    json.dump(all_metadata, f, indent=4)
    print(f"\n✅ Combined metadata written to {OUTPUT_FILE}")
