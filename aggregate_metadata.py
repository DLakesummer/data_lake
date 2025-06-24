import json
import os

print("👉 Running associative array version of aggregate_metadata.py")

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATASETS_DIR = os.path.join(ROOT_DIR, "datasets")
OUTPUT_FILE = os.path.join(ROOT_DIR, "data_lake", "all_metadata.json")  # Save inside data_lake folder

all_metadata = {}

for submodule_name in os.listdir(DATASETS_DIR):
    submodule_path = os.path.join(DATASETS_DIR, submodule_name)
    metadata_path = os.path.join(submodule_path, "metadata.json")

    if os.path.isdir(submodule_path) and os.path.isfile(metadata_path):
        try:
            with open(metadata_path, "r") as f:
                data = json.load(f)

                # If metadata is a list with one item, unwrap it
                if isinstance(data, list) and len(data) == 1:
                    data = data[0]

                all_metadata[submodule_name] = data
                print(f"✅ Loaded metadata from: {submodule_name}")
        except json.JSONDecodeError as e:
            print(f"⚠️ JSON decode error in {metadata_path}: {e}")

with open(OUTPUT_FILE, "w") as f:
    json.dump(all_metadata, f, indent=4)

print(f"\n✅ Combined metadata saved to {OUTPUT_FILE}")
