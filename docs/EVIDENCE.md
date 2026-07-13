# Evidence Contract

This repository records an external-consumer-path check for EdgeFit. The
consumer repository, model, target, workflow and retained outputs are public,
but they remain controlled by the EdgeFit author.

## Pinned inputs

- EdgeFit source and Action: `e80591f5e95503142f40396e9706f41309023c90`
- EdgeFit Release: `v0.5.0-alpha.1`
- ONNX model generator: `onnx==1.22.0`
- Passing model SHA-256: `e34c98d323f0cb02eab4e396411a39c2300076ef23777a20200be30a1c50f95d`
- Target: the ORT Mobile CPU seed copied from the same EdgeFit release line

## Claims supported

- A repository other than EdgeFit can install the checksum-verified Release.
- The Composite Action accepts direct ONNX input from a pull request.
- Passing and deployment-blocking results preserve SARIF and Markdown evidence.
- A complete Action commit SHA works as the consumer pin.

## Hosted results

| Case | Model SHA-256 | Decision | Planned arena | Evidence |
| --- | --- | --- | ---: | --- |
| Passing reference | `e34c98d323f0cb02eab4e396411a39c2300076ef23777a20200be30a1c50f95d` | `pass` | 12,288 bytes | [run 29223576823](https://github.com/nya-a-cat/edgefit-action-demo/actions/runs/29223576823), artifact `8268978141` |
| Model-only regression | `b26ac527a1a2f9708e5eab50ed1e5c6c84ec6d9f69d0a41b6a7bfb4071c0967d` | `fail` / `EF0501` | 96,000,000 bytes | [run 29223712404](https://github.com/nya-a-cat/edgefit-action-demo/actions/runs/29223712404), artifact `8269022353` |

Both runs used the same 25,165,824-byte activation budget. PR #2 changed only
`models/model.onnx` and was closed without merging.

## Claims not supported

- Independent project adoption or independent maintainer feedback.
- ONNX Runtime execution, numeric inference or device compatibility.
- Real latency, arena high-water, power, temperature or accelerator behavior.
- Promotion of any target profile above `seed` confidence.
