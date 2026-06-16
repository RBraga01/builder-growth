---
name: pricing-page-review
description: Use before publishing or changing any pricing, packaging, or plan page. Reviews pricing clarity, plan differentiation, target customer per tier, CTA clarity, risk reversal, objections, comparison logic, anchoring, limitations, upgrade path, and trust/proof. Blocks "the pricing speaks for itself" completions.
---

# Pricing Page Review

## The Law

```
A PRICING PAGE THAT CONFUSES IS A PRICING PAGE THAT LOSES THE SALE SILENTLY.
"The pricing speaks for itself" assumes the reader will do the work of comparing tiers, finding which one fits them, and trusting the numbers — work most readers abandon rather than complete.
Clarity + differentiation + per-tier fit + clear CTA + risk reversal + objection handling + comparison logic + honest anchoring + disclosed limitations + upgrade path + trust IS a reviewed pricing page.
```

## When to Use

Trigger before:
- Publishing a new pricing or packaging page
- Changing prices, tiers, or what's included in any existing plan
- Launching a new plan, add-on, or usage-based pricing component
- Any time customer feedback or sales objections suggest the pricing page is the friction point in the funnel (confirmed via `funnel-analysis`)

## When NOT to Use

- Custom/enterprise pricing communicated only through sales conversations with no public page (review the sales deck and proposal templates instead, using the same principles)
- Internal cost or margin documents (a different audience and purpose than a customer-facing pricing page)

## The Eleven Review Areas

A complete review covers all eleven. A pricing page can fail on just one of these and lose conversions that no amount of strength on the other ten will recover.

### 1 — Pricing Clarity

Can a reader state the price they would pay, in 10 seconds, without doing math or guessing what's excluded? Hidden fees, vague usage units, or pricing that requires a calculator to understand fails this.

### 2 — Plan Differentiation

Is it immediately clear what's different between tiers — not just "more of everything" but specific capabilities that map to specific customer needs? Tiers differentiated only by quantity (more seats, more credits) with no qualitative difference confuse readers about which tier they actually need.

### 3 — Target Customer Per Tier

Does each tier name (implicitly or explicitly) who it's for? "Starter / Pro / Enterprise" with no description of who fits each forces the reader to self-select with no guidance — most will pick the cheapest, unsure if they're underbuying.

### 4 — CTA Clarity

Is the action for each tier unambiguous — "Start free trial," "Buy now," "Talk to sales" — matched to that tier's actual sales motion? A self-serve tier with a "Contact us" CTA adds unnecessary friction; an enterprise tier with a "Buy now" button overpromises a self-serve checkout that doesn't exist.

### 5 — Risk Reversal

Is there a trial, guarantee, or cancel-anytime policy visible on the page itself — not buried in terms of service? Same requirement as `offer-quality-gate` Element 6, applied specifically to the moment of price commitment.

### 6 — Objections

Are the top pricing-specific objections answered on the page or immediately accessible (FAQ, tooltip)? Common objections: "what happens if I exceed my limit," "can I change plans later," "is there a contract."

### 7 — Comparison Logic

If a feature comparison table exists, is it accurate, current, and free of items that exist only to pad the table (features irrelevant to the buying decision listed just to make the table feel comprehensive)?

### 8 — Anchoring

Is the most expensive tier or feature legitimately positioned to make another tier look like the obvious choice — and is that anchor honest? An anchor tier that no one is meant to buy and is priced unrealistically high to manipulate perception, rather than reflecting real value at that level, is deceptive anchoring.

### 9 — Limitations

Are usage limits, fair-use policies, or feature restrictions per tier disclosed on the pricing page, not discovered after signup? Same principle as `ai-messaging-review` Category 4 — limitations disclosed at the point of the claim, not buried.

### 10 — Upgrade Path

Is it clear how and when a customer moves from one tier to the next, and does the transition avoid penalizing the customer for growing (e.g., losing data, re-onboarding, or a confusing migration)?

### 11 — Trust and Proof

Does the page carry appropriate trust signals (security/compliance badges if relevant, customer logos if reviewed via `social-proof-review`, money-back guarantee) without overclaiming?

## The Process

### Step 1 — Read the Page as Each Target Customer

For each tier's intended customer, read the page and time how long it takes to identify the price, what's included, and whether this tier fits them.

### Step 2 — Check Pricing Clarity

Can the price be stated without math? List any hidden calculation the reader has to do.

### Step 3 — Check Differentiation and Tier Fit

Confirm each tier has a qualitative reason to exist, not just a quantity difference, and that the target customer per tier is identifiable.

### Step 4 — Check CTA Match

Confirm each tier's CTA matches its actual sales motion.

### Step 5 — Check Risk Reversal and Objection Handling

Confirm a trial/guarantee/cancel-anytime is visible, and the top 2–3 pricing objections are answered on or near the page.

### Step 6 — Check Anchoring and Comparison Honesty

Confirm the anchor tier reflects real value, and the comparison table doesn't pad or omit material differences.

### Step 7 — Check Limitations and Upgrade Path

Confirm usage limits are disclosed up front, and the upgrade path is clear and not punitive.

### Step 8 — Check Trust Signals

Confirm any proof or trust badges used are accurate and, where applicable, already passed through `social-proof-review`.

### Step 9 — Flag and Revise

Mark each of the eleven areas PASS / REVISE. Document the fix for each REVISE.

### Step 10 — Store the Review

Store at `growth/pricing/<page>-review-<date>.md`.

## Rationalization Red Flags

These thoughts mean the pricing page was not reviewed — stop:

- *"The pricing speaks for itself"* — pricing pages with unclear tiers don't get clarified by the reader; the reader picks the cheapest option out of uncertainty, or leaves
- *"We need an expensive top tier to anchor the others"* — anchoring works when the top tier is a real, purchasable option at a price that reflects real value; an anchor no one is meant to buy, priced to manipulate, reads as a trick once noticed and damages trust in every other number on the page
- *"We'll explain the usage limits when they hit them"* — a customer who discovers a limit after they've built around the plan feels misled, regardless of intent; disclose it up front
- *"The feature comparison table looks more complete with more rows"* — padding the table with irrelevant rows makes the real differences harder to find, which is the opposite of what a comparison table is for
- *"Enterprise customers will just talk to sales, the page doesn't need to be clear for them"* — an unclear enterprise tier still has to convince the buyer that talking to sales is worth their time; an unclear page produces a lower-quality, less-informed first sales conversation

## Completion Statement Format

When pricing-page-review is satisfied, state it like this:

```
Pricing page review complete.
File: growth/pricing/<page>-review-<date>.md ✓

Pricing clarity: price statable in <N> seconds, no required calculation ✓
Plan differentiation: <N> tiers — each with a qualitative (not just quantity) distinction ✓
Target customer per tier: identifiable for all <N> tiers ✓
CTA clarity: each tier's CTA matches its sales motion ✓
Risk reversal: [trial/guarantee/cancel-anytime] visible on page ✓
Objections handled: <N> — [objection → answer] ✓
Comparison logic: accurate, no padding, no material omissions ✓
Anchoring: [anchor tier] — reflects real value, not manipulative ✓
Limitations: disclosed on page — [usage limits/fair-use named] ✓
Upgrade path: clear, non-punitive — [described] ✓
Trust/proof: [signals used] — verified via social-proof-review where applicable ✓

Items revised: <N>
Verdict: READY to publish / CONDITIONAL (fixes required) ✓
```

A pricing page with undisclosed limitations or a manipulative anchor tier fails this gate.

## Why This Matters

The pricing page is where interest converts to a decision, and confusion at that exact moment doesn't produce complaints — it produces silent abandonment that shows up in analytics as a vague "drop-off at pricing" with no obvious cause. Most pricing page failures are not about the price being too high; they are about the reader being unable to confidently determine which tier fits them, what they're actually committing to, and what happens if they're wrong. Fixing clarity, disclosure, and honest anchoring recovers conversions that no discount would have recovered, because the reader who left wasn't objecting to the price — they were objecting to the uncertainty.
