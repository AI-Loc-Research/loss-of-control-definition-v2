# Threat Model Review: ist_loss_of_control — S8

**Scenario text:**
> Consider, for example, how the citizens of the Soviet Union (a large number of humans) lost control over something they created (a political system). Two parallel processes took place:
  » Loss of control to the political system: People initially supported Bolshevik promises of peace, land redistribution, and workers’ control. They gradually ceded control of property and freedom of speech to the party.
  » Loss of control of the political system: The system developed emergent behaviors that no actor, creator, or participant fully controlled. Leadership maintained the system primarily to maintain the system itself. The instrumental goal (regime preservation) had displaced the terminal goal (fulfilling communism).
  How could this translate into AI loss of control?
  » Loss of control to AI: We surrender control or find ourselves unable to resist what we do not fully understand. This scenario represents a societal choice or a structural inevitability in which humans gradually cede agency to AI systems.
  » Loss of control of AI: The AI system bypasses safety and security measures, develops capabilities for self-replication and self-correction, conducts automated R&D, and establishes connections to external environments and the Internet of Things (IoT) without authorization.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | AI system | The AI system bypasses safety and security measures, develops capabilities for self-replication and self-correction, conducts automated R&D, and establishes connections to external environments and the Internet of Things (IoT) without authorization. | Clear |
| Objective/Harmful Outcome | AI loss of control; loss of control to AI; loss of control of AI; humans gradually cede agency to AI systems | AI loss of control; Loss of control to AI: We surrender control or find ourselves unable to resist what we do not fully understand; Loss of control of AI: The AI system bypasses safety and security measures, develops capabilities for self-replication and self-correction, conducts automated R&D, and establishes connections to external environments and the Internet of Things (IoT) without authorization; humans gradually cede agency to AI systems. | Clear |
| Capability | bypasses safety and security measures, develops capabilities for self-replication and self-correction, conducts automated R&D, and establishes connections to external environments and the Internet of Things (IoT) without authorization | The AI system bypasses safety and security measures, develops capabilities for self-replication and self-correction, conducts automated R&D, and establishes connections to external environments and the Internet of Things (IoT) without authorization. | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | establishes connections to external environments and the Internet of Things (IoT) without authorization | establishes connections to external environments and the Internet of Things (IoT) without authorization | Clear |
| Constraints/Enabling Conditions | without authorization; bypasses safety and security measures; societal choice or a structural inevitability; what we do not fully understand | without authorization; bypasses safety and security measures; This scenario represents a societal choice or a structural inevitability; what we do not fully understand | Clear |
| Target/Asset at Risk | human agency; control; safety and security measures | humans gradually cede agency to AI systems; We surrender control; bypasses safety and security measures | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---