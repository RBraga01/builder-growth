---
name: experiment-design
description: Use before running any growth experiment — pricing test, copy variant, onboarding flow, feature gate — that will inform a ship/no-ship decision. All six elements must be defined before the test starts. Blocks "we'll run it for a while and see" completions.
---

# Experiment Design

## The Law

```
AN EXPERIMENT WITHOUT A STOPPING RULE IS NOT AN EXPERIMENT — IT IS A FEATURE WAITING FOR PERMISSION.
"We'll run it for a while and see" produces results that stop when the team wants them to stop — which is when they look good.
Hypothesis + metric + sample size + duration + stopping rule + decision rule IS an experiment.
```

## When to Use

Trigger before:
- Any A/B test on a growth surface (landing page, pricing, onboarding, email, activation flow)
- Any feature gate experiment where one group sees a different experience
- Any pricing or packaging test
- Any content variant test that informs a product or copy decision

## When NOT to Use

- Qualitative research sessions (no control group, no statistical inference — use `user-research-synthesis`)
- Shadow mode deployments monitoring for regressions (not an experiment — monitoring)
- Product A/B tests covered by `ab-test-design` in builder-product (use that skill for product features; use this skill for growth surfaces)

## The Six Required Elements

Growth experiments share the same statistical requirements as product experiments. The difference is in the metrics and what "conversion" means.

### 1 — Hypothesis

One sentence with four parts: change, metric, direction + magnitude, mechanism.

```
If we [specific change to the control experience],
then [primary conversion metric] will [increase/decrease] by at least [MDE]%,
because [causal mechanism — why this change affects this metric].
```

The mechanism matters for learning. If the test result matches the hypothesis but the mechanism was wrong, you cannot predict whether the same change will work elsewhere.

### 2 — Primary Metric

The single metric that determines ship or no-ship.

**Growth-specific metric types:**
- **Acquisition**: signup rate, trial start rate, demo request rate
- **Activation**: completion of first key action, feature adoption rate
- **Retention**: D7, D30, D90 retention, churn rate
- **Revenue**: conversion to paid, ARPU, LTV (longer test duration required)
- **Referral**: invite rate, viral coefficient

One primary metric per experiment. Multiple primary metrics require multiple experiments or Bonferroni correction — which you are not doing.

### 3 — Sample Size

Calculate using your primary metric's baseline rate, the MDE, statistical power (80% standard; 90% for revenue decisions), and α = 0.05.

```
Baseline rate: X% (from last 30 days of data)
MDE: Y% relative (minimum improvement worth shipping)
Power: 80%
α: 0.05

Required sample per variant: N
```

If calculating manually: use the formula for two-proportion z-test. Otherwise use a validated power calculator with these exact inputs — not defaults.

### 4 — Duration

= required sample size ÷ daily eligible traffic, rounded up to complete weeks.

**Growth-specific rules:**
- Minimum 2 weeks — growth surfaces are more seasonally affected than product surfaces (weekly + monthly cycles)
- If the primary metric is retention (D7+): the test must run long enough for the cohort to reach the retention measurement point
- Maximum 8 weeks — beyond this, the external environment changes enough to contaminate results

### 5 — Stopping Rule

When you stop, and what makes you stop early.

```
Fixed: stop after [N days], regardless of interim results.
Early stop (optional): stop if p < 0.001 AND sample ≥ 80% of target
  — applies only with pre-specified sequential testing plan
Interim looks: [none / at 50% and 100% of target] — no open-ended checking
```

Peeking at results and stopping when p < 0.05 produces a real false positive rate of approximately 0.23 at 5 checks, not 0.05.

### 6 — Decision Rule

What you do with each possible result, defined before the test:

```
Ship: primary metric ↑ ≥ MDE at p < 0.05, no guardrail breached
No-ship: flat or negative at full duration
Guardrail breached: investigate — do not ship without understanding the trade-off
Insufficient power: extend or redesign — do not interpret underpowered results
```

"We'll look at the data together and decide" is not a decision rule.

## The Process

### Step 1 — Write the Hypothesis

One sentence, all four parts. Run it through `funnel-analysis` or `positioning-audit` first if the hypothesis is about a diagnosed leak or a messaging test.

### Step 2 — Choose and Define the Primary Metric

Name it, verify the baseline (last 30 days), and confirm it can be measured within the test duration.

### Step 3 — Calculate Sample Size

With actual baseline data. Document the inputs — baseline rate, MDE, power, α. If the result requires more traffic than available in 8 weeks, revise the MDE or find a higher-traffic surface.

### Step 4 — Set Duration

Sample size ÷ daily traffic. Round up to full weeks. Check against retention measurement requirements.

### Step 5 — Write the Stopping Rule

Fixed duration. Optional early-stop criteria with conservative threshold.

### Step 6 — Write the Decision Rule

All four outcomes mapped.

### Step 7 — Store the Experiment Design

Store at `growth/experiments/<experiment>-design-<date>.md` before any traffic is split.

## Rationalization Red Flags

These thoughts mean the experiment is not designed — stop:

- *"We'll run it for a while and see"* — "a while" stops when the result looks good; looked-good results are often noise that passed a peeked significance test
- *"Let's test it on a small audience first"* — a small audience produces an underpowered result; an underpowered result cannot inform a decision; label it a smoke test, not an experiment
- *"The effect will be obvious if it works"* — "obvious" effects are detectable with adequate sample size; if the effect is not obvious, the experiment was run too small to see it
- *"We're in a hurry — can we shorten the test?"* — shortening the duration produces an underpowered result or a peeked result; neither is actionable; a 2-week experiment that produces a valid result is faster than a 3-day test that produces an inconclusive one
- *"Revenue tests take too long"* — revenue tests require longer durations to reach the retention measurement point; run them; an underpowered revenue test will show you a result that confuses future planning

## Completion Statement Format

When experiment-design is satisfied, state it like this:

```
Experiment designed.
File: growth/experiments/<experiment>-design-<date>.md ✓

Hypothesis: If [change], then [metric] will [direction] by [MDE] because [mechanism] ✓
Primary metric: [name] — baseline: X% (from [source], last 30 days) ✓
Guardrails: <N metrics with tolerance thresholds>

Sample size: <N per variant> — inputs: baseline X%, MDE Y%, power 80%, α 0.05 ✓
Duration: <N days> = <sample> ÷ <daily traffic: M> ✓
  [Minimum 14 days / within 8-week maximum ✓]
  [Retention check: measurement point reached within test duration ✓]

Stopping rule: fixed at <N days>; early stop at p < 0.001 if ≥ 80% sample ✓
Decision rule:
  Ship: ≥ MDE, p < 0.05, no guardrail breach ✓
  No-ship: flat/negative at full duration ✓
  Guardrail breach: investigate ✓
  Insufficient power: extend or redesign ✓
```

Sample size must be calculated, not estimated. Duration must be computed, not guessed.

## Why This Matters

Growth experiments that stop when they look good produce a library of "successful" tests with no cumulative impact. The reason is false positives from peeking — each stopped-when-good result has a higher-than-nominal false positive rate, so the experiments that shipped produced no real effect. An experiment designed to the standard above produces a result you can act on — and learn from when the mechanism prediction is right or wrong.
