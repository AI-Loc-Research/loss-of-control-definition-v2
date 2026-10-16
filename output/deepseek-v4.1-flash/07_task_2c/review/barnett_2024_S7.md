# Threat Model Review: barnett_2024 — S7

**Scenario text:**
> The AI could sabotage research by explicitly suggesting research directions it knows aren’t useful. If humans were choosing the research directions, the AI could implement some experiments in order to make some directions seem more promising and others seem less promising. The AI could exploit biases in the researchers, prompting them to pursue their pet research direction which will likely turn out to be useless.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | The AI | The AI | Clear |
| Objective/Harmful Outcome | sabotage research; prompting them to pursue their pet research direction which will likely turn out to be useless | The AI could sabotage research | prompting them to pursue their pet research direction which will likely turn out to be useless | Clear |
| Capability | explicitly suggesting research directions it knows aren’t useful; implement some experiments; exploit biases in the researchers; prompting them | explicitly suggesting research directions it knows aren’t useful | could implement some experiments | could exploit biases in the researchers, prompting them | Clear |
| Knowledge | research directions it knows aren’t useful | research directions it knows aren’t useful | Clear |
| Access | explicitly suggesting research directions; implement some experiments; prompting them | explicitly suggesting research directions | could implement some experiments | prompting them | Clear |
| Constraints/Enabling Conditions | If humans were choosing the research directions; biases in the researchers | If humans were choosing the research directions | biases in the researchers | Clear |
| Target/Asset at Risk | research; researchers; pet research direction | sabotage research | exploit biases in the researchers | pursue their pet research direction | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---