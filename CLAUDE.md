# builder-growth — Claude Configuration

## Pack Version

builder-growth — AI Growth Skills Pack v1.0.0

## File Conventions

| Artifact | Path |
|---|---|
| Positioning documents | `growth/positioning/<product>-<date>.md` |
| Copy reviews | `growth/copy-reviews/<campaign>-<date>.md` |
| Funnel analyses | `growth/funnel-analysis/<funnel>-<date>.md` |
| Experiment designs | `growth/experiments/<experiment>-design-<date>.md` |
| Retention designs | `growth/retention/<feature>-design-<date>.md` |
| Messaging reviews | `growth/messaging-reviews/<campaign>-<date>.md` |
| Growth critiques | `growth/reviews/<work>/<date>-critique.md` |

## Skill Trigger Sequence

For any growth initiative:

1. `positioning-audit` → before any copy is written
2. `copy-quality-gate` → before any external copy ships
3. `funnel-analysis` → before any CRO effort starts
4. `experiment-design` → before any A/B test runs
5. `retention-design` → before any feature launches
6. `ai-messaging-review` → before any AI product claim ships externally

## Agent Usage

| Agent | When to Use |
|---|---|
| `growth-critic` | After positioning, copy, or experiment designs are drafted, before they ship |
| `experiment-designer` | When designing any growth experiment |
| `messaging-reviewer` | Before any external AI capability claim ships |

## What Makes This Pack Different From Generic Growth Frameworks

Standard growth frameworks optimise. This pack diagnoses before optimising:
- Every funnel optimisation starts with a diagnosed root cause
- Every experiment has a calculated sample size and a pre-specified stopping rule
- Every AI capability claim has a source or is removed
- Every retention initiative defines the activation moment before launch

Optimising without diagnosing is the most expensive growth mistake. This pack blocks it.
