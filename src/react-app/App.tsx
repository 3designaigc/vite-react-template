import { useRef, useState } from "react";
import "./App.css";

type Entry = {
	id: string;
	title: string;
	src: string;
	download?: string;
};

const entries = {
	homeA: {
		id: "home-a",
		title: "AIGC.4DBIM 3D 動畫",
		src: "/bauhaus_animation - A.html",
	},
	homeB: {
		id: "home-b",
		title: "AIGC.4DBIM 3D 動畫",
		src: "/bauhaus_animation - B.html",
	},
	pp01: {
		id: "pp01",
		title: "PP01 論文 GPT",
		src: "/presentations/PP01_reveal.html",
	},
	pp01Pdf: {
		id: "pp01-pdf",
		title: "PP01 PDF 文件",
		src: "/HTML/PDF/PP01_論文_GPT.pdf",
		download: "/HTML/PDF/PP01_論文_GPT.pdf",
	},
	pp02: {
		id: "pp02",
		title: "PP02 期刊 Web3D",
		src: "/presentations/PP02_reveal.html",
	},
	pp02Exact: {
		id: "pp02-exact",
		title: "PP02 PPTX 視覺復刻",
		src: "/presentations/PP02_Web3D_pptx_exact_reveal.html",
	},
	pp02Animation: {
		id: "pp02-animation",
		title: "PP02 原始 PPT 動畫",
		src: "/presentations/PP02_Web3D_original_animation.html",
	},
	pp02Pdf: {
		id: "pp02-pdf",
		title: "PP02 PDF 文件",
		src: "/HTML/PDF/PP02_期刊.pdf",
		download: "/HTML/PDF/PP02_期刊.pdf",
	},
	pp03: {
		id: "pp03",
		title: "PP03 MCP + Bonsai BIM 4D",
		src: "/presentations/PP03_reveal.html",
	},
	poster: {
		id: "poster",
		title: "PP03 研討會海報",
		src: "/HTML/PDF/PP03_海報.pdf",
		download: "/HTML/PDF/PP03_海報.pdf",
	},
	blender: {
		id: "blender",
		title: "2026 BlenderBIM 簡報",
		src: "/presentations/2026_BlenderBIM.html",
	},
	pp03Pdf: {
		id: "pp03-pdf",
		title: "PP03 PDF 文件",
		src: "/HTML/PDF/PP03_結合 MCP 之 Blender Bonsai BIM 4D 應用分析.pdf",
		download: "/HTML/PDF/PP03_結合 MCP 之 Blender Bonsai BIM 4D 應用分析.pdf",
	},
	rtx: {
		id: "rtx",
		title: "Architectural Design With Agents on NVIDIA RTX Spark",
		src: "https://www.youtube.com/embed/a6fUvL9gYAQ",
	},
	journalIndex: {
		id: "journal-index",
		title: "Journal_Index 第二層入口",
		src: "/HTML/Journal_Index.html",
	},
	journalWeb: {
		id: "journal-web",
		title: "Journal_Web",
		src: "/HTML/Journal_Web.html",
	},
	journalWebAni: {
		id: "journal-webani",
		title: "Journal_WebAni",
		src: "/HTML/Journal_WebAni.html",
	},
	web3dTech: {
		id: "web3d-tech",
		title: "PPj.YY3DW Web3D",
		src: "/HTML/web/PPj.YY3DW_web3d.html",
	},
	glbAni: {
		id: "glb-ani",
		title: "GLB three.js 動態",
		src: "/HTML/web/glb.3js_007AniE.html",
	},
	ifcViewer: {
		id: "ifc-viewer",
		title: "IFC / GLB viewer",
		src: "/HTML/web/GLB_IFC_http_server_viewer.html",
	},
} satisfies Record<string, Entry>;

function App() {
	const [activeEntry, setActiveEntry] = useState<Entry>(entries.homeA);
	const [reloadKey, setReloadKey] = useState(0);
	const viewerRef = useRef<HTMLDivElement>(null);

	function loadEntry(entry: Entry) {
		setActiveEntry(entry);
		setReloadKey((value) => value + 1);
		viewerRef.current?.scrollIntoView({ behavior: "smooth", block: "start" });
	}

	async function toggleFullscreen() {
		if (!viewerRef.current) return;
		if (!document.fullscreenElement) {
			await viewerRef.current.requestFullscreen();
		} else {
			await document.exitFullscreen();
		}
	}

	const isHomeMode = activeEntry.id === entries.homeA.id || activeEntry.id === entries.homeB.id;

	return (
		<div className="layout-wrapper">
			<header className="site-header">
				<div className="headline">
					<div className="kicker">AIGC.4D BIM WORKFLOW</div>
					<h1>AIGC.4DBIM</h1>
					<p>
						以台中大墩南路「雅園會館」為核心案例，聚焦於台灣第一座由 AIGC
						生成式人工智慧參與設計並實際完成之建築體，進一步探討 AIGC 在建築設計、4D施工整合與數位應用中的學術意義與實務價值
					</p>
				</div>
				<nav className="toolbar" aria-label="主入口">
					<button type="button" className={isHomeMode ? "is-active" : ""} onClick={() => loadEntry(entries.homeA)}>
						首頁動畫
					</button>
					<button type="button" className={activeEntry.id === entries.pp01.id ? "is-active" : ""} onClick={() => loadEntry(entries.pp01)}>
						PP01
					</button>
					<button type="button" className={activeEntry.id === entries.pp02.id ? "is-active" : ""} onClick={() => loadEntry(entries.pp02)}>
						PP02
					</button>
					<button type="button" className={activeEntry.id === entries.pp03.id ? "is-active" : ""} onClick={() => loadEntry(entries.pp03)}>
						PP03
					</button>
				</nav>
			</header>

			<section className="viewer-sticky" ref={viewerRef}>
				<div className="viewer-titlebar">
					<div className="viewer-title">{activeEntry.title}</div>
					<div className={isHomeMode ? "viewer-modes" : "viewer-modes is-hidden"}>
						<button type="button" className={activeEntry.id === entries.homeA.id ? "is-active" : ""} onClick={() => loadEntry(entries.homeA)}>
							靜態 A
						</button>
						<button type="button" className={activeEntry.id === entries.homeB.id ? "is-active" : ""} onClick={() => loadEntry(entries.homeB)}>
							動態 B
						</button>
					</div>
					<div className="viewer-actions">
						{activeEntry.download ? (
							<a className="download-link" href={activeEntry.download} download>
								下載 PDF
							</a>
						) : null}
						<button type="button" onClick={() => setReloadKey((value) => value + 1)}>
							重新載入
						</button>
						<button type="button" onClick={toggleFullscreen}>
							滿畫面
						</button>
					</div>
				</div>
				<div className="viewer">
					<iframe
						key={`${activeEntry.id}-${reloadKey}`}
						src={activeEntry.src}
						title={activeEntry.title}
						allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share; fullscreen; xr-spatial-tracking"
						allowFullScreen
					/>
				</div>
			</section>

			<section className="section">
				<h2 className="section-title">主簡報欄位</h2>
				<div className="grid-cards">
					<article className="card is-pp01">
						<span>Research Foundation</span>
						<h3>PP01 論文 GPT</h3>
						<p>生成式人工智慧在建築物入口設計之整合流程研究：AIGC、BIM/IFC 與 GRC 工法應用。</p>
						<div className="card-actions is-two">
							<button type="button" onClick={() => loadEntry(entries.pp01)}>
								簡報展示
							</button>
							<button type="button" onClick={() => loadEntry(entries.pp01Pdf)}>
								PDF 原文
							</button>
						</div>
					</article>

					<article className="card is-pp02">
						<span>Primary Web3D Core</span>
						<h3>PP02 期刊 Web3D</h3>
						<p>從 IFC 到互動式 Web3D：結合 AIGC 的建築資訊可視化「類 4D」施工順序展示。</p>
						<div className="card-actions is-four">
							<button type="button" onClick={() => loadEntry(entries.pp02)}>
								簡報展示
							</button>
							<button type="button" onClick={() => loadEntry(entries.pp02Exact)}>
								PPTX復刻
							</button>
							<button type="button" onClick={() => loadEntry(entries.pp02Animation)}>
								PPT動畫
							</button>
							<button type="button" onClick={() => loadEntry(entries.pp02Pdf)}>
								PDF 原文
							</button>
						</div>
					</article>

					<article className="card is-pp03">
						<span>Technical Extension</span>
						<h3>PP03 MCP + Bonsai 4D</h3>
						<p>結合 MCP 之 Blender Bonsai BIM 4D 應用分析：AI Agent 語意驅動工作流。</p>
						<div className="card-actions is-five">
							<button type="button" onClick={() => loadEntry(entries.pp03)}>
								簡報展示
							</button>
							<button type="button" onClick={() => loadEntry(entries.poster)}>
								海報
							</button>
							<button type="button" onClick={() => loadEntry(entries.blender)}>
								2026BlenderBIM(建研所)
							</button>
							<button type="button" onClick={() => loadEntry(entries.pp03Pdf)}>
								PDF 原文
							</button>
							<button type="button" className="full-width" onClick={() => loadEntry(entries.rtx)}>
								Architectural Design With Agents on NVIDIA RTX Spark
							</button>
						</div>
					</article>
				</div>
			</section>

			<section className="section">
				<h2 className="section-title">第二層 Web3D 展示入口</h2>
				<div className="file-list">
					<FileButton entry={entries.journalIndex} label="Journal_Index.html" onLoad={loadEntry} />
					<FileButton entry={entries.journalWeb} label="Journal_Web.html" tag="靜態展示" onLoad={loadEntry} />
					<FileButton entry={entries.journalWebAni} label="Journal_WebAni.html" tag="動態展示" onLoad={loadEntry} />
					<FileButton entry={entries.web3dTech} label="PPj.YY3DW_web3d.html" tag="技術整理" onLoad={loadEntry} />
					<FileButton entry={entries.glbAni} label="glb.3js_007AniE.html" tag="GLB 動態" onLoad={loadEntry} />
					<FileButton entry={entries.ifcViewer} label="GLB_IFC_http_server_viewer.html" tag="IFC 載入器" onLoad={loadEntry} />
				</div>
			</section>
		</div>
	);
}

function FileButton({
	entry,
	label,
	tag,
	onLoad,
}: {
	entry: Entry;
	label: string;
	tag?: string;
	onLoad: (entry: Entry) => void;
}) {
	return (
		<button type="button" className="file-item" onClick={() => onLoad(entry)}>
			<span>{label}</span>
			{tag ? <small>{tag}</small> : null}
		</button>
	);
}

export default App;
