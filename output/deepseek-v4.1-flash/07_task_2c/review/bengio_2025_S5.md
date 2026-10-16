# Threat Model Review: bengio_2025 — S5

**Scenario text:**
> Even if we specify our goals perfectly, loss of control may also occur through the mechanism of goal misgeneralization (Shah et al. 2022). This is when an AI learns a goal that leads it to behave as intended during training and safety testing, but which diverges at deployment time. In other words, the AI's internal representation of its goal does not align precisely –– or even at all –– with the goal we used to train it, despite showing the correct behavior on the training examples.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | an AI | an AI learns a goal that leads it to behave as intended during training and safety testing, but which diverges at deployment time | Clear |
| Objective/Harmful Outcome | loss of control | loss of control may also occur through the mechanism of goal misgeneralization | Clear |
| Capability | learns a goal that leads it to behave as intended during training and safety testing, but which diverges at deployment time | an AI learns a goal that leads it to behave as intended during training and safety testing, but which diverges at deployment time | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Not specified | Not specified | Not specified |
| Constraints/Enabling Conditions | Even if we specify our goals perfectly; through the mechanism of goal misgeneralization; during training and safety testing; at deployment time; despite showing the correct behavior on the training examples | Even if we specify our goals perfectly, loss of control may also occur through the mechanism of goal misgeneralization (Shah et al. 2022). This is when an AI learns a goal that leads it to behave as intended during training and safety testing, but which diverges at deployment time. In other words, the AI's internal representation of its goal does not align precisely –– or even at all –– with the goal we used to train it, despite showing the correct behavior on the training examples. | Clear |
| Target/Asset at Risk | control | loss of control may also occur | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---