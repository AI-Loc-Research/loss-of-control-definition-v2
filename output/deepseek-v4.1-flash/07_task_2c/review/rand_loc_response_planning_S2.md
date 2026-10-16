# Threat Model Review: rand_loc_response_planning — S2

**Scenario text:**
> Some researchers have argued further that greater agency will enable AI systems to actively evade and undermine human control, which is sometimes referred to as “active loss of control.” This concern centers on the possibility that sufficiently advanced AI systems may develop instrumental or intermediate goals that help them achieve any primary goal. For instance, a powerful AI system might develop the instrumental goal of evading shutdown because shutdown would prevent it from completing its primary goal. Such systems might also seek to acquire additional computational resources, create backup copies of themselves, develop capabilities to influence humans, and so forth.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | AI systems | greater agency will enable AI systems to actively evade and undermine human control | sufficiently advanced AI systems may develop instrumental or intermediate goals | a powerful AI system might develop the instrumental goal of evading shutdown | Clear |
| Objective/Harmful Outcome | active loss of control; actively evade and undermine human control; instrumental goal of evading shutdown; acquire additional computational resources; create backup copies of themselves; develop capabilities to influence humans | actively evade and undermine human control, which is sometimes referred to as “active loss of control.” | might develop the instrumental goal of evading shutdown | Such systems might also seek to acquire additional computational resources, create backup copies of themselves, develop capabilities to influence humans | Clear |
| Capability | actively evade and undermine human control; develop instrumental or intermediate goals; evading shutdown; acquire additional computational resources; create backup copies of themselves; develop capabilities to influence humans | greater agency will enable AI systems to actively evade and undermine human control | may develop instrumental or intermediate goals | might develop the instrumental goal of evading shutdown | Such systems might also seek to acquire additional computational resources, create backup copies of themselves, develop capabilities to influence humans | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Not specified | Not specified | Not specified |
| Constraints/Enabling Conditions | greater agency; sufficiently advanced AI systems; powerful AI system; shutdown would prevent it from completing its primary goal | greater agency will enable AI systems to actively evade and undermine human control | sufficiently advanced AI systems may develop instrumental or intermediate goals | a powerful AI system might develop the instrumental goal of evading shutdown | because shutdown would prevent it from completing its primary goal | Clear |
| Target/Asset at Risk | human control | actively evade and undermine human control | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---