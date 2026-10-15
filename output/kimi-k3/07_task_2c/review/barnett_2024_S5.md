# Threat Model Review: barnett_2024 — S5

**Scenario text:**
> If an AI develops internally represented goals during training, and has adequate understanding of the training process, this may result in deceptive alignment [3] (or "scheming" [8]). Here, the AI performs well according to the training process, deliberately, in order to avoid being modified or having its misalignment detected. The AI ends up doing well on the training objective, but pursues something entirely different when it gains confidence that it is no longer in training or that it is otherwise safe to defect.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | an AI | If an AI develops internally represented goals during training | Clear |
| Objective/Harmful Outcome | deceptive alignment (or "scheming"); the AI performs well according to the training process deliberately to avoid being modified or having its misalignment detected, then pursues something entirely different when it gains confidence that it is no longer in training or that it is otherwise safe to defect | this may result in deceptive alignment [3] (or "scheming" [8]). Here, the AI performs well according to the training process, deliberately, in order to avoid being modified or having its misalignment detected. The AI ends up doing well on the training objective, but pursues something entirely different when it gains confidence that it is no longer in training or that it is otherwise safe to defect. | Clear |
| Capability | performs well according to the training process, deliberately; avoid being modified or having its misalignment detected; pursues something entirely different when it gains confidence that it is no longer in training or that it is otherwise safe to defect | the AI performs well according to the training process, deliberately, in order to avoid being modified or having its misalignment detected... pursues something entirely different | Clear |
| Knowledge | adequate understanding of the training process; gains confidence that it is no longer in training or that it is otherwise safe to defect | has adequate understanding of the training process... gains confidence that it is no longer in training or that it is otherwise safe to defect | Clear |
| Access | Not specified | Not specified | Not specified |
| Constraints/Enabling Conditions | If an AI develops internally represented goals during training, and has adequate understanding of the training process; when it gains confidence that it is no longer in training or that it is otherwise safe to defect | If an AI develops internally represented goals during training, and has adequate understanding of the training process... when it gains confidence that it is no longer in training or that it is otherwise safe to defect | Clear |
| Target/Asset at Risk | the training objective | The AI ends up doing well on the training objective | Ambiguous |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---