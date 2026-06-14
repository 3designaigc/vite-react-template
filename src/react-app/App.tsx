import { useMemo, useRef, useState } from "react";
import "./App.css";

type Entry = {
	id: string;
	label: string;
	title: string;
	src: string;
	kind: "reveal" | "pdf" | "web3d" | "media" | "html";
	description: string;
	accent: "blue" | "red" | "green" | "yellow";
	download?: string;
};

const primaryEntries: Entry[] = [
	{
		id: "pp01",
		label: "PP01",
		title: "PP01 論文 GPT",
		src: "/presentations/PP01_reveal.html",
		kind: "reveal",
		description: "AIGC、BIM/IFC、GRC 工法與入口案例的研究背景。",
		accent: "blue",
	},
	{
		id: "pp02",
		label: "PP02",
		title: "PP02 期刊 Web3D",
		src: "/presentations/PP02_reveal.html",
		kind: "reveal",
		description: "IFC 到 GLB、Google AI Studio、three.js 與類 4D 展示。",
		accent: "red",
	},
	{
		id: "pp03",
		label: "PP03",
		title: "PP03 MCP + Bonsai BIM 4D",
		src: "/presentations/PP03_reveal.html",
		kind: "reveal",
		description: "Blender Bonsai、MCP、Skill 與 BIM 4D 語意工作流。",
		accent: "green",
	},
];

const pp02Entries: Entry[] = [
	{
		id: "pp02-exact",
		label: "PPTX 復刻",
		title: "PP02 PPTX 視覺復刻",
		src: "/presentations/PP02_Web3D_pptx_exact_reveal.html",
		kind: "reveal",
		description: "以 PowerPoint 匯出 PNG 逐頁重建，供差異比較。",
		accent: "red",
	},
	{
		id: "pp02-animation",
		label: "PPT 動畫",
		title: "PP02 原始 PPT 動畫",
		src: "/presentations/PP02_Web3D_original_animation.html",
		kind: "media",
		description: "保留 PowerPoint 淡入淡出與物件動畫節奏。",
		accent: "yellow",
	},
	{
		id: "blender-bim",
		label: "BIM 4D",
		title: "2026 BlenderBIM",
		src: "/presentations/2026_BlenderBIM.html",
		kind: "reveal",
		description: "延伸的 BlenderBIM / 4D BIM 展示簡報。",
		accent: "green",
	},
];

const pdfEntries: Entry[] = [
	{
		id: "pdf-pp01",
		label: "PP01 PDF",
		title: "PP01 PDF 文件",
		src: "/HTML/PDF/PP01_論文_GPT.pdf",
		download: "/HTML/PDF/PP01_論文_GPT.pdf",
		kind: "pdf",
		description: "PP01 原始閱讀文件。",
		accent: "blue",
	},
	{
		id: "pdf-pp02",
		label: "PP02 PDF",
		title: "PP02 PDF 文件",
		src: "/HTML/PDF/PP02_期刊.pdf",
		download: "/HTML/PDF/PP02_期刊.pdf",
		kind: "pdf",
		description: "PP02 期刊閱讀文件。",
		accent: "red",
	},
	{
		id: "pdf-pp03",
		label: "PP03 PDF",
		title: "PP03 PDF 文件",
		src: "/HTML/PDF/PP03_結合 MCP 之 Blender Bonsai BIM 4D 應用分析.pdf",
		download: "/HTML/PDF/PP03_結合 MCP 之 Blender Bonsai BIM 4D 應用分析.pdf",
		kind: "pdf",
		description: "PP03 MCP + Bonsai BIM 4D 閱讀文件。",
		accent: "green",
	},
	{
		id: "poster",
		label: "PP03 海報",
		title: "PP03 海報 PDF",
		src: "/HTML/PDF/PP03_海報.pdf",
		download: "/HTML/PDF/PP03_海報.pdf",
		kind: "pdf",
		description: "PP03 海報版輸出。",
		accent: "yellow",
	},
];

const web3dEntries: Entry[] = [
	{
		id: "journal-index",
		label: "Journal Index",
		title: "PP02 第二層 Web3D 入口",
		src: "/HTML/Journal_Index.html",
		kind: "web3d",
		description: "集中管理 Web3D / GLB / IFC / 類 4D 動態頁。",
		accent: "red",
	},
	{
		id: "journal-web",
		label: "Journal Web",
		title: "Journal Web 說明頁",
		src: "/HTML/Journal_Web.html",
		kind: "html",
		description: "PP02 Web3D 說明頁。",
		accent: "blue",
	},
	{
		id: "journal-webani",
		label: "WebAni",
		title: "Journal WebAni 動態頁",
		src: "/HTML/Journal_WebAni.html",
		kind: "web3d",
		description: "類 4D / 動態 Web3D 展示入口。",
		accent: "green",
	},
	{
		id: "bauhaus-a",
		label: "Bauhaus A",
		title: "Bauhaus Animation A",
		src: "/bauhaus_animation - A.html",
		kind: "html",
		description: "Bauhaus 風格動畫展示頁。",
		accent: "yellow",
	},
	{
		id: "bauhaus-b",
		label: "Bauhaus B",
		title: "Bauhaus Animation B",
		src: "/bauhaus_animation - B.html",
		kind: "html",
		description: "Bauhaus 風格動畫替代版本。",
		accent: "yellow",
	},
];

const allEntries = [...primaryEntries, ...pp02Entries, ...pdfEntries, ...web3dEntries];

function App() {
	const [activeEntry, setActiveEntry] = useState<Entry>(primaryEntries[1]);
	const [reloadKey, setReloadKey] = useState(0);
	const viewerRef = useRef<HTMLDivElement>(null);

	const downloadHref = activeEntry.download;
	const status = useMemo(() => {
		const byKind = allEntries.reduce<Record<string, number>>((acc, entry) => {
			acc[entry.kind] = (acc[entry.kind] ?? 0) + 1;
			return acc;
		}, {});

		return [
			`${allEntries.length} entries`,
			`${byKind.reveal ?? 0} reveal`,
			`${byKind.pdf ?? 0} PDF`,
			`${byKind.web3d ?? 0} Web3D`,
		];
	}, []);

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

	return (
		<div className="app-shell">
			<div className="shape-circle" aria-hidden="true" />
			<div className="shape-square" aria-hidden="true" />

			<header className="hero">
				<div>
					<p className="kicker">0613Paper / Vite + React + Hono + Cloudflare</p>
					<h1>AIGC.4DBIM 互動簡報網站</h1>
					<p className="hero-copy">
						以 React 管理第一層入口，靜態資產保留 reveal.js、PDF、Web3D demo 與影片。
						部署時由 Cloudflare Workers + Hono 提供 API 與 SPA fallback。
					</p>
				</div>
				<nav className="toolbar" aria-label="主簡報入口">
					{primaryEntries.map((entry) => (
						<button
							key={entry.id}
							type="button"
							className={activeEntry.id === entry.id ? "is-active" : ""}
							data-accent={entry.accent}
							onClick={() => loadEntry(entry)}
						>
							{entry.label}
						</button>
					))}
				</nav>
			</header>

			<section className="viewer-shell" ref={viewerRef}>
				<div className="viewer-titlebar">
					<div>
						<p className="viewer-kind">{activeEntry.kind}</p>
						<h2>{activeEntry.title}</h2>
					</div>
					<div className="viewer-actions">
						{downloadHref ? (
							<a className="download-link" href={downloadHref} download>
								下載
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
				<div className="viewer-frame">
					<iframe
						key={`${activeEntry.id}-${reloadKey}`}
						src={activeEntry.src}
						title={activeEntry.title}
						allow="fullscreen; autoplay; xr-spatial-tracking"
					/>
				</div>
			</section>

			<main className="content-grid">
				<section className="panel-section">
					<div className="section-heading">
						<p className="kicker">Primary Decks</p>
						<h2>三篇主簡報</h2>
					</div>
					<div className="entry-grid">
						{primaryEntries.map((entry) => (
							<EntryCard key={entry.id} entry={entry} active={entry.id === activeEntry.id} onLoad={loadEntry} />
						))}
					</div>
				</section>

				<section className="panel-section">
					<div className="section-heading">
						<p className="kicker">PP02 Modes</p>
						<h2>Web3D / 復刻 / 動畫</h2>
					</div>
					<div className="entry-grid compact">
						{pp02Entries.map((entry) => (
							<EntryCard key={entry.id} entry={entry} active={entry.id === activeEntry.id} onLoad={loadEntry} />
						))}
					</div>
				</section>

				<section className="panel-section">
					<div className="section-heading">
						<p className="kicker">PDF Documents</p>
						<h2>文件展示與下載</h2>
					</div>
					<div className="entry-grid compact">
						{pdfEntries.map((entry) => (
							<EntryCard key={entry.id} entry={entry} active={entry.id === activeEntry.id} onLoad={loadEntry} />
						))}
					</div>
				</section>

				<section className="panel-section">
					<div className="section-heading">
						<p className="kicker">Second Layer</p>
						<h2>Web3D 與 HTML 展示</h2>
					</div>
					<div className="entry-list">
						{web3dEntries.map((entry) => (
							<button
								key={entry.id}
								type="button"
								className={activeEntry.id === entry.id ? "list-item is-active" : "list-item"}
								data-accent={entry.accent}
								onClick={() => loadEntry(entry)}
							>
								<span>{entry.label}</span>
								<small>{entry.description}</small>
							</button>
						))}
					</div>
				</section>

				<section className="panel-section system-panel">
					<div className="section-heading">
						<p className="kicker">Architecture</p>
						<h2>VRHC 架構</h2>
					</div>
					<ul className="status-list">
						{status.map((item) => (
							<li key={item}>{item}</li>
						))}
					</ul>
					<p>
						React 負責互動入口與 viewer 狀態；`public` 保留舊網站資產；Hono Worker 提供 `/api/health`
						與 `/api/site-map`，Cloudflare Workers 可部署 SPA 與靜態資產。
					</p>
				</section>
			</main>
		</div>
	);
}

function EntryCard({
	entry,
	active,
	onLoad,
}: {
	entry: Entry;
	active: boolean;
	onLoad: (entry: Entry) => void;
}) {
	return (
		<article className={active ? "entry-card is-active" : "entry-card"} data-accent={entry.accent}>
			<span>{entry.kind}</span>
			<h3>{entry.title}</h3>
			<p>{entry.description}</p>
			<button type="button" onClick={() => onLoad(entry)}>
				展示
			</button>
		</article>
	);
}

export default App;
