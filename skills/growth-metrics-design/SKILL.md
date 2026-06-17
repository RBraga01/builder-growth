---
name: growth-metrics-design
description: Use before executing any growth initiative — campaign, launch, or experiment. Requires north star metric, input/output metrics, leading/lagging indicators, activation/retention/conversion metrics, measurement cadence, minimum viable tracking, and a named owner per metric to be defined before execution starts. Blocks "we'll know growth is working when we see it" completions.
---

# Growth Metrics Design

## The Law

```
GROWTH WORK WITHOUT NAMED METRICS PRODUCES A STORY, NOT A RESULT.
"We'll know it's working when we see it" means success gets defined after the fact, by whoever is most invested in the work having worked.
North star + input/output metrics + leading/lagging indicators + activation/retention/conversion metrics + cadence + tracking + owners IS a metrics design.
```

## When to Use

Trigger before:
- Executing any growth strategy, campaign, launch, or experiment defined by other builder-growth skills
- Setting quarterly or monthly growth goals
- Any time leadership asks "how will we know this is working?" and the honest answer is "we'll see"
- Before `campaign-brief-generator` or `launch-plan-design` references a success metric that has not been formally defined

## When NOT to Use

- One-off internal analyses with no recurring tracking need
- Metrics already fully defined and tracked from a prior cycle with no change in strategy — reference the existing metrics document instead of redefining it

## The Eleven Metrics Elements

A complete metrics design defines all eleven. Skipping any one means part of the system runs on assumption instead of measurement.

### 1 — North Star Metric

The single metric, from `growth-strategy-design`, that represents whether the strategy is working overall. One number the whole team can rally around.

### 2 — Input Metrics

The metrics representing the activities the team controls directly: campaigns shipped, content published, outbound sent, experiments run. Inputs are leverage — they are what the team changes to move outputs.

### 3 — Output Metrics

The metrics representing results the team influences but does not fully control: signups, conversion rate, revenue. Outputs are what inputs are supposed to move.

**Rule:** Never set a target on an output metric without a connected input metric. A revenue target with no defined activity to hit it is a hope, not a plan.

### 4 — Leading Indicators

Metrics that move before the north star does, giving an early read on whether the current approach is working — e.g., activation rate as a leading indicator of D30 retention.

### 5 — Lagging Indicators

Metrics that confirm the result after enough time has passed — e.g., D90 retention, LTV, expansion revenue. Necessary for the real answer, but too slow to react to in-week.

### 6 — Activation Metric

The metric defined in `retention-design` representing the moment a new user gets real value. Tracked here as the leading indicator that connects acquisition work to retention outcomes.

### 7 — Retention Metric

The cohort retention rate (commonly D7/D30/D90) that determines whether acquired users stay. Connects directly to `retention-design`.

### 8 — Conversion Metric

The rate at which the target segment moves from one funnel stage to the next, especially into the paying or committed stage. Connects directly to `funnel-analysis`.

### 9 — Measurement Cadence

How often each metric is reviewed: daily, weekly, monthly. Input metrics and fast-moving leading indicators are usually reviewed more often than lagging indicators.

### 10 — Minimum Viable Tracking

What must be instrumented before execution starts — the smallest set of events, dashboards, or reports that make every metric above actually measurable. Not the full analytics wishlist — the minimum that prevents flying blind.

### 11 — Owner for Each Metric

The named person accountable for each metric moving. A metric with no owner gets reported on, not acted on.

## The Process

### Step 1 — Confirm the North Star

Pull from `growth-strategy-design`. If no strategy exists yet, define the north star here and feed it back into strategy.

### Step 2 — Map Inputs to Outputs

List the activities the team controls (inputs) and the results each is meant to move (outputs). Every output should have at least one connected input.

### Step 3 — Identify Leading and Lagging Indicators

For each output, name the metric that signals early (leading) and the metric that confirms late (lagging).

### Step 4 — Pull Activation, Retention, and Conversion Metrics

Reference `retention-design` and `funnel-analysis` outputs if they exist; define baseline targets here if they don't yet.

### Step 5 — Set Cadence Per Metric

Match review frequency to how fast the metric can realistically move and how fast the team can react.

### Step 6 — Define Minimum Viable Tracking

List the exact events, dashboards, or reports required. Flag any metric above that has no tracking path yet — that is a blocker, not a detail.

### Step 7 — Assign an Owner to Every Metric

One name per metric. "The team" is not an owner.

### Step 8 — Store the Metrics Design

Store at `growth/metrics/<project>-metrics-<date>.md`.

## Rationalization Red Flags

These thoughts mean metrics were not designed — stop:

- *"We'll know it's working when we see it"* — "see it" is a retrospective judgment call made by whoever is most invested in the outcome; it is not a metric
- *"Revenue is the only metric that matters"* — revenue is a lagging output with no input attached; by the time it moves, weeks of uninformed activity have already happened; leading indicators exist so the team can react before the lagging number confirms a problem
- *"Everyone on the team owns the metrics"* — shared ownership with no named individual means no one is accountable when a metric stalls; assign one owner, even if multiple people contribute
- *"We don't have the tracking in place yet, we'll add it later"* — executing without minimum viable tracking means the team cannot tell, even after the fact, whether the work moved anything; instrument before executing, not after
- *"We'll track everything to be safe"* — tracking everything with no prioritized minimum produces dashboards no one reviews; define the minimum that gets checked on the stated cadence, then expand

## Completion Statement Format

When growth-metrics-design is satisfied, state it like this:

```
Growth metrics design complete.
File: growth/metrics/<project>-metrics-<date>.md ✓

North star metric: [metric] — baseline: <X>, target: <Y> ✓

Input metrics: <N> — [list] ✓
Output metrics: <N> — [list], each mapped to ≥1 input ✓

Leading indicators: [list] ✓
Lagging indicators: [list] ✓

Activation metric: [metric] — baseline: <X>% (from retention-design or unmeasured) ✓
Retention metric: [D7/D30/D90 rate] — baseline: <X>% ✓
Conversion metric: [stage→stage rate] — baseline: <X>% (from funnel-analysis or unmeasured) ✓

Measurement cadence: [metric → daily/weekly/monthly mapping] ✓
Minimum viable tracking: <N> events/dashboards — all instrumented / <N> pending (blocker) ✓

Owners: <N of N> metrics have a named owner ✓
```

Any metric with no owner or no tracking path fails this gate.

## Why This Matters

Growth work without named metrics still gets evaluated — informally, after the fact, by whoever talks about it most persuasively. That evaluation is unfalsifiable: a campaign that didn't move the north star can always be defended as "building brand awareness" or "early innings." Naming the north star, the inputs that are supposed to move it, the leading indicators that give an early read, and an owner for each one converts growth work from a narrative into something that can actually be judged — and improved, because a metric with an owner and a cadence gets looked at again next week, not just in the retro nobody schedules.
