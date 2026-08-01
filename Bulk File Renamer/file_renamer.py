import os

folder = "Bulk File Renamer/test_files"
prefix = "test_"

if not os.path.exists(folder):
    print("folder not found. Try again.")

try:
    files = os.listdir(folder)
    print(f"folder has : {files}")
except PermissionError:
    print("error: permission denied")

for file_name in files:
    if file_name.endswith("txt"):
        new_name = prefix + file_name

    old_path = os.path.join(folder , file_name)
    new_path = os.path.join(folder ,new_name)
    try:
        os.rename(old_path, new_path)
        print(f"✅ Renamed: {file_name} -> {new_name}")
    except FileExistsError:
        print(f"⚠️ Warning: '{new_name}' already exists. Skipping...")
    except PermissionError:
        print(f"❌ Error: Permission denied to rename '{file_name}'")
    except Exception as e:
        print(f"❌ Unexpected error renaming '{file_name}': {e}")
else:
    print(f"⏭️ Skipped: {file_name} (Not a .txt file)")
