from moviepy import editor
from pathlib import Path
import os

root = r"T:\Films"

folder_suffix = "Baumeister"

childs = [os.path.join(root, n) for n in os.listdir(root) if n.startswith(folder_suffix)]
folders = [ch for ch in childs if os.path.isdir(ch)]

for folder in folders:
    print(f"--------folder: {folder}")

    vfiles = [fn for fn in os.listdir(folder) if fn.endswith(".mp4")]

    for vf in vfiles:
        fname = os.path.splitext(vf)[0]
        print(f"    file: {fname}")

        vpath = os.path.join(folder, vf)
        apath = os.path.join(folder, f"{fname}.mp3")

        if not os.path.exists(apath):
            vclip = editor.VideoFileClip(vpath)
            aclip = vclip.audio
            if aclip:
                aclip.write_audiofile(apath)

                vclip.close()
                aclip.close()
                os.remove(vpath)
