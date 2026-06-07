---
name: funnel-analysis
description: Use before beginning any conversion rate optimisation effort. Requires the leak to be identified and root-caused before any solution is proposed. Blocks "let's improve our conversion rate" without knowing which step breaks.
---

# Funnel Analysis

## The Law

```
OPTIMISING A FUNNEL BEFORE DIAGNOSING IT OPTIMISES THE WRONG STEP.
"Let's improve the conversion rate" without identifying which step leaks most is guessing — you can improve every step but the broken one and the funnel does not move.
Leak identified + root-caused + hypothesis formed IS a funnel analysis.
```

## When to Use

Trigger before:
- Any CRO (conversion rate optimisation) effort
- Proposing any experiment targeting funnel improvement
- Allocating engineering or design time to "improve" any multi-step flow
- Presenting funnel performance to stakeholders

## When NOT to Use

- Single-step actions with no funnel (e.g., a standalone API call — no steps to diagnose)
- Features in pre-launch without traffic data to analyse

## The Four Diagnostic Steps

Do not propose solutions before completing all four.

### Step 1 — Map the Funnel

List every step between the user's entry point and the conversion goal.

```
Step 1: [Action] — e.g., "User arrives on landing page"
Step 2: [Action] — e.g., "User clicks CTA"
Step 3: [Action] — e.g., "User completes signup form"
Step 4: [Action] — e.g., "User activates (completes first key action)"
Goal:   [Conversion] — e.g., "User converts to paid"
```

Use the product's actual steps — not a generic template. Every step must be measurable.

### Step 2 — Quantify Each Step

For each step, collect:
- **Volume**: how many users enter this step per period
- **Exit rate**: percentage who leave without completing this step
- **Time in step**: median and p95 time spent before exit

```
| Step | Entered | Completed | Exit rate | Median time |
|------|---------|-----------|-----------|-------------|
| 1    | 10,000  | 8,100     | 19%       | 2s          |
| 2    | 8,100   | 2,430     | 70%       | 45s         |
| 3    | 2,430   | 2,070     | 15%       | 3min        |
| 4    | 2,070   | 830       | 60%       | 12h         |
```

The step with the highest exit rate AND the highest volume of exits (exits = entered × exit rate) is the primary leak. Both dimensions matter — a 70% exit rate on 100 users is smaller than a 20% exit rate on 10,000.

### Step 3 — Root-Cause the Primary Leak

Finding the leak step is not the analysis. Understanding why users leave is.

**Root cause methods:**
- **Session recordings**: watch users exit; what were they doing at the moment they left?
- **Exit surveys**: ask users who did not complete the step; "What stopped you?"
- **Heatmaps**: where do users click, scroll, and hover before exit?
- **Error logs**: are exits correlated with errors, slow load times, or validation failures?
- **Segmentation**: does the exit rate differ by device, traffic source, user segment, or A/B variant?

Document the root cause explicitly. "Users drop off at step 2" is not a root cause. "Users arrive at step 2, attempt to complete the form on mobile, encounter a keyboard overlap that hides the submit button, and exit within 8 seconds" is a root cause.

### Step 4 — Form a Testable Hypothesis

One hypothesis per root cause, in the form:

> If we [specific change], then the [step N] exit rate will decrease by [magnitude], because [mechanism connecting change to root cause].

This hypothesis goes directly into `ab-test-design` before any solution is built.

## Secondary Leaks

After the primary leak is diagnosed and a hypothesis is formed, identify the next two highest-impact leaks. Document them but do not begin work on them until the primary leak hypothesis is tested. Fixing two leaks simultaneously produces unattributable results.

## The Process

### Step 1 — Define the Funnel Boundary

Name the entry event and the conversion goal. Everything in between is a step.

### Step 2 — Pull the Step Data

Query volume, exit rate, and time-in-step for each step. Use actual data — not estimates.

### Step 3 — Calculate the Primary Leak

Volume × exit rate = exits. Rank steps by exits. The top-ranked step is the primary leak.

### Step 4 — Root-Cause Using at Least Two Methods

Use session recordings, exit surveys, heatmaps, error logs, or segmentation. Two independent methods reduce the risk of a single-method false root cause.

### Step 5 — Write the Hypothesis

One sentence in the required form.

### Step 6 — Store the Analysis

Store at `growth/funnel-analysis/<funnel>-<date>.md` with the step data table, root cause documentation, and hypothesis.

## Rationalization Red Flags

These thoughts mean the analysis was not done — stop:

- *"Let's improve the conversion rate"* — conversion rate of what? at which step? measured from where to where? — "improve conversion rate" is a goal, not a diagnosis
- *"The checkout page is the problem"* — maybe; the checkout page exit rate relative to other steps determines whether it's the primary leak; intuition about which step is the problem is wrong roughly half the time
- *"We should run an experiment on the landing page"* — before an experiment: which step is the primary leak, what is the root cause, and what does the hypothesis predict? a landing page experiment without a root-cause is a guess
- *"The data says the drop-off is at step 3"* — this is the leak identified but not root-caused; step 3 drop-off is a where, not a why; the experiment target is the why
- *"We've tried improving step 2 before"* — was the root cause of step 2 identified before the improvement was designed? if not, the previous effort was also a guess

## Completion Statement Format

When funnel-analysis is satisfied, state it like this:

```
Funnel analysis complete.
File: growth/funnel-analysis/<funnel>-<date>.md ✓

Funnel: [entry event] → [conversion goal], <N steps>
Data period: [date range], [data source]

Step data:
  | Step | Entered | Exit rate | Exits (vol × rate) |
  | [steps with real numbers] |

Primary leak: Step <N> — <X> exits/period (<Y>% exit rate) ✓
Root cause: [specific description — from session recordings + exit survey] ✓
  Methods used: [session recordings / exit survey / heatmap / error logs / segmentation]

Hypothesis: If [specific change], then Step N exit rate decreases by [X%] because [mechanism] ✓
Next step: ab-test-design ✓

Secondary leaks identified: Step <A> and Step <B> — queued after primary hypothesis test ✓
```

A root cause described as "users drop off" is not a root cause. The root cause names the specific friction, error, or mismatch the user encountered.

## Why This Matters

Funnel optimisation without diagnosis is a succession of guesses, each of which produces a result that may be noise. Teams that optimise without diagnosing spend months running experiments on steps that are not the primary leak, accumulate a library of inconclusive results, and conclude that "the funnel is hard to improve." The funnel is hard to improve when the primary leak is not identified. When it is, improvement is often a single change.
