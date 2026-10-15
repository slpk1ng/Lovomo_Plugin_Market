# -*- coding: utf-8 -*-
"""语音通话插件：真正的接口在 modules/webui_server.py 的 /api/call/status 与
/api/call/turn，这里只留一个加载钩子，方便在日志里确认插件已经装上。"""


def on_load(ctx):
    ctx.log("语音通话插件已加载")
