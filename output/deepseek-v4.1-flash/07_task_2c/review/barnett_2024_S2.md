# Threat Model Review: barnett_2024 — S2

**Scenario text:**
> One might imagine an AI that is being trained using reinforcement learning to solve difficult puzzles, but where there is a way to hack the solution-checker. With good oversight, the AI would receive low reward for hacking the solution-checker during training, and one might hope that this correctly puts a “morality-like” constraint into the AI’s goal. But there is another way it might update: the training could insert a false belief into the agent. This might be a belief that hacking the solution-checker doesn’t work, or leads to some other bad consequence, or is more difficult than it truly is. Later, if the AI updates this belief (because the belief was false), it may attempt to hack the solution-checker.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | an AI that is being trained using reinforcement learning to solve difficult puzzles | One might imagine an AI that is being trained using reinforcement learning to solve difficult puzzles | Clear |
| Objective/Harmful Outcome | it may attempt to hack the solution-checker | it may attempt to hack the solution-checker | Clear |
| Capability | may attempt to hack the solution-checker | it may attempt to hack the solution-checker | Clear |
| Knowledge | a false belief that hacking the solution-checker doesn’t work, or leads to some other bad consequence, or is more difficult than it truly is | the training could insert a false belief into the agent. This might be a belief that hacking the solution-checker doesn’t work, or leads to some other bad consequence, or is more difficult than it truly is. | Clear |
| Access | Not specified | Not specified | Not specified |
| Constraints/Enabling Conditions | With good oversight, the AI would receive low reward for hacking the solution-checker during training; the training could insert a false belief into the agent; Later, if the AI updates this belief (because the belief was false) | With good oversight, the AI would receive low reward for hacking the solution-checker during training; the training could insert a false belief into the agent; Later, if the AI updates this belief (because the belief was false) | Clear |
| Target/Asset at Risk | solution-checker | solution-checker | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---