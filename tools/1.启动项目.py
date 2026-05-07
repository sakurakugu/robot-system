#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""统一启动机器人项目。"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
脚本映射 = {
    "pc": ROOT_DIR / "repos" / "robot-pc" / "tools" / "1.启动电脑端.py",
    "cloud": ROOT_DIR / "repos" / "robot-cloud" / "tools" / "1.启动服务端.py",
    "phone": ROOT_DIR / "repos" / "robot-phone" / "tools" / "1.启动手机端.py",
    "onboard": ROOT_DIR / "repos" / "robot-onboard" / "tools" / "1.常用命令.py",
}


def 解析参数() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="统一启动机器人项目")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--pc", action="store_true", help="启动 robot-pc")
    group.add_argument("--cloud", action="store_true", help="启动 robot-cloud")
    group.add_argument("--phone", action="store_true", help="启动 robot-phone")
    group.add_argument("--onboard", action="store_true", help="启动 robot-onboard")
    return parser.parse_args()


def main() -> int:
    args = 解析参数()
    目标 = None
    if args.pc:
        目标 = "pc"
    elif args.cloud:
        目标 = "cloud"
    elif args.phone:
        目标 = "phone"
    elif args.onboard:
        目标 = "onboard"

    if 目标 is None:
        print("请使用 --pc / --cloud / --phone / --onboard 之一")
        return 1

    script_path = 脚本映射[目标]
    if not script_path.exists():
        print(f"未找到脚本: {script_path}", file=sys.stderr)
        return 1

    result = subprocess.run([sys.executable, str(script_path)], cwd=script_path.parent.parent)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
