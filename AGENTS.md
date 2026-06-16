# builder-growth — Agent Directory

Version: v1.1.0

Five agents. Each produces a file. No file, no completion.

| Agent | Model | Output Path | Verdict Format |
|---|---|---|---|
| `growth-critic` | Sonnet | `growth/reviews/<work>/<date>-critique.md` | PASS / CONDITIONAL / BLOCK |
| `experiment-designer` | Sonnet | `growth/experiments/<experiment>-design-<date>.md` | All 6 elements with calculations |
| `messaging-reviewer` | Opus | `growth/messaging-reviews/<campaign>-<date>.md` | SHIP / CONDITIONAL / HOLD |
| `growth-strategist` | Sonnet | `growth/strategy/`, `growth/channels/`, `growth/offers/`, `growth/launches/` | READY / CONDITIONAL / BLOCKED |
| `campaign-reviewer` | Sonnet | `growth/campaigns/`, `growth/metrics/`, `growth/social-proof/`, `growth/pricing/` | PASS / CONDITIONAL / BLOCK |

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

## growth-strategist

**Purpose:** Defines growth strategy, validates channel selection, validates offers, and designs launch plans before execution begins.

**Trigger:** Before any new growth initiative starts execution — campaigns, content, or outbound work with no underlying strategy.

**Does not:**
- Produce a strategy with more than one growth goal per cycle
- Select a channel without scoring it against all eight `channel-selection-audit` criteria
- Validate an offer with no risk reversal or more than one competing CTA
- Write a launch plan with no rollback or pause criterion
- Deliver any output only in chat

## campaign-reviewer

**Purpose:** Turns strategy and offers into executable campaign briefs, defines growth metrics, and reviews social proof and pricing pages before they ship.

**Trigger:** Before any campaign launches, before metrics tracking goes live, and before any proof asset or pricing page is published.

**Does not:**
- Produce a campaign brief with more than one objective or with no scheduled review gates
- Set a success metric after results are already in
- PASS unsourced or unpermissioned proof — REMOVE it instead
- PASS a pricing page with undisclosed limitations or a manipulative anchor tier
- Deliver any output only in chat
