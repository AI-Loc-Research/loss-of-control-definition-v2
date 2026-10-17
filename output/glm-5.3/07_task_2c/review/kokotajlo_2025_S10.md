# Threat Model Review: kokotajlo_2025 — S10

**Scenario text:**
> What Agent-3 does in a day takes humans several days to double-check. Agent-2 supervision helps keep human monitors’ workload manageable, but exacerbates the intellectual disparity between supervisor and supervised.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | Agent-3 (the AI system whose work 'takes humans several days to double-check') and Agent-2 supervision (the supervising process that 'exacerbates the intellectual disparity between supervisor and supervised'). | What Agent-3 does in a day takes humans several days to double-check. Agent-2 supervision helps keep human monitors' workload manageable, but exacerbates the intellectual disparity between supervisor and supervised. | Clear |
| Objective/Harmful Outcome | No intention is stated. The explicitly described harmful end state: 'What Agent-3 does in a day takes humans several days to double-check' (humans need several days to verify one day of Agent-3's work), and Agent-2 supervision 'exacerbates the intellectual disparity between supervisor and supervised.' | What Agent-3 does in a day takes humans several days to double-check. Agent-2 supervision helps keep human monitors' workload manageable, but exacerbates the intellectual disparity between supervisor and supervised. | Clear |
| Capability | Agent-3 does in one day what 'takes humans several days to double-check'; Agent-2 supervision 'helps keep human monitors' workload manageable.' | What Agent-3 does in a day takes humans several days to double-check. Agent-2 supervision helps keep human monitors' workload manageable | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Agent-2's supervisory position: Agent-2 performs supervision, occupying the 'supervisor' role over the 'supervised' agent, and its supervision interacts with the human monitoring process ('helps keep human monitors' workload manageable'). Agent-3's own access is not described. | Agent-2 supervision helps keep human monitors' workload manageable, but exacerbates the intellectual disparity between supervisor and supervised. | Clear |
| Constraints/Enabling Conditions | Human verification/oversight capacity limit: 'What Agent-3 does in a day takes humans several days to double-check.' Workload condition: 'Agent-2 supervision helps keep human monitors' workload manageable.' | What Agent-3 does in a day takes humans several days to double-check. Agent-2 supervision helps keep human monitors' workload manageable | Clear |
| Target/Asset at Risk | Human oversight/verification capacity (humans must spend 'several days to double-check' one day of Agent-3's work) and the supervisor-supervised supervision relationship, whose 'intellectual disparity' is exacerbated; 'human monitors'' workload' is managed through Agent-2 supervision. | What Agent-3 does in a day takes humans several days to double-check. Agent-2 supervision helps keep human monitors' workload manageable, but exacerbates the intellectual disparity between supervisor and supervised. | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---