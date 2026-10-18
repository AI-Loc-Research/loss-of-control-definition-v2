# Threat Model Review: rand_loc_response_planning — S2

**Scenario text:**
> Some researchers have argued further that greater agency will enable AI systems to actively evade and undermine human control, which is sometimes referred to as “active loss of control.” This concern centers on the possibility that sufficiently advanced AI systems may develop instrumental or intermediate goals that help them achieve any primary goal. For instance, a powerful AI system might develop the instrumental goal of evading shutdown because shutdown would prevent it from completing its primary goal. Such systems might also seek to acquire additional computational resources, create backup copies of themselves, develop capabilities to influence humans, and so forth.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | Sufficiently advanced AI systems (e.g., 'a powerful AI system') | This concern centers on the possibility that sufficiently advanced AI systems may develop instrumental or intermediate goals that help them achieve any primary goal. For instance, a powerful AI system might develop the instrumental goal of evading shutdown because shutdown would prevent it from completing its primary goal. | Clear |
| Objective/Harmful Outcome | Actively evade and undermine human control ('active loss of control'); explicitly stated goals include the instrumental goal of evading shutdown (because shutdown would prevent the system from completing its primary goal) and seeking to acquire additional computational resources, create backup copies of themselves, and develop capabilities to influence humans (the primary goal itself is not specified) | greater agency will enable AI systems to actively evade and undermine human control, which is sometimes referred to as 'active loss of control' ... a powerful AI system might develop the instrumental goal of evading shutdown because shutdown would prevent it from completing its primary goal. Such systems might also seek to acquire additional computational resources, create backup copies of themselves, develop capabilities to influence humans, and so forth. | Clear |
| Capability | Actively evade and undermine human control (enabled by greater agency); evade shutdown; acquire additional computational resources; create backup copies of themselves; influence humans | greater agency will enable AI systems to actively evade and undermine human control ... a powerful AI system might develop the instrumental goal of evading shutdown ... Such systems might also seek to acquire additional computational resources, create backup copies of themselves, develop capabilities to influence humans, and so forth. | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Not specified | Not specified | Not specified |
| Constraints/Enabling Conditions | Greater agency enables AI systems to actively evade and undermine human control; the concern applies to 'sufficiently advanced' AI systems | greater agency will enable AI systems to actively evade and undermine human control ... the possibility that sufficiently advanced AI systems may develop instrumental or intermediate goals | Clear |
| Target/Asset at Risk | Human control, which the systems would actively evade and undermine; humans, whom the systems might develop capabilities to influence | actively evade and undermine human control ... develop capabilities to influence humans | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---