from .listingManagement import *


# Utility function to save files and return their paths
def save_files(files: List[UploadFile], directory: str) -> List[str]:
    os.makedirs(directory, exist_ok=True)
    paths = []
    for file in files:
        file_path = os.path.join(directory, file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        paths.append(file_path)
    return paths
