# -*- coding: utf-8 -*-
from pathlib import Path
import html
import shutil
import time

import win32com.client


ROOT = Path(r"F:\Resilio\AIGC\Projects\0613Paper")
OUT = ROOT / "website"
REVEAL_DIR = OUT / "reveal.js"


def rgb(r, g, b):
    return r + (g * 256) + (b * 65536)


PP01 = {
    "id": "PP01",
    "file": "PP01_reveal.html",
    "pptx": "PP01_AIGC_BIM_auxiliary.pptx",
    "preview": "PP01_AIGC_BIM_auxiliary_preview",
    "label": "PP01 論文 GPT",
    "title": "生成式人工智慧在建築物入口之設計與施工之研究",
    "subtitle": "以台中雅園會館為例：AIGC、BIM/IFC 與 GRC 工法的開放式整合流程",
    "role": "研究背景與方法論基礎",
    "accent": "#003049",  # Bauhaus Blue
    "slides": [
        {
            "kicker": "PP01 / Research Foundation",
            "title": "AIGC 不只是圖像生成，而是建築流程的開放式協作引擎",
            "lead": "本篇作為三篇簡報的背景與方法論基礎，說明生成式 AI 如何串接 BIM、IFC、Blender/Rhino/Revit 與 GRC 工法。",
            "points": ["研究案例：台中雅園會館入口", "核心路線：AIGC -> BIM/IFC -> GRC 施工", "銜接 PP02：將模型與流程轉成 Web3D 展示"],
            "side": "AIGC\nBIM\nIFC\nGRC",
        },
        {
            "kicker": "Research Context",
            "title": "研究背景：AIGC 進入建築設計流程",
            "lead": "傳統建築流程常把概念生成、模型整合與施工落地切成不同工具與不同階段；AIGC 提供重新串接這些環節的機會。",
            "points": ["生成式 AI 從圖像工具轉為設計協作工具", "入口造型是視覺、結構、材料與施工整合的高複雜場域", "研究需要從概念效果走向可驗證、可施工、可溝通的流程"],
            "side": "傳統流程\nvs\nAIGC 流程",
        },
        {
            "kicker": "Research Questions",
            "title": "研究問題：如何從生成式概念走向可施工構件",
            "lead": "關鍵不只是產生漂亮圖像，而是讓概念能進入 BIM/IFC、材料工法與施工階段。",
            "points": ["建築設計如何從 AIGC 概念轉成可建模資料", "BIM/IFC 如何支援跨軟體整合與資料交換", "GRC 工法如何承接自由曲面與入口構件落地"],
            "side": "設計生成\n模型整合\n施工落地",
        },
        {
            "kicker": "Technology Map",
            "title": "文獻與技術脈絡：AIGC、BIM、IFC 與材料工法",
            "lead": "PP01 建立的是一張技術地圖，讓後續 PP02 的 Web3D 與 PP03 的 MCP/Bonsai 4D 有共同語言。",
            "points": ["AIGC：概念生成、快速迭代與多代理協同", "BIM/IFC：跨軟體模型資料與建築資訊語意", "GRC：材料科技、自由曲面構件與施工落地"],
            "side": "AIGC\n+\nOpenBIM",
        },
        {
            "kicker": "Method",
            "title": "研究方法：開放式 AIGC-BIM-IFC 流程",
            "lead": "研究方法以開放流程取代封閉工具鏈，讓 AI、模型、材料與展示可以在同一條管線上迭代。",
            "points": ["概念生成層：AIGC 與提示詞迭代", "模型整合層：Blender / Rhino / Revit / IFC", "落地驗證層：GRC 製作、施工階段與展示溝通"],
            "side": "OABIF\n開放流程",
        },
        {
            "kicker": "Case",
            "title": "案例執行：台中雅園會館入口",
            "lead": "案例作為研究驗證場域，將入口造型從設計效果、3D 模型、構件邏輯一路推進到材料與施工。",
            "points": ["設計生成：AIGC 影像與概念探索", "模型整合：Blender / Rhino / Revit 的幾何與資料串接", "施工落地：GRC 製作、分件與現場施工階段"],
            "side": "概念\n模型\n構件\n施工",
        },
        {
            "kicker": "Contribution",
            "title": "研究貢獻：補足 AIGC 在建築落地應用中的斷點",
            "lead": "PP01 的重點在於建立從 AI 概念到施工實務的完整論述，並為 PP02/PP03 的 Web3D 與自動化工作流提供基礎。",
            "points": ["補足 AIGC 在建築應用中的學理與實務空白", "建立 AIGC、BIM/IFC 與 GRC 工法整合流程", "為建築產業數位轉型與智慧施工提供案例"],
            "side": "研究\n方法\n案例",
        },
        {
            "kicker": "Bridge",
            "title": "銜接 PP02：從研究流程走向互動式 Web3D 展示",
            "lead": "PP01 建立流程，PP02 將 IFC/GLB 與模型展示變成瀏覽器可操作的學術簡報主體。",
            "points": ["PP01：提出 AIGC + BIM/IFC + GRC 的研究流程", "PP02：把模型與類 4D 敘事轉成 Web3D 展示", "PP03：再把工作流推進到 MCP + Bonsai BIM 4D 自動化"],
            "side": "Next\nPP02",
        },
    ],
}


PP03 = {
    "id": "PP03",
    "file": "PP03_reveal.html",
    "pptx": "PP03_MCP_Bonsai_BIM4D_auxiliary.pptx",
    "preview": "PP03_MCP_Bonsai_BIM4D_auxiliary_preview",
    "label": "PP03 MCP + Bonsai BIM 4D",
    "title": "結合 MCP 之 Blender Bonsai BIM 4D 應用分析",
    "subtitle": "從 Open BIM 4D 排程到 AI Agent 語意驅動工作流",
    "role": "技術延伸與未來工作",
    "accent": "#496f55",  # Adapted slightly, we use this accent for headers
    "slides": [
        {
            "kicker": "PP03 / Technical Extension",
            "title": "Bonsai 4D + MCP：讓 BIM 4D 從手動操作走向語意驅動",
            "lead": "本篇作為 PP02 之後的技術延伸，說明 Blender Bonsai、MCP 與 Skill 如何把 IFC 分析、任務建立、排程與動畫控制封裝成可重複工作流。",
            "points": ["核心工具：Blender Bonsai", "核心協定：Model Context Protocol", "核心目標：降低 BIM 4D 操作門檻並提升流程一致性"],
            "side": "Open BIM\nMCP\nSkill",
            "image": "PP03_analysis/image2.jpeg",
        },
        {
            "kicker": "Problem",
            "title": "研究背景：BIM 4D 的工具斷裂問題",
            "lead": "主流 BIM 商業環境在建模上成熟，但 4D 排程與施工動畫仍常依賴外部工具，造成資料、流程與展示斷裂。",
            "points": ["模型、排程、動畫與展示常分散在不同工具", "BIM 與施工排程的整合成本高", "Open BIM 需要可實驗、可自動化的替代路徑"],
            "side": "模型\n排程\n動畫\n展示",
            "image": "PP03_analysis/image1.png",
        },
        {
            "kicker": "Research Gap",
            "title": "研究缺口：Bonsai 4D 與 MCP 工作流仍缺少系統性論述",
            "lead": "問題不只在 Bonsai 能不能做 4D，而是如何用 MCP 與 Skill 把操作封裝成可被 AI Agent 執行的任務。",
            "points": ["Bonsai 在 4D 面向的完整性與特有性需要整理", "MCP 如何連接 Bonsai 並執行 BIM 4D 操作仍待探索", "Skill 可將重複任務轉成穩定模板"],
            "side": "缺口\n方法\n貢獻",
            "image": "PP03_analysis/image4.png",
        },
        {
            "kicker": "Technology Stack",
            "title": "技術基礎：IFC、Bonsai、MCP 與 Skill",
            "lead": "PP03 的技術結構可視為四層：資料層、工具層、協定層與任務層。",
            "points": ["IFC / buildingSMART：Open BIM 資料基礎", "Blender Bonsai：IFC/BIM 操作與 4D 排程環境", "MCP 與 Skill：工具連接與流程封裝"],
            "side": "Data\nTool\nProtocol\nTask",
            "image": "PP03_analysis/image3.png",
        },
        {
            "kicker": "Workflow",
            "title": "研究工作流：IFC -> Bonsai 4D -> MCP 指令 -> Skill 封裝",
            "lead": "工作流的目標是把 4D 建置拆成可描述、可執行、可驗證的任務序列。",
            "points": ["建立 Work Schedule、Task 與施工動畫", "將模型構件與任務排程關聯", "透過 MCP 與 Skill 封裝 4D 控制流程"],
            "side": "IFC\nSchedule\nMCP\nSkill",
            "image": "PP03_analysis/image7.png",
        },
        {
            "kicker": "Implementation",
            "title": "系統實作：Bonsai 4D 排程與動畫模擬",
            "lead": "Bonsai 不只是 IFC 檢視器，也能在同一環境中建立施工任務、任務條、模型關聯與動畫模擬。",
            "points": ["建立施工任務與時間資訊", "將模型構件與任務關聯", "使用 Animation Tools 與 Task Bars 呈現施工順序"],
            "side": "排程\n關聯\n動畫",
            "image": "PP03_analysis/image6.png",
        },
        {
            "kicker": "Findings",
            "title": "三項發現：Bonsai 4D 具備完整性、特有性與自動化潛力",
            "lead": "實作結果顯示，Bonsai 4D 可作為 Open BIM 研究與展示的可行路徑；MCP/Skill 則讓它具備語意控制與自動化意義。",
            "points": ["Bonsai 具備 BIM 4D 應用的基本功能完整性", "相較商業 BIM 工作流，Bonsai 在 4D 面向展現開源整合優勢", "MCP 與 Skill 讓 Bonsai 4D 具備語意控制與流程封裝潛力"],
            "side": "完整性\n特有性\n自動化",
            "image": "PP03_analysis/image8.jpeg",
        },
        {
            "kicker": "Bridge",
            "title": "銜接網站：PP03 是 PP02 Web3D 之後的自動化延伸",
            "lead": "PP02 展示模型如何進入瀏覽器，PP03 則說明模型、任務與動畫資料如何被更穩定地建立與控制。",
            "points": ["PP02：Web3D 展示與類 4D 互動敘事", "PP03：Bonsai 4D 排程、MCP 指令與 Skill 封裝", "未來：Web 視覺化、Digital Twin、5D 成本與 6D 維運延伸"],
            "side": "Next\nAutomation",
            "image": "PP03_analysis/image5.jpeg",
        },
    ],
}


DECKS = [PP01, PP03]


CSS = """
    :root {
      color-scheme: light;
      --bg: #f4f4f2;
      --paper: #ffffff;
      --ink: #111111;
      --muted: #555555;
      --line: #111111;
      --teal: #003049; /* Bauhaus Blue */
      --brick: #d62828; /* Bauhaus Red */
      --gold: #fcbf49; /* Bauhaus Yellow */
    }
    .reveal {
      font-family: "Noto Sans TC", "Segoe UI", Arial, sans-serif;
      color: var(--ink);
      background-color: var(--bg);
      background-image:
        linear-gradient(rgba(0, 48, 73, 0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 48, 73, 0.04) 1px, transparent 1px);
      background-size: 20px 20px;
    }
    .reveal .slides { text-align: left; }
    .reveal .slides section { box-sizing: border-box; }
    .reveal h1, .reveal h2, .reveal h3 {
      font-family: 'Oswald', 'Noto Sans TC', sans-serif;
      letter-spacing: -0.01em;
      text-transform: uppercase;
      line-height: 1.05;
      color: var(--ink);
      font-weight: 700;
    }
    .reveal h1 { font-size: 2.38em; max-width: 1040px; }
    .reveal h2 { font-size: 1.62em; margin-bottom: 0.42em; }
    .reveal h3 { font-size: 0.82em; color: var(--accent); margin: 0 0 0.45em; text-transform: uppercase; }
    .reveal p, .reveal li { color: var(--muted); font-size: 0.58em; line-height: 1.6; font-weight: 700; }
    .kicker {
      color: var(--brick);
      font-family: 'Oswald', sans-serif;
      font-size: 0.4em;
      font-weight: 700;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      margin-bottom: 1.2em;
    }
    .lead { max-width: 920px; font-size: 0.72em !important; color: #333333 !important; }
    .title-grid {
      display: grid;
      grid-template-columns: minmax(0, 1.15fr) minmax(300px, 0.85fr);
      gap: 34px;
      align-items: center;
    }
    .split {
      display: grid;
      grid-template-columns: minmax(0, 0.95fr) minmax(300px, 1.05fr);
      gap: 28px;
      align-items: center;
    }
    .panel-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; margin-top: 24px; }
    .panel {
      border: 3px solid var(--line);
      background: #fff;
      padding: 20px;
      min-height: 170px;
      box-shadow: 4px 4px 0px #111111;
      border-radius: 0;
    }
    .panel p { font-size: 0.5em; }
    .statement {
      border: 3px solid var(--line);
      border-left: 12px solid var(--accent);
      background: #fff;
      padding: 24px;
      max-width: 1000px;
      box-shadow: 4px 4px 0px #111111;
      border-radius: 0;
    }
    .statement p { font-size: 0.76em !important; color: var(--ink) !important; }
    .side-stage {
      height: 420px;
      border: 3px solid var(--line);
      background:
        linear-gradient(135deg, color-mix(in srgb, var(--accent) 20%, transparent), transparent 45%),
        linear-gradient(315deg, rgba(214, 40, 40, 0.15), transparent 38%),
        #fff;
      display: grid;
      place-items: center;
      padding: 22px;
      text-align: center;
      box-shadow: 6px 6px 0px #111111;
      border-radius: 0;
    }
    .side-stage strong { color: var(--accent); font-family: 'Oswald', sans-serif; font-size: 1.1em; line-height: 1.25; white-space: pre-line; text-transform: uppercase; }
    .flow { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-top: 24px; }
    .flow .step { border: 3px solid var(--line); background: #fff; padding: 16px; min-height: 150px; box-shadow: 4px 4px 0px #111111; border-radius: 0; }
    .flow b { color: var(--accent); font-size: 0.4em; display: block; margin-bottom: 0.5em; font-family: 'Oswald', sans-serif; }
    .flow p { font-size: 0.45em; line-height: 1.45; }
    .media-frame {
      border: 3px solid var(--line);
      background: #fff;
      min-height: 360px;
      display: grid;
      place-items: center;
      overflow: hidden;
      box-shadow: 6px 6px 0px #111111;
      border-radius: 0;
    }
    .media-frame img {
      display: block;
      width: 100%;
      height: 100%;
      max-height: 520px;
      object-fit: contain;
    }
    .caption { color: var(--muted) !important; font-size: 0.38em !important; margin-top: 18px; }
    .navlinks { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 22px; }
    .navlinks a {
      border: 3px solid var(--line);
      background: #fff;
      color: var(--accent);
      text-decoration: none;
      padding: 8px 12px;
      font-size: 0.38em;
      font-weight: 700;
      font-family: 'Oswald', sans-serif;
      box-shadow: 3px 3px 0px #111111;
    }
    .navlinks a:hover {
      transform: translate(-1px, -1px);
      box-shadow: 4px 4px 0px #111111;
      background: var(--gold);
      color: var(--ink);
    }
    @media (max-width: 900px) {
      .title-grid, .split, .panel-grid, .flow { grid-template-columns: 1fr; }
      .side-stage { height: 320px; }
    }
    @media (max-width: 640px) {
      .reveal .slides section { height: 100%; overflow-y: auto; padding: 18px 16px !important; }
      .reveal h1 { font-size: 1.6em; line-height: 1.12; }
      .reveal h2 { font-size: 1.18em; line-height: 1.16; }
      .reveal p, .reveal li { font-size: 0.72em; line-height: 1.48; }
      .kicker { font-size: 0.5em; margin-bottom: 0.8em; }
      .lead { font-size: 0.82em !important; line-height: 1.5 !important; }
      .panel, .statement, .flow .step { padding: 14px; min-height: auto; box-shadow: 2px 2px 0px #111111; }
      .statement { border-left-width: 6px; }
      .statement p { font-size: 0.86em !important; }
      .side-stage { height: 220px; box-shadow: 3px 3px 0px #111111; }
      .side-stage strong { font-size: 0.88em; }
      .flow b { font-size: 0.55em; }
      .flow p, .panel p { font-size: 0.66em; }
      .navlinks a { font-size: 0.55em; box-shadow: 2px 2px 0px #111111; }
    }
"""


def esc(text):
    return html.escape(text, quote=True)


def render_reveal(deck):
    sections = []
    first = deck["slides"][0]
    sections.append(f"""
      <section>
        <div class="title-grid">
          <div>
            <div class="kicker">{esc(first["kicker"])}</div>
            <h1>{esc(deck["title"])}</h1>
            <p class="lead">{esc(deck["subtitle"])}</p>
            <div class="navlinks">
              <a href="index.html">回總入口</a>
              <a href="PP02_reveal.html">PP02 Web3D</a>
            </div>
          </div>
          <div class="side-stage"><strong>{esc(first["side"])}</strong></div>
        </div>
      </section>
""")
    for slide in deck["slides"]:
        points = "".join(f"<div class=\"panel fragment fade-up\"><h3>{esc(p.split('：', 1)[0])}</h3><p>{esc(p)}</p></div>" for p in slide["points"][:3])
        extra = ""
        if len(slide["points"]) > 3:
            extra = "<div class=\"flow\">" + "".join(
                f"<div class=\"step fragment fade-up\"><b>{i:02d}</b><p>{esc(point)}</p></div>"
                for i, point in enumerate(slide["points"], start=1)
            ) + "</div>"
        else:
            extra = f"<div class=\"panel-grid\">{points}</div>"
        
        if "image" in slide:
            sections.append(f"""
      <section data-transition="slide">
        <div class="split">
          <div>
            <div class="kicker">{esc(slide["kicker"])}</div>
            <h2>{esc(slide["title"])}</h2>
            <div class="statement fragment fade-right slow"><p>{esc(slide["lead"])}</p></div>
            {extra}
          </div>
          <div class="media-frame fragment fade-left slow">
            <img src="{esc(slide["image"])}" alt="{esc(slide["title"])}">
          </div>
        </div>
      </section>
""")
        else:
            sections.append(f"""
      <section data-transition="slide">
        <div class="kicker">{esc(slide["kicker"])}</div>
        <h2>{esc(slide["title"])}</h2>
        <div class="statement fragment fade-up slow"><p>{esc(slide["lead"])}</p></div>
        {extra}
      </section>
""")
    html_doc = f"""<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(deck["label"])}</title>
  <link rel="stylesheet" href="reveal.js/dist/reveal.css">
  <link rel="stylesheet" href="reveal.js/dist/theme/white.css">
  <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Noto+Sans+TC:wght@400;700;900&display=swap" rel="stylesheet">
  <style>
    :root {{ --accent: {deck["accent"]}; }}
{CSS}
  </style>
</head>
<body>
  <div class="reveal">
    <div class="slides">
{''.join(sections)}
    </div>
  </div>
  <script src="reveal.js/dist/reveal.js"></script>
  <script>
    const mobileQuery = window.matchMedia("(max-width: 640px)");
    const deckSize = mobileQuery.matches
      ? {{ width: 390, height: 760, margin: 0.02, center: false }}
      : {{ width: 1280, height: 720, margin: 0.05, center: true }};
    Reveal.initialize({{
      hash: true,
      controls: true,
      progress: true,
      center: deckSize.center,
      transition: "slide",
      width: deckSize.width,
      height: deckSize.height,
      margin: deckSize.margin,
      minScale: 0.2,
      maxScale: 1.4
    }});
    mobileQuery.addEventListener("change", () => window.location.reload());
  </script>
</body>
</html>
"""
    (OUT / deck["file"]).write_text(html_doc, encoding="utf-8")


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


def build_pptx(deck):
    pptx_path = OUT / deck["pptx"]
    preview_dir = OUT / deck["preview"]
    if preview_dir.exists():
        shutil.rmtree(preview_dir)
    preview_dir.mkdir(parents=True, exist_ok=True)

    ppt = win32com.client.Dispatch("PowerPoint.Application")
    ppt.Visible = True
    presentation = ppt.Presentations.Add()
    presentation.PageSetup.SlideSize = 13
    presentation.PageSetup.SlideWidth = 960
    presentation.PageSetup.SlideHeight = 540

    ink = rgb(24, 35, 41)
    muted = rgb(92, 107, 115)
    line = rgb(215, 223, 223)
    paper = rgb(248, 249, 248)
    panel = rgb(255, 255, 255)
    soft = rgb(237, 243, 243)
    accent = rgb(11, 113, 128) if deck["id"] == "PP01" else rgb(73, 111, 85)

    for idx, data in enumerate(deck["slides"], start=1):
        slide = presentation.Slides.Add(idx, 12)
        slide.FollowMasterBackground = False
        slide.Background.Fill.ForeColor.RGB = paper
        add_textbox(slide, 28, 20, 760, 22, data["kicker"], 11, accent, True)
        add_textbox(slide, 28, 58, 740, 92, data["title"], 29, ink, True)
        add_textbox(slide, 32, 156, 700, 48, data["lead"], 15, muted, False)
        add_panel(slide, 36, 244, 700, 248, panel, line)
        body_text = "\r".join(f"- {point}" for point in data["points"])
        body = add_textbox(slide, 60, 266, 650, 204, body_text, 16, muted, False)
        body.TextFrame2.MarginLeft = 0
        side = add_panel(slide, 802, 84, 132, 408, soft, line)
        set_text(side, data["side"], 20, accent, True)
        side.TextFrame2.VerticalAnchor = 3
        side.TextFrame2.TextRange.ParagraphFormat.Alignment = 2
        add_textbox(slide, 32, 510, 760, 18, str(OUT / deck["file"]), 8, muted, False)

    if pptx_path.exists():
        pptx_path.unlink()
    presentation.SaveAs(str(pptx_path))
    for i in range(1, presentation.Slides.Count + 1):
        presentation.Slides.Item(i).Export(str(preview_dir / f"slide-{i:02d}.png"), "PNG", 1280, 720)
    presentation.Close()
    ppt.Quit()
    time.sleep(0.3)
    return pptx_path, preview_dir


def render_index():
    # index is now generated dynamically, but the actual index.html in website/ is Bauhaus styled manually to support the advanced layout.
    # We write a basic fallback index page or keep it consistent. We keep render_index simple or aligned with the Bauhaus index.html.
    # To keep things clean, we will let this python script write the same Bauhaus layout if it ever runs render_index!
    pass


def patch_pp02_for_site_root():
    path = OUT / "PP02_reveal.html"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    text = text.replace('src="../HTML/Journal_Index.html"', 'src="HTML/Journal_Index.html"')
    text = text.replace(
        r"F:\Resilio\AIGC\Projects\0613Paper\HTML\Journal_Index.html",
        r"F:\Resilio\AIGC\Projects\0613Paper\website\HTML\Journal_Index.html",
    )
    path.write_text(text, encoding="utf-8")


def main():
    if not REVEAL_DIR.exists():
        raise SystemExit(f"Missing reveal.js assets: {REVEAL_DIR}")
    for deck in DECKS:
        render_reveal(deck)
        pptx, preview = build_pptx(deck)
        print(pptx, pptx.stat().st_size)
        print(preview, len(list(preview.glob("*.png"))))
    patch_pp02_for_site_root()
    print(OUT / "index.html")


if __name__ == "__main__":
    main()
