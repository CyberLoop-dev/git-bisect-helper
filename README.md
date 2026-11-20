<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:f97316&height=180&section=header&text=git-bisect-helper&fontSize=42&fontColor=ffffff&animation=fadeIn" alt="Git Bisect Helper banner" width="100%"/>

<a href="https://github.com/CyberLoop-dev/git-bisect-helper">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1100&color=f97316&center=true&vCenter=true&width=720&lines=Git%20Bisect%20Helper;Small+tools.+Clear+feedback.+Local+first." alt="Typing title"/>
</a>

<p><strong>Plan a read-only Git bisect session by validating good and bad commits and estimating binary-search steps.</strong></p>

[![License](https://img.shields.io/github/license/CyberLoop-dev/git-bisect-helper)](LICENSE)
[![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/git-bisect-helper)](https://github.com/CyberLoop-dev/git-bisect-helper)
[![Stars](https://img.shields.io/github/stars/CyberLoop-dev/git-bisect-helper?style=flat)](https://github.com/CyberLoop-dev/git-bisect-helper/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/git-bisect-helper)](https://github.com/CyberLoop-dev/git-bisect-helper/commits/main)

<img src="assets/overview.svg" alt="Git Bisect Helper project illustration" width="100%"/>

</div>

## ✨ Overview

Plan a read-only Git bisect session by validating good and bad commits and estimating binary-search steps. **Git Bisect Helper** is a small Python command-line tool built with the standard library. It is designed for local use and keeps its behavior explicit.

## 🚀 Features

- ✨ 🔎 Verify that both refs resolve to commits.
- ✨ 🌳 Check that the good commit is an ancestor of the bad commit.
- ✨ 🧮 Estimate the number of binary-search checks.
- ✨ 🛡️ Never starts or resets a bisect session automatically.

## 🖥️ Demo

```bash
python main.py --repo . --good <good-ref> --bad <bad-ref>
```

Run the command inside a Git repository, replacing the refs with a known-good and known-bad commit. The tool only reads Git metadata and prints commands for you to review.

## ⚡ Quick Start

```bash
python main.py --repo . --good <good-ref> --bad <bad-ref>
```

Python 3.10 or newer is required. No third-party packages are needed.

## 🧰 Tech Stack

- **Language:** Python 3.10+
- **Libraries:** Python standard library
- **Dependencies:** None

## 📁 Folder Structure

```text
git-bisect-helper/
├── assets/overview.svg
├── tests/test_main.py
├── main.py
├── pyproject.toml
├── .gitignore
├── LICENSE
└── README.md
```

## 🗺️ Roadmap

- [ ] Add optional path filters for monorepos.
- [ ] Add a plain-text report export.

## 🤝 Contributing

Issues and pull requests are welcome. Include a minimal input example, expected behavior, and a regression test when changing parsing or quoting rules.

## 📄 License

Released under the [MIT License](LICENSE).

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:f97316,100:0f172a&height=110&section=footer" alt="Animated wave footer" width="100%"/>
</div>
