# ruff: noqa: E402

from nonebot.plugin import PluginMetadata

from . import __main__ as __main__
from .config import ConfigModel

__version__ = "0.1.0"
__plugin_meta__ = PluginMetadata(
    name="修复 QQ 图床 SSL 错误",
    description="如名",
    usage="加载即有效",
    type="library",
    homepage="https://github.com/lgc-NB2Dev/nonebot-plugin-fix-qq-img-ssl",
    config=ConfigModel,
    supported_adapters=None,
    extra={"License": "MIT", "Author": "LgCookie"},
)
