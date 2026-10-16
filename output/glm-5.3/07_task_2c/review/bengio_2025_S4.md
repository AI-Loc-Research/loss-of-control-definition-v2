# Threat Model Review: bengio_2025 — S4

**Scenario text:**
> Loss of control may arise due to goal misspecification (Rudner and Toner 2021). This failure mode occurs when there are multiple interpretations of a goal, i.e., it is poorly specified or under-specified and may be pursued in a way that humans did not intend. Goal misspecification is the result of a fundamental difficulty in precisely defining what we find unacceptable in AI behavior. If an AI takes life-and-death decisions, we would like it to act ethically. It unfortunately appears impossible to formally articulate the difference between morally right and wrong behavior without enumerating all the possible cases. This is similar to the difficulty of stating laws in legal language without having any loopholes for humans to exploit. When it is in one's interest to find a way around the law, by satisfying its letter but not its spirit, one often dedicates substantial effort to do so.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | Goal misspecification (a failure mode/process, not an intentional actor): 'Loss of control may arise due to goal misspecification (Rudner and Toner 2021).' | Loss of control may arise due to goal misspecification (Rudner and Toner 2021). | Clear |
| Objective/Harmful Outcome | Harmful outcome only (no intention is stated for any actor): 'Loss of control' — a poorly specified or under-specified goal 'may be pursued in a way that humans did not intend.' | Loss of control may arise due to goal misspecification (Rudner and Toner 2021). This failure mode occurs when there are multiple interpretations of a goal, i.e., it is poorly specified or under-specified and may be pursued in a way that humans did not intend. | Clear |
| Capability | Not specified | If an AI takes life-and-death decisions, we would like it to act ethically. | Ambiguous |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Not specified | Not specified | Not specified |
| Constraints/Enabling Conditions | The failure mode occurs 'when there are multiple interpretations of a goal, i.e., it is poorly specified or under-specified'; goal misspecification 'is the result of a fundamental difficulty in precisely defining what we find unacceptable in AI behavior'; and 'it unfortunately appears impossible to formally articulate the difference between morally right and wrong behavior without enumerating all the possible cases.' | This failure mode occurs when there are multiple interpretations of a goal, i.e., it is poorly specified or under-specified and may be pursued in a way that humans did not intend. Goal misspecification is the result of a fundamental difficulty in precisely defining what we find unacceptable in AI behavior. | 'It unfortunately appears impossible to formally articulate the difference between morally right and wrong behavior without enumerating all the possible cases.' | Clear |
| Target/Asset at Risk | Control ('loss of control' may arise); the goal being pursued as humans intended (risk that it is 'pursued in a way that humans did not intend'); the desired ethical behavior of an AI that takes life-and-death decisions ('If an AI takes life-and-death decisions, we would like it to act ethically'). | Loss of control may arise due to goal misspecification (Rudner and Toner 2021). This failure mode occurs when there are multiple interpretations of a goal, i.e., it is poorly specified or under-specified and may be pursued in a way that humans did not intend. | 'If an AI takes life-and-death decisions, we would like it to act ethically.' | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---