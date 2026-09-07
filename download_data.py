import kagglehub

# Download latest version
path = kagglehub.dataset_download("hansespinosa2/40000-video-game-midi-files")

print("Path to dataset files:", path)