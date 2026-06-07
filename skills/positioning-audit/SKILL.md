---
name: positioning-audit
description: Use before any marketing copy is written for a product, feature, or campaign. Requires a clear category, a specific audience, and a differentiated claim — verified against the "so what?" test — before any copy is produced. Blocks "we'll develop the messaging as we write" completions.
---

# Positioning Audit

## The Law

```
COPY WRITTEN WITHOUT A DEFINED POSITION IS DECORATION.
"We'll develop the messaging as we go" ships language that describes the product instead of solving the audience's problem — and is heard by nobody because it sounds like every other product.
Clear category + specific audience + differentiated claim IS a position.
```

## When to Use

Trigger before:
- Writing any marketing copy (homepage, landing pages, ads, email campaigns)
- Launching a new product, feature, or market segment
- Repositioning an existing product after a significant change
- Writing a sales deck or pitch that will represent the product externally

## When NOT to Use

- Internal documentation (no audience positioning required)
- Support copy (the audience is already a customer — different communication goal)
- Copy for features inside the product (UI copy — different from marketing copy)

## The Three Positioning Elements

A complete position has all three. Missing any one produces copy that is either too broad to resonate, too narrow to reach anyone, or too generic to be believed.

### 1 — Category

What type of product is this, in the audience's language?

Category determines how the audience evaluates the product. The wrong category activates the wrong comparison set. "An AI productivity tool" puts the product against every productivity tool. "A prompt management system for LLM teams" activates a much smaller, much more relevant comparison set.

**Rules:**
- Use the audience's language, not the industry's language
- Specific categories outperform broad categories (narrower = easier to be the best)
- The category should already exist in the audience's mind — creating a new category is a 2-year marketing project, not a launch

**Test:** Ask: "What would I search for if I was looking for a product like this?" That search query is your category.

### 2 — Audience

Who is this for, specifically?

The narrower the audience definition, the more specifically you can speak to them. "Software teams" is not an audience. "Engineering managers at companies with 5–50 engineers who are responsible for AI feature quality" is an audience.

**Required specificity:**
- Job title or role
- Company type or size
- Current pain or situation
- What they are using now (what you are replacing or competing with)

**Test:** Can you name 10 specific people who fit this audience definition? If yes, it's specific enough. If you are describing "anyone who could benefit," you are not describing an audience.

### 3 — Differentiated Claim

Why this, not that?

The claim must be:
- **True**: provable by the product's behaviour, not by marketing aspiration
- **Specific**: "reduces hallucination rates" beats "improves AI quality"
- **Differentiated**: the claim must not apply equally to the main alternative the audience would consider

**Test:** Ask: "Does this claim also describe [main competitor or alternative]?" If yes, it is not differentiated.

**What does NOT count:**
- "The best [category]" — superlatives are not claims; they are aspirations
- "Powerful and easy to use" — applies to every product in every category
- "AI-powered" — this is a technology description, not a user benefit

## The "So What?" Test

After writing the position, ask "so what?" from the audience's perspective.

```
Your position: "We manage prompts across your LLM team."
Audience: "So what?"
Your answer: "So when a model update breaks your output format, you know which prompt changed, when, by whom, and what the quality impact was — in two minutes, not two days."
```

If the "so what?" answer contains the actual value, the position was incomplete. Move the "so what?" answer into the position itself.

## The Process

### Step 1 — Define the Category

Write the category in one noun phrase. Test it with the search query test.

### Step 2 — Define the Audience

Write the audience in one sentence including: role, company type/size, current situation, and what they use now.

### Step 3 — Write the Differentiated Claim

One sentence that is true, specific, and does not apply equally to the main alternative.

### Step 4 — Run the "So What?" Test

Ask "so what?" as the audience. If the answer reveals additional value, revise the claim to include it.

### Step 5 — Write the One-Paragraph Position

Category + audience + claim in one paragraph. This is the reference document for all copy in this campaign.

### Step 6 — Store the Positioning Document

Store at `growth/positioning/<product>-<date>.md`. All copy writers reference this document — not each other's interpretation of it.

## Rationalization Red Flags

These thoughts mean positioning was not done — stop:

- *"Our audience is anyone who needs [broad category]"* — broad audiences produce copy so general it reaches nobody who identifies with it; "anyone who needs AI tools" is every software company in the world
- *"The copy will define the position"* — copy written before positioning defines nothing; it describes features; the audience will not translate feature descriptions into the value they should care about
- *"We have good copy, we don't need a formal positioning exercise"* — test the copy against the "so what?" chain; if the value is not in the first sentence, the position was not done
- *"We'll differentiate on execution"* — execution is not a differentiator in copy; it is invisible until the product is used; differentiation in copy must be a claim that can be evaluated before purchase
- *"Our audience is broad on purpose — we don't want to exclude anyone"* — broad positioning excludes everyone by speaking to no one specifically; narrowing makes you the obvious choice for a real group

## Completion Statement Format

When positioning-audit is satisfied, state it like this:

```
Positioning complete.
File: growth/positioning/<product>-<date>.md ✓

Category: "[one noun phrase in audience language]" ✓
  Search query test: "[what audience searches for]" → category matches ✓

Audience: "[role] at [company type/size] who [situation] and currently use [alternative]" ✓
  Named examples: <N specific people/companies who fit> ✓

Differentiated claim: "[specific, provable, not-applicable-to-alternative statement]" ✓
  "So what?" chain complete — value stated in first sentence ✓
  Competitor test: claim does NOT apply equally to [main alternative] ✓

One-paragraph position written — all copy in this campaign references this document ✓
```

A broad audience definition fails the positioning audit. A claim that applies equally to the main competitor fails the positioning audit.

## Why This Matters

Copy written without positioning describes the product. Copy written with positioning solves the audience's problem. The audience does not read descriptions — they scan for relevance. A precise category, specific audience, and differentiated claim are what make the product visible to the right people and invisible to the wrong ones. "We didn't resonate" is almost always a positioning failure dressed as a copy problem.
