# Threat Model Review: bengio_2025 — S4

**Scenario text:**
> Loss of control may arise due to goal misspecification (Rudner and Toner 2021). This failure mode occurs when there are multiple interpretations of a goal, i.e., it is poorly specified or under-specified and may be pursued in a way that humans did not intend. Goal misspecification is the result of a fundamental difficulty in precisely defining what we find unacceptable in AI behavior. If an AI takes life-and-death decisions, we would like it to act ethically. It unfortunately appears impossible to formally articulate the difference between morally right and wrong behavior without enumerating all the possible cases. This is similar to the difficulty of stating laws in legal language without having any loopholes for humans to exploit. When it is in one's interest to find a way around the law, by satisfying its letter but not its spirit, one often dedicates substantial effort to do so.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | AI with a poorly specified or under-specified goal (goal misspecification) | Loss of control may arise due to goal misspecification... If an AI takes life-and-death decisions | Ambiguous |
| Objective/Harmful Outcome | Loss of control; the goal "may be pursued in a way that humans did not intend" | Loss of control may arise due to goal misspecification... it is poorly specified or under-specified and may be pursued in a way that humans did not intend | Clear |
| Capability | takes life-and-death decisions | If an AI takes life-and-death decisions | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Not specified | Not specified | Not specified |
| Constraints/Enabling Conditions | goal is poorly specified or under-specified; it is impossible to formally articulate the difference between morally right and wrong behavior without enumerating all the possible cases | This failure mode occurs when there are multiple interpretations of a goal, i.e., it is poorly specified or under-specified... It unfortunately appears impossible to formally articulate the difference between morally right and wrong behavior without enumerating all the possible cases | Clear |
| Target/Asset at Risk | Not specified | Not specified | Not specified |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---