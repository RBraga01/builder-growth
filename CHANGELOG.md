# Changelog — builder-growth

## 1.1.0 — 2026-06-16

Complete Growth Planning Expansion.

### Added

Skills (8):
- `growth-strategy-design` — growth stage + segment + goal + constraint + channel hypothesis + offer + north star + 90-day hypothesis before execution
- `channel-selection-audit` — every candidate channel scored against 8 criteria before a campaign is built
- `offer-quality-gate` — target customer + problem + outcome + mechanism + proof + risk reversal + pricing + CTA + objections before copy is written
- `launch-plan-design` — launch goal + timeline + task ownership + success metrics + rollback criteria before launch day
- `growth-metrics-design` — north star + input/output metrics + leading/lagging indicators + metric owners before execution
- `campaign-brief-generator` — objective + audience + offer + message + channel + creative specs + success metric before execution
- `social-proof-review` — every testimonial, logo, case study, and quantified result sourced and permissioned before publication
- `pricing-page-review` — pricing clarity + tier differentiation + risk reversal + disclosed limitations before a pricing page ships

Agents (2):
- `growth-strategist` (Sonnet) — defines growth strategy, validates channel selection and offers, designs launch plans; READY / CONDITIONAL / BLOCKED
- `campaign-reviewer` (Sonnet) — builds campaign briefs, defines growth metrics, reviews social proof and pricing pages; PASS / CONDITIONAL / BLOCK

Documentation:
- `docs/ORCHESTRATION.md` — defines how external orchestrators, agent workflows, and manual project workflows route work to builder-growth

- `positioning-audit` public discussion evidence guidance, including optional X/Xquik collection workflow. Original contribution by @kriptoburak in PR #2.

### Changed

- README updated for full growth lifecycle (Strategy → Channel Selection → Offer → Campaign → Launch → Metrics → Funnel → Experiment → Retention → Messaging Review); skill/agent counts updated to 14 skills / 5 agents
- CLAUDE.md updated with expanded file conventions and 14-step trigger sequence
- AGENTS.md updated with `growth-strategist` and `campaign-reviewer` entries

## 1.0.0 — 2026-06-07

Initial release.

### Skills (6)
- `positioning-audit` — category + specific audience + differentiated claim before any copy
- `copy-quality-gate` — "so what?", "who cares?", "why now?" tests before any copy ships
- `funnel-analysis` — leak identified + root-caused + hypothesis before any optimisation
- `experiment-design` — hypothesis + metric + sample size + stopping rule + decision rule
- `retention-design` — activation moment + habit loop + reactivation path before launch
- `ai-messaging-review` — quantified claims sourced + capability claims scoped + AI labels defined

### Agents (3)
- `growth-critic` (Sonnet) — audits positioning, copy, and experiments; PASS / CONDITIONAL / BLOCK
- `experiment-designer` (Sonnet) — designs experiments with calculated sample sizes and stopping rules
- `messaging-reviewer` (Opus) — audits AI capability claims for source, scope, and accuracy
