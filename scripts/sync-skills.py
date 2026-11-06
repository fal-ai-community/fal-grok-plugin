#!/usr/bin/env python3
"""Refresh or check only generated skills against the pinned canonical source."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]

def snapshot(folder):
    return {p.relative_to(folder).as_posix(): p.read_bytes() for p in folder.rglob('*')
            if p.is_file() and not any(v in {'__pycache__', 'node_modules', '.DS_Store'}
                                      for v in p.relative_to(folder).parts)}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, help='Canonical checkout at the locked commit')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    lock = json.loads((ROOT / 'skills-source.lock.json').read_text(encoding='utf-8'))
    with tempfile.TemporaryDirectory(prefix='fal-canonical-') as tmp:
        tmp = Path(tmp); source = args.source
        if source is None:
            source = tmp / 'source'
            subprocess.run(['git', 'clone', '--no-checkout',
                            'git@github.com:fal-ai-community/skills.git', str(source)], check=True)
            subprocess.run(['git', '-C', str(source), 'fetch', 'origin', lock['commit']], check=True)
            subprocess.run(['git', '-C', str(source), 'checkout', '--detach', lock['commit']], check=True)
        if (source / '.git').exists():
            head = subprocess.check_output(['git', '-C', str(source), 'rev-parse', 'HEAD'], text=True).strip()
            if head != lock['commit']:
                raise SystemExit('Source is not at the locked commit')
            if subprocess.check_output(['git', '-C', str(source), 'status', '--porcelain'], text=True).strip():
                raise SystemExit('Source has uncommitted changes')
        out = tmp / 'bundle'
        command = [sys.executable, str(source / 'scripts/build-packages.py'),
                   '--profile', lock['profile'], '--source-ref', lock['commit'],
                   '--output', str(out)]
        if 'bundle' in lock:
            command += ['--bundle', lock['bundle']]
        subprocess.run(command, check=True)
        expected = snapshot(out / 'skills'); actual = snapshot(ROOT / 'skills')
        generated_lock = json.loads((out / 'skills-source.lock.json').read_text(encoding='utf-8'))
        if args.check:
            if expected != actual or generated_lock != lock:
                missing = sorted(set(expected) - set(actual))
                extra = sorted(set(actual) - set(expected))
                changed = sorted(p for p in set(actual) & set(expected) if actual[p] != expected[p])
                raise SystemExit(f'Generated bundle drift: missing={missing}, extra={extra}, changed={changed}')
            print(f'Canonical bundle verified: {len(expected)} files at {lock["commit"]}')
        else:
            shutil.rmtree(ROOT / 'skills'); shutil.copytree(out / 'skills', ROOT / 'skills')
            shutil.copy2(out / 'skills-source.lock.json', ROOT / 'skills-source.lock.json')
            print('Refreshed skills only; native manifests, connectors, icons and evals were preserved')

if __name__ == '__main__': main()
