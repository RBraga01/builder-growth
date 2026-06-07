---
name: ai-messaging-review
description: Use before any AI product messaging ships externally. Audits capability claims for accuracy, quantified claims for evidence, and "AI" labels for specificity. Blocks "10x productivity" without measurement and "AI-powered" without definition.
---

# AI Messaging Review

## The Law

```
AN AI CAPABILITY CLAIM WITHOUT EVIDENCE IS A LIABILITY, NOT A DIFFERENTIATOR.
"10x productivity" without measurement is a promise users test on their first session and don't forgive when it fails.
Every quantified claim sourced + every capability claim scoped + every "AI" label defined IS reviewed messaging.
```

## When to Use

Trigger before:
- Publishing any marketing copy that makes claims about an AI product's capabilities
- Launching any campaign that references AI performance, accuracy, or productivity impact
- Publishing any press release, case study, or sales collateral about an AI product
- Making any public quantified claim ("saves X hours", "Y% more accurate", "Z× faster")

## When NOT to Use

- Internal technical documentation (accuracy matters but external credibility risk is lower)
- Product UI copy describing what a feature does — tested separately with `copy-quality-gate`

## The Four Review Categories

Every piece of AI marketing copy is reviewed against all four. One failure in any category is a fail.

### Category 1 — Quantified Claims

Every number in AI marketing copy must have a source.

**Required for any quantified claim:**
- The study or measurement that produced the number
- The population it was measured on (user segment, task type, timeframe)
- The comparison baseline (X× faster than what? Y% more accurate than what?)
- Whether it is reproducible by a new customer

```
✗ "Save 10 hours per week"
  — no measurement, no population, no baseline, not reproducible

✓ "In a study of 50 engineering teams using the tool for 90 days,
   teams reported an average of 6.5 hours saved per engineer per week
   compared to their previous process (survey, N=342, 95% CI: 5.8–7.2h)"
```

**Simplification allowed:** "Teams save an average of 6.5 hours per engineer per week (from our 2026 customer study — see details)." The full methodology must be available on request, not necessarily in the headline.

**Rules:**
- Self-reported surveys are evidence but must be labelled as surveys
- A single customer's result cannot be presented as a typical result
- "Up to X" claims must represent at least the 80th percentile, not the maximum

### Category 2 — Capability Claims

What can this AI actually do, consistently, in production?

AI capabilities are probabilistic. A capability claim that describes best-case performance is a misrepresentation.

**Required:**
- Capability claims must reflect typical performance, not cherry-picked examples
- Limitations and error rates must be disclosed in the same surface (not buried in footnotes)
- Domain scope must be explicit ("accurately extracts dates from US legal contracts" not "accurately extracts information")

```
✗ "Our AI reads and understands any document"
  — "understands" is anthropomorphism; "any document" includes documents it will fail on

✓ "Our AI extracts key clauses and dates from standard commercial contracts with 94% accuracy
   (tested on 500 contracts across 5 formats; performance varies on non-standard formatting)"
```

**High-risk claims requiring special review:**
- Medical/legal/financial accuracy claims — require external validation and explicit disclaimer
- Security/privacy claims — require technical verification, not just product intention
- Claims about what the model "knows," "understands," or "reasons" — must be operationalised

### Category 3 — "AI" Labels

"AI" in marketing copy must be defined or removed.

"AI-powered" describes nothing. It has been used for decision trees, regex, spell checkers, and LLMs equally. If the claim is "AI-powered," the reader cannot evaluate whether the AI is relevant to their problem.

**Required:**
- What the AI specifically does in this product (not "AI powers our platform")
- What the AI's role is relative to the user (assistant, automator, advisor)
- What the user controls vs. what the AI decides

```
✗ "AI-powered document management"
  — no specificity about what the AI does or why it matters

✓ "Automatically extracts key terms, parties, and dates from uploaded contracts
   — reviewed and editable before any action is taken"
```

### Category 4 — Trust and Accuracy Transparency

AI messaging must not create over-trust.

**Required:**
- Accuracy limitations disclosed in the same surface as the accuracy claim
- Instructions for how to verify AI output before acting on it
- Clear human-in-the-loop positioning for high-stakes outputs

**Red flags:**
- "Our AI never makes mistakes" — no model has 100% accuracy; this claim will be disproved
- "Trust the AI" — trust must be calibrated, not commanded
- "AI-generated insights" without any indication of confidence, source, or verification path

## The Review Process

### Step 1 — List Every Claim

Extract every claim from the copy: quantified claims, capability claims, AI labels, and accuracy statements. List them line by line.

### Step 2 — Audit Each Claim Against Its Category

For quantified claims: does a source exist? Is the population and baseline defined?
For capability claims: does this reflect typical performance? Is the domain scoped?
For AI labels: what specifically does the AI do?
For trust claims: is accuracy disclosed? Is verification path offered?

### Step 3 — Flag and Revise

Mark each claim: PASS / REVISE / REMOVE. Write revised copy for REVISE items. Remove items that cannot be sourced or scoped.

### Step 4 — Store the Review

Store at `growth/messaging-reviews/<campaign>-<date>.md` with original claims, audit results, and revised copy.

## Rationalization Red Flags

These thoughts mean the review was not done — stop:

- *"Every company says 10x — we need to be competitive"* — claims that every company makes are ignored by readers and investigated by regulators; be the company that says "6.5 hours" with a methodology and you are the only credible one in the category
- *"Our customers told us they save that much"* — self-reported results are evidence when labelled correctly as self-reported; they are a liability when presented as independent measurement
- *"AI-powered is industry standard language"* — it is noise; specificity is the differentiator; say what the AI does, not that AI is involved
- *"We'll add the caveats in footnotes"* — regulators and reviewers read footnotes; readers don't, but they do experience the failure when the claim is not met; the limitation belongs near the claim
- *"The copy is aspirational"* — aspirational claims about AI performance are tested by users on first session; failed expectations produce churn and public criticism, not charitable interpretation of ambition

## Completion Statement Format

When ai-messaging-review is satisfied, state it like this:

```
AI messaging review complete.
File: growth/messaging-reviews/<campaign>-<date>.md ✓

Claims audited: <N total>
  Quantified claims: <N> — all sourced ✓ / <N> removed (no source)
  Capability claims: <N> — all scoped to domain and typical performance ✓
  "AI" labels: <N> — all replaced with specific descriptions ✓
  Trust/accuracy claims: <N> — all limitations disclosed in same surface ✓

Revised claims: <N>
  Removed claims: <N> — reason: [no source / overclaim / unverifiable]

Claims requiring external validation: <N / none>
  Status: [validated / pending — do not ship until complete]

Final copy: all claims sourced, scoped, and accurate to typical performance ✓
```

Any unsourced quantified claim is a REMOVE, not a REVISE. Any trust claim without a disclosed limitation is a REVISE.

## Why This Matters

AI marketing claims that fail users' first experience produce a specific type of churn: the user who tries the product because of the claim, finds it doesn't match, and tells others. "10x productivity" claims tested by a user in 20 minutes produce a negative first impression that cannot be recovered by a better onboarding experience. Accurate, specific claims attract users whose expectations the product can meet — and those users retain.
