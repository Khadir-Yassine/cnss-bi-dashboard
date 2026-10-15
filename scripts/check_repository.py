"""Check the portfolio manifest and relative Markdown file links, without dependencies."""
import hashlib
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def main():
    problems = []
    entries = (ROOT / 'SHA256SUMS').read_text(encoding='utf-8').splitlines()
    for entry in entries:
        digest, name = entry.split('  ', 1)
        path = ROOT / name
        if not path.is_file():
            problems.append(f'Missing manifest file: {name}')
        elif hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            problems.append(f'Checksum mismatch: {name}')
    checked_links = 0
    for document in ROOT.rglob('*.md'):
        if '.git' in document.relative_to(ROOT).parts:
            continue
        for target in re.findall(r'\]\(([^\s)]+)\)', document.read_text(encoding='utf-8')):
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith('#'):
                continue
            checked_links += 1
            if not (document.parent / unquote(parsed.path)).is_file():
                problems.append(f'Broken link in {document.relative_to(ROOT)}: {target}')
    if problems:
        raise SystemExit('\n'.join(problems))
    print(f'PASS: {len(entries)} file checksums and {checked_links} local documentation links.')


if __name__ == '__main__':
    main()
