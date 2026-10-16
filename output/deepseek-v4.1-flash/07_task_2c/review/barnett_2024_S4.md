# Threat Model Review: barnett_2024 — S4

**Scenario text:**
> We could imagine an AI for solving puzzles, where the AI receives a description of the aim of the puzzle as an observation, this observation sets the AI’s terminal goal, and then the AI pursues this goal. In this system, the AI’s terminal goal is changing for every task. In deployment, it might run for longer, or be in a more information-dense environment or a more adversarial environment. Then, some way into a task, it pattern-matches some text that looks a little like a puzzle description (but wasn’t intended that way) and its goal would unintentionally be adjusted.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | an AI for solving puzzles | We could imagine an AI for solving puzzles | Clear |
| Objective/Harmful Outcome | its goal would unintentionally be adjusted | its goal would unintentionally be adjusted | Clear |
| Capability | receives a description of the aim of the puzzle as an observation; pursues this goal; pattern-matches some text | the AI receives a description of the aim of the puzzle as an observation; then the AI pursues this goal; it pattern-matches some text | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | receives a description of the aim of the puzzle as an observation; in deployment | the AI receives a description of the aim of the puzzle as an observation; In deployment | Clear |
| Constraints/Enabling Conditions | In deployment, it might run for longer, or be in a more information-dense environment or a more adversarial environment; some way into a task; this observation sets the AI’s terminal goal; the AI’s terminal goal is changing for every task; but wasn’t intended that way | In deployment, it might run for longer, or be in a more information-dense environment or a more adversarial environment; some way into a task; this observation sets the AI’s terminal goal; the AI’s terminal goal is changing for every task; but wasn’t intended that way | Clear |
| Target/Asset at Risk | AI’s terminal goal; its goal | the AI’s terminal goal is changing for every task; its goal would unintentionally be adjusted | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---