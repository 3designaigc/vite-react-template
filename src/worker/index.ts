import { Hono } from "hono";

const app = new Hono<{ Bindings: Env }>();

app.get("/api/health", (c) =>
	c.json({
		ok: true,
		app: "0613Paper VRHC",
		stack: ["Vite", "React", "Hono", "Cloudflare Workers"],
	}),
);

app.get("/api/site-map", (c) =>
	c.json({
		primary: [
			"/presentations/PP01_reveal.html",
			"/presentations/PP02_reveal.html",
			"/presentations/PP03_reveal.html",
		],
		pp02: [
			"/presentations/PP02_Web3D_pptx_exact_reveal.html",
			"/presentations/PP02_Web3D_original_animation.html",
			"/HTML/Journal_Index.html",
		],
		pdf: [
			"/HTML/PDF/PP01_論文_GPT.pdf",
			"/HTML/PDF/PP02_期刊.pdf",
			"/HTML/PDF/PP03_結合 MCP 之 Blender Bonsai BIM 4D 應用分析.pdf",
		],
	}),
);

app.get("/api/", (c) => c.redirect("/api/health"));

export default app;
