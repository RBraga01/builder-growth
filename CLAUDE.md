# builder-growth — Claude Configuration

## Pack Version

builder-growth — AI Growth Skills Pack v1.1.0

## File Conventions

| Artifact | Path |
|---|---|
| Growth strategies | `growth/strategy/<project>-<date>.md` |
| Channel audits | `growth/channels/<project>-channel-audit-<date>.md` |
| Offer quality gates | `growth/offers/<offer>-quality-gate-<date>.md` |
| Positioning documents | `growth/positioning/<product>-<date>.md` |
| Campaign briefs | `growth/campaigns/<campaign>-brief-<date>.md` |
| Copy reviews | `growth/copy-reviews/<campaign>-<date>.md` |
| Launch plans | `growth/launches/<project>-launch-plan-<date>.md` |
| Growth metrics designs | `growth/metrics/<project>-metrics-<date>.md` |
| Funnel analyses | `growth/funnel-analysis/<funnel>-<date>.md` |
| Experiment designs | `growth/experiments/<experiment>-design-<date>.md` |
| Retention designs | `growth/retention/<feature>-design-<date>.md` |
| Social proof reviews | `growth/social-proof/<campaign>-proof-review-<date>.md` |
| Pricing page reviews | `growth/pricing/<page>-review-<date>.md` |
| Messaging reviews | `growth/messaging-reviews/<campaign>-<date>.md` |
| Growth critiques | `growth/reviews/<work>/<date>-critique.md` |

## Skill Trigger Sequence

This is the full lifecycle order. Not every skill is required on every project — trigger the ones that match the work in front of you. A pure copy review on an already-launched product does not need `growth-strategy-design` re-run; a brand-new initiative does.

1. `growth-strategy-design` → before any channel, offer, or campaign decision is made
2. `channel-selection-audit` → before any campaign, content plan, or outbound motion is built
3. `offer-quality-gate` → before any copy or campaign is built around an offer
4. `positioning-audit` → before any copy is written
5. `campaign-brief-generator` → before a campaign moves from strategy to creative production
6. `copy-quality-gate` → before any external copy ships
7. `launch-plan-design` → before any approved project, product, or campaign launches
8. `growth-metrics-design` → before any growth initiative executes
9. `funnel-analysis` → before any CRO effort starts
10. `experiment-design` → before any A/B test runs
11. `retention-design` → before any feature launches
12. `social-proof-review` → before any testimonial, logo, case study, or quantified result ships
13. `pricing-page-review` → before any pricing or packaging page ships
14. `ai-messaging-review` → before any AI product claim ships externally

## Agent Usage

| Agent | When to Use |
|---|---|
| `growth-critic` | After positioning, copy, or experiment designs are drafted, before they ship |
| `experiment-designer` | When designing any growth experiment |
| `messaging-reviewer` | Before any external AI capability claim ships |
| `growth-strategist` | When a project needs growth strategy, channel selection, offer validation, or a launch plan defined |
| `campaign-reviewer` | When a campaign brief, metrics design, social proof, or pricing page needs to be built or reviewed before it ships |

## What Makes This Pack Different From Generic Growth Frameworks

Standard growth frameworks optimise. This pack diagnoses and plans before optimising:
- Every growth initiative starts with a named stage, segment, goal, and constraint — not a default channel
- Every channel is scored against the same eight criteria before budget is committed
- Every offer has risk reversal and a single CTA before copy is written
- Every funnel optimisation starts with a diagnosed root cause
- Every experiment has a calculated sample size and a pre-specified stopping rule
- Every launch has a named rollback or pause criterion, decided before launch day
- Every AI capability claim has a source or is removed
- Every retention initiative defines the activation moment before launch
- Every pricing page and proof asset is reviewed for clarity and source before it ships

Optimising without diagnosing — and executing without a strategy — is the most expensive growth mistake. This pack blocks it.
