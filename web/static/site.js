/* Local-only interaction layer. SPDX-License-Identifier: MIT */
const root = document.documentElement;
const preference = document.querySelector('#theme');
const media = matchMedia('(prefers-color-scheme: dark)');
const diagrams = [...document.querySelectorAll('.mermaid')].map(node => ({node, source: node.textContent}));
let mermaid;
let diagramJob = Promise.resolve();
async function drawDiagrams() {
  if (!diagrams.length) return;
  mermaid ??= (await import('/assets/vendor/mermaid/mermaid.esm.min.mjs')).default;
  mermaid.initialize({startOnLoad:false, securityLevel:'strict', theme:root.dataset.theme === 'dark' ? 'dark' : 'neutral', fontFamily:'system-ui, sans-serif', flowchart:{htmlLabels:false}});
  for (const {node, source} of diagrams) { node.removeAttribute('data-processed'); node.textContent = source; }
  await mermaid.run({nodes:diagrams.map(item => item.node)});
}
function queueDiagrams() { diagramJob = diagramJob.then(drawDiagrams); window.vdmtDiagramsReady = diagramJob; return diagramJob; }
function applyTheme(mode) {
  if (!['system','light','dark'].includes(mode)) mode = 'system';
  root.dataset.preference = mode;
  root.dataset.theme = mode === 'system' ? (media.matches ? 'dark' : 'light') : mode;
  preference.value = mode;
  return queueDiagrams();
}
preference.value = root.dataset.preference || 'system';
preference.addEventListener('change', () => { try { localStorage.setItem('vdmt-theme', preference.value); } catch (_) {} applyTheme(preference.value); });
media.addEventListener('change', () => { if (root.dataset.preference === 'system') applyTheme('system'); });
queueDiagrams();

const menu = document.querySelector('#menu-dialog');
const searchDialog = document.querySelector('#search-dialog');
const searchInput = document.querySelector('#search-input');
const results = document.querySelector('#search-results');
const status = document.querySelector('#search-status');
let searchIndex;
let requestNumber = 0;
let timer;
async function getIndex() {
  if (!searchIndex) {
    const response = await fetch('/search.json');
    if (!response.ok) throw new Error('Search index unavailable.');
    searchIndex = await response.json();
  }
  return searchIndex;
}
async function search() {
  const ownRequest = ++requestNumber;
  const terms = searchInput.value.toLocaleLowerCase().trim().split(/\s+/).filter(Boolean).slice(0, 12);
  results.replaceChildren();
  if (!terms.length) { status.textContent = 'Search article titles and the complete text.'; return; }
  try {
    const index = await getIndex();
    if (ownRequest !== requestNumber) return;
    const matches = index.map(item => {
      const title = item.title.toLocaleLowerCase();
      const description = item.description.toLocaleLowerCase();
      const text = item.text.toLocaleLowerCase();
      const score = terms.every(term => title.includes(term) || description.includes(term) || text.includes(term))
        ? terms.reduce((total, term) => total + (title.includes(term) ? 10 : 0) + (description.includes(term) ? 3 : 0) + (text.includes(term) ? 1 : 0), 0) : 0;
      return {item, score};
    }).filter(result => result.score > 0).sort((a,b) => b.score - a.score || a.item.title.localeCompare(b.item.title));
    status.textContent = `${matches.length} matching articles${matches.length > 20 ? ' · showing the first 20' : ''}.`;
    for (const {item} of matches.slice(0, 20)) {
      const link = document.createElement('a'); link.className = 'search-result'; link.href = item.url;
      const title = document.createElement('strong'); title.textContent = item.title;
      const detail = document.createElement('small'); detail.textContent = `${item.section} · ${item.description}`;
      link.append(title, detail); results.append(link);
    }
  } catch (_) { status.textContent = 'Search could not load. The chapter navigation and Markdown index remain available.'; }
}
function openSearch() { if (menu.open) menu.close(); if (!searchDialog.open) searchDialog.showModal(); searchInput.focus(); }
document.querySelectorAll('.search-open').forEach(button => button.addEventListener('click', openSearch));
document.querySelector('#menu-open').addEventListener('click', () => menu.showModal());
document.querySelectorAll('[data-close]').forEach(button => button.addEventListener('click', () => document.getElementById(button.dataset.close).close()));
searchInput.addEventListener('input', () => { clearTimeout(timer); timer = setTimeout(search, 120); });
// Search inputs can consume Escape to clear text before native dialog cancellation.
// Make a single Escape consistently dismiss the active publication dialog.
document.addEventListener('keydown', event => {
  if (event.key !== 'Escape') return;
  const activeDialog = searchDialog.open ? searchDialog : menu.open ? menu : null;
  if (activeDialog) { event.preventDefault(); event.stopPropagation(); activeDialog.close(); }
}, true);
document.addEventListener('keydown', event => {
  if (event.key === '/' && !event.ctrlKey && !event.metaKey && !['INPUT','TEXTAREA','SELECT'].includes(document.activeElement.tagName) && !document.activeElement.isContentEditable) { event.preventDefault(); openSearch(); }
});
const toast = document.querySelector('#copy-status');
let toastTimer;
document.querySelectorAll('[data-copy]').forEach(button => button.addEventListener('click', async () => {
  let copied = false;
  try { await navigator.clipboard.writeText(button.dataset.copy); copied = true; } catch (_) {
    const area = document.createElement('textarea'); area.value = button.dataset.copy; area.style.position = 'fixed'; area.style.opacity = '0'; document.body.append(area); area.select();
    copied = document.execCommand('copy'); area.remove(); button.focus();
  }
  toast.textContent = copied ? 'Copied to clipboard' : 'Copy was blocked by the browser'; toast.classList.add('show'); clearTimeout(toastTimer); toastTimer = setTimeout(() => toast.classList.remove('show'), 2300);
}));
