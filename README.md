# design_atlas

**One capability bit from GBT V8, packaged standalone.** No. 26 of 341,
`creation` domain (Creation).

<p>
<img alt="python" src="https://img.shields.io/badge/python-3.9%2B-blue">
<img alt="license" src="https://img.shields.io/badge/license-MIT-green">
<img alt="deps" src="https://img.shields.io/badge/runtime%20dependencies-0-brightgreen">
</p>

> **设计与审美图鉴的口**（吞天吞来的外部手册 → 人话找到"该读哪一节"）。素材：`flash-hero/GOATED-UI-SKILL`（**MIT**）的 18 份手册（component-recipes / webgl-shaders-3d / interactions / scroll-gsap / motion-principles / typography / color-surfaces / page-transitions / text-effects / backgrounds-svg-canvas / layout-composition / css-modern / libraries / performance-a11y …）。常用说法：滚动驱动 / 视差 / 文字动画 / 缓动 / 弹簧 / 毛玻璃 / 渐变 / 阴影 / 粒子 / 过渡 / 悬停 / 英雄区 / 卡片 / 无障碍 / 性能 / 着色器 / 三维 / 排版 / 字体 / 配色 / 灵感来源。op=status/build/find/where：`build` 扫手册提 **recipe（标题+行号+摘要+代码语言）** 与 **来源条目（类别+名+URL）** 落 `store/design_atlas/index.jsonl`（只追加）；`find` 人话 → **哪份文件哪一节（`文件#L行号`）**，命中 0 就是 0。铁律：**只读 · 零执行**（绝不跑上游任何 `.mjs`）· **不改上游一个字节** · 摘要只取自该节正文。

That description is copied verbatim from the registry. `tests/test_spec.py` pins it,
so documentation drift fails the build instead of shipping quietly.

## What this package actually is

It is the **contract** for one capability: its name, its parameters, the values it
accepts, and whether it can change state that cannot be restored. It is not the
implementation — that lives in the runtime this bit was extracted from.

So `run()` goes through a narrow `Backend` protocol, and the default backend is a
stub that **says so**:

```
status="validated"   backend="stub"   data={"executed": false}
```

Never `status="ok"`. A stub that reports success is worse than no stub, because the
caller stops looking for the real thing.

## Install

```bash
git clone https://github.com/gbtweilai-star/gbt-design-atlas.git
cd gbt-design-atlas
python -m pip install -e ".[dev]"
```

## Use

```bash
python -m gbt_design_atlas info                  # capability card
python -m gbt_design_atlas spec --json           # machine-readable contract
python -m gbt_design_atlas check --payload '{}'
python -m gbt_design_atlas run   --payload '{}'
```

Real `info` output from this machine:

```text
design_atlas  (creation)  v1.0.0
----------------------------------------
**设计与审美图鉴的口**（吞天吞来的外部手册 → 人话找到"该读哪一节"）。素材：`flash-hero/GOATED-UI-SKILL`（**MIT**）的 18 份手册（component-recipes / webgl-shaders-3d / interactions / scroll-gsap / motion-principles / typography / color-surfaces / page-transitions / text-effects / backgrounds-svg-canvas / layout-composition / css-modern / libraries / performance-a11y …）。常用说法：滚动驱动 / 视差 / 文字动画 / 缓动 / 弹簧 / 毛玻璃 / 渐变 / 阴影 / 粒子 / 过渡 / 悬停 / 英雄区 / 卡片 / 无障碍 / 性能 / 着色器 / 三维 / 排版 / 字体 / 配色 / 灵感来源。op=status/build/find/where：`build` 扫手册提 **recipe（标题+行号+摘要+代码语言）** 与 **来源条目（类别+名+URL）** 落 `store/design_atlas/index.jsonl`（只追加）；`find` 人话 → **哪份文件哪一节（`文件#L行号`）**，命中 0 就是 0。铁律：**只读 · 零执行**（绝不跑上游任何 `.mjs`）· **不改上游一个字节** · 摘要只取自该节正文。

gated      : False
external   : False
multi-op   : True
params     : (none)
values     : status, build, find, where
```

Wire a real implementation:

```python
from gbt_design_atlas import run

class MyBackend:
    name = "my-backend"
    def invoke(self, cap, payload):
        return {"cap": cap, "handled": sorted(payload)}

result = run({}, backend=MyBackend())
assert result.status == "ok"
```

## Parameters

| name | required | notes |
|---|---|---|
| — | no | the registry declares no required parameters |

Registry hint (`params_hint`): (empty)

**注册表登记的取值 / 子动作（4 个）**：`status`、`build`、`find`、`where`

Types are deliberately absent: the registry does not declare them, and an invented
type is worse than no type, because callers believe it.

## Boundaries

- Not gated: the registry marks this bit `safe: true`.
- No external service dependency declared.
- Multi-op (`multi_op: true`): several sub-actions share one name — read `op` before calling.
- No implementation ships here. Bring a backend; the protocol is one method.

## What this is not

Not a wrapper around a hosted API. Not a model. Not a promise that calling it does
anything on its own. It is the typed seam plus the validation, which is the part that
stays correct even when the implementation changes.

## Tests

```bash
python -m pytest
```

```text
20 passed, 3 skipped in 0.09s
```

## Provenance

| field | value |
|---|---|
| capability | `design_atlas` |
| domain | `creation` |
| handler | `design_atlas` |
| safe | `True` (gated = `False`) |
| external | `False` |
| atlas page | [creation/design_atlas](https://github.com/gbtweilai-star/gbt-caps/blob/main/caps/creation/design_atlas.md) |
| full index | [https://github.com/gbtweilai-star/gbt-caps](https://github.com/gbtweilai-star/gbt-caps) |

The parent README says 348 capabilities; an AST pass over the registry enumerates
`341 + 0 unimplemented + 0 disabled = 341`. The extra 7 are historical duplicates.
Numbering here follows 341 and matches the `gbt-caps` index one-to-one.

## License

MIT.
