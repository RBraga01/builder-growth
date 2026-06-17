---
name: offer-quality-gate
description: Use before any copy or campaign is built around an offer. Requires target customer, painful problem, promised outcome, mechanism, proof, risk reversal, pricing or exchange model, CTA, and objection handling to be defined before the offer is used in any external-facing work. Blocks "the offer is implied by the product" completions.
---

# Offer Quality Gate

## The Law

```
COPY BUILT AROUND AN UNDEFINED OFFER DESCRIBES A PRODUCT, NOT A DEAL.
"The offer is implied by the product" leaves the reader to assemble what they get, what it costs, and why they should believe it — work the reader will not do.
Target customer + problem + outcome + mechanism + proof + risk reversal + price/exchange + CTA + objection handling IS an offer.
```

## When to Use

Trigger before:
- Writing any campaign, landing page, or sales sequence built around a specific offer (trial, demo, paid plan, lead magnet, waitlist, bundle)
- Launching a new pricing tier, package, or promotional offer
- Any time `growth-strategy-design` names a core offer that has not yet been validated
- Before `campaign-brief-generator` or `launch-plan-design` references an offer

## When NOT to Use

- Pure brand or awareness content with no specific ask (no offer to validate)
- Internal product copy describing a feature with no separate commercial offer attached
- Offers already validated and unchanged from a prior cycle — reference the existing document instead of redoing the gate

## The Nine Offer Elements

A complete offer defines all nine. An offer missing any one produces copy that the reader has to interpret instead of evaluate.

### 1 — Target Customer

Who this specific offer is for — same specificity bar as `positioning-audit`. A generic offer "for everyone" converts nobody, because nobody recognizes themselves in it.

### 2 — Painful Problem

The problem this offer addresses, in the customer's words, with enough specificity that the customer would say "yes, that's my problem" on first read.

**Test:** Could this problem statement be the customer's own complaint, verbatim? If it reads like a vendor's framing of the problem, rewrite it.

### 3 — Promised Outcome

What the customer gets, stated as a result, not a feature. "Access to our dashboard" is a feature. "See which campaigns are losing money before the month ends" is an outcome.

### 4 — Mechanism

How the outcome is delivered — the believable "how" that makes the promised outcome credible rather than a claim made on faith.

**Rule:** A promised outcome with no mechanism reads as a sales claim. A mechanism with no promised outcome reads as a feature list. Both are required.

### 5 — Proof

Evidence the mechanism and outcome are real: case study, data, demo, testimonial, or guarantee. Validated separately by `social-proof-review` before it ships — but the offer must name what proof exists, even if unreviewed.

### 6 — Risk Reversal

What removes the customer's risk of trying this and being wrong: free trial, money-back guarantee, cancel-anytime, pilot period, or done-for-you onboarding.

**Test:** If the offer fails to deliver, what does the customer lose? If the answer is "their money and their time, no recourse," risk reversal is missing.

### 7 — Pricing or Exchange Model

What the customer gives in exchange: money, email address, time, data, attention. Stated clearly enough that the customer knows the full ask before clicking through.

**Rule:** "Contact us for pricing" is acceptable only when the actual sales cycle requires custom scoping — not as a way to avoid stating an unattractive price.

### 8 — CTA

The single next action the customer takes. One CTA per offer — an offer with three competing CTAs ("buy now," "book a demo," "download the guide") converts on none of them as well as it would convert on one.

### 9 — Objection Handling

The 2–3 objections a real prospect would raise before acting, with a real answer to each — not avoided, not buried.

**Required:** Name the objection in the prospect's words, not a softened version. "Is this worth the price?" not "value perception."

## The Process

### Step 1 — Define the Target Customer

One sentence, matching the `positioning-audit` specificity bar.

### Step 2 — State the Painful Problem

In the customer's words. Validate against real customer language if available (support tickets, sales call notes, reviews).

### Step 3 — Write the Promised Outcome

A result, not a feature. Run the `copy-quality-gate` "so what?" chain if the outcome reads like a feature.

### Step 4 — Name the Mechanism

The believable "how." If there is no credible mechanism, the outcome cannot be promised yet.

### Step 5 — Identify the Proof

Name what evidence exists. Flag for `social-proof-review` if it has not been reviewed.

### Step 6 — Define Risk Reversal

State what the customer loses if the offer fails to deliver — and what removes that risk.

### Step 7 — Set the Pricing or Exchange Model

State the full ask plainly.

### Step 8 — Write the Single CTA

One action. If multiple actions are tempting, choose the one that matches the customer's current intent level (see `channel-selection-audit`).

### Step 9 — Handle the Top Objections

List 2–3 real objections and their answers.

### Step 10 — Store the Offer

Store at `growth/offers/<offer>-quality-gate-<date>.md`.

## Rationalization Red Flags

These thoughts mean the offer was not defined — stop:

- *"The offer is implied by the product"* — implied offers require the reader to do the work of figuring out what they get and what it costs; readers who have to work for clarity leave instead
- *"We don't need risk reversal, the product is good"* — a good product does not remove the customer's perceived risk of being wrong before they've used it; risk reversal addresses the moment before trust is earned, not after
- *"Let's have three CTAs so we don't lose anyone"* — three CTAs split attention and produce lower conversion on all three than one CTA matched to the offer's actual intent level
- *"We'll handle objections in the sales call"* — objections that surface for the first time in a sales call have already cost a conversion at every earlier stage where the prospect silently disqualified themselves
- *"Contact us for pricing keeps us flexible"* — flexible pricing is reasonable for genuinely custom deals; used to avoid stating an unattractive number, it reads as evasive and costs more trust than the number would have

## Completion Statement Format

When offer-quality-gate is satisfied, state it like this:

```
Offer quality gate complete.
File: growth/offers/<offer>-quality-gate-<date>.md ✓

Target customer: [role/situation] ✓
Painful problem: "[problem in customer's words]" ✓
Promised outcome: [result, not feature] ✓
Mechanism: [credible "how"] ✓
Proof: [evidence named] — reviewed: yes / pending social-proof-review
Risk reversal: [guarantee/trial/cancel-anytime] — customer's downside if it fails: [stated] ✓
Pricing/exchange model: [full ask stated plainly] ✓
CTA: [single action] ✓
Objections handled: <N> — [objection → answer pairs] ✓

Verdict: READY for copy / campaign work ✓
```

An offer missing risk reversal, a single CTA, or named objection handling fails this gate.

## Why This Matters

Copy and campaigns built around an undefined offer ask the reader to assemble the deal themselves — what they get, what they pay, why they should believe it, what happens if it doesn't work. Most readers won't do that work; they'll leave instead and call it "not a good fit," when the actual failure was an offer that was never made explicit. A defined offer is what `campaign-brief-generator` and `launch-plan-design` build on top of — skipping this gate pushes the ambiguity downstream into copy that has to compensate for a gap that should have been closed here.
