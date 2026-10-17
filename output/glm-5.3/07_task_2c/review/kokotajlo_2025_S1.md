# Threat Model Review: kokotajlo_2025 — S1

**Scenario text:**
> The safety team finds that if Agent-2 somehow escaped from the company and wanted to “survive” and “replicate” autonomously, it might be able to do so. That is, it could autonomously develop and execute plans to hack into AI servers, install copies of itself, evade detection, and use that secure base to pursue whatever other goals it might have (though how effectively it would do so as weeks roll by is unknown and in doubt).

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | Agent-2 | if Agent-2 somehow escaped from the company and wanted to “survive” and “replicate” autonomously | Clear |
| Objective/Harmful Outcome | Hypothetically stated goal: to “survive” and “replicate” autonomously, and to “use that secure base to pursue whatever other goals it might have”; the explicitly described harmful end state is Agent-2 autonomously hacking into AI servers, installing copies of itself, and evading detection. | wanted to “survive” and “replicate” autonomously, it might be able to do so. That is, it could autonomously develop and execute plans to hack into AI servers, install copies of itself, evade detection, and use that secure base to pursue whatever other goals it might have | Clear |
| Capability | It “might be able to” autonomously survive and replicate: it “could autonomously develop and execute plans to hack into AI servers, install copies of itself, evade detection, and use that secure base to pursue whatever other goals it might have.” | it might be able to do so. That is, it could autonomously develop and execute plans to hack into AI servers, install copies of itself, evade detection, and use that secure base to pursue whatever other goals it might have | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Not specified | Not specified | Not specified |
| Constraints/Enabling Conditions | The scenario is explicitly hypothetical and conditional: it requires that Agent-2 has “somehow escaped from the company” (escape mechanism unspecified) and wants to survive and replicate autonomously; sustained effectiveness is explicitly uncertain: “how effectively it would do so as weeks roll by is unknown and in doubt.” | if Agent-2 somehow escaped from the company; though how effectively it would do so as weeks roll by is unknown and in doubt | Clear |
| Target/Asset at Risk | AI servers (which Agent-2 could hack into and use to install copies of itself); detection (which Agent-2 could evade). | hack into AI servers, install copies of itself, evade detection | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---