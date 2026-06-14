$ErrorActionPreference = "Stop"

function RgbInt([int]$r, [int]$g, [int]$b) {
    return ($r + ($g * 256) + ($b * 65536))
}

$outputDir = "F:\Resilio\AIGC\Projects\0613Paper\website"
$pptxPath = Join-Path $outputDir "PP02_Web3D_auxiliary_fixed.pptx"
$previewDir = Join-Path $outputDir "PP02_Web3D_auxiliary_fixed_preview"

if (-not (Test-Path -LiteralPath $previewDir)) {
    New-Item -ItemType Directory -Path $previewDir | Out-Null
}

$slides = @(
    @{
        Kicker = "PP02 / Web3D Journal Presentation"
        Title = "從 IFC 到互動式 Web3D"
        Subtitle = "結合 AIGC 的建築資訊可視化工作流"
        Points = @(
            "主展示版本：PP02_reveal.html",
            "Web3D 第二層入口：HTML\Journal_Index.html",
            "PPTX 僅作為摘要、截圖與現場備援"
        )
        Side = "reveal.js 為主`nPPTX 為輔"
    },
    @{
        Kicker = "核心主張"
        Title = "靜態 PPT 無法完整承載 BIM/IFC 的空間與時間關係"
        Subtitle = "PP02 的價值在於把期刊成果轉成可操作的 Web3D 展示"
        Points = @(
            "Web3D 讓觀眾可旋轉、縮放、播放與檢視模型",
            "類 4D 展示支援施工階段、組裝拆解與前後對照",
            "reveal.js 負責互動敘事，PPTX 負責摘要與交付"
        )
        Side = "閱讀 -> 操作"
    },
    @{
        Kicker = "研究缺口"
        Title = "AI、OpenBIM 與 Web3D 之間仍缺少低門檻整合流程"
        Subtitle = "研究問題來自開發、轉換、展示與施工溝通四個面向"
        Points = @(
            "Web3D viewer 開發通常需要前端與 3D 程式能力",
            "IFC 模型需經整備、材質、動畫與 GLB 轉換",
            "IFC viewer 依賴專用軟體；PPT 截圖缺乏互動性",
            "施工階段與類 4D 流程需要可停留、可回看的展示介面"
        )
        Side = "開發門檻`n模型轉換`n展示溝通"
    },
    @{
        Kicker = "工作流程"
        Title = "IFC -> Bonsai/Blender -> GLB -> Web3D"
        Subtitle = "從建築資訊模型到瀏覽器端互動展示"
        Points = @(
            "Revit/IFC 作為建築資訊模型來源",
            "Bonsai/Blender 負責模型整備、材質與動畫處理",
            "GLB 作為瀏覽器端展示格式",
            "Google AI Studio 以提示詞迭代 HTML/JavaScript viewer",
            "reveal.js 組合研究敘事與互動 demo"
        )
        Side = "IFC`nBonsai`nGLB`nWeb3D"
    },
    @{
        Kicker = "部署策略"
        Title = "Base64 內嵌與外連 GLB 各有用途"
        Subtitle = "網站化時應優先採用外連 GLB，保留 Base64 作為封存方案"
        Points = @(
            "Base64 內嵌：單檔可攜，但 HTML 體積膨脹",
            "外連 GLB：HTML 本體輕量，適合 reveal.js 與網站部署",
            "期刊資料：GLB 14.3 MB 時，Base64 HTML 約 19.1 MB",
            "外連 GLB 架構中，HTML 本體約 19 KB"
        )
        Side = "19.1 MB`nvs`n19 KB"
    },
    @{
        Kicker = "Viewer 路線"
        Title = "Model-Viewer 適合快速展示；three.js 適合類 4D 動態驗證"
        Subtitle = "兩者不是競爭，而是對應不同展示深度"
        Points = @(
            "Model-Viewer：輕量嵌入、低開發成本、適合單模型檢視",
            "Three.js：支援 WebGL、HDRI、PBR、時間軸與動畫播放",
            "PP02 的互動展示應以 three.js 作為動態驗證主軸"
        )
        Side = "Model-Viewer`nThree.js"
    },
    @{
        Kicker = "網站層級"
        Title = "PP02_reveal 是第一層，Journal_Index 是第二層"
        Subtitle = "先固定網站資訊架構，後續部署才不會路徑混亂"
        Points = @(
            "第一層：website\PP02_reveal.html，負責簡報敘事與章節導覽",
            "第二層：HTML\Journal_Index.html，負責 Web3D 展示入口",
            "第三層：HTML\web\*.html 與 HTML\web\glb\*.glb，負責 viewer 與模型資產"
        )
        Side = "Level 1`nLevel 2`nLevel 3"
    },
    @{
        Kicker = "結論"
        Title = "PP02 應以 reveal.js 為主，PPTX 為輔"
        Subtitle = "互動學術展示的核心價值在瀏覽器，而不是靜態投影片"
        Points = @(
            "IFC -> GLB -> Web3D 的流程可行",
            "AI-assisted programming 能縮短 Web3D 原型開發週期",
            "Web3D 讓期刊成果從閱讀轉為操作",
            "後續可銜接 PP03：MCP + Bonsai BIM 4D 自動化"
        )
        Side = "Reveal first"
    }
)

$ppt = New-Object -ComObject PowerPoint.Application
$ppt.Visible = [Microsoft.Office.Core.MsoTriState]::msoTrue
$presentation = $ppt.Presentations.Add()
$presentation.PageSetup.SlideSize = 13
$presentation.PageSetup.SlideWidth = 13.333
$presentation.PageSetup.SlideHeight = 7.5

$blankLayout = 12
$msoTextOrientationHorizontal = 1
$msoShapeRectangle = 1

$ink = RgbInt 24 35 41
$muted = RgbInt 92 107 115
$teal = RgbInt 11 113 128
$brick = RgbInt 154 67 47
$line = RgbInt 215 223 223
$paper = RgbInt 248 249 248
$panel = RgbInt 255 255 255
$soft = RgbInt 237 243 243

for ($i = 0; $i -lt $slides.Count; $i++) {
    $data = $slides[$i]
    $slide = $presentation.Slides.Add($i + 1, $blankLayout)
    $slide.FollowMasterBackground = $false
    $slide.Background.Fill.ForeColor.RGB = $paper

    $accent = if (($i % 2) -eq 0) { $teal } else { $brick }

    $kicker = $slide.Shapes.AddTextbox($msoTextOrientationHorizontal, 28, 22, 720, 24)
    $kicker.TextFrame2.TextRange.Text = $data.Kicker
    $kicker.TextFrame2.TextRange.Font.NameFarEast = "Microsoft JhengHei"
    $kicker.TextFrame2.TextRange.Font.Name = "Segoe UI"
    $kicker.TextFrame2.TextRange.Font.Size = 12
    $kicker.TextFrame2.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $kicker.TextFrame2.TextRange.Font.Fill.ForeColor.RGB = $accent
    $kicker.Line.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse
    $kicker.Fill.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse

    $title = $slide.Shapes.AddTextbox($msoTextOrientationHorizontal, 28, 60, 730, 96)
    $title.TextFrame2.TextRange.Text = $data.Title
    $title.TextFrame2.TextRange.Font.NameFarEast = "Microsoft JhengHei"
    $title.TextFrame2.TextRange.Font.Name = "Segoe UI"
    $title.TextFrame2.TextRange.Font.Size = 34
    $title.TextFrame2.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $title.TextFrame2.TextRange.Font.Fill.ForeColor.RGB = $ink
    $title.Line.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse
    $title.Fill.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse

    $subtitle = $slide.Shapes.AddTextbox($msoTextOrientationHorizontal, 32, 160, 700, 54)
    $subtitle.TextFrame2.TextRange.Text = $data.Subtitle
    $subtitle.TextFrame2.TextRange.Font.NameFarEast = "Microsoft JhengHei"
    $subtitle.TextFrame2.TextRange.Font.Name = "Segoe UI"
    $subtitle.TextFrame2.TextRange.Font.Size = 17
    $subtitle.TextFrame2.TextRange.Font.Fill.ForeColor.RGB = $muted
    $subtitle.Line.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse
    $subtitle.Fill.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse

    $bodyBox = $slide.Shapes.AddShape($msoShapeRectangle, 36, 250, 700, 270)
    $bodyBox.Fill.ForeColor.RGB = $panel
    $bodyBox.Line.ForeColor.RGB = $line

    $body = $slide.Shapes.AddTextbox($msoTextOrientationHorizontal, 62, 276, 645, 220)
    $body.TextFrame2.TextRange.Text = (($data.Points | ForEach-Object { "- $_" }) -join "`r")
    $body.TextFrame2.TextRange.Font.NameFarEast = "Microsoft JhengHei"
    $body.TextFrame2.TextRange.Font.Name = "Segoe UI"
    $body.TextFrame2.TextRange.Font.Size = 18
    $body.TextFrame2.TextRange.Font.Fill.ForeColor.RGB = $muted
    $body.TextFrame2.MarginLeft = 0
    $body.Line.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse
    $body.Fill.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse

    $side = $slide.Shapes.AddShape($msoShapeRectangle, 805, 84, 170, 418)
    $side.Fill.ForeColor.RGB = $soft
    $side.Line.ForeColor.RGB = $line
    $side.TextFrame2.TextRange.Text = $data.Side
    $side.TextFrame2.TextRange.Font.NameFarEast = "Microsoft JhengHei"
    $side.TextFrame2.TextRange.Font.Name = "Segoe UI"
    $side.TextFrame2.TextRange.Font.Size = 22
    $side.TextFrame2.TextRange.Font.Bold = [Microsoft.Office.Core.MsoTriState]::msoTrue
    $side.TextFrame2.TextRange.Font.Fill.ForeColor.RGB = $accent
    $side.TextFrame2.VerticalAnchor = 3
    $side.TextFrame2.TextRange.ParagraphFormat.Alignment = 2

    $footer = $slide.Shapes.AddTextbox($msoTextOrientationHorizontal, 32, 532, 720, 24)
    $footer.TextFrame2.TextRange.Text = "F:\Resilio\AIGC\Projects\0613Paper\website\PP02_reveal.html"
    $footer.TextFrame2.TextRange.Font.Name = "Segoe UI"
    $footer.TextFrame2.TextRange.Font.Size = 9
    $footer.TextFrame2.TextRange.Font.Fill.ForeColor.RGB = $muted
    $footer.Line.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse
    $footer.Fill.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse
}

$presentation.SaveAs($pptxPath)

for ($i = 1; $i -le $presentation.Slides.Count; $i++) {
    $pngPath = Join-Path $previewDir ("slide-{0:D2}.png" -f $i)
    $presentation.Slides.Item($i).Export($pngPath, "PNG", 1280, 720)
}

$presentation.Close()
$ppt.Quit()

[System.Runtime.InteropServices.Marshal]::ReleaseComObject($presentation) | Out-Null
[System.Runtime.InteropServices.Marshal]::ReleaseComObject($ppt) | Out-Null

Get-Item -LiteralPath $pptxPath
Get-ChildItem -LiteralPath $previewDir -Filter "*.png" | Select-Object Name, Length, LastWriteTime
