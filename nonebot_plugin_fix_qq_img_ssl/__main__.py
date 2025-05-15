import ssl
from functools import wraps

from httpx import AsyncClient

_old_httpx_async_client_init = AsyncClient.__init__


@wraps(_old_httpx_async_client_init)
def _new_httpx_async_client_init(self: AsyncClient, **kwargs):
    context = ssl.create_default_context()
    context.set_ciphers("DEFAULT")
    kwargs["verify"] = context
    _old_httpx_async_client_init(self, **kwargs)


AsyncClient.__init__ = _new_httpx_async_client_init
