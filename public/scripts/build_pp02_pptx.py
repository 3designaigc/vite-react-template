# -*- coding: utf-8 -*-
from pathlib import Path
import shutil
import time

import win32com.client


def rgb(r, g, b):
    return r + (g * 256) + (b * 65536)


OUTPUT_DIR = Path(r"F:\Resilio\AIGC\Projects\0613Paper\website")
PPTX_PATH = OUTPUT_DIR / "PP02_Web3D_auxiliary_fixed.pptx"
PREVIEW_DIR = OUTPUT_DIR / "PP02_Web3D_auxiliary_fixed_preview"

if PREVIEW_DIR.exists():
    shutil.rmtree(PREVIEW_DIR)
PREVIEW_DIR.mkdir(parents=True, exist_ok=True)

slides = [
    {
        "kicker": "PP02 / Web3D Journal Presentation",
        "title": "從 IFC 到互動式 Web3D",
        "subtitle": "結合 AIGC 的建築資訊可視化工作流",
        "points": [
            "主展示版本：PP02_reveal.html",
            "Web3D 第二層入口：HTML\\Journal_Index.html",
            "PPTX 僅作為摘要、截圖與現場備援",
        ],
        "side": "reveal.js 為主\nPPTX 為輔",
    },
    {
        "kicker": "核心主張",
        "title": "靜態 PPT 無法完整承載 BIM/IFC 的空間與時間關係",
        "subtitle": "PP02 的價值在於把期刊成果轉成可操作的 Web3D 展示",
        "points": [
            "Web3D 讓觀眾可旋轉、縮放、播放與檢視模型",
            "類 4D 展示支援施工階段、組裝拆解與前後對照",
            "reveal.js 負責互動敘事，PPTX 負責摘要與交付",
        ],
        "side": "閱讀\n轉為\n操作",
    },
    {
        "kicker": "研究缺口",
        "title": "AI、OpenBIM 與 Web3D 之間仍缺少低門檻整合流程",
        "subtitle": "研究問題來自開發、轉換、展示與施工溝通四個面向",
        "points": [
            "Web3D viewer 開發通常需要前端與 3D 程式能力",
            "IFC 模型需經整備、材質、動畫與 GLB 轉換",
            "IFC viewer 依賴專用軟體；PPT 截圖缺乏互動性",
            "施工階段與類 4D 流程需要可停留、可回看的展示介面",
        ],
        "side": "開發門檻\n模型轉換\n展示溝通",
    },
    {
        "kicker": "工作流程",
        "title": "IFC -> Bonsai/Blender -> GLB -> Web3D",
        "subtitle": "從建築資訊模型到瀏覽器端互動展示",
        "points": [
            "Revit/IFC 作為建築資訊模型來源",
            "Bonsai/Blender 負責模型整備、材質與動畫處理",
            "GLB 作為瀏覽器端展示格式",
            "Google AI Studio 以提示詞迭代 HTML/JavaScript viewer",
            "reveal.js 組合研究敘事與互動 demo",
        ],
        "side": "IFC\nBonsai\nGLB\nWeb3D",
    },
    {
        "kicker": "部署策略",
        "title": "Base64 內嵌與外連 GLB 各有用途",
        "subtitle": "網站化時應優先採用外連 GLB，保留 Base64 作為封存方案",
        "points": [
            "Base64 內嵌：單檔可攜，但 HTML 體積膨脹",
            "外連 GLB：HTML 本體輕量，適合 reveal.js 與網站部署",
            "期刊資料：GLB 14.3 MB 時，Base64 HTML 約 19.1 MB",
            "外連 GLB 架構中，HTML 本體約 19 KB",
        ],
        "side": "19.1 MB\nvs\n19 KB",
    },
    {
        "kicker": "Viewer 路線",
        "title": "Model-Viewer 適合快速展示；three.js 適合類 4D 動態驗證",
        "subtitle": "兩者不是競爭，而是對應不同展示深度",
        "points": [
            "Model-Viewer：輕量嵌入、低開發成本、適合單模型檢視",
            "Three.js：支援 WebGL、HDRI、PBR、時間軸與動畫播放",
            "PP02 的互動展示應以 three.js 作為動態驗證主軸",
        ],
        "side": "Model-\nViewer\n\nThree.js",
    },
    {
        "kicker": "網站層級",
        "title": "PP02_reveal 是第一層，Journal_Index 是第二層",
        "subtitle": "先固定網站資訊架構，後續部署才不會路徑混亂",
        "points": [
            "第一層：website\\PP02_reveal.html，負責簡報敘事與章節導覽",
            "第二層：HTML\\Journal_Index.html，負責 Web3D 展示入口",
            "第三層：HTML\\web\\*.html 與 HTML\\web\\glb\\*.glb，負責 viewer 與模型資產",
        ],
        "side": "Level 1\nLevel 2\nLevel 3",
    },
    {
        "kicker": "結論",
        "title": "PP02 應以 reveal.js 為主，PPTX 為輔",
        "subtitle": "互動學術展示的核心價值在瀏覽器，而不是靜態投影片",
        "points": [
            "IFC -> GLB -> Web3D 的流程可行",
            "AI-assisted programming 能縮短 Web3D 原型開發週期",
            "Web3D 讓期刊成果從閱讀轉為操作",
            "後續可銜接 PP03：MCP + Bonsai BIM 4D 自動化",
        ],
        "side": "Reveal\nfirst",
    },
]


def set_text(shape, text, size, color, bold=False):
    shape.TextFrame2.TextRange.Text = text
    font = shape.TextFrame2.TextRange.Font
    font.Name = "Segoe UI"
    font.NameFarEast = "Microsoft JhengHei"
    font.Size = size
    font.Bold = -1 if bold else 0
    font.Fill.ForeColor.RGB = color


def add_textbox(slide, x, y, w, h, text, size, color, bold=False):
    shape = slide.Shapes.AddTextbox(1, x, y, w, h)
    shape.Fill.Visible = 0
    shape.Line.Visible = 0
    set_text(shape, text, size, color, bold)
    return shape


def add_panel(slide, x, y, w, h, fill, line):
    shape = slide.Shapes.AddShape(1, x, y, w, h)
    shape.Fill.ForeColor.RGB = fill
    shape.Line.ForeColor.RGB = line
    return shape


def main():
    ppt = win32com.client.Dispatch("PowerPoint.Application")
    ppt.Visible = True
    presentation = ppt.Presentations.Add()
    presentation.PageSetup.SlideSize = 13
    presentation.PageSetup.SlideWidth = 960
    presentation.PageSetup.SlideHeight = 540

    blank_layout = 12
    ink = rgb(24, 35, 41)
    muted = rgb(92, 107, 115)
    teal = rgb(11, 113, 128)
    brick = rgb(154, 67, 47)
    line = rgb(215, 223, 223)
    paper = rgb(248, 249, 248)
    panel = rgb(255, 255, 255)
    soft = rgb(237, 243, 243)

    for idx, data in enumerate(slides, start=1):
        slide = presentation.Slides.Add(idx, blank_layout)
        slide.FollowMasterBackground = False
        slide.Background.Fill.ForeColor.RGB = paper

        accent = teal if idx % 2 else brick

        add_textbox(slide, 28, 20, 760, 22, data["kicker"], 11, accent, True)
        add_textbox(slide, 28, 58, 740, 92, data["title"], 31, ink, True)
        add_textbox(slide, 32, 156, 700, 48, data["subtitle"], 16, muted, False)

        add_panel(slide, 36, 244, 700, 248, panel, line)
        body_text = "\r".join(f"- {point}" for point in data["points"])
        body = add_textbox(slide, 60, 266, 650, 204, body_text, 17, muted, False)
        body.TextFrame2.MarginLeft = 0

        side = add_panel(slide, 802, 84, 132, 408, soft, line)
        set_text(side, data["side"], 21, accent, True)
        side.TextFrame2.VerticalAnchor = 3
        side.TextFrame2.TextRange.ParagraphFormat.Alignment = 2

        add_textbox(
            slide,
            32,
            510,
            760,
            18,
            r"F:\Resilio\AIGC\Projects\0613Paper\website\PP02_reveal.html",
            8,
            muted,
            False,
        )

    if PPTX_PATH.exists():
        PPTX_PATH.unlink()
    presentation.SaveAs(str(PPTX_PATH))

    for i in range(1, presentation.Slides.Count + 1):
        png_path = PREVIEW_DIR / f"slide-{i:02d}.png"
        presentation.Slides.Item(i).Export(str(png_path), "PNG", 1280, 720)

    presentation.Close()
    ppt.Quit()
    time.sleep(0.5)

    print(PPTX_PATH)
    print(PPTX_PATH.stat().st_size)
    for png in sorted(PREVIEW_DIR.glob("*.png")):
        print(png.name, png.stat().st_size)


if __name__ == "__main__":
    main()
