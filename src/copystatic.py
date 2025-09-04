import os
import shutil


def copy_directory_recursive(source_dir, destination_dir, root_call = True):
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Source directory not found: {source_dir}")
    if root_call and os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
        print(f"Deleted: {destination_dir}")
    if root_call:
        os.makedirs(destination_dir, exist_ok=True)
        print(f"Created: {destination_dir}")
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        destination_path = os.path.join(destination_dir, item)
        if os.path.isdir(source_path):
            copy_directory_recursive(source_path, destination_path, root_call = False)
        else:
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            shutil.copy2(source_path, destination_path)
            print(f"Copied file: {source_path} to {destination_path}")
    if root_call:
        print(f"Copied: {source_dir} to {destination_dir}")
