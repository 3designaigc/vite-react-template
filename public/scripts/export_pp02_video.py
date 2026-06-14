# -*- coding: utf-8 -*-
from pathlib import Path
import time

import win32com.client


ROOT = Path(r"F:\Resilio\AIGC\Projects\0613Paper\website")
PPTX = ROOT / "PP02_Web3D.pptx"
MP4 = ROOT / "PP02_Web3D_original_animation.mp4"


def main():
    if MP4.exists():
        MP4.unlink()

    ppt = win32com.client.Dispatch("PowerPoint.Application")
    ppt.Visible = True
    presentation = ppt.Presentations.Open(str(PPTX), WithWindow=False)

    # UseTimingsAndNarrations=True preserves existing transition/animation timings where present.
    presentation.CreateVideo(str(MP4), True, 4, 1080, 30, 85)

    # ppMediaTaskStatusDone = 3, ppMediaTaskStatusFailed = 4
    for _ in range(300):
        status = presentation.CreateVideoStatus
        if status == 3:
            break
        if status == 4:
            raise RuntimeError("PowerPoint video export failed")
        time.sleep(1)
    else:
        raise TimeoutError("PowerPoint video export timed out")

    presentation.Close()
    ppt.Quit()

    print(MP4)
    print(MP4.stat().st_size)


if __name__ == "__main__":
    main()
