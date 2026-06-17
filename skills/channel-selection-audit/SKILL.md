---
name: channel-selection-audit
description: Use before building any campaign, content plan, or outbound motion. Scores every candidate growth channel against eight criteria — audience presence, intent, cost to test, feedback speed, trust requirement, sales cycle fit, operational complexity, and measurement feasibility — before one is chosen. Blocks "let's try everything" and "we picked the channel everyone else uses" completions.
---

# Channel Selection Audit

## The Law

```
A CHANNEL CHOSEN BY DEFAULT IS A CHANNEL CHOSEN WRONG.
"Let's try everything" splits a limited budget across channels with no comparable signal, so nothing gets enough volume to learn anything before the budget runs out.
"Everyone else uses paid ads" describes a competitor's constraint, not yours.
Every candidate channel scored against the same eight criteria IS channel selection.
```

## When to Use

Trigger before:
- Building a campaign, content calendar, or outbound sequence for a new segment or offer
- Reallocating growth budget across channels
- Entering a new market, segment, or product line where prior channel performance does not transfer
- Any time `growth-strategy-design` produced a channel hypothesis that has not yet been validated

## When NOT to Use

- Channels with an established, measured track record for this exact segment and offer — re-running the audit is redundant; review the existing data instead
- Single-channel constraints with no real alternative (e.g., a regulated industry where only one channel is compliant) — document the constraint instead of auditing alternatives that aren't available

## The Candidate Channels

Score the channels that are realistically available given the strategy's segment, offer, and constraint. Not every channel applies to every project.

```
SEO · content · outbound · paid ads · partnerships · community ·
marketplaces · referrals · social · product-led growth · sales-led growth
```

Do not score channels with no plausible audience overlap with the target segment — note them as "not applicable" and move on.

## The Eight Selection Criteria

Score each candidate channel 1–5 on every criterion. A channel that scores well on three criteria and poorly on the other five is not a strong channel — it is a channel with a narrow use case.

### 1 — Audience Presence

Is the target segment actually active on this channel, in measurable numbers? Presence without intent (browsing social media) scores lower than presence with intent (searching for a solution).

### 2 — Intent Level

How close is the audience, on this channel, to actively looking for a solution to the problem the offer solves? Outbound and SEO often score high; awareness-stage social scores lower.

### 3 — Cost to Test

What does it cost — in budget and time — to get a directional read on whether this channel works? Paid ads can be tested cheaply and fast; partnerships and SEO are slow and compounding.

### 4 — Speed of Feedback

How long until the channel produces a usable signal (not final results — a directional signal)? Outbound and paid ads can signal in days. SEO and community can take months.

### 5 — Trust Requirement

How much existing trust does this channel require before it converts? Cold outbound and paid ads require the offer to build trust in the moment. Referrals and community inherit trust from the referrer or group.

### 6 — Sales Cycle Fit

Does the channel's typical engagement window match the segment's actual decision timeline? A channel that delivers a lead in 2 minutes is wasted on a 6-month enterprise sales cycle if there is no nurture path.

### 7 — Operational Complexity

What does running this channel well require — team skills, tooling, ongoing maintenance? Score lower for channels requiring capabilities the team does not have and cannot acquire within the strategy's timeframe.

### 8 — Measurement Feasibility

Can this channel's contribution be isolated and measured, or does it only show up as unattributable lift? Channels that cannot be measured cannot be optimised — score them lower regardless of theoretical potential.

## The Process

### Step 1 — List Candidate Channels

Pull the primary and secondary hypotheses from `growth-strategy-design`. Add any other channel with plausible audience overlap.

### Step 2 — Score Each Channel

Score every candidate 1–5 against all eight criteria. Use real data where it exists; mark estimates explicitly as estimates.

```
| Channel    | Audience | Intent | Cost | Speed | Trust | Sales fit | Complexity | Measurable | Total |
|------------|----------|--------|------|-------|-------|-----------|------------|------------|-------|
| [channel]  | X        | X      | X    | X     | X     | X         | X          | X          | sum   |
```

### Step 3 — Weight by Constraint

Re-weight the totals against the primary constraint from the strategy. A budget-constrained project weights "cost to test" higher; a trust-constrained project weights "trust requirement" higher.

### Step 4 — Select Primary and Secondary Channels

Choose one primary channel (highest weighted score with sufficient audience presence) and 1–2 secondary channels to test next.

### Step 5 — Document the Rejected Channels

Name every channel considered and not chosen, with the specific criterion that ruled it out. This prevents the same channel from being re-proposed without new information.

### Step 6 — Store the Audit

Store at `growth/channels/<project>-channel-audit-<date>.md`.

## Rationalization Red Flags

These thoughts mean the audit was not done — stop:

- *"Let's try everything and see what sticks"* — every channel run with a fraction of the budget produces a fraction of the signal; none of them get enough volume to be conclusive, and the budget runs out before any channel proves itself
- *"This is the channel everyone in our space uses"* — a competitor's channel choice reflects their constraint and audience, not necessarily yours; copying the channel without copying the underlying fit produces worse-than-average results in someone else's strongest channel
- *"Paid ads are the obvious starting point"* — paid ads score well on speed but poorly on trust requirement and cost to test at scale; "obvious" is not one of the eight criteria
- *"We'll figure out measurement later"* — a channel that cannot be measured cannot be told apart from a channel that isn't working; investing in it before measurement is in place is investing blind
- *"Our sales cycle doesn't matter for channel choice"* — a channel that produces fast, low-intent leads against a long enterprise sales cycle produces leads that go cold before the cycle completes; sales cycle fit is not optional

## Completion Statement Format

When channel-selection-audit is satisfied, state it like this:

```
Channel selection audit complete.
File: growth/channels/<project>-channel-audit-<date>.md ✓

Candidate channels scored: <N>
Constraint weighting applied: [primary constraint from strategy] ✓

Scores (weighted):
  | Channel | Total (weighted) |
  | [ranked list] |

Primary channel selected: [channel] ✓
  Strongest criteria: [top 2–3 scoring criteria]
  Risk: [weakest criterion and mitigation]

Secondary channels: [1–2 channels] — queued for test after primary signal ✓

Rejected channels: <N> — each with the disqualifying criterion named ✓

Next step: campaign-brief-generator or launch-plan-design for [primary channel] ✓
```

A channel chosen without a documented score against all eight criteria fails this gate.

## Why This Matters

Channel choice made by habit or imitation puts a real budget behind an unvalidated assumption. The eight criteria force the same comparison every time, which means the choice can be defended, revisited, and learned from — instead of being a preference dressed up as a decision. Most channel failures are not channel failures; they are fit failures that a structured audit would have surfaced before the budget was spent.
