<!-- Source: Best-README-Template BLANK_README (Unlicense) — https://github.com/othneildrew/Best-README-Template -->
<a id="readme-top"></a>

# BinarySsearch Python

A Python script implementing iterative binary search that verifies itself against 1000 randomly generated sorted lists on every run.

**English** · [简体中文](README.zh-CN.md)

[![CI](https://github.com/anyingiit/BinarySsearch_Python/actions/workflows/ci.yml/badge.svg)](https://github.com/anyingiit/BinarySsearch_Python/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/anyingiit/BinarySsearch_Python)](LICENSE)

[Report a bug](https://github.com/anyingiit/BinarySsearch_Python/issues/new?template=bug_report.yml) · [Request a feature](https://github.com/anyingiit/BinarySsearch_Python/issues/new?template=feature_request.yml)

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

`binary_search.py` is a self-contained implementation of the classic iterative
binary search algorithm. `generationRandomIntList` and
`generationRandomOrderIntList` build a random sorted list of integers, and
`binary_search` narrows a search range in half on each step until it finds the
target or the range is empty, printing its progress as it goes. Run directly,
the script repeats this 1000 times over freshly generated lists and reports,
for each round, whether the index it found matches the one the script expected.

See the [open issues](https://github.com/anyingiit/BinarySsearch_Python/issues) for planned features and known issues.

## Getting Started

### Prerequisites

- Python 3.9 or newer — the script annotates return values as `list[int]`
  (PEP 585), which needs 3.9+ without a `from __future__ import annotations`
  import, and the file has none
- No third-party packages — `binary_search.py` imports only the standard
  library modules `math` and `random`

### Installation

Nothing needs to be built or installed beyond Python itself; cloning the
repository is the whole setup.

```sh
git clone https://github.com/anyingiit/BinarySsearch_Python.git
cd BinarySsearch_Python
```

## Usage

Run the script directly:

```sh
python binary_search.py
```

It performs its own check: 1000 rounds, each building a random sorted list of
integers, searching it for one of the list's own elements, and printing the
number of comparisons `binary_search` needed and whether the index it
returned matched the one the script expected.

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) for how to open an issue or a pull request, and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for the standards expected of everyone taking part.

Please do not report security issues in public issues or pull requests. [SECURITY.md](SECURITY.md) explains how to report them privately.

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

## Contact

Project link: [https://github.com/anyingiit/BinarySsearch_Python](https://github.com/anyingiit/BinarySsearch_Python)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
