# Threat Model Review: amodei_2026 — S3

**Scenario text:**
> The usual argument for this (which goes back at least 20 years and probably much earlier) is that if an AI model is trained in a wide variety of environments to agentically achieve a wide variety of goals—for example, writing an app, proving a theorem, designing a drug, etc.—there are certain common strategies that help with all of these goals, and one key strategy is gaining as much power as possible in any environment. So, after being trained on a large number of diverse environments that involve reasoning about how to accomplish very expansive tasks, and where power-seeking is an effective method for accomplishing those tasks, the AI model will “generalize the lesson,” and develop either an inherent tendency to seek power, or a tendency to reason about each task it is given in a way that predictably causes it to seek power as a means to accomplish that task. They will then apply that tendency to the real world (which to them is just another task), and will seek power in it, at the expense of humans.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | an AI model | if an AI model is trained in a wide variety of environments to agentically achieve a wide variety of goals | Clear |
| Objective/Harmful Outcome | will seek power in it, at the expense of humans | will seek power in it, at the expense of humans | Clear |
| Capability | trained in a wide variety of environments to agentically achieve a wide variety of goals; gaining as much power as possible in any environment; apply that tendency to the real world | agentically achieve a wide variety of goals; gaining as much power as possible in any environment; apply that tendency to the real world | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | trained in a wide variety of environments; apply that tendency to the real world | trained in a wide variety of environments; apply that tendency to the real world | Clear |
| Constraints/Enabling Conditions | after being trained on a large number of diverse environments that involve reasoning about how to accomplish very expansive tasks, and where power-seeking is an effective method for accomplishing those tasks | after being trained on a large number of diverse environments that involve reasoning about how to accomplish very expansive tasks, and where power-seeking is an effective method for accomplishing those tasks | Clear |
| Target/Asset at Risk | humans | at the expense of humans | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---