import os
for root, dirs, files in os.walk("materials"):
    for file in files:
        if file.endswith(".vmt"):
            with open(os.path.join(root, file)) as f:
                if 'ModelGlowColor' not in f.read():
                    f.close()
                    os.remove(os.path.join(root, file))