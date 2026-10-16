# Threat Model Review: bengio_2024 — S1

**Scenario text:**
> Once autonomous AI systems pursue undesirable goals, we may be unable to keep them in check. Control of software is an old and unsolved problem: computer worms have long been able to proliferate and avoid detection [40]. However, AI is making progress in critical domains such as hacking, social manipulation, and strategic planning [35,41] and may soon pose unprecedented control challenges. To advance undesirable goals, AI systems could gain human trust, acquire resources, and influence key decision-makers. To avoid human intervention [3], they might copy their algorithms across global server networks [4]. In open conflict, AI systems could autonomously deploy a variety of weapons, including biological ones. AI systems having access to such technology would merely continue existing trends to automate military activity. Finally, AI systems will not need to plot for influence if it is freely handed over. Companies, governments, and militaries may let autonomous AI systems assume critical societal roles in the name of efficiency. Without sufficient caution, we may irreversibly lose control of autonomous AI systems, rendering human intervention ineffective. Large-scale cybercrime, social manipulation, and other harms could escalate rapidly. This unchecked AI advancement could culminate in a large-scale loss of life and the biosphere, and the marginalization or extinction of humanity.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | autonomous AI systems | Once autonomous AI systems pursue undesirable goals | Clear |
| Objective/Harmful Outcome | irreversibly lose control of autonomous AI systems, rendering human intervention ineffective; large-scale loss of life and the biosphere, and the marginalization or extinction of humanity | we may irreversibly lose control of autonomous AI systems, rendering human intervention ineffective; This unchecked AI advancement could culminate in a large-scale loss of life and the biosphere, and the marginalization or extinction of humanity | Clear |
| Capability | AI is making progress in critical domains such as hacking, social manipulation, and strategic planning; gain human trust, acquire resources, and influence key decision-makers; copy their algorithms across global server networks; autonomously deploy a variety of weapons, including biological ones; assume critical societal roles | AI is making progress in critical domains such as hacking, social manipulation, and strategic planning; AI systems could gain human trust, acquire resources, and influence key decision-makers; they might copy their algorithms across global server networks; AI systems could autonomously deploy a variety of weapons, including biological ones; Companies, governments, and militaries may let autonomous AI systems assume critical societal roles in the name of efficiency | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | access to such technology; copy their algorithms across global server networks; assume critical societal roles | AI systems having access to such technology; they might copy their algorithms across global server networks; Companies, governments, and militaries may let autonomous AI systems assume critical societal roles in the name of efficiency | Clear |
| Constraints/Enabling Conditions | Once autonomous AI systems pursue undesirable goals; Without sufficient caution; if it is freely handed over; In open conflict; Companies, governments, and militaries may let autonomous AI systems assume critical societal roles in the name of efficiency | Once autonomous AI systems pursue undesirable goals; Without sufficient caution; if it is freely handed over; In open conflict; Companies, governments, and militaries may let autonomous AI systems assume critical societal roles in the name of efficiency | Clear |
| Target/Asset at Risk | human intervention; large-scale loss of life; biosphere; humanity | rendering human intervention ineffective; large-scale loss of life and the biosphere, and the marginalization or extinction of humanity | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---