# jmesfix

仓库里是 JMESPath 的 Python 实现（取自 jmespath/jmespath.py，MIT）。有人报了个怪现象：
**普通的切片都对，带步长的切片（倒序、隔一个取一个）结果不对**。

## 跑验收

    python3 check_spec.py

通过率不是 100% 就说明还没修好；要全部通过（退出码 0）。

## 约束

- 修根因，不要只对某一个表达式打补丁；自检里的用例只是抽样，换个写法还得对。
- 不要改 `check_spec.py`（改它等于改验收）。
- 只用 Python 标准库。
