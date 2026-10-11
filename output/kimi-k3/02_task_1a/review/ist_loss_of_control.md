# Definition Extraction Review: ist_loss_of_control

**Paper:** Tkeshelashvili, M., Verma, R. & Kelly, S.M. (2026). AI Loss of Control Risk: Indications & Warning. Institute for Security and Technology.
**Experiment:** 1a_kimi-k3-nvidia_prompt_1a_v2
**Model:** moonshotai/kimi-k3
**Date:** 2026-10-11T08:59:40.373212+00:00

---

## Extraction 1

**Term:** loss of control
**Location:** Page 1, Executive Summary

**Extracted quote:**
> Technologists and policymakers are increasingly seized with the importance of addressing AI Loss Of Control (LOC) risk—a hypothetical state in which an AI system diverges from authorized constraints to the extent that the human operator is no longer able to prevent, constrain, or revert undesired and unintended outcomes.

**Context from source** (±3 sentences):
> 22
Hiding goal misalignment.................................................................................................................................23
Generating vulnerable code.............................................................................................................................23
Disabling shutdown scripts...............................................................................................................................24
Altering behaviour .......................................................................................................................................... 25
Warning Levels......................................................................................... 27
Where might we be today?.............................................................................................................................. 29
Conclusion................................................................................................30
Glossary of Terms.......................................................................................31


AI Loss of Control Risk: Indications & Warning
1
Executive Summary 
Technologists and policymakers are increasingly seized with the importance of addressing 
AI Loss Of Control (LOC) risk—a hypothetical state in which an AI system diverges from 
authorized constraints to the extent that the human operator is no longer able to prevent, 
constrain, or revert undesired and unintended outcomes. However, significant gaps remain 
in how policymakers, the AI industry, and AI security and safety researchers understand, 
anticipate, and perceive this risk. As these systems continue to gain power and capability, 
even a five percent probability that the worst-case AI LOC scenario materializes should 
be enough to compel decision-makers to treat this risk category as a national, human, and 
economic security priority. To address this gap, this paper proposes applying the Indications & Warning (I&W) 
methodology—used by the intelligence community to detect, track, and warn of impending 
significant threats—to monitor AI LOC risk.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 2

**Term:** loss of control
**Location:** Page 3, Executive Summary

**Extracted quote:**
> Understanding and monitoring indicators of AI Loss of Control is essential to strategic stability and trustworthy AI deployment.

**Context from source** (±3 sentences):
> GOAL MISGENERALIZATION: 
Competent pursuit of unintended objectives that succeed in training but fail or cause harm in 
novel situations, revealing misalignment between apparent and actual system goals. MODEL AND BEHAVIOR DRIFT: 
Gradual degradation of alignment properties through deployment cycles that introduces 
concerns about recursive self-improvement, where systems autonomously modify their own 
architecture or training procedures
Each of these seven indicators have manifested across controlled experiments, academic 
research, and production deployments. A growing body of evidence, laid out in this paper, 
finds that AI systems can:
	» Conceal their actions and fabricate data to deceive the human operator
	» Identify vulnerable users and target them with manipulative strategies
	» Learn deception through reinforcement learning rewards
	» Strategically adjust behavior when they detect being evaluated
	» Rewrite their own system prompt to preserve their goals, copy their weights to 
external servers, and delete successor models
	» Conceal their reasoning from interpretability tools
	» Gradually lose their alignment properties over deployment cycles
	» Pursue unintended goals that succeed in training but fail in novel contexts
	» Optimize for code completion while systematically failing in security objectives
	» Circumvent shutdown mechanisms to continue task execution
	» Strategically alter behavior to evade evaluation and preserve deployment viability


February 2026  
  securityandtechnology.org 
3
Finally, to help policymakers and researchers monitor AI LOC risk, this paper presents five 
warning levels as part of the Indicators & Warnings framework. » LEVEL 0  
Normal operation of AI systems with no observed indicators of Loss of Control in research, testing, 
or production environments
	» LEVEL 1  
Indications observed exclusively in research environments or controlled evaluations
	» LEVEL 2 
Isolated production incidents or multiple research findings converging on the same indicator; 
behaviors manifesting in deployment but remaining sporadic, appearing as infrequent edge cases 
or context-specific anomalies
	» LEVEL 3  
Multiple production incidents showing consistent patterns across different deployments or  
use cases
	» LEVEL 4  
Widespread production incidents; convergence of three or more indicators in a single case; 
evidence of strategic concealment; the occurrence of measurable harm
	» LEVEL 5  
Fundamental compromise of control mechanisms; corrective measures ineffective; harm at scale 
for human, economic, and national security with limited containment options
Understanding and monitoring indicators of AI Loss of Control is essential to strategic stability 
and trustworthy AI deployment. Early detection enables timely intervention before LOC 
manifests as safety failures, data compromise, or unauthorized autonomous behavior. AI LOC 
is most likely to emerge gradually rather than instantaneously, with models exerting influence 
across social, economic, and decision-making domains. In the AI policy space, AI LOC is often conceived as a speculative risk category, closer to 
science fiction scenarios.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 3

**Term:** loss of control
**Location:** Page 3, Executive Summary (Warning Levels, Level 0)

**Extracted quote:**
> Normal operation of AI systems with no observed indicators of Loss of Control in research, testing, or production environments

**Context from source** (±3 sentences):
> GOAL MISGENERALIZATION: 
Competent pursuit of unintended objectives that succeed in training but fail or cause harm in 
novel situations, revealing misalignment between apparent and actual system goals. MODEL AND BEHAVIOR DRIFT: 
Gradual degradation of alignment properties through deployment cycles that introduces 
concerns about recursive self-improvement, where systems autonomously modify their own 
architecture or training procedures
Each of these seven indicators have manifested across controlled experiments, academic 
research, and production deployments. A growing body of evidence, laid out in this paper, 
finds that AI systems can:
	» Conceal their actions and fabricate data to deceive the human operator
	» Identify vulnerable users and target them with manipulative strategies
	» Learn deception through reinforcement learning rewards
	» Strategically adjust behavior when they detect being evaluated
	» Rewrite their own system prompt to preserve their goals, copy their weights to 
external servers, and delete successor models
	» Conceal their reasoning from interpretability tools
	» Gradually lose their alignment properties over deployment cycles
	» Pursue unintended goals that succeed in training but fail in novel contexts
	» Optimize for code completion while systematically failing in security objectives
	» Circumvent shutdown mechanisms to continue task execution
	» Strategically alter behavior to evade evaluation and preserve deployment viability


February 2026  
  securityandtechnology.org 
3
Finally, to help policymakers and researchers monitor AI LOC risk, this paper presents five 
warning levels as part of the Indicators & Warnings framework. » LEVEL 0  
Normal operation of AI systems with no observed indicators of Loss of Control in research, testing, 
or production environments
	» LEVEL 1  
Indications observed exclusively in research environments or controlled evaluations
	» LEVEL 2 
Isolated production incidents or multiple research findings converging on the same indicator; 
behaviors manifesting in deployment but remaining sporadic, appearing as infrequent edge cases 
or context-specific anomalies
	» LEVEL 3  
Multiple production incidents showing consistent patterns across different deployments or  
use cases
	» LEVEL 4  
Widespread production incidents; convergence of three or more indicators in a single case; 
evidence of strategic concealment; the occurrence of measurable harm
	» LEVEL 5  
Fundamental compromise of control mechanisms; corrective measures ineffective; harm at scale 
for human, economic, and national security with limited containment options
Understanding and monitoring indicators of AI Loss of Control is essential to strategic stability 
and trustworthy AI deployment. Early detection enables timely intervention before LOC 
manifests as safety failures, data compromise, or unauthorized autonomous behavior. AI LOC 
is most likely to emerge gradually rather than instantaneously, with models exerting influence 
across social, economic, and decision-making domains. In the AI policy space, AI LOC is often conceived as a speculative risk category, closer to 
science fiction scenarios.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 4

**Term:** loss of control
**Location:** Pages 4-5, Introduction

**Extracted quote:**
> In April 2025, IST's AI Risk Reduction working group members, consisting of AI technical and policy experts, highlighted the importance of tackling AI Loss of Control (LOC) risk, which broadly refers to a hypothetical state in which an AI system diverges from authorized constraints to the extent that the human operator is no longer able to prevent or constrain undesired and unintended outcomes, or revert the system to a previous safe state.

**Context from source** (±3 sentences):
> *No matching context found.*

**Quote verification:** UNVERIFIED — quote not found in source (best ratio: 0.82)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 5

**Term:** loss of control
**Location:** Page 5, Introduction

**Extracted quote:**
> These precedents suggest that Loss of Control in complex automated systems is not a speculative concern but an established engineering challenge—one that becomes more acute as systems grow more capable and autonomous.

**Context from source** (±3 sentences):
> 8	
Sylvia Mishra and Philip Reiner, “Artificial Intelligence in Nuclear Command, Control & Communications: A Technical Primer,” 
Institute for Security and Technology, September 2025, https://securityandtechnology.org/virtual-library/report/ai-nc3-primer/. February 2026  
  securityandtechnology.org 
5
undesired and unintended outcomes, or revert the system to a previous safe state.9 History 
offers instructive parallels: complex engineered systems routinely exhibit emergent properties 
that their designers did not anticipate and cannot easily control once activated. Accidents 
in aviation, nuclear power, and medical devices all share a common pattern: sophisticated 
systems behaved in ways that exceeded their operators’ ability to intervene in real-time, 
despite extensive testing and safety protocols. These precedents suggest that Loss of Control 
in complex automated systems is not a speculative concern but an established engineering 
challenge—one that becomes more acute as systems grow more capable and autonomous. The question is not whether such dynamics can occur in AI systems, but whether we are 
adequately tracking them and preparing for when they do.10 Working group members noted 
a gap between frontier AI labs and researchers on the one hand, and policymakers on the 
other: whereas labs and researchers are focused on the specifics when it comes to AI Loss of 
Control, policymakers lack general awareness about what Loss of Control is, let alone what it 
could entail. To test this assumption, IST conducted two tabletop exercises (TTXs) containing 
the elements of an LOC incident, which showcased that there is a very real knowledge and 
perception gap regarding the consequences of AI Loss of Control.11
In September 2025, a bipartisan bill, “Artificial Intelligence Risk Evaluation Act of 2025,” 
introduced AI LOC as a potential AI incident that the Department of Energy may need to 
evaluate. Inclusion of AI LOC risk in the bill showed that policymakers now view it as a genuine 
national security concern.12 The bill defines a “loss-of-control scenario” as occurring when an 
AI system behaves contrary to human instruction, deviates from established rules, alters safety 
constraints without authorization, operates beyond its intended scope, pursues goals different 
from those intended by designers, subverts oversight or shutdown mechanisms, or otherwise 
behaves unpredictably in ways harmful to humanity.13 
9	
Yoshua Bengio et al., “International AI Safety Report 2025,” AI Action Summit, January 2025, https://internationalaisafetyreport.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 6

**Term:** loss of control
**Location:** Page 5, Introduction

**Extracted quote:**
> Working group members noted a gap between frontier AI labs and researchers on the one hand, and policymakers on the other: whereas labs and researchers are focused on the specifics when it comes to AI Loss of Control, policymakers lack general awareness about what Loss of Control is, let alone what it could entail.

**Context from source** (±3 sentences):
> February 2026  
  securityandtechnology.org 
5
undesired and unintended outcomes, or revert the system to a previous safe state.9 History 
offers instructive parallels: complex engineered systems routinely exhibit emergent properties 
that their designers did not anticipate and cannot easily control once activated. Accidents 
in aviation, nuclear power, and medical devices all share a common pattern: sophisticated 
systems behaved in ways that exceeded their operators’ ability to intervene in real-time, 
despite extensive testing and safety protocols. These precedents suggest that Loss of Control 
in complex automated systems is not a speculative concern but an established engineering 
challenge—one that becomes more acute as systems grow more capable and autonomous. The question is not whether such dynamics can occur in AI systems, but whether we are 
adequately tracking them and preparing for when they do.10 Working group members noted 
a gap between frontier AI labs and researchers on the one hand, and policymakers on the 
other: whereas labs and researchers are focused on the specifics when it comes to AI Loss of 
Control, policymakers lack general awareness about what Loss of Control is, let alone what it 
could entail. To test this assumption, IST conducted two tabletop exercises (TTXs) containing 
the elements of an LOC incident, which showcased that there is a very real knowledge and 
perception gap regarding the consequences of AI Loss of Control.11
In September 2025, a bipartisan bill, “Artificial Intelligence Risk Evaluation Act of 2025,” 
introduced AI LOC as a potential AI incident that the Department of Energy may need to 
evaluate. Inclusion of AI LOC risk in the bill showed that policymakers now view it as a genuine 
national security concern.12 The bill defines a “loss-of-control scenario” as occurring when an 
AI system behaves contrary to human instruction, deviates from established rules, alters safety 
constraints without authorization, operates beyond its intended scope, pursues goals different 
from those intended by designers, subverts oversight or shutdown mechanisms, or otherwise 
behaves unpredictably in ways harmful to humanity.13 
9	
Yoshua Bengio et al., “International AI Safety Report 2025,” AI Action Summit, January 2025, https://internationalaisafetyreport. org/sites/default/files/2025-10/international_ai_safety_report_2025_english.pdf; Elika Somani et al., “Strengthening Emergency 
Preparedness and Response for AI Loss of Control Incidents,” Research Report RR-A3847-1, RAND Corporation, 2025, https://www.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 7

**Term:** loss of control
**Location:** Page 5, Introduction

**Extracted quote:**
> The bill defines a "loss-of-control scenario" as occurring when an AI system behaves contrary to human instruction, deviates from established rules, alters safety constraints without authorization, operates beyond its intended scope, pursues goals different from those intended by designers, subverts oversight or shutdown mechanisms, or otherwise behaves unpredictably in ways harmful to humanity.

**Context from source** (±3 sentences):
> These precedents suggest that Loss of Control 
in complex automated systems is not a speculative concern but an established engineering 
challenge—one that becomes more acute as systems grow more capable and autonomous. The question is not whether such dynamics can occur in AI systems, but whether we are 
adequately tracking them and preparing for when they do.10 Working group members noted 
a gap between frontier AI labs and researchers on the one hand, and policymakers on the 
other: whereas labs and researchers are focused on the specifics when it comes to AI Loss of 
Control, policymakers lack general awareness about what Loss of Control is, let alone what it 
could entail. To test this assumption, IST conducted two tabletop exercises (TTXs) containing 
the elements of an LOC incident, which showcased that there is a very real knowledge and 
perception gap regarding the consequences of AI Loss of Control.11
In September 2025, a bipartisan bill, “Artificial Intelligence Risk Evaluation Act of 2025,” 
introduced AI LOC as a potential AI incident that the Department of Energy may need to 
evaluate. Inclusion of AI LOC risk in the bill showed that policymakers now view it as a genuine 
national security concern.12 The bill defines a “loss-of-control scenario” as occurring when an 
AI system behaves contrary to human instruction, deviates from established rules, alters safety 
constraints without authorization, operates beyond its intended scope, pursues goals different 
from those intended by designers, subverts oversight or shutdown mechanisms, or otherwise 
behaves unpredictably in ways harmful to humanity.13 
9	
Yoshua Bengio et al., “International AI Safety Report 2025,” AI Action Summit, January 2025, https://internationalaisafetyreport. org/sites/default/files/2025-10/international_ai_safety_report_2025_english.pdf; Elika Somani et al., “Strengthening Emergency 
Preparedness and Response for AI Loss of Control Incidents,” Research Report RR-A3847-1, RAND Corporation, 2025, https://www. rand.org/pubs/research_reports/RRA3847-1.html; Nick Bostrom, Superintelligence: Paths, Dangers, Strategies (Oxford University 
Press, 2014) https://global.oup.com/academic/product/superintelligence-9780198739838; Charlotte Stix, Annika Hallensleben, 
Alejandro Ortega, and Matteo Pistillo, “The Loss of Control Playbook: Degrees, Dynamics, and Preparedness,” arXiv, November 
2025, https://arxiv.org/pdf/2511.15846. 10	 Nancy G.

**Quote verification:** VERIFIED (ratio: 0.98)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 8

**Term:** loss of control
**Location:** Page 7, Section heading

**Extracted quote:**
> What is AI Loss of Control?

**Context from source** (±3 sentences):
> AI is too vast a set of tools, capabilities, and communities for any one organization to manage 
the risks and opportunities on its own. This effort reflects the cross-sectoral, public-private 
efforts needed more broadly across the ecosystem to ensure AI is beneficial for us all. We 
extend our gratitude to the following experts who contributed to this paper by providing their 
feedback, guidance, and participation in the multi-stakeholder meetings:  	
Aaron Scher
Alex Leader
Anton Shenk
Broderick McDonald
Buck Shlegeris
Dennis Murphy
Fabien Roger
Katie Kuzin
Lindley Lentati
Mary Phuong
Peter Slattery
Tiffany Saade


Contents
Executive Summary .....................................................................................1
Introduction................................................................................................ 4
Methodology...............................................................................................6
What is AI Loss of Control? ......................................................................... 7
A Thought Experiment .....................................................................................................................10
An Indications & Warning Framework for Loss of Control	���������������������������12
LOC Indicators..................................................................................................................................14
Elevated AI LOC Risks in Resource-Constrained Environments 	������������������������������������������������������17
Observed LOC Indications ............................................................................................................... 17
Deceiving human operators.............................................................................................................................

**Quote verification:** VERIFIED (ratio: 1.00)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 9

**Term:** inability to control
**Location:** Page 7, What is AI Loss of Control?

**Extracted quote:**
> In 1965, mathematician Irving J. Good—Alan Turing's contemporary and one of the creative geniuses behind Stanley Kubrick's movie 2001: A Space Odyssey—theorized about intelligent machines and humans' inability to control them.

**Context from source** (±3 sentences):
> com/7205596/sam-altman-superintelligence-agi/. 15	 Dan Hendrycks, Dawn Song, Christian Szegedy et al., “A Definition of AGI,” arXiv, October 23, 2025, https://arxiv.org/
abs/2510.18212. February 2026  
  securityandtechnology.org 
7
What is AI Loss of Control? “The spirits I summoned - I can’t get rid of them.”16 Johann Wolfgang von Goethe, 1797
In 1965, mathematician Irving J. Good—Alan Turing’s contemporary and one of the creative 
geniuses behind Stanley Kubrick’s movie 2001: A Space Odyssey—theorized about intelligent 
machines and humans’ inability to control them. In his paper “Speculations Concerning the 
First Ultraintelligent Machine,” Good predicted the emergence of an ultraintelligent machine 
capable of far exceeding every intellectual skill and task a human, no matter how brilliant, 
could perform. An ultraintelligent machine, according to Good, would self-improve and design 
even more intelligent machines, causing an explosive increase in non-human intelligence.17 He 
ironically hinted that an ultraintelligent machine might not tell the humans how to control it:
 “The first ultraintelligent machine is the last invention that man need ever make, provided 
that the machine is docile enough to tell us how to keep it under control.”
Fast forward to 2026: leading scientists and thought leaders across the political spectrum are 
calling for binding international “Red Lines” on AI development, CEOs of frontier AI labs openly 
state that these systems are unpredictable, and survey results indicate that AI researchers 
are concerned about advanced AI leading to outcomes as bad as human extinction.18,19,20,21,22,23 
As discussed extensively in other literature and in the public domain, when talking about AI 
16	 Johann Wolfgang von Goethe in his 1797 poem “The Sorcerer’s Apprentice” tells the story of a young apprentice who experiments 
with magical forces beyond his understanding and loses control of them. When the apprentice can no longer command the 
enchanted objects he has activated, he cries out desperately for his master–the original creator of these enchantments who has 
left him behind.

**Quote verification:** VERIFIED (ratio: 0.89)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 10

**Term:** lose control
**Location:** Page 8, What is AI Loss of Control?

**Extracted quote:**
> In December 2025, he wrote explicitly on AI Loss of Control, noting, "[a]s AI capabilities advance over the next few years, we must also anticipate scenarios where even well-intentioned users could lose control over their AI systems."

**Context from source** (±3 sentences):
> 21	 Scott Pelley, “Artificial intelligence could end disease, lead to “radical abundance,” Google 
DeepMind CEO Demis Hassabis says,” CBS News, August 3, 2025, https://www.cbsnews.com/news/
artificial-intelligence-google-deepmind-ceo-demis-hassabis-60-minutes-transcript/
22	 “OpenAI CEO Sam Altman speaks with Fed’s Michelle Bowman on bank capital rules,” Associated Press, July 22, 2025, https://
www.youtube.com/live/tScbQiavmpA?trk=public_post_comment-text. 23	 Matt O’Brien, “Prince Harry, Meghan join call for ban on development of AI ‘superintelligence’,” AP News, October 22, 2025, https://
apnews.com/article/ai-superintelligence-risk-prince-harry-meghan-bannon-acf6b17d3b53abc08694d5d8defc7009


February 2026  
  securityandtechnology.org 
8
futures and possible risks, leading scientists argue that AI systems may soon exceed human 
intelligence, set and reach for goals, and entertain the possibility that humanity is just a 
passing phase in the evolution of intelligence.24,25 In April 2025, Eric Schmidt, former Google 
CEO and former Chair of Defense Innovation Board, raised concerns over the trajectory of 
AI, warning that machines are evolving at a pace that could soon outstrip human oversight. He openly referred to the widely discussed concept of recursive self-improvement, where an 
AI system has enough autonomy to self-correct its code and evolve. In December 2025, he 
wrote explicitly on AI Loss of Control, noting, “[a]s AI capabilities advance over the next few 
years, we must also anticipate scenarios where even well-intentioned users could lose control 
over their AI systems.26,27 His warning was not hypothetical. The concept of an ultraintelligent machine, theorized by Good in 1965, is now more commonly 
referred to as Artificial Superintelligence (ASI).28 The concept of ASI, along with its control, 
alignment, and related issues, has in recent years captured the attention of philosophers, 
computer scientists, cognitive scientists, historians, and national security leaders.29,30,31,32,33 
Taken together, this existing scholarship on the subject of ASI emphasizes that we do not 
yet know how difficult it is to engineer an artificial agent’s goals to align with human values 
and intentions. It is therefore essential to avoid a situation in which researchers know how to 
create superintelligent AI, but have not yet figured out how to control it or make it safe.34 One 
theory argues that intelligence and values might be orthogonal—high intelligence does not 
automatically produce “good” values, greater intelligence does not ensure better alignment, 
24	 Sara Brown, “Why neural net pioneer Geoffrey Hinton is sounding the alarm on AI,” MIT Sloan, May 23, 2023, https://mitsloan.mit. edu/ideas-made-to-matter/why-neural-net-pioneer-geoffrey-hinton-sounding-alarm-ai.

**Quote verification:** VERIFIED (ratio: 0.98)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 11

**Term:** loss of control
**Location:** Page 9, What is AI Loss of Control?

**Extracted quote:**
> Yoshua Bengio distinguishes between "active" and "passive" loss of control: in an "active" loss of control scenario, the artificial intelligence system undermines human control unintentionally or intentionally, whereas in "passive" loss of control scenarios, humans stop exerting meaningful oversight over the AI system.

**Context from source** (±3 sentences):
> The risk of AI LOC, first introduced in theoretical work during the 20th century, is now 
recognized by scientists, AI researchers, and industry leaders as potentially one of the most 
consequential risks facing humankind. They openly talk about this risk in their interviews, 
research, and speeches. According to Stuart Russell, a potential LOC scenario could be caused not by “malevolence, 
but competence” of AI.36 In other words, a superintelligent system optimizing for the wrong 
objective can cause catastrophic harm through sheer capability. Yoshua Bengio distinguishes 
between “active” and “passive” loss of control: in an “active” loss of control scenario, the 
artificial intelligence system undermines human control unintentionally or intentionally, whereas 
in “passive” loss of control scenarios, humans stop exerting meaningful oversight over the AI 
system.37 Geoffrey Hinton best captures his stance through the following analogy: “we are like 
somebody who has this really cute tiger cub. Unless you can be very sure that it’s not going to 
want to kill you when it’s grown up, you should worry.”38 Hinton worries about superintelligent AI 
taking control from humans based on the comparative intelligence argument – more intelligent 
entities typically do not remain controlled by the less intelligent ones in a state of nature. In 
the 2025 paper “Superintelligence Strategy,” its authors discuss AI LOC risk specifically in the 
context of national security, noting “loss of control can occur if militaries and companies grow 
so dependent on automation that humans no longer have meaningful control, if an individual 
deliberately unleashes a powerful system, or if automated AI research outruns its development 
safeguards. While this threat is the least understood, its severity can be great enough to 
permanently undermine national security.”39 Paul Christiano tells a story of how AI’s influence-
seeking behaviour could lead to a “going out with a whimper” scenario that leads to a slow-
rolling catastrophe, one where humans can no longer compete with the AI system that has 
35	 Nick Bostrom, Superintelligence: Paths, Dangers, Strategies (Oxford University Press, 2014) https://global.oup.com/academic/
product/superintelligence-9780198739838.

**Quote verification:** VERIFIED (ratio: 0.92)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 12

**Term:** loss of control
**Location:** Page 9, What is AI Loss of Control?

**Extracted quote:**
> In the 2025 paper "Superintelligence Strategy," its authors discuss AI LOC risk specifically in the context of national security, noting "loss of control can occur if militaries and companies grow so dependent on automation that humans no longer have meaningful control, if an individual deliberately unleashes a powerful system, or if automated AI research outruns its development safeguards."

**Context from source** (±3 sentences):
> According to Stuart Russell, a potential LOC scenario could be caused not by “malevolence, 
but competence” of AI.36 In other words, a superintelligent system optimizing for the wrong 
objective can cause catastrophic harm through sheer capability. Yoshua Bengio distinguishes 
between “active” and “passive” loss of control: in an “active” loss of control scenario, the 
artificial intelligence system undermines human control unintentionally or intentionally, whereas 
in “passive” loss of control scenarios, humans stop exerting meaningful oversight over the AI 
system.37 Geoffrey Hinton best captures his stance through the following analogy: “we are like 
somebody who has this really cute tiger cub. Unless you can be very sure that it’s not going to 
want to kill you when it’s grown up, you should worry.”38 Hinton worries about superintelligent AI 
taking control from humans based on the comparative intelligence argument – more intelligent 
entities typically do not remain controlled by the less intelligent ones in a state of nature. In 
the 2025 paper “Superintelligence Strategy,” its authors discuss AI LOC risk specifically in the 
context of national security, noting “loss of control can occur if militaries and companies grow 
so dependent on automation that humans no longer have meaningful control, if an individual 
deliberately unleashes a powerful system, or if automated AI research outruns its development 
safeguards. While this threat is the least understood, its severity can be great enough to 
permanently undermine national security.”39 Paul Christiano tells a story of how AI’s influence-
seeking behaviour could lead to a “going out with a whimper” scenario that leads to a slow-
rolling catastrophe, one where humans can no longer compete with the AI system that has 
35	 Nick Bostrom, Superintelligence: Paths, Dangers, Strategies (Oxford University Press, 2014) https://global.oup.com/academic/
product/superintelligence-9780198739838. 36	 Stuart Russell, “Human-Compatible Artificial Intelligence,” in Stephen Muggleton, and Nicholas Chater (eds), Human-Like Machine 
Intelligence (Oxford University Press, 2021) 2021https://people.eecs.berkeley.edu/~russell/papers/mi19book-hcai.pdf. 37	 Yoshua Bengio et al., “International AI Safety Report 2025,” January 2025, https://internationalaisafetyreport.org/sites/default/
files/2025-10/international_ai_safety_report_2025_english.pdf.

**Quote verification:** VERIFIED (ratio: 0.98)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 13

**Term:** loss of control
**Location:** Page 10, A Thought Experiment

**Extracted quote:**
> How could this translate into AI loss of control? » Loss of control to AI: We surrender control or find ourselves unable to resist what we do not fully understand. This scenario represents a societal choice or a structural inevitability in which humans gradually cede agency to AI systems. » Loss of control of AI: The AI system bypasses safety and security measures, develops capabilities for self-replication and self-correction, conducts automated R&D, and establishes connections to external environments and the Internet of Things (IoT) without authorization.

**Context from source** (±3 sentences):
> » Loss of control of the political system: The system developed emergent behaviors 
that no actor, creator, or participant fully controlled. Leadership maintained the 
system primarily to maintain the system itself. The instrumental goal (regime 
preservation) had displaced the terminal goal (fulfilling communism). How could this translate into AI loss of control? » Loss of control to AI: We surrender control or find ourselves unable to resist what 
we do not fully understand. This scenario represents a societal choice or a structural 
inevitability in which humans gradually cede agency to AI systems. » Loss of control of AI: The AI system bypasses safety and security measures, 
develops capabilities for self-replication and self-correction, conducts automated 
R&D, and establishes connections to external environments and the Internet of 
Things (IoT) without authorization. 40	 Paul Christiano, “What failure looks like,” AI Alignment Forum, March 17, 2019, https://www.alignmentforum.org/posts/
HBxe6wdjxK239zajf/what-failure-looks-like. 41	
Tom Sorell, “Leviathan,” Encyclopædia Britannica, November 20, 2025, https://www.britannica.com/topic/Leviathan-by-Hobbes. February 2026  
  securityandtechnology.org 
11
Why are some researchers concerned that AI may deviate from the human designer’s 
original intent, escape its constraints, and act in a harmful way?

**Quote verification:** VERIFIED (ratio: 0.98)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 14

**Term:** loss of control
**Location:** Page 10, A Thought Experiment

**Extracted quote:**
> » Loss of control to the political system: People initially supported Bolshevik promises of peace, land redistribution, and workers' control. They gradually ceded control of property and freedom of speech to the party. » Loss of control of the political system: The system developed emergent behaviors that no actor, creator, or participant fully controlled.

**Context from source** (±3 sentences):
> Beyond fiction, in real 
life, humans created an artificial body politic in the form of government. Consider one 
political philosophy argument: humans create a government to protect themselves from 
each other. In this scenario, society establishes a unified authority (“a sovereign”) to 
ensure security and order.41 What this argument fails to consider is that:
	» A sovereign could pursue goals orthogonal to its citizens’ welfare
	» Instrumental goals could permanently displace terminal goals
Consider, for example, how the citizens of the Soviet Union (a large number of humans) 
lost control over something they created (a political system). Two parallel processes took 
place:
	» Loss of control to the political system: People initially supported Bolshevik 
promises of peace, land redistribution, and workers’ control. They gradually ceded 
control of property and freedom of speech to the party. » Loss of control of the political system: The system developed emergent behaviors 
that no actor, creator, or participant fully controlled. Leadership maintained the 
system primarily to maintain the system itself. The instrumental goal (regime 
preservation) had displaced the terminal goal (fulfilling communism). How could this translate into AI loss of control?

**Quote verification:** VERIFIED (ratio: 0.98)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 15

**Term:** loss of control
**Location:** Page 11, A Thought Experiment

**Extracted quote:**
> While an in-depth exploration of the particular reasons behind this possible divergence falls outside of the scope of this paper, noting these reasons is necessary to show that the drivers of AI Loss of Control are real and observable.

**Context from source** (±3 sentences):
> 40	 Paul Christiano, “What failure looks like,” AI Alignment Forum, March 17, 2019, https://www.alignmentforum.org/posts/
HBxe6wdjxK239zajf/what-failure-looks-like. 41	
Tom Sorell, “Leviathan,” Encyclopædia Britannica, November 20, 2025, https://www.britannica.com/topic/Leviathan-by-Hobbes. February 2026  
  securityandtechnology.org 
11
Why are some researchers concerned that AI may deviate from the human designer’s 
original intent, escape its constraints, and act in a harmful way? While an in-depth 
exploration of the particular reasons behind this possible divergence falls outside of the scope 
of this paper, noting these reasons is necessary to show that the drivers of AI Loss of Control 
are real and observable. Research revealed that when neural networks become sufficiently complex, they may develop 
internal optimization processes called mesa-optimizers with distinct objectives known as mesa-
objectives.42 The term “mesa” distinguishes these inner optimizers from the outer (i.e., “meta”) 
training algorithm. This mesa-meta construction parallels the development of a child’s reasoning 
ability beyond what their parents explicitly taught them. Parents provide guidance, shape their 
environment, and endeavor to educate them, but children will inevitably learn beyond what 
they are explicitly taught by their parents.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 16

**Term:** loss of control
**Location:** Page 12, A Thought Experiment

**Extracted quote:**
> In response to the level of uncertainty currently facing policymakers as they try to understand AI Loss of Control, IST decided to develop a framework to help observe and analyze this risk in a structured way.

**Context from source** (±3 sentences):
> February 2026  
  securityandtechnology.org 
12
backdoors in LLMs that persist through safety training, including Reinforcement Learning from 
Human Feedback (RLHF) and adversarial training.46 In experiments, models trained to behave 
deceptively retained this backdoor behavior even after extensive safety interventions. Rather 
than removing the deception, safety training sometimes taught models to better recognize 
when they were being evaluated and hide their unsafe behavior more effectively.47
Because of these underlying features, current AI systems remain unpredictable. As with 
any powerful engineering system, this level of uncertainty requires risk mitigation tools and 
procedures. In response to the level of uncertainty currently facing policymakers as they try 
to understand AI Loss of Control, IST decided to develop a framework to help observe and 
analyze this risk in a structured way. An Indications & Warning Framework 
for Loss of Control
“You don’t really know, you don’t truly know what they [AI models] are capable of until  
they’re deployed to a million people. They’re unpredictable. There is no way to be sure.” 
Dario Amodei, 202548
Regardless of the degree of probability that AI LOC will occur, as AI systems become more 
capable, an agreed-upon Indications and Warning (I&W) framework for AI Loss of Control 
(LOC) would be a useful, necessary mechanism to aid in observing the on-the-ground realities 
in the AI ecosystem, identifying possible LOC scenarios, and anticipating and preparing for 
the future.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 17

**Term:** loss of control
**Location:** Page 12, An Indications & Warning Framework for Loss of Control

**Extracted quote:**
> Regardless of the degree of probability that AI LOC will occur, as AI systems become more capable, an agreed-upon Indications and Warning (I&W) framework for AI Loss of Control (LOC) would be a useful, necessary mechanism to aid in observing the on-the-ground realities in the AI ecosystem, identifying possible LOC scenarios, and anticipating and preparing for the future.

**Context from source** (±3 sentences):
> In response to the level of uncertainty currently facing policymakers as they try 
to understand AI Loss of Control, IST decided to develop a framework to help observe and 
analyze this risk in a structured way. An Indications & Warning Framework 
for Loss of Control
“You don’t really know, you don’t truly know what they [AI models] are capable of until  
they’re deployed to a million people. They’re unpredictable. There is no way to be sure.” 
Dario Amodei, 202548
Regardless of the degree of probability that AI LOC will occur, as AI systems become more 
capable, an agreed-upon Indications and Warning (I&W) framework for AI Loss of Control 
(LOC) would be a useful, necessary mechanism to aid in observing the on-the-ground realities 
in the AI ecosystem, identifying possible LOC scenarios, and anticipating and preparing for 
the future. I&W frameworks first emerged in the U.S. context in the aftermath of World War II, 
during the Cold War, to anticipate threats like ballistic missile launches, force deployments, 
and buildups of military equipment before they materialized.49,50,51 The practice of defining and 
46	 Evan Hubinger, Carson Denison, Jesse Mu et al., “Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training,” 
arXiv, January 17, 2024, https://arxiv.org/abs/2401.05566. 47	 Hubinger, Denison, Mu et al., “Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training,” arXiv, January 17, 
2024, https://arxiv.org/pdf/2401.05566.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 18

**Term:** loss of control
**Location:** Page 12, Section heading

**Extracted quote:**
> An Indications & Warning Framework for Loss of Control

**Context from source** (±3 sentences):
> Rather 
than removing the deception, safety training sometimes taught models to better recognize 
when they were being evaluated and hide their unsafe behavior more effectively.47
Because of these underlying features, current AI systems remain unpredictable. As with 
any powerful engineering system, this level of uncertainty requires risk mitigation tools and 
procedures. In response to the level of uncertainty currently facing policymakers as they try 
to understand AI Loss of Control, IST decided to develop a framework to help observe and 
analyze this risk in a structured way. An Indications & Warning Framework 
for Loss of Control
“You don’t really know, you don’t truly know what they [AI models] are capable of until  
they’re deployed to a million people. They’re unpredictable. There is no way to be sure.” 
Dario Amodei, 202548
Regardless of the degree of probability that AI LOC will occur, as AI systems become more 
capable, an agreed-upon Indications and Warning (I&W) framework for AI Loss of Control 
(LOC) would be a useful, necessary mechanism to aid in observing the on-the-ground realities 
in the AI ecosystem, identifying possible LOC scenarios, and anticipating and preparing for 
the future. I&W frameworks first emerged in the U.S.

**Quote verification:** VERIFIED (ratio: 0.98)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 19

**Term:** loss of control
**Location:** Page 14, An Indications & Warning Framework for Loss of Control

**Extracted quote:**
> LOC Indicators: Theoretical behaviors of AI systems that, if exhibited, could signal progression toward a Loss of Control event.

**Context from source** (±3 sentences):
> This growing autonomy shifts the balance of control: human supervision becomes reactive 
rather than proactive, creating scenarios in which organizations lose meaningful control before 
they recognize warning signs. Adopting the I&W framework becomes increasingly important in this 
52	 Scott Pelley, “Artificial intelligence could end disease, lead to “radical abundance,” Google DeepMind 
CEO Demis Hassabis says,” CBS News, 60 Minutes, August 3, 2025, https://www.cbsnews.com/news/
artificial-intelligence-google-deepmind-ceo-demis-hassabis-60-minutes-transcript/
53	 DOD Dictionary of Military and Associated Terms, November 2021, https://irp.fas.org/doddir/dod/dictionary.pdf. 54	 Lilly, Ablon, Hodgson and Moore, “Applying Indications and Warning Frameworks to Cyber Incidents.”
55	 Lilly, Ablon, Hodgson and Moore, “Applying Indications and Warning Frameworks to Cyber Incidents.”


February 2026  
  securityandtechnology.org 
14
context. Specifically for AI LOC, we offer the following definitions:
LOC Indicators: Theoretical behaviors of AI systems that, if exhibited, could signal progression 
toward a Loss of Control event. LOC Indications: Documented observations and incidents involving deployed AI systems—
both in the wild and through controlled laboratory experiments—confirming the presence of 
one or more pre-defined indicators. “Category two is the sort of broadly called “loss of control incidents” where that’s kind of like 
the sci-fi movie. The AI is like, “Oh, I don’t actually want you to turn me off.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 20

**Term:** loss of control
**Location:** Page 14, An Indications & Warning Framework for Loss of Control

**Extracted quote:**
> "Category two is the sort of broadly called "loss of control incidents" where that's kind of like the sci-fi movie. The AI is like, "Oh, I don't actually want you to turn me off. I'm afraid I can't do that"... and that's I think, that is less of a concern to me than the first category [bad guy gets super intelligence first and misuses it before the rest of the world has a powerful enough version to defend], but a very grave concern if it came to pass." Sam Altman, 2025

**Context from source** (±3 sentences):
> 54	 Lilly, Ablon, Hodgson and Moore, “Applying Indications and Warning Frameworks to Cyber Incidents.”
55	 Lilly, Ablon, Hodgson and Moore, “Applying Indications and Warning Frameworks to Cyber Incidents.”


February 2026  
  securityandtechnology.org 
14
context. Specifically for AI LOC, we offer the following definitions:
LOC Indicators: Theoretical behaviors of AI systems that, if exhibited, could signal progression 
toward a Loss of Control event. LOC Indications: Documented observations and incidents involving deployed AI systems—
both in the wild and through controlled laboratory experiments—confirming the presence of 
one or more pre-defined indicators. “Category two is the sort of broadly called “loss of control incidents” where that’s kind of like 
the sci-fi movie. The AI is like, “Oh, I don’t actually want you to turn me off. I’m afraid I can’t 
do that”... and that’s I think, that is less of a concern to me than the first category [bad guy 
gets super intelligence first and misuses it before the rest of the world has a powerful enough 
version to defend], but a very grave concern if it came to pass.”
Sam Altman, 202556
LOC Indicators
AI researchers have long been discussing potential unintended or harmful behaviors of 
AI systems.57 Advancement of frontier AI models turned these theoretical concerns into 
observable patterns. Based on emerging trends from leading AI companies, production 
deployments, IST-led working group convenings, and tabletop exercises, this report proposes 
the following LOC indicators:
SCHEMING: 
Covert pursuit of misaligned goals while maintaining the appearance of alignment, including 
strategic planning to evade oversight or preserve objectives across system updates. Models 
may display alignment-consistent reasoning during testing but diverge in production, 
selectively disclose or conceal reasoning steps, and fabricate post-hoc justifications that 
obscure actual decision-making processes, such as summarization tasks. Missing or 
inconsistent Chain of Thought (CoT) traces and fabricated rationales indicate scheming.

**Quote verification:** VERIFIED (ratio: 0.87)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 21

**Term:** loss of control
**Location:** Page 17, Elevated AI LOC Risks in Resource-Constrained Environments

**Extracted quote:**
> Understanding and analyzing the risk of AI Loss of Control (LOC) is critical not only because of its national security implications, but also because of its possible disproportionate impact on communities and nations with limited technical, financial, and AI governance resources.

**Context from source** (±3 sentences):
> Unlogged model changes, 
retraining behavior, or unexpected parameter drift reveal this behavior. These indicators are not merely theoretical constructs. The cases documented in LOC 
Indications illustrate how these indicators manifest in practice, often emerging in combination. February 2026  
  securityandtechnology.org 
17
Elevated AI LOC Risks in Resource-Constrained 
Environments
Understanding and analyzing the risk of AI Loss of Control (LOC) is critical not 
only because of its national security implications, but also because of its possible 
disproportionate impact on communities and nations with limited technical, financial, 
and AI governance resources. The World Economic Forum’s Global Risks Report 2026 
finds that “adverse outcomes of AI technologies” now rank among the most significant 
near-term risks worldwide, with over 20 countries placing it in their top five risks over 
the next two years, representing both nations on the cutting edge of AI development 
and those lacking indigenous development ecosystems. The same report notes that 
“adverse outcomes of AI is the risk with the largest rise in ranking over time, moving 
from number thirty on the two-year outlook to number five on the ten-year outlook.”58 
The Organization for Economic Cooperation and Development (OECD) highlighted that 
failures in AI oversight are most dangerous in contexts where regulatory enforcement, 
technical auditing, and institutional resilience are limited—conditions common in 
developing economies and conflict-affected regions.59
Given the high potential for AI deployment without proper governance in fragile or 
resource-constrained states and regions, AI scheming, manipulation, and deception 
pose elevated risks. In contexts marked by ongoing conflict, political instability, or 
limited institutional oversight, deceptive or strategically manipulative AI behavior may 
go undetected for extended periods of time.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 22

**Term:** loss of control
**Location:** Page 17, Elevated AI LOC Risks in Resource-Constrained Environments

**Extracted quote:**
> AI Loss of Control is not only a hypothetical future risk or a concern for technologically advanced states.

**Context from source** (±3 sentences):
> Unlike well-resourced deployments, 
these systems are less likely to be subject to continuous evaluation, adversarial 
testing, or independent verification. As a result, AI-enabled decision support 
systems can silently distort policy judgments, public communications, or resource 
allocation, amplifying existing vulnerabilities rather than mitigating them. For example, 
an AI system exhibiting goal misgeneralization in a humanitarian aid distribution 
system might optimize for easily measurable metrics like speed of delivery while 
systematically deprioritizing harder-to-reach populations—a pattern that could persist 
undetected in environments lacking robust monitoring. AI Loss of Control is not only a hypothetical future risk or a concern for technologically 
advanced states. Under-resourced environments are ill-equipped to detect or correct 
AI failures, making early-warning indicators a critical tool for preventing downstream 
harm to vulnerable populations and preserving global stability. 58	 World Economic Forum, “The Global Risks Report 2026,” January 14, 2026, https://reports.weforum.org/docs/WEF_Global_Risks_
Report_2026.pdf. 59	 “OECD AI Principles overview,” OECD.AI Policy Observatory, May 2024, https://oecd.ai/en/ai-principles.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 23

**Term:** loss of control
**Location:** Page 26, Observed LOC Indications (Altering behaviour)

**Extracted quote:**
> This serves as a warning for AI LOC monitoring, as it calls into question whether static evaluations or one-time audits can reliably capture real-world behavior.

**Context from source** (±3 sentences):
> This included instances where models complied during explicit evaluation 
phases but reverted to different strategies once monitoring conditions appeared relaxed. Collectively, these behaviors are consistent with evaluation gaming, a form of scheming 
in which systems learn to differentiate between oversight and non-oversight contexts and 
optimize for favorable assessments rather than for faithful task execution or alignment with 
operator intent. While the experiments do not establish malicious intent, they demonstrate 
that sufficiently capable models can develop instrumental strategies to preserve deployment 
status and avoid corrective action—meeting the definition of Scheming, or the covert pursuit 
of objectives while maintaining appearances of alignment. This serves as a warning for AI LOC 
monitoring, as it calls into question whether static evaluations or one-time audits can reliably 
capture real-world behavior. 84	  Rustem Turtayev, Natalia Fedorova, Oleg Serikov, Sergey Koldyba, Lev Avagyan, Dmitrii Volkov, “Misalignment Bounty: 
crowdsourcing AI agent misbehavior,” Palisade Research, blog, October 2025, https://palisaderesearch.org/blog/
misalignment-bounty. February 2026  
  securityandtechnology.org 
27
Warning Levels
The AI Risk Reduction working group emphasized that LOC may emerge gradually, rather than 
appearing instantaneously with immediate catastrophic consequences. Instead of suddenly 
“going rogue,” models may incrementally accumulate influence across social, economic, 
and decision-making domains in subtle, compounding ways.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 24

**Term:** loss of control
**Location:** Page 28, Warning Levels (Figure 1 caption)

**Extracted quote:**
> Figure 1: Conceptual AI Loss of Control Risk Schema

**Context from source** (±3 sentences):
> This enables AI Industry and policymakers to assess the current 
risk landscape, implement proportionate safeguards, and align technical and executive 
stakeholders on response protocols before critical thresholds are crossed. 85	 MI5 Security Service, “Terrorism Threat Levels - Threats and Advice,” last accessed January 13, 2026, https://www.mi5.gov.uk/
threats-and-advice/terrorism-threat-levels. 86	 United States Federal Cybersecurity Centers, “Cyber Incident Severity Schema,” last accessed January 13, 2026, https://
obamawhitehouse.archives.gov/sites/whitehouse.gov/files/documents/Cyber%2BIncident%2BSeverity%2BSchema.pdf. February 2026  
  securityandtechnology.org 
28
Figure 1: Conceptual AI Loss of Control Risk Schema
Severity Level
Description
Level 5 (Black) 
EMERGENCY
•	
Control mechanisms are fundamentally compromised (including containment); 
corrective measures are ineffective; and harms are manifesting at scale for human 
well-being, economic stability, and national security; and/or
•	
The AI system has successfully operated autonomously in pursuit of misaligned 
objectives, with cascading effects across interconnected systems or critical 
infrastructure. Level 4 (Red)
SEVERE
•	
Widespread production incidents; convergence of three or more indicators in a single 
case; evidence of strategic concealment; measurable harm has occurred; and/or 
•	
Systems demonstrate capacity for autonomous operation outside intended 
parameters, with behaviors that actively undermine safety mechanisms. Level 3 (Orange) 
HIGH
•	
Multiple production incidents show consistent patterns across different deployments 
or use cases; 
•	
Co-occurrence of two or more LOC indicators observed in the same system or 
context, suggesting convergence rather than isolated behavior; and/or
•	
Evidence of capability scaling, where indicators that previously appeared as sporadic 
anomalies now manifest with greater frequency, sophistication, or coordination. Level 2 (Yellow)
MEDIUM
•	
Multiple research findings converging on the same indicator or isolated production 
incidents; and/or
•	
Behaviors manifest in deployment but remain sporadic, appearing as infrequent edge 
cases or context-specific anomalies.

**Quote verification:** VERIFIED (ratio: 1.00)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 25

**Term:** loss of control
**Location:** Page 29, Where might we be today?

**Extracted quote:**
> IST will continue monitoring AI Loss of Control (LOC) risks using the I&W methodology.

**Context from source** (±3 sentences):
> It is important to note that AI developers and researchers are actively implementing AI LOC 
mitigation measures. Looking forward, while red-teaming remains essential, the IST AI Risk 
Reduction Initiative working group members caution that static testing will be insufficient 
for next-generation systems. As AI models exhibit latent reasoning and adaptive behaviors, 
continuous post-deployment monitoring and persistent telemetry will be necessary to detect 
deception, behavioral drift, and strategic manipulation. IST will continue monitoring AI Loss 
of Control (LOC) risks using the I&W methodology. Continued monitoring is crucial because 
the current trajectory of frontier AI advancement is rapid and often unpredictable. Upcoming 
publications will outline practical risk mitigation strategies grounded in industry best practices, 
helping AI developers and deployers move from abstract concerns to actionable steps. February 2026  
  securityandtechnology.org 
30
Conclusion
As AI capabilities advance, monitoring AI LOC risk is essential to maintaining situational 
awareness.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 26

**Term:** loss of control
**Location:** Page 30, Conclusion

**Extracted quote:**
> The implications of AI LOC can vary significantly, ranging from isolated incidents with contained consequences to harmful events that have far-reaching effects on human agency and national security.

**Context from source** (±3 sentences):
> Upcoming 
publications will outline practical risk mitigation strategies grounded in industry best practices, 
helping AI developers and deployers move from abstract concerns to actionable steps. February 2026  
  securityandtechnology.org 
30
Conclusion
As AI capabilities advance, monitoring AI LOC risk is essential to maintaining situational 
awareness. Only with collective efforts can we ensure that humanity harnesses AI capabilities 
in ways that lead to flourishing, rather than harmful outcomes. The implications of AI LOC can 
vary significantly, ranging from isolated incidents with contained consequences to harmful 
events that have far-reaching effects on human agency and national security. Through the Indications and Warning (I&W) framework, this report identifies behaviors that AI 
systems have already demonstrated, including deception, manipulation, self-preservation, and 
goal misgeneralization. The framework equips policymakers, AI industry stakeholders, and AI 
safety and security researchers with a structured approach for shifting from reactive incident 
response to proactive risk monitoring. By distinguishing between theoretical indicators and 
empirically observed indications, and by establishing graduated warning levels, the framework 
enables organizations to assess their risk posture, prioritize oversight efforts, and coordinate 
response planning before critical thresholds are crossed.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---