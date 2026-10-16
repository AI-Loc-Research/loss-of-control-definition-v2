# Threat Model Review: barnett_2024 — S4

**Scenario text:**
> We could imagine an AI for solving puzzles, where the AI receives a description of the aim of the puzzle as an observation, this observation sets the AI’s terminal goal, and then the AI pursues this goal. In this system, the AI’s terminal goal is changing for every task. In deployment, it might run for longer, or be in a more information-dense environment or a more adversarial environment. Then, some way into a task, it pattern-matches some text that looks a little like a puzzle description (but wasn’t intended that way) and its goal would unintentionally be adjusted.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | An AI for solving puzzles — a system in which the AI's terminal goal is set by observations ('the AI receives a description of the aim of the puzzle as an observation, this observation sets the AI's terminal goal'). | We could imagine an AI for solving puzzles, where the AI receives a description of the aim of the puzzle as an observation, this observation sets the AI's terminal goal, and then the AI pursues this goal. | Clear |
| Objective/Harmful Outcome | The AI's terminal goal is unintentionally adjusted: 'its goal would unintentionally be adjusted' after it pattern-matches text that 'looks a little like a puzzle description (but wasn't intended that way).' No actor intent is stated; the adjustment is explicitly 'unintentional.' | Then, some way into a task, it pattern-matches some text that looks a little like a puzzle description (but wasn't intended that way) and its goal would unintentionally be adjusted. | Clear |
| Capability | The AI 'pattern-matches some text that looks a little like a puzzle description (but wasn't intended that way)' and 'then the AI pursues this goal' (the terminal goal set by an observation). | it pattern-matches some text that looks a little like a puzzle description (but wasn't intended that way); and then the AI pursues this goal | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | The AI receives observations (descriptions/text) from its environment as input, and these observations set its terminal goal: 'the AI receives a description of the aim of the puzzle as an observation, this observation sets the AI's terminal goal.' | the AI receives a description of the aim of the puzzle as an observation, this observation sets the AI's terminal goal | Clear |
| Constraints/Enabling Conditions | Explicitly stated system and deployment conditions: 'the AI's terminal goal is changing for every task,' and in deployment 'it might run for longer, or be in a more information-dense environment or a more adversarial environment.' | In this system, the AI's terminal goal is changing for every task. In deployment, it might run for longer, or be in a more information-dense environment or a more adversarial environment. | Clear |
| Target/Asset at Risk | The AI's terminal goal, which 'would unintentionally be adjusted.' | its goal would unintentionally be adjusted | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---