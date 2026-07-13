"""生成 reference consumer 使用的最小 ONNX 模型。

该脚本只维护同一 Add 图的通过与超预算两种固定 shape，避免把模型生成
逻辑扩展成新的通用 CLI 或测试框架。
"""

from __future__ import annotations

import argparse
from pathlib import Path

import onnx
from onnx import TensorProto, helper


CASES = {
    "pass": [1, 1_024],
    "over-budget": [1, 8_000_000],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate the EdgeFit reference ONNX model.")
    parser.add_argument("--case", choices=sorted(CASES), required=True)
    parser.add_argument("--out", type=Path, required=True)
    return parser.parse_args()


def build_model(shape: list[int]) -> onnx.ModelProto:
    left = helper.make_tensor_value_info("left", TensorProto.FLOAT, shape)
    right = helper.make_tensor_value_info("right", TensorProto.FLOAT, shape)
    output = helper.make_tensor_value_info("sum", TensorProto.FLOAT, shape)
    node = helper.make_node("Add", ["left", "right"], ["sum"], name="add_reference")
    graph = helper.make_graph([node], "edgefit_reference_add", [left, right], [output])
    model = helper.make_model(
        graph,
        producer_name="edgefit-action-demo",
        opset_imports=[helper.make_opsetid("", 13)],
    )
    model.ir_version = min(model.ir_version, 10)
    onnx.checker.check_model(model)
    return model


def main() -> int:
    args = parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    onnx.save(build_model(CASES[args.case]), args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
