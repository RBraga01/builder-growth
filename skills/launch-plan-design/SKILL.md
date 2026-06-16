---
name: launch-plan-design
description: Use before launching any approved project, product, feature, or campaign externally. Requires launch goal, audience, offer, assets, channels, timeline, pre-launch and launch-day tasks, post-launch follow-up, success metrics, risks, and rollback criteria to be defined before launch day. Blocks "we'll figure out launch day as we go" completions.
---

# Launch Plan Design

## The Law

```
A LAUNCH WITHOUT A ROLLBACK CRITERION IS A COMMITMENT, NOT A TEST.
"We'll figure out launch day as we go" means the first time anyone decides what "going badly" looks like is in the middle of it going badly.
Goal + audience + offer + assets + channels + timeline + pre/launch/post tasks + metrics + risks + rollback criteria IS a launch plan.
```

## When to Use

Trigger before:
- Launching any new product, feature, or campaign to an external audience
- Re-launching after a significant pause, rebrand, or pivot
- Any coordinated multi-channel push (PR, paid, social, email, partners) with a fixed go-live date
- Any time `growth-strategy-design` and `offer-quality-gate` have produced an approved strategy and offer that now need a go-to-market plan

## When NOT to Use

- Continuous, ungated rollouts with no fixed launch moment (e.g., gradual feature flag rollout with no external announcement)
- Internal-only releases with no external audience or campaign attached

## The Twelve Launch Elements

A complete launch plan defines all twelve before launch day, not during it.

### 1 — Launch Goal

The single outcome this launch is meant to produce — tied to the north star metric from `growth-strategy-design`. One goal; a launch optimising for press coverage, signups, and revenue simultaneously will not be evaluated cleanly against any of them.

### 2 — Audience

Who this launch reaches first — typically the segment from the strategy, possibly narrowed further for a phased rollout.

### 3 — Offer

The validated offer from `offer-quality-gate` this launch is built around.

### 4 — Launch Assets

Every asset required: landing page, demo video, press kit, social posts, email sequence, sales collateral. Named and owned, not assumed to "come together."

### 5 — Channels

The channels this launch will use, from `channel-selection-audit` — primary and any secondary channels activated specifically for launch (e.g., a one-time press push that is not an ongoing channel).

### 6 — Timeline

Dated milestones from kickoff to launch day to the post-launch review. Specific dates, not "soon" or "next quarter."

### 7 — Pre-Launch Tasks

Everything that must be true before launch day: assets finished and reviewed, tracking instrumented, team briefed, support prepared for volume, legal/compliance cleared if applicable.

### 8 — Launch Day Tasks

The sequence of actions on launch day itself, with named owners and times: who publishes what, when, and what is monitored in real time.

### 9 — Post-Launch Follow-Up

What happens in the days and weeks after launch day: thank-you sequences, retargeting, sales follow-up on inbound leads, content amplification.

### 10 — Success Metrics

The specific metrics that determine whether the launch worked, with baselines and targets — feeding from `growth-metrics-design`.

### 11 — Risks

What could go wrong: traffic spike the infrastructure can't handle, a channel partner falling through, a competitor launching the same week, negative reception. Named with a mitigation or an accepted-risk note.

### 12 — Rollback or Pause Criteria

The specific conditions under which the launch is paused, rolled back, or the messaging is pulled — decided before launch day, not during the moment it might be needed.

**Rule:** "We'll know it if something goes wrong" is not a rollback criterion. A rollback criterion names a metric and a threshold: "If error rate exceeds 5% in the first hour, pause new signups and investigate."

## The Process

### Step 1 — Confirm the Launch Goal

One goal, tied to the strategy's north star metric.

### Step 2 — Confirm Audience and Offer

Pull directly from the approved strategy and offer gate — do not redefine them here.

### Step 3 — List and Assign Launch Assets

Every asset, with an owner and a due date ahead of launch day.

### Step 4 — Confirm Channels and Sequencing

Which channels fire when, from `channel-selection-audit`. Sequence channels so early signal from fast channels can inform slower ones if there's still time.

### Step 5 — Build the Timeline

Dated milestones, working backward from launch day.

### Step 6 — Write Pre-Launch and Launch-Day Task Lists

Specific tasks, owners, and times. No task without an owner.

### Step 7 — Write the Post-Launch Follow-Up Plan

What happens in the week after, and who runs it.

### Step 8 — Set Success Metrics

Pull from `growth-metrics-design`, or define them here if metrics design has not yet run.

### Step 9 — Name the Risks

List the realistic risks and their mitigations.

### Step 10 — Write the Rollback or Pause Criteria

Specific metric and threshold, decided in advance.

### Step 11 — Store the Launch Plan

Store at `growth/launches/<project>-launch-plan-<date>.md`.

## Rationalization Red Flags

These thoughts mean the launch was not planned — stop:

- *"We'll figure out launch day as we go"* — launch day is the worst time to improvise task ownership; whoever is available, not whoever should be doing it, ends up doing the critical task
- *"We don't need a rollback plan, it's going to go well"* — the rollback plan is what prevents a bad first hour from becoming a bad first week; it costs nothing to write and is never needed when things go well
- *"Success metrics will be obvious from the results"* — metrics defined after the results come in are chosen to match whatever happened, which makes every launch retroactively a success
- *"The team knows what to do"* — "the team knows" produces three people independently deciding to post the announcement at different times with different messaging
- *"We don't have time for a full launch plan, we need to move fast"* — a launch with no asset owners, no timeline, and no rollback criteria moves fast toward an outcome nobody is evaluating against anything

## Completion Statement Format

When launch-plan-design is satisfied, state it like this:

```
Launch plan complete.
File: growth/launches/<project>-launch-plan-<date>.md ✓

Launch goal: [single outcome] — tied to north star: [metric] ✓
Audience: [segment, from strategy] ✓
Offer: [offer, from offer-quality-gate] ✓

Launch assets: <N> — all owned and dated ✓
Channels: [primary + secondary, from channel-selection-audit] ✓
Timeline: kickoff [date] → launch [date] → post-launch review [date] ✓

Pre-launch tasks: <N> — all assigned ✓
Launch-day tasks: <N> — sequenced with owners and times ✓
Post-launch follow-up: [plan summary] — owner: [name] ✓

Success metrics: [metric(s)] — baseline: <X>, target: <Y> ✓
Risks: <N> named — each with mitigation or accepted-risk note ✓
Rollback/pause criteria: [metric] exceeds/falls below [threshold] → [action] ✓
```

A launch plan with no rollback criterion or no owner on launch-day tasks fails this gate.

## Why This Matters

Launches fail in two ways: the offer or channel was wrong (caught earlier, by `offer-quality-gate` and `channel-selection-audit`), or the execution was uncoordinated — assets missing, no one owning launch day, no agreed signal for when to pause. The second failure mode is entirely preventable and has nothing to do with whether the underlying strategy was sound. A launch plan turns a high-stakes, one-time event into a checklist that can be executed by anyone on the team, and gives everyone — including leadership — a pre-agreed answer to "is this working" instead of a debate that happens in the moment, under pressure, with the loudest voice winning.
