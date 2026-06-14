# PP02 Web3D 網站層級規劃

## 核心原則

`PP02_reveal.html` 是第一層入口，負責學術簡報敘事、章節導航、研究主張與簡報播放。

`Journal_Index.html` 是第二層展示入口，負責 Web3D viewer、GLB/IFC 展示、類 4D 動態頁與技術展示頁的集中管理。

## 目前對應路徑

第一層：

- `F:\Resilio\AIGC\Projects\0613Paper\website\PP02_reveal.html`
- URL：`http://127.0.0.1:8014/PP02_reveal.html`

第二層：

- `F:\Resilio\AIGC\Projects\0613Paper\HTML\Journal_Index.html`
- 在第一層中以 iframe 載入：`../HTML/Journal_Index.html`

第三層資產與展示頁：

- `F:\Resilio\AIGC\Projects\0613Paper\HTML\Journal_Web.html`
- `F:\Resilio\AIGC\Projects\0613Paper\HTML\Journal_WebAni.html`
- `F:\Resilio\AIGC\Projects\0613Paper\HTML\web\PPj.YY3DW_web3d.html`
- `F:\Resilio\AIGC\Projects\0613Paper\HTML\web\*.html`
- `F:\Resilio\AIGC\Projects\0613Paper\HTML\web\glb\*.glb`

## 未來網站化建議

部署成網站時，建議維持這個邏輯：

```text
site-root/
  PP02_reveal.html          # 第一層：主簡報入口
  reveal.js/                # reveal.js 靜態資產
  HTML/
    Journal_Index.html      # 第二層：Web3D 展示入口
    Journal_Web.html
    Journal_WebAni.html
    web/
      *.html                # 第三層：viewer 與展示頁
      glb/
        *.glb               # 3D 模型資產
```

若要讓網站根目錄直接打開簡報，可以另外做 `index.html` 轉址到 `PP02_reveal.html`，但不要讓 `Journal_Index.html` 取代第一層入口。
