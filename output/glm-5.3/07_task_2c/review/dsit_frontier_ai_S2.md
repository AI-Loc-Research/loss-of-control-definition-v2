# Threat Model Review: dsit_frontier_ai — S2

**Scenario text:**
> A bad actor could give an AI system an objective that causes it to reduce human control, for example a self-preservation objective. If there are safeguards in place, bad actors might dismantle them.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | A bad actor; also the AI system, which is given an objective that causes it to reduce human control | A bad actor could give an AI system an objective that causes it to reduce human control, for example a self-preservation objective. If there are safeguards in place, bad actors might dismantle them. | Clear |
| Objective/Harmful Outcome | Reduction of human control (the bad actor could give the AI system an objective that causes it to reduce human control, for example a self-preservation objective) | an objective that causes it to reduce human control, for example a self-preservation objective | Clear |
| Capability | The bad actor could give an AI system an objective that causes it to reduce human control; bad actors might dismantle safeguards; the AI system, given such an objective, reduces human control | could give an AI system an objective that causes it to reduce human control, for example a self-preservation objective; bad actors might dismantle them | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Not specified | could give an AI system an objective (implies interaction with the AI system, but no explicit route or position of access is stated) | Ambiguous |
| Constraints/Enabling Conditions | If there are safeguards in place, bad actors might dismantle them (the presence of safeguards is an explicit condition) | If there are safeguards in place, bad actors might dismantle them | Clear |
| Target/Asset at Risk | Human control (reduced by the AI system); safeguards (dismantled by bad actors) | an objective that causes it to reduce human control; if there are safeguards in place, bad actors might dismantle them | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---