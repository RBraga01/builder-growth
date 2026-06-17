---
name: growth-strategy-design
description: Use before any copy, campaign, or experiment work begins on a new project or growth initiative. Requires growth stage, target segment, growth goal, primary constraint, channel hypothesis, core offer, north star metric, a 90-day hypothesis, and named risks to be defined before any execution starts. Blocks "let's just start running campaigns" completions.
---

# Growth Strategy Design

## The Law

```
EXECUTION WITHOUT A STRATEGY OPTIMISES RANDOM SURFACES.
"Let's just start running campaigns" produces copy, channels, and experiments chosen by who is in the room that week, not by what the growth stage and constraint actually require.
Stage + segment + goal + constraint + channel hypothesis + offer + north star + 90-day hypothesis + risks IS a growth strategy.
```

## When to Use

Trigger before:
- Starting growth work on any new project, product, or market segment
- Restarting growth work after a pivot, a stalled funnel, or a leadership change in growth goals
- Allocating budget or headcount to growth for the next quarter
- Any work that would otherwise begin with `channel-selection-audit`, `campaign-brief-generator`, or `launch-plan-design` without an underlying strategy to reference

## When NOT to Use

- Single isolated copy or campaign requests inside an already-defined strategy — reference the existing strategy document instead of rewriting it
- Pure execution tasks (sending a campaign, fixing a funnel leak) where the strategy is already approved and unchanged
- Internal tooling or features with no external growth surface

## The Ten Strategy Elements

A complete strategy defines all ten. Missing any one means execution decisions get made ad hoc, by whoever is doing the work that week.

### 1 — Growth Stage

Name the stage honestly: pre-product-market-fit, early PMF, scaling, or mature/optimisation. The stage determines what "growth" even means right now.

**Rule:** Pre-PMF growth work is retention and qualitative signal, not acquisition volume. Scaling-stage growth work is channel efficiency, not channel discovery. Naming the wrong stage produces strategy built for a different company.

### 2 — Target Segment

The specific segment growth work serves right now — not the eventual total addressable market.

**Required specificity:** same bar as `positioning-audit` — role/persona, situation, current alternative. "Everyone who could use this" is not a segment.

### 3 — Growth Goal

One named goal for this strategy cycle: acquisition, activation, retention, revenue, or referral. One goal, not a list — a strategy that optimises for five things optimises for none.

### 4 — Primary Constraint

The single resource or condition most limiting growth right now: budget, team capacity, traffic volume, trust/credibility, product readiness, or sales cycle length.

**Test:** If this constraint were removed, would growth meaningfully accelerate? If not, it is not the primary constraint — keep looking.

### 5 — Primary Channel Hypothesis

The channel most likely to work given the segment, goal, and constraint — stated as a hypothesis, not a decision. Validated or rejected by `channel-selection-audit`.

### 6 — Secondary Channel Options

2–3 channels worth testing next if the primary hypothesis underperforms. Named now, not discovered later under pressure.

### 7 — Core Offer

The single offer growth work is built around right now (trial, demo, paid plan, lead magnet, waitlist). Validated by `offer-quality-gate` before any campaign references it.

### 8 — North Star Metric

The one metric that, if it moves, means the strategy is working. Feeds directly into `growth-metrics-design`.

### 9 — 90-Day Growth Hypothesis

One sentence: "If we focus on [segment] through [primary channel] with [offer], [north star metric] will move from [baseline] to [target] within 90 days, because [mechanism]." Time-boxed — strategies without an expiry date never get re-evaluated.

### 10 — Risks and Assumptions

Every assumption the strategy depends on, and what breaks the strategy if it's wrong. Untested assumptions are risks, not facts.

## The Process

### Step 1 — Name the Growth Stage

State the stage and the evidence for it (retention data, revenue, qualitative signal).

### Step 2 — Define the Target Segment

One sentence with role/situation/current alternative, matching the `positioning-audit` bar.

### Step 3 — Set the Growth Goal

One goal for this cycle. State what was deprioritised to focus on it.

### Step 4 — Identify the Primary Constraint

Apply the removal test. Name the constraint that, if relaxed, would most accelerate growth.

### Step 5 — Form the Channel Hypothesis

Name the primary channel hypothesis and 2–3 secondary options. Hand off to `channel-selection-audit` for validation.

### Step 6 — Confirm the Core Offer

Name the offer this cycle is built around. Hand off to `offer-quality-gate` if not yet validated.

### Step 7 — Set the North Star Metric

Name the metric and its current baseline. Hand off to `growth-metrics-design` for the full metrics tree.

### Step 8 — Write the 90-Day Hypothesis

One sentence, all parts: segment, channel, offer, metric, baseline, target, mechanism.

### Step 9 — List Risks and Assumptions

Every assumption the hypothesis depends on, and the impact if each one is wrong.

### Step 10 — Store the Strategy

Store at `growth/strategy/<project>-<date>.md`. All channel audits, offers, campaigns, and launches for this cycle reference this document.

## Rationalization Red Flags

These thoughts mean strategy was not done — stop:

- *"Let's just start running campaigns and see what works"* — "see what works" without a segment, channel hypothesis, or north star metric cannot distinguish a working campaign from a lucky one
- *"Our strategy is to grow"* — grow what, for whom, through which channel, limited by what? "Grow" is an objective, not a strategy
- *"We'll figure out the constraint as we go"* — the constraint determines which channels and offers are even viable; discovering it mid-execution means the first month of work was aimed at the wrong lever
- *"Our segment is anyone who might want this"* — broad segments produce strategies that try every channel and every offer at once, which is not a strategy, it is a budget without a plan
- *"We don't need a 90-day deadline, we'll know it when it works"* — strategies without an expiry date are never formally re-evaluated; they just quietly get abandoned for the next idea

## Completion Statement Format

When growth-strategy-design is satisfied, state it like this:

```
Growth strategy complete.
File: growth/strategy/<project>-<date>.md ✓

Growth stage: [pre-PMF / early PMF / scaling / mature] — evidence: [data/signal] ✓
Target segment: [role/situation] currently using [alternative] ✓
Growth goal: [acquisition / activation / retention / revenue / referral] — single goal ✓
Primary constraint: [resource/condition] — removal test confirmed ✓

Primary channel hypothesis: [channel] — pending channel-selection-audit
Secondary channel options: [2–3 channels named]

Core offer: [offer] — pending offer-quality-gate
North star metric: [metric] — baseline: <X>

90-day hypothesis: If we focus on [segment] through [channel] with [offer],
  [metric] will move from <baseline> to <target> within 90 days because [mechanism] ✓

Risks and assumptions: <N> listed, each with impact-if-wrong stated ✓

Next steps: channel-selection-audit, offer-quality-gate, growth-metrics-design ✓
```

A strategy with no named constraint or no expiry date on the hypothesis fails this gate.

## Why This Matters

Growth teams without a written strategy still make strategic decisions — they just make them implicitly, one campaign at a time, usually defaulting to whatever channel the most vocal person in the room prefers. Naming the stage, segment, goal, constraint, and hypothesis up front means every later skill — channel selection, offer validation, campaign briefs, launch plans — has something concrete to validate against instead of inventing its own assumptions. A strategy that turns out wrong in 90 days is a fast, cheap lesson. Three months of campaigns with no stated hypothesis is neither fast nor cheap, and nobody can say afterward what was actually being tested.
