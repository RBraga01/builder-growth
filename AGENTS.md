# builder-growth — Agent Directory

Version: v1.0.0

Three agents. Each produces a file. No file, no completion.

| Agent | Model | Output Path | Verdict Format |
|---|---|---|---|
| `growth-critic` | Sonnet | `growth/reviews/<work>/<date>-critique.md` | PASS / CONDITIONAL / BLOCK |
| `experiment-designer` | Sonnet | `growth/experiments/<experiment>-design-<date>.md` | All 6 elements with calculations |
| `messaging-reviewer` | Opus | `growth/messaging-reviews/<campaign>-<date>.md` | SHIP / CONDITIONAL / HOLD |

## growth-critic

**Purpose:** Audits positioning, copy, and experiment designs against all builder-growth skill gates before they ship.

**Trigger:** After any growth work is drafted, before it ships or traffic is split.

**Does not:**
- Suggest creative alternatives
- PASS positioning with a broad audience definition
- PASS an experiment without a calculated sample size
- PASS copy with unsourced quantified claims
- Deliver the critique only in chat

## experiment-designer

**Purpose:** Designs growth experiments with calculated sample size, duration, stopping rule, and decision rule.

**Trigger:** Before any A/B test on a growth surface is launched.

**Does not:**
- Calculate sample size against estimated baselines — asks for actual data
- Set open-ended stopping rules
- Design experiments with durations over 8 weeks without flagging feasibility
- Deliver the design only in chat

## messaging-reviewer

**Purpose:** Audits AI product messaging for sourced claims, scoped capability descriptions, and specific AI labels.

**Trigger:** Before any external AI capability claim ships.

**Does not:**
- PASS quantified claims with a promise of finding the source later
- Soften REMOVE items to REVISE
- Accept vague AI labels as "industry standard"
- Deliver the review only in chat
