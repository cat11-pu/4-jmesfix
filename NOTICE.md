# 素材出处与改动说明

- `jmespath/` 取自开源项目 jmespath/jmespath.py（MIT），源码基本原样。
- 本次在 `jmespath/visitor.py` 里注入了一处缺陷：切片构造时丢掉了步长（普通切片看不出，只有带步长的切片会错）。
- `check_spec.py` 是本题新增的规范自检，作为验收标准。

上游许可与版权见 `LICENSE`。
