# -*- coding: utf-8 -*-
from pathlib import Path
import shutil
import time

import win32com.client


ROOT = Path(r"F:\Resilio\AIGC\Projects\0613Paper\website")
PPTX = ROOT / "PP02_Web3D.pptx"
OUT = ROOT / "PP02_Web3D_exact_slides"


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True, exist_ok=True)

    ppt = win32com.client.Dispatch("PowerPoint.Application")
    ppt.Visible = True
    presentation = ppt.Presentations.Open(str(PPTX), WithWindow=False)

    for i in range(1, presentation.Slides.Count + 1):
        # 1920x1080 keeps a clean 16:9 comparison image while remaining web-friendly.
        presentation.Slides.Item(i).Export(str(OUT / f"slide-{i:02d}.png"), "PNG", 1920, 1080)

    presentation.Close()
    ppt.Quit()
    time.sleep(0.5)

    print(OUT)
    for png in sorted(OUT.glob("*.png")):
        print(png.name, png.stat().st_size)


if __name__ == "__main__":
    main()
