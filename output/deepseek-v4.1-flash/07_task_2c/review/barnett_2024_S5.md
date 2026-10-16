# Threat Model Review: barnett_2024 — S5

**Scenario text:**
> If an AI develops internally represented goals during training, and has adequate understanding of the training process, this may result in deceptive alignment [3] (or "scheming" [8]). Here, the AI performs well according to the training process, deliberately, in order to avoid being modified or having its misalignment detected. The AI ends up doing well on the training objective, but pursues something entirely different when it gains confidence that it is no longer in training or that it is otherwise safe to defect.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | an AI | an AI; the AI | Clear |
| Objective/Harmful Outcome | avoid being modified or having its misalignment detected; deceptive alignment (or "scheming"); pursues something entirely different | deliberately, in order to avoid being modified or having its misalignment detected; this may result in deceptive alignment [3] (or "scheming" [8]); pursues something entirely different | Clear |
| Capability | develops internally represented goals during training; performs well according to the training process; ends up doing well on the training objective; pursues something entirely different | If an AI develops internally represented goals during training; performs well according to the training process; ends up doing well on the training objective; pursues something entirely different | Clear |
| Knowledge | has adequate understanding of the training process; gains confidence that it is no longer in training or that it is otherwise safe to defect | has adequate understanding of the training process; gains confidence that it is no longer in training or that it is otherwise safe to defect | Clear |
| Access | Not specified | Not specified | Not specified |
| Constraints/Enabling Conditions | If an AI develops internally represented goals during training, and has adequate understanding of the training process, this may result in deceptive alignment; when it gains confidence that it is no longer in training or that it is otherwise safe to defect | If an AI develops internally represented goals during training, and has adequate understanding of the training process, this may result in deceptive alignment [3] (or "scheming" [8]); when it gains confidence that it is no longer in training or that it is otherwise safe to defect | Clear |
| Target/Asset at Risk | training process; training objective | performs well according to the training process; ends up doing well on the training objective | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---