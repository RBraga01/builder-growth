---
name: social-proof-review
description: Use before any testimonial, case study, logo, quantified result, screenshot, review, or before/after claim is used in marketing. Verifies source, context, permission, and accuracy for every piece of proof. Blocks "this looks credible enough" completions and unsourced or misleading proof.
---

# Social Proof Review

## The Law

```
PROOF WITHOUT A SOURCE IS A CLAIM WEARING A CUSTOMER'S NAME.
"This looks credible enough" substitutes the reader's trust in the format of proof (a quote, a logo, a chart) for actual verification that the proof is real, current, and representative.
Source verified + context preserved + permission confirmed + accuracy checked IS reviewed social proof.
```

## When to Use

Trigger before:
- Publishing any testimonial, customer quote, or review excerpt
- Adding any customer logo to a website, deck, or campaign
- Publishing any case study or quantified customer result
- Using any screenshot of a product, dashboard, or customer data in marketing
- Making any before/after comparison claim

## When NOT to Use

- Internal reporting using real customer data with no external publication (different standard — accuracy still matters, permission and public presentation do not apply the same way)
- Aggregated, anonymised statistics with no identifiable individual customer (still subject to `ai-messaging-review` if AI-related, but not to the permission requirements here)

## The Eight Proof Categories

Every category requires its own verification before publication. A logo and a testimonial are not interchangeable proof — each has its own failure mode.

### 1 — Testimonials

**Verify:** the person is real, currently consents to being quoted, and the quote is unedited beyond minor grammatical cleanup that does not change meaning.

**Rule:** No testimonial without context — name, role, and company (or an honest reason why one of these is withheld, such as anonymisation by request). "Anonymous CEO" with no other context reads as fabricated.

### 2 — Customer Quotes

**Verify:** the quote is attributed to its actual source, was given in the context implied (e.g., not pulled from an unrelated conversation and recontextualised), and the customer would recognise and stand behind the quote as published.

### 3 — Logos

**Verify:** explicit permission to display the logo exists, the relationship described (customer, partner, integration) is accurate, and the logo is current (the company hasn't rebranded, been acquired, or churned).

**Rule:** No logos without permission. A "we have 50 enterprise customers" logo wall built from publicly known users who never agreed to be featured is a liability, not proof.

### 4 — Case Studies

**Verify:** the customer reviewed and approved the published version, the results described are accurately attributed to the product (not coincidental with other changes the customer made), and the methodology is disclosed.

### 5 — Quantified Results

**Verify:** same bar as `ai-messaging-review` Category 1 — source, population, baseline, and reproducibility. A specific customer's result requires explicit labelling as one customer's result, not implied as typical.

**Rule:** No customer result presented as typical unless validated against a representative sample. "One customer saved 40%" is fine; "customers save 40%" implies it's typical and requires validation across a real sample.

### 6 — Screenshots

**Verify:** no private or sensitive data is visible (other customers' names, emails, financial figures, internal notes) unless explicitly cleared for publication; the screenshot reflects current product behaviour, not a deprecated or mocked-up version.

**Rule:** No screenshots exposing private data — redact or use synthetic/demo data instead of real customer data whenever the screenshot's purpose can be served either way.

### 7 — Reviews

**Verify:** the review excerpt is not edited in a way that changes its meaning, the platform and date are disclosed, and selectively-quoted positive snippets are not used to misrepresent an overall mixed or negative review.

### 8 — Before/After Claims

**Verify:** "before" and "after" states are comparable (same metric, same conditions, same time period scale), and the change is attributable to the product, not to an unrelated factor the customer also changed at the same time.

**Rule:** No misleading before/after comparisons — a before/after that compares different metrics, cherry-picks an unusually bad "before" period, or omits a confound the customer mentioned is misleading even if every individual number is technically accurate.

## The Process

### Step 1 — Inventory Every Piece of Proof

List every testimonial, quote, logo, case study, quantified result, screenshot, review, and before/after claim used in the work under review.

### Step 2 — Verify Source for Each Item

Confirm who said it, when, in what context, and whether it's still accurate today.

### Step 3 — Confirm Permission and Context

For logos, quotes, and case studies: confirm permission exists and context (name/role/company or honest reason for anonymity) is preserved.

### Step 4 — Check for Misleading Presentation

For quantified results and before/after claims: confirm typical vs. one-off framing, and comparable before/after conditions.

### Step 5 — Check for Private Data Exposure

For screenshots: confirm no unintended private or sensitive data is visible.

### Step 6 — Flag and Resolve

Mark each item PASS / REVISE / REMOVE. Document what was changed for REVISE items and why for REMOVE items.

### Step 7 — Store the Review

Store at `growth/social-proof/<campaign>-proof-review-<date>.md`.

## Rationalization Red Flags

These thoughts mean proof was not reviewed — stop:

- *"This looks credible enough"* — looking credible and being verified are different; the review exists because unverified-but-credible-looking proof is exactly the kind that turns into a public correction later
- *"The customer probably wouldn't mind"* — "probably" is not permission; confirm it, or don't use it
- *"It's basically true even if the numbers are rounded up"* — "basically true" quantified claims fail the same way unsourced ones do: the customer reading the exact number can disprove it
- *"We blurred the parts that matter"* — verify the blur actually obscures the sensitive data at the resolution and zoom level the published asset will be viewed at, not just at a glance during editing
- *"This logo is a well-known company, everyone assumes we're not actually claiming a relationship"* — readers do assume a relationship when a logo is presented as a customer or partner; if there is none, remove it

## Completion Statement Format

When social-proof-review is satisfied, state it like this:

```
Social proof review complete.
File: growth/social-proof/<campaign>-proof-review-<date>.md ✓

Proof items reviewed: <N total>
  Testimonials: <N> — all sourced, contextualised, consent confirmed ✓
  Customer quotes: <N> — all attributed and contextually accurate ✓
  Logos: <N> — all with confirmed permission and current relationship ✓
  Case studies: <N> — all customer-approved with disclosed methodology ✓
  Quantified results: <N> — all sourced; <N> typical-claims validated / <N> labelled as single-customer ✓
  Screenshots: <N> — no private/sensitive data exposed ✓
  Reviews: <N> — unedited in meaning, platform/date disclosed ✓
  Before/after claims: <N> — comparable conditions, no omitted confounds ✓

Items revised: <N>
Items removed: <N> — reason: [no permission / unsourced / misleading / private data exposed]

Final proof set: all sourced, permissioned, and accurately presented ✓
```

Any logo without confirmed permission or any screenshot exposing private data is a REMOVE, not a REVISE.

## Why This Matters

Proof is the part of marketing the reader trusts most — and the part most likely to backfire publicly when it turns out to be wrong. A fabricated-feeling testimonial, an unauthorised logo, or a cherry-picked before/after doesn't just fail to convert; when caught, it actively destroys trust in every other claim the company makes, including the true ones. The cost of verifying proof before publication is small. The cost of a customer publicly disputing a quote attributed to them, or a partner asking why their logo is on a page they never approved, is not.
