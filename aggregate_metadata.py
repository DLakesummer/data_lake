import json
import os

# Set up paths
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SUBMODULES_DIR = os.path.join(ROOT_DIR, "datasets")
OUTPUT_FILE = os.path.join(ROOT_DIR, "all_metadata.json")

all_metadata = {}

# Read each submodule folder
for submodule_name in os.listdir(SUBMODULES_DIR):
    if submodule_name.startswith("."):
        continue  # Skip hidden/system folders

    submodule_path = os.path.join(SUBMODULES_DIR, submodule_name)
    metadata_path = os.path.join(submodule_path, "metadata.json")

    if os.path.isdir(submodule_path) and os.path.isfile(metadata_path):
        try:
            with open(metadata_path, "r") as f:
                data = json.load(f)
                all_metadata[submodule_name] = data
                print(f"✅ Loaded metadata from: {submodule_name}")
        except Exception as e:
            print(f"⚠️ Could not read {metadata_path}: {e}")

# Save to all_metadata.json using Python dict formatting (not valid JSON)
with open(OUTPUT_FILE, "w") as f:
    f.write("{\n")
    for i, (name, metadata) in enumerate(all_metadata.items()):
        f.write(f"  '{name}': {json.dumps(metadata, indent=2)}")
        if i < len(all_metadata) - 1:
            f.write(",\n")
        else:
            f.write("\n")
    f.write("}\n")

print(f"\n✅ Finished! Output written to {OUTPUT_FILE}")
