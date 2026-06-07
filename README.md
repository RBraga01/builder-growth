# builder-growth — AI Growth Skills Pack v1.0.0

Skills and agents that enforce quality in AI-assisted growth work: positioning that survives the "so what?" test, copy that clears the "who cares?" test, funnels diagnosed before they are optimised, experiments designed with stopping rules before they run, retention loops defined before launch, and AI capability claims reviewed for accuracy before they ship.

**[→ Visual overview](https://rbraga01.github.io/builder-growth/)**

Works standalone or alongside [A Team](https://github.com/RBraga01/a-team), [builder-ai](https://github.com/RBraga01/builder-ai), [builder-design](https://github.com/RBraga01/builder-design), and [builder-product](https://github.com/RBraga01/builder-product).

## Skills

| Skill | What It Enforces |
|---|---|
| `positioning-audit` | Clear category, specific audience, and differentiated claim before any copy is written |
| `copy-quality-gate` | "So what?", "who cares?", and "why now?" tests before any copy ships |
| `funnel-analysis` | Leak identified and root-caused before any optimisation begins |
| `experiment-design` | Hypothesis, metric, sample size, duration, stopping rule, decision rule before any test runs |
| `retention-design` | Activation moment, habit loop, and reactivation path defined before launch |
| `ai-messaging-review` | AI capability claims reviewed for source, scope, and accuracy — no unsourced quantified claims |

## Agents

| Agent | Role |
|---|---|
| `growth-critic` (Sonnet) | Reviews positioning, copy, and experiments against skill gates; PASS / CONDITIONAL / BLOCK |
| `experiment-designer` (Sonnet) | Designs growth experiments with calculated sample sizes and pre-specified stopping rules |
| `messaging-reviewer` (Opus) | Reviews AI product messaging for sourced claims, scoped capabilities, and specific AI labels |

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
| [A Team](https://github.com/RBraga01/a-team) | Engineering baseline | 18 | 25 |
| [builder-ai](https://github.com/RBraga01/builder-ai) | LLM engineering | 8 | 5 |
| [builder-design](https://github.com/RBraga01/builder-design) | AI UI design | 8 | 5 |
| [builder-product](https://github.com/RBraga01/builder-product) | Product quality | 6 | 3 |
| **builder-growth** | Growth & messaging | 6 | 3 |

All packs share the same enforcement model: Completion Statement Formats that require real values, not summaries.

## License

MIT — Ricardo Romão Marques Braga
