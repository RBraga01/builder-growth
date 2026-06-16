---
name: campaign-brief-generator
description: Use before any campaign moves from strategy to execution. Transforms a growth strategy and offer into an executable brief — campaign objective, audience, offer, message, channel, creative requirements, landing destination, CTA, success metric, review gates, and launch checklist. Blocks "the team knows what we're going for" completions.
---

# Campaign Brief Generator

## The Law

```
A CAMPAIGN WITHOUT A BRIEF IS EXECUTED FROM MEMORY, AND MEMORY DIVERGES PER PERSON.
"The team knows what we're going for" means the copywriter, the designer, and the media buyer are each executing their own interpretation of a conversation, and the gaps between those interpretations show up as a campaign with three competing messages.
Objective + audience + offer + message + channel + creative requirements + landing destination + CTA + success metric + review gates + checklist IS an executable brief.
```

## When to Use

Trigger before:
- Any campaign moves from idea to creative production
- Briefing a copywriter, designer, or media buyer on a new campaign
- Repurposing an existing campaign for a new channel or segment
- Any time `growth-strategy-design`, `channel-selection-audit`, and `offer-quality-gate` have already produced their outputs and the work is ready to become an executable campaign

## When NOT to Use

- Ongoing always-on content with no discrete campaign structure (use the relevant content or editorial process instead)
- Minor creative refreshes of an already-briefed, still-running campaign (update the existing brief instead of generating a new one)

## The Eleven Brief Elements

A complete brief defines all eleven. A brief missing any one leaves a decision to be made independently by whoever executes that part of the campaign.

### 1 — Campaign Objective

The single result this campaign is meant to produce, tied to a `growth-metrics-design` output metric. One objective — a campaign briefed for "awareness and conversions and retention" gets executed as three different campaigns by three different people.

### 2 — Target Audience

The specific segment this campaign speaks to — from the strategy, possibly narrowed for this specific campaign.

### 3 — Offer

The validated offer from `offer-quality-gate` this campaign promotes. The brief does not redefine the offer — it references it.

### 4 — Message

The core message in one sentence, derived from the offer's promised outcome and validated by `positioning-audit` and `copy-quality-gate` before the brief is finalised.

### 5 — Channel

The channel(s) this campaign runs on, from `channel-selection-audit`, with channel-specific format requirements (e.g., a paid social campaign needs different asset dimensions than an email sequence).

### 6 — Creative Requirements

The specific assets needed: formats, dimensions, length limits, brand constraints, required elements (logo, disclaimer, CTA button). Specific enough that a designer or copywriter does not have to guess.

### 7 — Landing Destination

Where the campaign sends traffic, and what that destination must contain to deliver on the campaign's message (message match between ad and landing page is required, not optional).

### 8 — CTA

The single action the campaign drives toward — matching the offer's CTA, not a different one invented for this channel.

### 9 — Success Metric

The specific metric and target this campaign is evaluated against, from `growth-metrics-design`. Not "see how it does" — a number with a baseline.

### 10 — Review Gates

The checkpoints before launch where the campaign is reviewed against builder-growth skill gates: positioning, copy quality, AI messaging (if applicable), social proof, and pricing (if applicable).

### 11 — Launch Checklist

The final pre-launch checklist: assets approved, tracking instrumented, landing page live and tested, budget approved, stakeholders notified.

## The Process

### Step 1 — Confirm the Objective

One objective, tied to a named output metric.

### Step 2 — Pull Audience and Offer

Reference the strategy and offer documents directly — do not redefine them in the brief.

### Step 3 — Write the Core Message

One sentence. Run it through `positioning-audit` and `copy-quality-gate` if not already validated.

### Step 4 — Confirm Channel and Format

Pull from `channel-selection-audit`. Specify exact format requirements per channel.

### Step 5 — Define Creative Requirements

List every asset needed with specs precise enough to execute without follow-up questions.

### Step 6 — Confirm the Landing Destination

Verify message match between the campaign and the destination. If the destination doesn't exist yet or doesn't match, flag it as a blocker.

### Step 7 — Confirm the CTA

Match it to the offer's single CTA.

### Step 8 — Set the Success Metric

Pull from `growth-metrics-design`, with baseline and target.

### Step 9 — Schedule Review Gates

List which skill gates this campaign must pass before launch, and when each review happens in the timeline.

### Step 10 — Write the Launch Checklist

Final pre-launch items, each with an owner.

### Step 11 — Store the Brief

Store at `growth/campaigns/<campaign>-brief-<date>.md`.

## Rationalization Red Flags

These thoughts mean the brief was not written — stop:

- *"The team knows what we're going for"* — every person on the team has a slightly different mental model of "what we're going for"; the brief is what makes those models match
- *"We don't need creative requirements, the designer will figure it out"* — a designer without specs produces something, but whether it matches the channel's actual format requirements is luck, not design
- *"The landing page is close enough to the message"* — "close enough" message mismatch between ad and landing page is one of the most common, most fixable causes of high cost-per-click and low conversion; match them exactly or change one of them
- *"We'll figure out the success metric after we see the results"* — see `growth-metrics-design`: a metric defined after the results come in is chosen to match whatever happened
- *"Review gates will slow us down"* — a campaign that skips review gates and ships an unsourced claim or an undefined audience is slower than one that passes review once, because the unreviewed version gets pulled and redone after it underperforms or causes a complaint

## Completion Statement Format

When campaign-brief-generator is satisfied, state it like this:

```
Campaign brief complete.
File: growth/campaigns/<campaign>-brief-<date>.md ✓

Objective: [single result] — tied to metric: [output metric] ✓
Audience: [segment] ✓
Offer: [offer, from offer-quality-gate] ✓
Message: "[one sentence]" — positioning-audit ✓ / copy-quality-gate ✓

Channel: [channel(s), from channel-selection-audit] ✓
Creative requirements: <N assets> — specs defined ✓
Landing destination: [URL/page] — message match confirmed ✓
CTA: [single action, matches offer] ✓

Success metric: [metric] — baseline: <X>, target: <Y> ✓

Review gates scheduled: [positioning-audit / copy-quality-gate / ai-messaging-review / social-proof-review / pricing-page-review — as applicable] ✓
Launch checklist: <N items> — all owned ✓
```

A brief with no success metric or no scheduled review gates fails this gate.

## Why This Matters

The gap between a growth strategy and a shipped campaign is where most of the actual divergence happens — not because the strategy was wrong, but because the people executing it each filled the gaps in the brief with their own assumptions. A complete brief removes the gaps before execution starts, so the campaign that ships is the campaign that was strategized, not a committee's average interpretation of a hallway conversation.
