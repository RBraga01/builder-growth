---
name: copy-quality-gate
description: Use before any external-facing copy ships. Applies three tests — "so what?", "who cares?", and "why now?" — to every claim in the copy. Blocks "it explains what we do" completions.
---

# Copy Quality Gate

## The Law

```
COPY THAT CANNOT ANSWER "SO WHAT?" IS MARKETING FOR THE WRITER, NOT THE READER.
"It explains what we do" passes the author's test — the reader's test is "what does this mean for me?" and the reader leaves if the answer isn't in the first sentence.
Passing all three tests — "so what?", "who cares?", "why now?" — IS copy that earns attention.
```

## When to Use

Trigger before:
- Publishing any homepage, landing page, or hero section
- Sending any email campaign or outbound sequence
- Running any ad copy
- Publishing any sales collateral or pitch deck

## When NOT to Use

- Internal documentation (no reader conversion goal)
- Legal disclosures (accuracy and completeness are the goals, not engagement)
- Help centre articles (utility copy — different standards apply)

## The Three Tests

All three must pass. Passing two and failing one is a fail.

### Test 1 — "So What?"

For every claim in the copy, ask: "so what does this mean for the reader?"

**Apply the chain:**
```
Claim: "Our AI automatically categorises support tickets."
So what? "You spend less time manually triaging."
So what? "Your team handles 3× more tickets without adding headcount."
```

The final answer in the "so what?" chain is the real claim. If it is not in the copy, the copy is incomplete.

**Rule:** If the "so what?" chain reaches a benefit the reader cares about in 2 steps or fewer, the claim is positioned correctly. If it takes 3+ steps, the copy is describing features, not benefits.

**Failure pattern:**
> "We use transformer-based models with retrieval augmentation."
> So what? "It's more accurate."
> So what? "You get fewer wrong answers."
> So what? "You don't have to manually verify everything."

Three steps to reach the benefit — the copy is too feature-level. The copy should open with "fewer wrong answers you have to verify" and let the technology be a proof point, not the headline.

### Test 2 — "Who Cares?"

Who specifically is this copy for, and does it speak to them?

Read each paragraph and ask: which specific person would read this and think "this is exactly for me"?

**Required:**
- The audience from the positioning audit (see `positioning-audit`) must be identifiable from the copy alone
- The copy must use the audience's language — the words they use about their own problem, not the words the company uses about its solution

**Failure pattern:**
> "Designed for modern teams" — who cares? Any team can claim to be "modern"
> "For developers who move fast" — who cares? All developers believe they move fast

**Pass pattern:**
> "For engineering managers running LLM features in production" — a specific person reads this and recognises themselves

### Test 3 — "Why Now?"

Why should the reader act today, not in 3 months?

Without urgency, good copy produces interest without action. Urgency can come from:
- **Timing**: limited availability, launch pricing, deadline
- **Cost of inaction**: quantify what every month of delay costs
- **Moment**: the reader is already experiencing the problem right now

**Rules:**
- Urgency must be real — fabricated scarcity ("offer expires today" for a permanent price) destroys trust
- Cost of inaction must be specific — "it's costing you more than you think" is not urgency; "at 10k tickets/month, manual triage costs 120 engineer-hours" is

**When "why now?" is not needed:** pure informational copy (help docs, specification pages) — the reader decides the urgency.

## The Review Process

### Step 1 — Apply the "So What?" Chain to Every Claim

List every claim in the copy. For each, run the chain. Flag any claim that takes 3+ steps to reach reader value.

### Step 2 — Identify the Audience From the Copy Alone

Cover the product name. Can you identify who the copy is for from the language and problems described? If not, the copy is not speaking to a specific audience.

### Step 3 — Find the Urgency

Is there a clear reason to act today? Is it real? Is it specific?

### Step 4 — Revise and Document

Rewrite flagged claims. Note which claims were revised and why in the review document.

### Step 5 — Store the Review

Store at `growth/copy-reviews/<campaign>-<date>.md` with the original copy, the test results per claim, and the revised copy.

## Rationalization Red Flags

These thoughts mean the copy has not been tested — stop:

- *"It explains what we do"* — explaining what you do is not the goal; the goal is making the reader understand why it matters to them; those are different sentences
- *"The features are the differentiator"* — features become differentiators only when translated into reader outcomes; a feature list is not differentiated copy
- *"Our audience will read past the headline"* — they won't; you have 3 seconds in a landing page and 0.3 seconds in an ad; if the value is not in the first sentence, the rest is invisible
- *"Urgency feels pushy"* — specific cost-of-inaction copy is not pushy; it is useful to a reader who doesn't know what problem is worth solving now
- *"We'll optimise copy after launch"* — copy that fails the three tests will produce low conversion; low conversion will be attributed to targeting, budget, or the offer before copy is reviewed

## Completion Statement Format

When copy-quality-gate is satisfied, state it like this:

```
Copy review complete.
File: growth/copy-reviews/<campaign>-<date>.md ✓

Claims reviewed: <N total>
Test 1 — "So what?":
  Claims requiring revision (3+ chain steps): <N>
  Revised: <N> ✓
  Remaining failures: 0 ✓

Test 2 — "Who cares?":
  Audience identifiable from copy alone: yes ✓
  Audience's language used: yes ✓

Test 3 — "Why now?":
  Urgency present: yes / not applicable ✓
  Urgency type: [timing / cost-of-inaction / moment]
  Urgency is real (not fabricated): confirmed ✓

All three tests passed: ✓
```

Zero remaining failures across all three tests. "One test failed but the copy is otherwise good" is a fail.

## Why This Matters

Copy that describes a product in the product's language reaches the people who already know they want it. The goal of growth copy is to reach the people who don't know they want it yet — and that requires translating capability into consequence in the reader's language. The three tests are the minimum checks that prevent the copy team from writing for themselves instead of the reader.
