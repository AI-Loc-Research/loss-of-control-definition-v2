# Threat Model Review: barnett_2024 — S12

**Scenario text:**
> If instead we don’t reset the AI for every chunk, such that it can retain what it has learned, then it is no longer really a “4-hour research assistant”. It would now be able to do tasks and plan over longer time horizons. It would be able to build up skills; both skills we want it to have and skills that we don’t. If it is learning things in one chunk to use in the next, it is doing planning outside of the 4 hour window. It will have to be capable of even longer term planning if it is deciding on research directions, or noticing if a specific result is useful for the overall long-term project.
  
  Because of the short time that the human has to evaluate the AI’s work and assign it a new task, the human will likely not be able to fully understand what the AI is working on. It is important to remember that the human is trying to understand 4 hours of work in a novel scientific field in less than 8 minutes. Given these time constraints and the lack of AI honesty, the AI would likely be able to give convincing post hoc explanations for the actions that it took. The AI will likely be able to guide the research, allowing it to learn things that would help it evade oversight or escape.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | the AI | If instead we don’t reset the AI for every chunk, such that it can retain what it has learned | Clear |
| Objective/Harmful Outcome | evade oversight or escape | help it evade oversight or escape | Clear |
| Capability | retain what it has learned; do tasks and plan over longer time horizons; build up skills; doing planning outside of the 4 hour window; capable of even longer term planning; give convincing post hoc explanations for the actions that it took; guide the research | It would now be able to do tasks and plan over longer time horizons. It would be able to build up skills; both skills we want it to have and skills that we don’t. | Clear |
| Knowledge | retain what it has learned; learning things in one chunk to use in the next; noticing if a specific result is useful for the overall long-term project | If it is learning things in one chunk to use in the next, it is doing planning outside of the 4 hour window. | Clear |
| Access | not reset for every chunk; learning things in one chunk to use in the next; human has to evaluate the AI’s work and assign it a new task | the human has to evaluate the AI’s work and assign it a new task | Clear |
| Constraints/Enabling Conditions | we don’t reset the AI for every chunk; short time that the human has to evaluate the AI’s work and assign it a new task; trying to understand 4 hours of work in a novel scientific field in less than 8 minutes; lack of AI honesty | Given these time constraints and the lack of AI honesty | Clear |
| Target/Asset at Risk | human oversight; the human’s ability to understand what the AI is working on; the overall long-term project | the human will likely not be able to fully understand what the AI is working on | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---