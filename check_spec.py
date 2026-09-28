# -*- coding: utf-8 -*-
"""规范自检：把一批 JMESPath 表达式跑在样例文档上，逐个比对结果。
全过退出码 0；有不过的打印「不过」并退出码 1。"""
import json
import sys

sys.path.insert(0, ".")
import jmespath  # noqa: E402

DOC = {
    "a": [1, 2, 3, 4, 5],
    "s": "hello",
    "objs": [{"n": 3, "t": "x"}, {"n": 1, "t": "y"}, {"n": 2, "t": "z"}],
    "nested": [[1, 2], [3], []],
    "flag": True,
}

CASES = [
    ("普通下标", "a[0]", 1),
    ("普通区间", "a[1:3]", [2, 3]),
    ("省起点", "a[:2]", [1, 2]),
    ("倒序切片", "a[::-1]", [5, 4, 3, 2, 1]),
    ("步长二", "a[::2]", [1, 3, 5]),
    ("倒序步长二", "a[::-2]", [5, 3, 1]),
    ("带界倒序", "a[4:0:-1]", [5, 4, 3, 2]),
    ("投影取字段", "objs[*].n", [3, 1, 2]),
    ("管道后倒序", "objs[*].n | [::-1]", [2, 1, 3]),
    ("过滤投影", "objs[?n > `1`].t", ["x", "z"]),
    ("展平", "nested[]", [1, 2, 3]),
    ("管道", "objs[*].n | [0]", 3),
    ("多选哈希", "{first: a[0], last: a[-1]}", {"first": 1, "last": 5}),
    ("取长度", "length(a)", 5),
    ("排序", "sort_by(objs, &n)[*].t", ["y", "z", "x"]),
    ("最大值", "max(a)", 5),
    ("非表达式", "!flag", False),
    ("字面量比较", "s == 'hello'", True),
    ("切片后取长度", "a[::-1] | length(@)", 5),
]


def main():
    bad = 0
    for label, expr, want in CASES:
        try:
            got = jmespath.search(expr, DOC)
        except Exception as error:  # noqa: BLE001
            got = "报错:" + str(error)[:40]
        if got == want:
            print("通过", label, "=", json.dumps(got, ensure_ascii=False))
        else:
            bad += 1
            print("不过", label, "期望", json.dumps(want, ensure_ascii=False),
                  "实际", json.dumps(got, ensure_ascii=False, default=str))
    print("用例 %d/%d 通过" % (len(CASES) - bad, len(CASES)))
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
