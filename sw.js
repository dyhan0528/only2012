/* ONLY2012 오프라인 캐시: 앱 화면은 새 버전 우선(네트워크 → 캐시), 글꼴·아이콘은 캐시 우선 */
const VER = "only2012-v1";
const CORE = ["/", "/manifest.webmanifest", "/icons/icon-192.png", "/icons/icon-512.png"];
self.addEventListener("install", e => {
  e.waitUntil(caches.open(VER).then(c => c.addAll(CORE)).then(() => self.skipWaiting()));
});
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VER).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener("fetch", e => {
  const req = e.request, url = new URL(req.url);
  if (req.method !== "GET" || url.pathname.startsWith("/_vercel/")) return;
  if (req.mode === "navigate") {
    e.respondWith(fetch(req).then(r => { const cp = r.clone(); caches.open(VER).then(c => c.put("/", cp)); return r; })
      .catch(() => caches.match("/")));
    return;
  }
  const fonts = url.hostname === "fonts.googleapis.com" || url.hostname === "fonts.gstatic.com";
  if (fonts || url.origin === location.origin) {
    e.respondWith(caches.match(req).then(hit => hit || fetch(req).then(r => {
      if (r.ok || r.type === "opaque") { const cp = r.clone(); caches.open(VER).then(c => c.put(req, cp)); }
      return r;
    })));
  }
});
