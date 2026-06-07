---
name: retention-design
description: Use before launching any new feature or product. Requires the activation moment, habit loop, and reactivation path to be designed before launch. Blocks "users will come back if they like it" completions.
---

# Retention Design

## The Law

```
A FEATURE LAUNCHED WITHOUT A DESIGNED RETENTION LOOP IS A FEATURE DESIGNED TO CHURN.
"Users will come back if they like it" has no activation moment, no habit trigger, and no reactivation path — which describes every churned product, because users who liked it also forgot about it.
Activation moment + habit loop + reactivation path defined before launch IS retention design.
```

## When to Use

Trigger before:
- Launching any new product or significant new feature
- Redesigning an existing flow where D7 or D30 retention is below target
- Adding a feature whose primary value is realised over repeated sessions (not first use)
- Building any AI assistant, tool, or agent that requires habit formation

## When NOT to Use

- One-time-use features where the user's goal is fully completed in a single session (e.g., a one-time document export — retention is not the right metric)
- Features for internal tools where users are required to return (no voluntary retention decision being made)

## The Three Retention Elements

### 1 — Activation Moment

The specific action a user takes that predicts they will return.

Activation is not the first session. It is the moment in the first session when the user understands what the product can do for them — the "aha moment."

**How to find it:**
- Compare the behaviour of retained users (D30+) vs. churned users
- Find the action that is significantly overrepresented in retained users in the first session
- Verify causality vs. correlation: does encouraging new users to reach this action earlier improve D30?

**What it looks like:**
```
Slack: send your first message
Dropbox: put a file in a folder and access it from another device
GitHub Copilot: accept the first autocomplete suggestion
```

**Required in the design:**
- Name the activation action
- Measure how many new users reach it in the first session (baseline)
- Design the first-session flow to lead users to this action

### 2 — Habit Loop

The cue → routine → reward cycle that brings users back.

A habit loop is not an email reminder. It is a design pattern that creates an internal trigger — a situation in the user's life that makes them think of the product.

**Three components:**

**Cue (external or internal trigger):**
- External: notification, email, scheduled event, someone else's action
- Internal: a recurring situation in the user's work/life that the product addresses (e.g., "every time I need to review a document, I use this tool")

**Routine:**
- The action the user takes in response to the cue (open the product, do the key action)
- Must be simple enough to become automatic — if the routine requires significant effort, the habit doesn't form

**Reward:**
- The variable or fixed reward that reinforces the behaviour
- For productivity tools: task completion, saved time, or quality improvement
- For communication tools: response from others, social acknowledgment
- For AI features: a useful, surprising, or accurate output

**Design requirements:**
- Name the cue type (external notification / internal trigger)
- If external: define the notification (timing, content, frequency ceiling)
- If internal: define the use-case that creates the internal trigger
- Define the reward the user receives in each session

### 3 — Reactivation Path

What happens when a user misses the habit window?

Even well-designed habit loops produce lapsed users. Reactivation is the designed path back.

**Reactivation requires:**
- A lapse definition: what interval qualifies as "lapsed"? (e.g., no activity for 7 days)
- A reactivation trigger: what prompts the lapsed user to return? (email, push, in-app)
- Reactivation copy that reflects the user's gap (not generic "we miss you")
- A landing experience that reconnects the user to the activation moment (not the home screen)
- A reactivation metric: what % of lapsed users return within N days of the trigger?

**Reactivation is not a batch email sequence.** Batch sequences produce the same message to all lapsed users. Effective reactivation is personalised to what the user was doing, what they completed, or what has changed since they left.

## The Process

### Step 1 — Define the Activation Moment

Analyse retained vs. churned users or design the activation moment based on product understanding. Write: "The activation action is [X]. Target: [Y]% of new users reach it in the first session."

### Step 2 — Design the First-Session Flow

Map every step from landing to activation. Eliminate any step that does not lead toward the activation action.

### Step 3 — Design the Habit Loop

Name the cue, routine, and reward. Define the notification plan (if external cue) or the use-case articulation (if internal cue).

### Step 4 — Design the Reactivation Path

Define lapse, trigger, copy approach, landing experience, and reactivation metric.

### Step 5 — Define the Retention Metrics

North star: D30 retention rate. Diagnostics: first-session activation rate, D7 retention rate, reactivation rate. Set baselines and targets.

### Step 6 — Store the Retention Design

Store at `growth/retention/<feature>-design-<date>.md`.

## Rationalization Red Flags

These thoughts mean retention was not designed — stop:

- *"Users will come back if they like it"* — liking a product and habitual return are different; users who liked Vine also stopped using it; habit formation requires a loop, not just satisfaction
- *"We'll add retention features after launch"* — you will add them after the D7 data shows churn; the users who churned in the first 30 days are not coming back for the retention features; design before launch
- *"Notifications will handle retention"* — notifications are an external cue; an external cue only works if it triggers an internal desire; if the user has no internal motivation, notifications produce unsubscribes
- *"Our power users retained — the product works"* — power users retain without retention design; the design question is whether the median user retains; measure the median, not the tail
- *"We don't know the activation moment yet"* — then find it before launch by analysing analogous products or running qualitative sessions; launching without a defined activation moment means the first-session flow leads nowhere in particular

## Completion Statement Format

When retention-design is satisfied, state it like this:

```
Retention design complete.
File: growth/retention/<feature>-design-<date>.md ✓

Activation moment:
  Action: [specific action name] ✓
  Baseline: <X>% of new users reach it in session 1 (or "target: X%, currently unmeasured — tracking in scope") ✓
  First-session flow: designed to lead to activation, <N steps> ✓

Habit loop:
  Cue type: external (notification: [timing, content]) / internal (use-case: [description]) ✓
  Routine: [key action] ✓
  Reward: [task completion / social / AI output quality — described] ✓

Reactivation path:
  Lapse definition: [N days without activity] ✓
  Trigger: [email / push / in-app] ✓
  Copy approach: personalised to [user behaviour / completion state / product change] ✓
  Landing experience: [activation moment / last action / what's new] — not home screen ✓
  Reactivation metric: % of lapsed users return within [N days] of trigger ✓

Retention metrics:
  North star: D30 retention — baseline: <X>%, target: <Y>% ✓
  Diagnostics: first-session activation %, D7 retention %, reactivation % ✓
```

Retention metrics with no baseline are targets, not measurements. Activation moment with no first-session flow design is a label, not a design.

## Why This Matters

New user churn in the first 30 days is the primary growth leak for most products. Every user acquired who does not retain produces zero long-term revenue and raises CAC relative to LTV. The activation moment, habit loop, and reactivation path are not post-launch optimisations — they are the design decisions that determine whether the product works for the median user, not just the power user who would have retained regardless.
