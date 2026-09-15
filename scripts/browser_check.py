#!/usr/bin/env python3
"""Exercise rendered articles, math, diagrams, navigation, and theme behavior.
SPDX-License-Identifier: MIT
"""
from __future__ import annotations
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import threading
import traceback
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


def main() -> None:
    data = json.loads((ROOT / 'site' / 'articles.json').read_text())
    output = ROOT / 'validation'
    output.mkdir(exist_ok=True)
    server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(ROOT / 'site')))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f'http://127.0.0.1:{server.server_port}'
    report = {'source_commit': data['source_commit'], 'pages': [], 'mobile_pages': [], 'errors': [], 'interactions': {}}
    try:
        with sync_playwright() as playwright:
            launch = {'headless': True}
            if os.environ.get('VDMT_BROWSER_EXECUTABLE'):
                launch['executable_path'] = os.environ['VDMT_BROWSER_EXECUTABLE']
            browser = playwright.chromium.launch(**launch)
            context = browser.new_context(viewport={'width': 1440, 'height': 1000}, color_scheme='light')
            page = context.new_page()
            page.on('pageerror', lambda error: report['errors'].append(str(error)))
            for record in data['articles']:
                response = page.goto(base + record['url'], wait_until='networkidle')
                assert response is not None and response.status == 200, record['url']
                page.evaluate('async () => { await MathJax.startup.promise; await window.vdmtDiagramsReady; }')
                assert page.locator('h1').count() == 1, record['url']
                math_count = page.locator('.math').count()
                if math_count:
                    assert page.locator('mjx-container[jax="SVG"]').count() > 0, record['url']
                assert page.locator('[data-mml-node="merror"]').count() == 0, record['url']
                diagrams = page.locator('.mermaid').count()
                assert page.locator('.mermaid svg').count() == diagrams, record['url']
                assert not page.evaluate('document.documentElement.scrollWidth > innerWidth + 2'), 'Desktop overflow: ' + record['url']
                raw = context.request.get(base + record['markdown_url'])
                assert raw.status == 200 and raw.body() == (ROOT / 'DOCS' / record['path']).read_bytes(), 'Markdown mismatch: ' + record['url']
                report['pages'].append({'url': record['url'], 'math_regions': math_count, 'diagrams': diagrams, 'markdown_exact': True})
            page.goto(base + '/', wait_until='networkidle')
            page.evaluate('async () => { await MathJax.startup.promise; await window.vdmtDiagramsReady; }')
            assert page.locator('html').get_attribute('data-theme') == 'light', 'Initial system theme'
            page.screenshot(path=str(output / 'home-light.png'), full_page=True)
            page.emulate_media(color_scheme='dark')
            page.wait_for_function('document.documentElement.dataset.theme === "dark"')
            page.screenshot(path=str(output / 'home-dark.png'), full_page=True)
            page.select_option('#theme', 'light')
            page.reload(wait_until='networkidle')
            assert page.locator('html').get_attribute('data-theme') == 'light', 'Persisted manual theme'
            page.select_option('#theme', 'system')
            page.wait_for_function('document.documentElement.dataset.theme === "dark"')
            report['interactions']['system_and_manual_theme'] = True
            page.locator('.sidebar .search-open').click()
            page.fill('#search-input', 'context closure')
            page.wait_for_selector('.search-result')
            assert page.locator('.search-result').count() > 0, 'Search result count'
            page.keyboard.press('Escape')
            page.wait_for_function('!document.querySelector("#search-dialog").open')
            report['interactions']['search_and_escape'] = True
            page.goto(base + '/white-paper/', wait_until='networkidle')
            page.evaluate('async () => { await MathJax.startup.promise; await window.vdmtDiagramsReady; }')
            # Select mathematical content by its role, not a title-specific CSS ID.
            page.locator('.prose div.math').first.scroll_into_view_if_needed()
            page.screenshot(path=str(output / 'white-paper-math.png'))
            page.set_viewport_size({'width': 390, 'height': 844})
            page.emulate_media(color_scheme='light')
            for record in data['articles']:
                page.goto(base + record['url'], wait_until='networkidle')
                page.evaluate('async () => { await MathJax.startup.promise; await window.vdmtDiagramsReady; }')
                assert not page.evaluate('document.documentElement.scrollWidth > innerWidth + 2'), 'Mobile overflow: ' + record['url']
                report['mobile_pages'].append(record['url'])
            page.goto(base + '/', wait_until='networkidle')
            page.locator('#menu-open').click()
            assert page.locator('#menu-dialog').evaluate('(node) => node.open'), 'Mobile navigation opens'
            page.keyboard.press('Escape')
            page.wait_for_function('!document.querySelector("#menu-dialog").open')
            page.screenshot(path=str(output / 'mobile.png'), full_page=True)
            report['interactions']['mobile_navigation_and_layout'] = True
            browser.close()
    except Exception:
        report['errors'].append(traceback.format_exc())
        try:
            page.screenshot(path=str(output / 'failure.png'), full_page=True)
        except Exception:
            pass  # The browser may already be closed; retain the primary error.
    finally:
        server.shutdown()
        server.server_close()
        (output / 'browser.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'pages_checked': len(report['pages']), 'mobile_pages_checked': len(report['mobile_pages']), 'interactions': report['interactions'], 'errors': report['errors']}, indent=2))
    if report['errors']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
