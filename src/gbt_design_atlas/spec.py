"""The capability contract, copied verbatim from the GBT V8 registry.

Do not hand-edit: ``tests/test_spec.py`` pins every field against the
registry snapshot so drift fails the build instead of shipping quietly.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

_RAW = r"""{
 "name": "design_atlas",
 "domain": "creation",
 "desc": "**设计与审美图鉴的口**（吞天吞来的外部手册 → 人话找到\"该读哪一节\"）。素材：`flash-hero/GOATED-UI-SKILL`（**MIT**）的 18 份手册（component-recipes / webgl-shaders-3d / interactions / scroll-gsap / motion-principles / typography / color-surfaces / page-transitions / text-effects / backgrounds-svg-canvas / layout-composition / css-modern / libraries / performance-a11y …）。常用说法：滚动驱动 / 视差 / 文字动画 / 缓动 / 弹簧 / 毛玻璃 / 渐变 / 阴影 / 粒子 / 过渡 / 悬停 / 英雄区 / 卡片 / 无障碍 / 性能 / 着色器 / 三维 / 排版 / 字体 / 配色 / 灵感来源。op=status/build/find/where：`build` 扫手册提 **recipe（标题+行号+摘要+代码语言）** 与 **来源条目（类别+名+URL）** 落 `store/design_atlas/index.jsonl`（只追加）；`find` 人话 → **哪份文件哪一节（`文件#L行号`）**，命中 0 就是 0。铁律：**只读 · 零执行**（绝不跑上游任何 `.mjs`）· **不改上游一个字节** · 摘要只取自该节正文。",
 "handler": "design_atlas",
 "safe": true,
 "external": false,
 "requires_params": false,
 "params": [],
 "params_hint": "",
 "multi_op": true,
 "ops": [
  "status",
  "build",
  "find",
  "where"
 ],
 "ops_hint": ""
}"""


@dataclass(frozen=True)
class CapSpec:
    """Immutable description of one capability bit."""

    name: str
    domain: str
    desc: str
    handler: str
    safe: bool
    external: bool
    requires_params: bool
    params: Tuple[str, ...] = ()
    params_hint: str = ""
    multi_op: bool = False
    ops: Tuple[str, ...] = ()
    ops_hint: str = ""

    @property
    def gated(self) -> bool:
        """True when the registry marks this bit ``safe: false``.

        Gated does not mean "dangerous"; it means the action can change state
        that cannot be restored by running the inverse action.
        """
        return not self.safe

    @property
    def summary(self) -> str:
        """First clause of the description, for one-line listings."""
        for sep in ("\uff08", "\uff1b", "\u3002", ";"):
            if sep in self.desc:
                head = self.desc.split(sep, 1)[0].strip()
                if head:
                    return head
        return self.desc.strip()

    def as_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "domain": self.domain,
            "desc": self.desc,
            "handler": self.handler,
            "safe": self.safe,
            "gated": self.gated,
            "external": self.external,
            "requires_params": self.requires_params,
            "params": list(self.params),
            "params_hint": self.params_hint,
            "multi_op": self.multi_op,
            "ops": list(self.ops),
            "ops_hint": self.ops_hint,
        }


_data = json.loads(_RAW)

SPEC = CapSpec(
    name=_data["name"],
    domain=_data["domain"],
    desc=_data["desc"],
    handler=_data["handler"],
    safe=_data["safe"],
    external=_data["external"],
    requires_params=_data["requires_params"],
    params=tuple(_data["params"]),
    params_hint=_data["params_hint"],
    multi_op=_data["multi_op"],
    ops=tuple(_data["ops"]),
    ops_hint=_data["ops_hint"],
)
