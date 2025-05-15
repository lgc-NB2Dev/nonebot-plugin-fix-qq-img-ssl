<!-- markdownlint-disable MD031 MD033 MD036 MD041 -->

<div align="center">

<a href="https://v2.nonebot.dev/store">
  <img src="https://raw.githubusercontent.com/A-kirami/nonebot-plugin-template/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo">
</a>

<p>
  <img src="https://raw.githubusercontent.com/lgc-NB2Dev/readme/main/template/plugin.svg" alt="NoneBotPluginText">
</p>

# NoneBot-Plugin-Fix-QQ-Img-SSL

_✨ 修复访问 QQ 图床的 SSL 错误 ✨_

<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">
<a href="https://pdm.fming.dev">
  <img src="https://img.shields.io/badge/pdm-managed-blueviolet" alt="pdm-managed">
</a>
<a href="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/f4778875-45a4-4688-8e1b-b8c844440abb">
  <img src="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/f4778875-45a4-4688-8e1b-b8c844440abb.svg" alt="wakatime">
</a>

<br />

<a href="https://pydantic.dev">
  <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/lgc-NB2Dev/readme/main/template/pyd-v1-or-v2.json" alt="Pydantic Version 1 Or 2" >
</a>
<a href="./LICENSE">
  <img src="https://img.shields.io/github/license/lgc-NB2Dev/nonebot-plugin-fix-qq-img-ssl.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-fix-qq-img-ssl">
  <img src="https://img.shields.io/pypi/v/nonebot-plugin-fix-qq-img-ssl.svg" alt="pypi">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-fix-qq-img-ssl">
  <img src="https://img.shields.io/pypi/dm/nonebot-plugin-fix-qq-img-ssl" alt="pypi download">
</a>

<br />

<a href="https://registry.nonebot.dev/plugin/nonebot-plugin-fix-qq-img-ssl:nonebot_plugin_fix_qq_img_ssl">
  <img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fnbbdg.lgc2333.top%2Fplugin%2Fnonebot-plugin-fix-qq-img-ssl" alt="NoneBot Registry">
</a>
<a href="https://registry.nonebot.dev/plugin/nonebot-plugin-fix-qq-img-ssl:nonebot_plugin_fix_qq_img_ssl">
  <img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fnbbdg.lgc2333.top%2Fplugin-adapters%2Fnonebot-plugin-fix-qq-img-ssl" alt="Supported Adapters">
</a>

</div>

## 📖 介绍

Monkey Patch 了 `httpx.AsyncClient` 的 `__init__` 方法，使其始终携带一个自定义的 `SSLContext`

## 💿 安装

以下提到的方法 任选**其一** 即可

<details open>
<summary>[推荐] 使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

```bash
nb plugin install nonebot-plugin-fix-qq-img-ssl
```

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

```bash
pip install nonebot-plugin-fix-qq-img-ssl
```

</details>
<details>
<summary>pdm</summary>

```bash
pdm add nonebot-plugin-fix-qq-img-ssl
```

</details>
<details>
<summary>poetry</summary>

```bash
poetry add nonebot-plugin-fix-qq-img-ssl
```

</details>
<details>
<summary>conda</summary>

```bash
conda install nonebot-plugin-fix-qq-img-ssl
```

</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分的 `plugins` 项里追加写入

```toml
[tool.nonebot]
plugins = [
    # ...
    "nonebot_plugin_fix_qq_img_ssl"
]
```

</details>

## ⚙️ 配置

没有

## 🎉 使用

加载即有效，快来试试吧

## 📞 联系

QQ：3076823485  
Telegram：[@lgc2333](https://t.me/lgc2333)  
吹水群：[1105946125](https://jq.qq.com/?_wv=1027&k=Z3n1MpEp)  
邮箱：<lgc2333@126.com>

## 💡 鸣谢

### [LagrangeDev/Lagrange.Core/issues/315](https://github.com/LagrangeDev/Lagrange.Core/issues/315)

## 💰 赞助

**[赞助我](https://blog.lgc2333.top/donate)**

感谢大家的赞助！你们的赞助将是我继续创作的动力！

## 📝 更新日志

芝士刚刚发布的插件，还没有更新日志的说 qwq~
