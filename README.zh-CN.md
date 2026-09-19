[English](README.md) · **简体中文**

> 英文版是规范版本。本页与 [README.md](README.md) 不一致时，以英文版为准。

<!-- translation-of: README.md sha256:3d7ef0123da4c9ef -->

<!-- Source: Best-README-Template BLANK_README (Unlicense) — https://github.com/othneildrew/Best-README-Template -->
<a id="readme-top"></a>

# BinarySsearch Python

一个实现迭代式二分查找的 Python 脚本，每次运行都会用 1000 个随机生成的有序列表自我验证。

[![CI](https://github.com/anyingiit/BinarySsearch_Python/actions/workflows/ci.yml/badge.svg)](https://github.com/anyingiit/BinarySsearch_Python/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/anyingiit/BinarySsearch_Python)](LICENSE)

[报告问题](https://github.com/anyingiit/BinarySsearch_Python/issues/new?template=bug_report.yml) · [提出需求](https://github.com/anyingiit/BinarySsearch_Python/issues/new?template=feature_request.yml)

<details>
  <summary>目录</summary>
  <ol>
    <li><a href="#about-the-project">关于本项目</a></li>
    <li><a href="#getting-started">开始使用</a></li>
    <li><a href="#usage">用法</a></li>
    <li><a href="#contributing">参与贡献</a></li>
    <li><a href="#license">许可证</a></li>
    <li><a href="#contact">联系方式</a></li>
  </ol>
</details>

## 关于本项目

`binary_search.py` 是经典迭代式二分查找算法的一个独立实现。
`generationRandomIntList` 和 `generationRandomOrderIntList`
用于构建一个随机的有序整数列表，`binary_search`
则在每一步都将查找范围缩小一半，直到找到目标值或范围为空，
并在此过程中打印查找进度。直接运行该脚本时，它会在新生成的列表上
重复这一过程 1000 次，并在每一轮报告：找到的下标是否与预期的下标一致。

计划中的功能与已知问题，见 [open issues](https://github.com/anyingiit/BinarySsearch_Python/issues)。

## 开始使用

### 环境要求

- Python 3.9 或更高版本——该脚本将返回值注解为 `list[int]`
  （PEP 585），若没有 `from __future__ import annotations` 导入
  （本文件确实没有），就需要 3.9 及以上版本才能运行
- 无需任何第三方依赖包——`binary_search.py` 只导入标准库中的
  `math` 和 `random` 两个模块

### 安装

除了安装 Python 本身之外，不需要构建或安装任何其他东西；
克隆仓库就是全部的准备工作。

```sh
git clone https://github.com/anyingiit/BinarySsearch_Python.git
cd BinarySsearch_Python
```

## 用法

直接运行该脚本：

```sh
python binary_search.py
```

它会执行自身的验证流程：共 1000 轮，每一轮都会构建一个随机的有序整数
列表，在其中查找列表自身的某个元素，并打印 `binary_search`
所用的比较次数，以及它返回的下标是否与预期的下标一致。

## 参与贡献

欢迎参与。[CONTRIBUTING.md](CONTRIBUTING.md) 说明如何提交 issue 或 pull request，[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) 说明对所有参与者的行为要求。

请不要在公开的 issue 或 pull request 中报告安全问题。[SECURITY.md](SECURITY.md) 说明了私下报告的方式。

## 许可证

以 MIT 许可证分发。详见 [LICENSE](LICENSE)。

## 联系方式

项目地址：[https://github.com/anyingiit/BinarySsearch_Python](https://github.com/anyingiit/BinarySsearch_Python)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
