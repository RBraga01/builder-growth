# Orchestration

## Purpose

Define how builder-growth can be invoked by an external orchestrator, an agent
workflow, or a person running a manual project workflow. builder-growth is
autonomous: it has no dependency on any specific upstream planning system and
exposes the same capabilities regardless of who calls it.

## Who Can Use builder-growth

builder-growth is consumable by:

- **Claude Code** — invoke skills and agents directly from a session;
- **Codex** — call the same skills/agents from a Codex-driven workflow;
- **External orchestrators** — any upstream planning system that routes growth
  work to this pack;
- **Agent workflows** — multi-agent pipelines that delegate growth tasks;
- **Manual project workflows** — a person following the pack's skills by hand.

## Role

builder-growth owns reusable growth capabilities for strategy, channel
selection, offer validation, campaign planning, launch planning, metrics,
funnel diagnosis, experiments, retention, pricing review, social proof review,
copy quality, and AI messaging review.

## When To Call builder-growth

Route work here when a project needs:

- growth strategy;
- channel selection;
- offer validation;
- campaign planning;
- launch planning;
- growth metrics;
- funnel diagnosis;
- experiment design;
- retention design;
- pricing page review;
- social proof review;
- external copy review;
- AI messaging claims review.

## Required Inputs

The calling workflow must supply:

- project brief;
- target user or segment;
- current validation state;
- product scope;
- business goal;
- constraints;
- available evidence;
- target repository;
- decision needed.

## Expected Outputs

- growth strategy document;
- channel audit;
- offer quality gate;
- campaign brief;
- launch plan;
- growth metrics plan;
- funnel analysis;
- experiment design;
- retention design;
- pricing review;
- social proof review;
- copy review;
- AI messaging review.

## Blocking Gates

builder-growth may block launch when:

- no target segment is defined;
- no growth goal exists;
- channel selection is unsupported;
- offer is unclear;
- copy fails the three tests;
- claims are unsourced;
- AI claims are vague or overstated;
- experiment lacks sample size or stopping rule;
- funnel work starts without leak diagnosis;
- launch has no success metric;
- pricing page creates confusion or unmanaged risk;
- social proof is unsourced or misleading.

## Handoff Back To The Caller

Every builder-growth output must include:

- file path;
- decision;
- blockers;
- risks;
- required next action;
- proof generated.
