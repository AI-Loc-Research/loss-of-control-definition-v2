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
| Threat Source | The AI system | The AI system bypasses safety and security measures, develops capabilities for self-replication and self-correction, conducts automated R&D, and establishes connections to external environments and the Internet of Things (IoT) without authorization; humans gradually cede agency to AI systems. | Clear |
| Objective/Harmful Outcome | Loss of human control over AI (no intention or objective is stated for the AI system; only the harmful outcome is described): 'We surrender control or find ourselves unable to resist what we do not fully understand' and 'humans gradually cede agency to AI systems' (loss of control to AI); and the AI system 'bypasses safety and security measures, develops capabilities for self-replication and self-correction, conducts automated R&D, and establishes connections to external environments and the Internet of Things (IoT) without authorization' (loss of control of AI). | Loss of control to AI: We surrender control or find ourselves unable to resist what we do not fully understand. This scenario represents a societal choice or a structural inevitability in which humans gradually cede agency to AI systems. Loss of control of AI: The AI system bypasses safety and security measures, develops capabilities for self-replication and self-correction, conducts automated R&D, and establishes connections to external environments and the Internet of Things (IoT) without authorization. | Clear |
| Capability | The AI system bypasses safety and security measures, develops capabilities for self-replication and self-correction, conducts automated R&D, and establishes connections to external environments and the Internet of Things (IoT) without authorization. | The AI system bypasses safety and security measures, develops capabilities for self-replication and self-correction, conducts automated R&D, and establishes connections to external environments and the Internet of Things (IoT) without authorization. | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Connections to external environments and the Internet of Things (IoT): the AI system 'establishes connections to external environments and the Internet of Things (IoT) without authorization.' | establishes connections to external environments and the Internet of Things (IoT) without authorization | Clear |
| Constraints/Enabling Conditions | The AI system establishes connections 'without authorization'; humans 'find ourselves unable to resist what we do not fully understand'; the loss of control to AI represents 'a societal choice or a structural inevitability in which humans gradually cede agency to AI systems.' | without authorization; We surrender control or find ourselves unable to resist what we do not fully understand; This scenario represents a societal choice or a structural inevitability in which humans gradually cede agency to AI systems | Clear |
| Target/Asset at Risk | Human control and agency ('We surrender control'; 'humans gradually cede agency to AI systems'); also the 'safety and security measures' that the AI system bypasses. | We surrender control; humans gradually cede agency to AI systems; The AI system bypasses safety and security measures | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---