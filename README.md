# EdgeFit Action Reference Consumer

This repository exercises the published
[`nya-a-cat/edgefit`](https://github.com/nya-a-cat/edgefit) Composite Action from
outside the EdgeFit source repository. It installs the verified
`v0.5.0-alpha.1` Release binary and checks a committed ONNX model against a
committed target profile.

This repository is maintained by the EdgeFit author. It proves the external
distribution and pull-request integration path; it is **not** evidence of
independent adoption, device execution, or hardware measurement.

## Copy the workflow

Copy [`.github/workflows/edgefit.yml`](.github/workflows/edgefit.yml), then
replace these two paths:

```yaml
with:
  model: models/model.onnx
  target: targets/ort-mobile-cpu.yaml
```

The example pins EdgeFit to the complete source commit for
`v0.5.0-alpha.1`:

```yaml
uses: nya-a-cat/edgefit@e80591f5e95503142f40396e9706f41309023c90
```

The workflow writes `edgefit.sarif`, publishes `edgefit-summary.md` to the job
summary, uploads both files as a retained artifact, and restores EdgeFit's
exit status after publishing the evidence.

## Hosted evidence

| Path | Expected result | Evidence |
| --- | --- | --- |
| Reference model | Pass | [PR #1](https://github.com/nya-a-cat/edgefit-action-demo/pull/1) |
| Larger-shape model with the same graph and target | Activation-budget failure | [PR #2](https://github.com/nya-a-cat/edgefit-action-demo/pull/2) |

The failure changes only the committed model shape. The target profile remains
unchanged, so the result demonstrates a model-budget regression instead of a
configuration change.

## Fixture provenance

`models/model.onnx` is generated from the small, reviewable script in
[`tools/generate_model.py`](tools/generate_model.py). To reproduce either
fixture with ONNX 1.22.0:

```bash
uv run --with onnx==1.22.0 tools/generate_model.py \
  --case pass \
  --out models/model.onnx
```

Use `--case over-budget` to reproduce the intentionally failing PR fixture.

## Evidence boundary

```text
Reference consumer integration: verified by hosted pull-request runs
Independent adoption: not observed
Runtime reference: pinned seed profile and ONNX adapter
Hardware measurement: none
Deployment budgets: seed assumptions
```
