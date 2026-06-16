# builder-growth — AI Growth Skills Pack v1.1.0

Skills and agents that enforce quality across the full growth lifecycle:

```
Strategy → Channel Selection → Offer → Campaign → Launch → Metrics → Funnel → Experiment → Retention → Messaging Review
```

Growth strategy defined before channels are chosen, channels chosen before campaigns are built, offers validated before copy is written, copy that clears the "who cares?" test, launches planned with rollback criteria, metrics named before execution, funnels diagnosed before they are optimised, experiments designed with stopping rules before they run, retention loops defined before launch, pricing and social proof reviewed before they ship, and AI capability claims reviewed for accuracy before they ship.

**[→ Visual overview](https://rbraga01.github.io/builder-growth/)**

Works standalone or alongside [A Team](https://github.com/RBraga01/a-team), [builder-ai](https://github.com/RBraga01/builder-ai), [builder-design](https://github.com/RBraga01/builder-design), and [builder-product](https://github.com/RBraga01/builder-product).

## Skills

Not every skill is required on every project — use the ones that match the work in front of you. See [CLAUDE.md](CLAUDE.md) for the full trigger sequence.

| Skill | What It Enforces |
|---|---|
| `growth-strategy-design` | Growth stage, segment, goal, constraint, channel hypothesis, offer, north star, and 90-day hypothesis defined before execution |
| `channel-selection-audit` | Every candidate channel scored against 8 criteria before a campaign is built |
| `offer-quality-gate` | Target customer, problem, outcome, mechanism, proof, risk reversal, pricing, CTA, and objections defined before copy is written |
| `positioning-audit` | Clear category, specific audience, and differentiated claim before any copy is written |
| `campaign-brief-generator` | Objective, audience, offer, message, channel, creative specs, and success metric defined before execution |
| `copy-quality-gate` | "So what?", "who cares?", and "why now?" tests before any copy ships |
| `launch-plan-design` | Launch goal, timeline, task ownership, success metrics, and rollback criteria defined before launch day |
| `growth-metrics-design` | North star, input/output metrics, leading/lagging indicators, and metric owners defined before execution |
| `funnel-analysis` | Leak identified and root-caused before any optimisation begins |
| `experiment-design` | Hypothesis, metric, sample size, duration, stopping rule, decision rule before any test runs |
| `retention-design` | Activation moment, habit loop, and reactivation path defined before launch |
| `social-proof-review` | Every testimonial, logo, case study, and quantified result sourced and permissioned before publication |
| `pricing-page-review` | Pricing clarity, tier differentiation, risk reversal, and disclosed limitations before a pricing page ships |
| `ai-messaging-review` | AI capability claims reviewed for source, scope, and accuracy — no unsourced quantified claims |

## Agents

| Agent | Role |
|---|---|
| `growth-critic` (Sonnet) | Reviews positioning, copy, and experiments against skill gates; PASS / CONDITIONAL / BLOCK |
| `experiment-designer` (Sonnet) | Designs growth experiments with calculated sample sizes and pre-specified stopping rules |
| `messaging-reviewer` (Opus) | Reviews AI product messaging for sourced claims, scoped capabilities, and specific AI labels |
| `growth-strategist` (Sonnet) | Defines growth strategy, validates channel selection and offers, designs launch plans; READY / CONDITIONAL / BLOCKED |
| `campaign-reviewer` (Sonnet) | Builds campaign briefs, defines growth metrics, reviews social proof and pricing pages; PASS / CONDITIONAL / BLOCK |

## Install

```bash
# bash (macOS / Linux / WSL)
bash <(curl -fsSL https://raw.githubusercontent.com/RBraga01/builder-growth/master/install.sh)

# PowerShell (Windows)
irm https://raw.githubusercontent.com/RBraga01/builder-growth/master/install.ps1 | iex
```

Or clone directly:
```bash
git clone https://github.com/RBraga01/builder-growth
cp -rn builder-growth/skills your-project/
cp -rn builder-growth/.claude your-project/
```

## The builder-* Ecosystem

| Pack | Domain | Skills | Agents |
|---|---|---|---|
| [A Team](https://github.com/RBraga01/a-team) | Engineering baseline | 19 | 26 |
| [builder-ai](https://github.com/RBraga01/builder-ai) | LLM engineering | 8 | 5 |
| [builder-design](https://github.com/RBraga01/builder-design) | AI UI design | 8 | 5 |
| [builder-product](https://github.com/RBraga01/builder-product) | Product quality | 7 | 3 |
| **builder-growth** | Growth & messaging | 14 | 5 |

All packs share the same enforcement model: Completion Statement Formats that require real values, not summaries.

## License

MIT — Ricardo Romão Marques Braga
