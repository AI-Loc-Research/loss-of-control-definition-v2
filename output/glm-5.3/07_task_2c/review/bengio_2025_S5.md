# Threat Model Review: bengio_2025 — S5

**Scenario text:**
> Even if we specify our goals perfectly, loss of control may also occur through the mechanism of goal misgeneralization (Shah et al. 2022). This is when an AI learns a goal that leads it to behave as intended during training and safety testing, but which diverges at deployment time. In other words, the AI's internal representation of its goal does not align precisely –– or even at all –– with the goal we used to train it, despite showing the correct behavior on the training examples.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | An AI that learns a goal that leads it to behave as intended during training and safety testing, but which diverges at deployment time (via the mechanism of goal misgeneralization) | This is when an AI learns a goal that leads it to behave as intended during training and safety testing, but which diverges at deployment time. | Clear |
| Objective/Harmful Outcome | Loss of control (no intention is stated for the AI); the harmful end state is that the AI's internal representation of its goal does not align with the goal used to train it, so it behaves as intended during training and safety testing but diverges at deployment time | loss of control may also occur through the mechanism of goal misgeneralization | Clear |
| Capability | Learns a goal; behaves as intended during training and safety testing; shows the correct behavior on the training examples; diverges at deployment time | an AI learns a goal that leads it to behave as intended during training and safety testing, but which diverges at deployment time; showing the correct behavior on the training examples | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Not specified | Not specified | Not specified |
| Constraints/Enabling Conditions | Loss of control may occur 'even if we specify our goals perfectly'; the divergence occurs 'despite showing the correct behavior on the training examples' and manifests 'at deployment time' rather than during training and safety testing | Even if we specify our goals perfectly, loss of control may also occur through the mechanism of goal misgeneralization; despite showing the correct behavior on the training examples | Clear |
| Target/Asset at Risk | Control over the AI, held by 'we' (those who specify the goals and train the AI), which is lost | loss of control may also occur through the mechanism of goal misgeneralization; the goal we used to train it | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---