import json
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATASETS_DIR = os.path.join(ROOT_DIR, "datasets")
OUTPUT_FILE = os.path.join(ROOT_DIR, "all_metadata.json")

combined_metadata = []

for submodule_name in os.listdir(DATASETS_DIR):
    submodule_path = os.path.join(DATASETS_DIR, submodule_name)
    metadata_path = os.path.join(submodule_path, "metadata.json")

    # Check if it is a directory and metadata.json exists
    if os.path.isdir(submodule_path) and os.path.isfile(metadata_path):
        with open(metadata_path, "r") as f:
            try:
                data = json.load(f)
                # If metadata.json contains a list, extend the combined list
                if isinstance(data, list):
                    combined_metadata.extend(data)
                else:
                    combined_metadata.append(data)
                print(f"Loaded metadata from {submodule_name}")
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in {metadata_path}: {e}")

# Write combined list to output file as JSON array
with open(OUTPUT_FILE, "w") as f:
    json.dump(combined_metadata, f, indent=4)

print(f"\nAll metadata combined into {OUTPUT_FILE}")
