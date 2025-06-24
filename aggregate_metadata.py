import json
import os

# Set up paths
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATASETS_DIR = os.path.join(ROOT_DIR, "datasets")
OUTPUT_FILE = os.path.join(ROOT_DIR, "all_metadata.json")

# This will store metadata per submodule name
all_metadata = {}

# Loop through each folder inside datasets/
for submodule_name in os.listdir(DATASETS_DIR):
    submodule_path = os.path.join(DATASETS_DIR, submodule_name)
    metadata_path = os.path.join(submodule_path, "metadata.json")

    # Skip if not a directory or metadata.json not found
    if os.path.isdir(submodule_path) and os.path.isfile(metadata_path):
        try:
            with open(metadata_path, "r") as f:
                metadata = json.load(f)

                # If the metadata is a list (wrapped), just grab the first item
                if isinstance(metadata, list) and len(metadata) == 1:
                    metadata = metadata[0]

                all_metadata[submodule_name] = metadata
                print(f"✅ Loaded metadata from: {submodule_name}")

        except json.JSONDecodeError as e:
            print(f"⚠️ Error reading {metadata_path}: {e}")

# Dump the dictionary (not a list!) to all_metadata.json
with open(OUTPUT_FILE, "w") as f:
    json.dump(all_metadata, f, indent=4)

print(f"\n✅ Combined metadata saved to {OUTPUT_FILE}")
