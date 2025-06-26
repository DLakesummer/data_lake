import json
import os

def generate_metadata(submodules_dir, output_file):
    all_metadata = {}
    
    for submodule_name in os.listdir(submodules_dir):
        submodule_path = os.path.join(submodules_dir, submodule_name)
        metadata_path = os.path.join(submodule_path, "metadata.json")

        if os.path.isdir(submodule_path) and os.path.isfile(metadata_path):
            with open(metadata_path, "r") as f:
                try:
                    data = json.load(f)
                    all_metadata[submodule_name] = data
                    print(f"Loaded metadata from: {submodule_name}")
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON in {metadata_path}: {e}")

    # Save to all_metadata.json
    with open(output_file, "w") as f:
        json.dump(all_metadata, f, indent=4)
        print(f"\n Combined metadata saved to {output_file}")

if __name__ == "__main__":
    # Default paths for repo layout: scripts/, datasets/, all_metadata.json
    ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    SUBMODULES_DIR = os.path.join(ROOT_DIR, "datasets")
    OUTPUT_FILE = os.path.join(ROOT_DIR, "all_metadata.json")

    generate_metadata(SUBMODULES_DIR, OUTPUT_FILE)
