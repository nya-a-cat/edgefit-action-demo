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

## Claims not supported

- Independent project adoption or independent maintainer feedback.
- ONNX Runtime execution, numeric inference or device compatibility.
- Real latency, arena high-water, power, temperature or accelerator behavior.
- Promotion of any target profile above `seed` confidence.
