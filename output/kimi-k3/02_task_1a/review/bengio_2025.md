# Definition Extraction Review: bengio_2025

**Paper:** Bengio, Y., Cohen, M., Fornasiere, D., Ghosn, J., Greiner, P. et al. (2025). Superintelligent Agents Pose Catastrophic Risks: Can Scientist AI Offer a Safer Path.
**Experiment:** 1a_kimi-k3-nvidia_prompt_1a_v2
**Model:** moonshotai/kimi-k3
**Date:** 2026-10-11T13:33:29.133737+00:00

---

## Extraction 1

**Term:** loss of human control
**Location:** Abstract

**Extracted quote:**
> Despite how useful these systems might be, unchecked AI agency poses significant risks to public safety and security, ranging from misuse by malicious actors to a potentially irreversible loss of human control.

**Context from source** (±3 sentences):
> Superintelligent Agents Pose Catastrophic Risks:
Can Scientist AI Offer a Safer Path? Yoshua Bengio∗1,2, Michael Cohen3, Damiano Fornasiere1, Joumana Ghosn1, Pietro Greiner1, Matt
MacDermott4,1, S¨oren Mindermann1, Adam Oberman1,5, Jesse Richardson1, Oliver Richardson1,2,
Marc-Antoine Rondeau1, Pierre-Luc St-Charles1, David Williams-King1
1Mila — Quebec AI Institute
2Universit´e de Montr´eal
3University of California, Berkeley
4Imperial College London
5McGill University
Abstract
The leading AI companies are increasingly focused on building generalist AI agents—systems that can
autonomously plan, act, and pursue goals across almost all tasks that humans can perform. Despite how
useful these systems might be, unchecked AI agency poses significant risks to public safety and security,
ranging from misuse by malicious actors to a potentially irreversible loss of human control. We discuss
how these risks arise from current AI training methods. Indeed, various scenarios and experiments
have demonstrated the possibility of AI agents engaging in deception or pursuing goals that were not
specified by human operators and that conflict with human interests, such as self-preservation. Following
the precautionary principle, we see a strong need for safer, yet still useful, alternatives to the current
agency-driven trajectory.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 2

**Term:** loss of human control
**Location:** Section 1.1, p. 5

**Extracted quote:**
> This alternative path could allow us to harness AI’s benefits while maintaining crucial safety controls. Scientist AIs might allow us to reap the benefits of AI innovation in areas that matter most to society (Ipsos 2017) while avoiding major risks stemming from unintentional loss of human control.

**Context from source** (±3 sentences):
> as a tool to help human scientists dramatically accelerate scientific progress, including high-reward
areas like healthcare;
2. as a guardrail to protect from unsafe agentic AIs, by double-checking actions they propose to perform
and enabling their safe deployment; and
3. as an AI research tool to help more safely build even smarter (superintelligent) AIs in the future, a
task which is particularly dangerous to attempt by leveraging agentic systems. This alternative path could allow us to harness AI’s benefits while maintaining crucial safety
controls. Scientist AIs might allow us to reap the benefits of AI innovation in areas that matter most to
society (Ipsos 2017) while avoiding major risks stemming from unintentional loss of human control. Crucially,
we believe our proposed system will be able to interoperate with agentic AI systems, compute the probability
of various harms that could occur from a candidate action, and decide whether or not to allow the action
based on our risk tolerances. As the stakes become higher, either because of increased capabilities of the AI
or because of the domains in which it is applied (e.g., involving human life in war, medical treatments or the
catastrophic misuse of AI (Y. Bengio, Mindermann, et al.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 3

**Term:** loss of human control
**Location:** Section 1.2, p. 5

**Extracted quote:**
> Powerful AI agents pose significant risks, including loss of human control. Scenarios have been identified, without arguments proving their impossibility, that an irreversible loss of human control over agentic AI can occur, due to technical failures, corner cutting, or intentional malicious use.

**Context from source** (±3 sentences):
> Building AI agents
with superhuman intelligence before figuring out how to control them is viewed by some (Bostrom 2014;
Tegmark 2018; S. Russell 2019) as analogous to the risk posed by the creation of a new species with a
superhuman intellect. With this in mind, we use various methodologies, such as fixing a training objective
independent of real-world interactions, or restricting to counterfactual queries, to reduce the risk of agency
emerging in the Scientist AI, or it exerting influence on the world in other, more subtle ways. 1.2
Mapping out ways of losing control
Powerful AI agents pose significant risks, including loss of human control. Scenarios have been
identified, without arguments proving their impossibility, that an irreversible loss of human control over
agentic AI can occur, due to technical failures, corner cutting, or intentional malicious use. Making sure
an AI will not cause harm is a notoriously difficult unsolved technical problem, which we illustrate below
through the concepts of goal misspecification and goal misgeneralization. The less cautious the developer
of the AI, e.g., because of perceived competitive pressures, the greater the risk of loss-of-control accidents. Some players may even want to intentionally develop or deploy an unaligned or dangerous ASI.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 4

**Term:** loss of control
**Location:** Section 1.2, p. 5

**Extracted quote:**
> Loss of control may arise due to goal misspecification (Rudner and Toner 2021).

**Context from source** (±3 sentences):
> Making sure
an AI will not cause harm is a notoriously difficult unsolved technical problem, which we illustrate below
through the concepts of goal misspecification and goal misgeneralization. The less cautious the developer
of the AI, e.g., because of perceived competitive pressures, the greater the risk of loss-of-control accidents. Some players may even want to intentionally develop or deploy an unaligned or dangerous ASI. Loss of control may arise due to goal misspecification (Rudner and Toner 2021). This failure
mode occurs when there are multiple interpretations of a goal, i.e., it is poorly specified or under-specified and
may be pursued in a way that humans did not intend. Goal misspecification is the result of a fundamental
difficulty in precisely defining what we find unacceptable in AI behavior. If an AI takes life-and-death
decisions, we would like it to act ethically.

**Quote verification:** VERIFIED (ratio: 1.00)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 5

**Term:** loss of control
**Location:** Section 1.2, p. 6

**Extracted quote:**
> Even if we specify our goals perfectly, loss of control may also occur through the mechanism of goal misgeneralization (Shah et al. 2022).

**Context from source** (±3 sentences):
> This can occur, for example, in pursuit of an instru-
mental goal (a subgoal to help accomplish the overall goal). Several arguments and case studies have been
presented strongly suggesting that dangerous instrumental goals such as self-preservation and power-seeking
are likely to emerge, no matter the initial goal (Bostrom 2012; Omohundro 2018). In this paper, we devise
methods to detect and mitigate such loopholes in our goal specifications. Even if we specify our goals perfectly, loss of control may also occur through the mechanism
of goal misgeneralization (Shah et al. 2022). This is when an AI learns a goal that leads it to behave
as intended during training and safety testing, but which diverges at deployment time. In other words, the
AI’s internal representation of its goal does not align precisely –– or even at all –– with the goal we used to
train it, despite showing the correct behavior on the training examples. One particularly concerning possibility is that of reward tampering (Denison et al.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 6

**Term:** loss of control / loss of human control
**Location:** Section 1.3, p. 7

**Extracted quote:**
> While Scientist AI is intended to prevent accidental loss of control, further measures are needed to prevent misuse. Bad actors could for example decide to turn the non-agentic AI into an unguarded agent, maybe for military or economic purposes. If done without the proper societal guardrails, this could yield loss of human control.

**Context from source** (±3 sentences):
> This allows us to obtain hard safety guarantees
asymptotically as the amount of compute is increased. This does not change the fact that more data or data
that is more informative would reduce the uncertainty expressed by those probabilities. As usual, more and
better data would allow the model to discover aspects of the world that may otherwise remain invisible. While Scientist AI is intended to prevent accidental loss of control, further measures are
needed to prevent misuse. Bad actors could for example decide to turn the non-agentic AI into an
unguarded agent, maybe for military or economic purposes. If done without the proper societal guardrails,
this could yield loss of human control. This transformation from non-agentic to agentic can be done by
asking the Scientist AI what one should do to achieve some goal, for example how to build a dangerous new
weapon, and by continuously feeding the AI with the observations that follow from each of its actions. These
types of issues must be dealt with through technical guardrails derived from the Scientist AI, through the
security measures surrounding the use of the Scientist AI, and through legal and regulatory means. To address the uncertainty in the timeline to AGI (Wynroe, Atkinson, and Sevilla 2023; Y.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 7

**Term:** loss of control
**Location:** Section 2, p. 8

**Extracted quote:**
> This section reviews arguments for how loss of control to generalist agentic AI may occur, with potentially catastrophic consequences, providing motivation for Section 3 on designing safe non-agentic AI.

**Context from source** (±3 sentences):
> We structure our
research plan with a tiered approach, featuring progressively safer yet more ambitious solutions for different
time horizons. The objective is to hedge our bets and allocate resources to both short-term and long-term
efforts in parallel rather than only start the long-term plans when the short-term ones are completed, so as
to be ready with improved solutions at any time compared with a previous time point. 7


2
Understanding loss of control to agentic AI
This paper consists of two main sections. This section reviews arguments for how loss of control to generalist
agentic AI may occur, with potentially catastrophic consequences, providing motivation for Section 3 on
designing safe non-agentic AI. Section 2 is structured as follows. Section 2.1 introduces some preliminaries and terminology. Then, we
examine in Section 2.2 the current AI R&D trajectory, headed towards AGI and then ASI agents, and why,
at a high level, this could yield a loss of human control and the emergence of rogue AI agents.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 8

**Term:** loss of human control
**Location:** Section 2, p. 8

**Extracted quote:**
> Then, we examine in Section 2.2 the current AI R&D trajectory, headed towards AGI and then ASI agents, and why, at a high level, this could yield a loss of human control and the emergence of rogue AI agents.

**Context from source** (±3 sentences):
> This section reviews arguments for how loss of control to generalist
agentic AI may occur, with potentially catastrophic consequences, providing motivation for Section 3 on
designing safe non-agentic AI. Section 2 is structured as follows. Section 2.1 introduces some preliminaries and terminology. Then, we
examine in Section 2.2 the current AI R&D trajectory, headed towards AGI and then ASI agents, and why,
at a high level, this could yield a loss of human control and the emergence of rogue AI agents. We discuss
plausible consequences of the emergence of such rogue AIs, which could threaten democratic institutions
and the future of humankind. We move to Section 2.3, which analyzes the AI behaviors and skills that
would make an uncontrolled AI dangerous, such as deception, persuasion, hacking, and collusion. The last
two sections go deeper into two principal ways dangerous misalignment and self-preservation could emerge:
firstly, due to reward maximization (Section 2.4), and secondly, due to imitation of humans (Section 2.5).

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 9

**Term:** uncontrolled
**Location:** Section 2, p. 8

**Extracted quote:**
> We move to Section 2.3, which analyzes the AI behaviors and skills that would make an uncontrolled AI dangerous, such as deception, persuasion, hacking, and collusion.

**Context from source** (±3 sentences):
> Section 2.1 introduces some preliminaries and terminology. Then, we
examine in Section 2.2 the current AI R&D trajectory, headed towards AGI and then ASI agents, and why,
at a high level, this could yield a loss of human control and the emergence of rogue AI agents. We discuss
plausible consequences of the emergence of such rogue AIs, which could threaten democratic institutions
and the future of humankind. We move to Section 2.3, which analyzes the AI behaviors and skills that
would make an uncontrolled AI dangerous, such as deception, persuasion, hacking, and collusion. The last
two sections go deeper into two principal ways dangerous misalignment and self-preservation could emerge:
firstly, due to reward maximization (Section 2.4), and secondly, due to imitation of humans (Section 2.5). The arguments in this paper support the case that the Scientist AI approach would not only help reduce
the likelihood of loss of human control but would also help us build more trustworthy and explanatory AI
systems that could accelerate scientific research. Additionally, the paper proposes how a Scientist AI could
be used to double-check or guardrail any other AI system.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 10

**Term:** loss of human control
**Location:** Section 2, p. 8

**Extracted quote:**
> The arguments in this paper support the case that the Scientist AI approach would not only help reduce the likelihood of loss of human control but would also help us build more trustworthy and explanatory AI systems that could accelerate scientific research.

**Context from source** (±3 sentences):
> We discuss
plausible consequences of the emergence of such rogue AIs, which could threaten democratic institutions
and the future of humankind. We move to Section 2.3, which analyzes the AI behaviors and skills that
would make an uncontrolled AI dangerous, such as deception, persuasion, hacking, and collusion. The last
two sections go deeper into two principal ways dangerous misalignment and self-preservation could emerge:
firstly, due to reward maximization (Section 2.4), and secondly, due to imitation of humans (Section 2.5). The arguments in this paper support the case that the Scientist AI approach would not only help reduce
the likelihood of loss of human control but would also help us build more trustworthy and explanatory AI
systems that could accelerate scientific research. Additionally, the paper proposes how a Scientist AI could
be used to double-check or guardrail any other AI system. 2.1
Preliminaries: agents, goals, plans, affordances and knowledge
We start by recalling and specifying some important terms. Agents observe their environment and act in it in order to achieve goals.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 11

**Term:** loss of human control
**Location:** Section 2.2, p. 9

**Extracted quote:**
> We focus here mostly on the risk of loss of human control because it is a risk whose severity could go as far as human extinction, according to a large number of AI researchers (Center for AI Safety 2023; Grace et al. 2024).

**Context from source** (±3 sentences):
> 2025) for a survey. In risk
analysis, it is important to distinguish the likelihood of the harmful event from its severity, i.e., how bad
the consequences would be if the harmful event occurs. While as humans we are often drawn to consider
risks that have high probability and we may dismiss events of low probability as unrealistic, it can be just as
worrying for an event to have low probability but very high severity. We focus here mostly on the risk of loss
of human control because it is a risk whose severity could go as far as human extinction, according to a large
number of AI researchers (Center for AI Safety 2023; Grace et al. 2024). Opinions vary on its probability,
but if we do build AGI as envisioned by several major corporations (OpenAI 2023; Google DeepMind 2024),
there are difficult-to-dismiss scenarios in which humanity’s future as a whole could be in peril, as discussed
below, with behaviors and skills that make loss of control dangerous (as described in Section 2.3). 2.2.1
AI agents may be misaligned and self-preserving
In this paper we will discuss various catastrophic scenarios involving rogue AI agents. These scenarios are
not due to AIs developing explicit malicious intent towards humans, like a fictional villain, but are rather the
result of AIs trying to achieve their goals.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 12

**Term:** loss of control
**Location:** Section 2.2.5, p. 12

**Extracted quote:**
> More precisely, the probability of loss of control may increase simply because such an event requires an AI with sufficient capabilities in key areas (e.g., cyber attacks, deception, etc.) to free itself from our control. The severity of a loss-of-control event also increases with computational power of the AI because some capabilities (such as the design of bioweapons or the ability to control robots) significantly increase the amount of damage that a rogue AI could inflict.

**Context from source** (±3 sentences):
> In this paper, we propose that the degree of agency
is an important feature of any AI system which can help us distinguish between the dangerous competitor
and the useful tool. 2.2.5
Risks associated with agentic AIs scale with capabilities and compute
Since more dangerous AI plans require more compute, we can expect that existential risks increase as more
computational resources are devoted to agentic AI development, and we are indeed seeing an acceleration
of such investments (Cottier et al. 2024; OpenAI 2025a). More precisely, the probability of loss of control
may increase simply because such an event requires an AI with sufficient capabilities in key areas (e.g.,
cyber attacks, deception, etc.) to free itself from our control. The severity of a loss-of-control event also
increases with computational power of the AI because some capabilities (such as the design of bioweapons or
the ability to control robots) significantly increase the amount of damage that a rogue AI could inflict. We
stress this point because in Section 3.5.2, we propose to consider ways to reverse this trend such that more
computational resources would generally increase safety, thereby charting a path where further technological
advances are to our benefit rather than our disadvantage. 2.3
Dangerous AI behaviors and capabilities
Supposing the emergence of an ASI agent with a misaligned self-preservation goal, we now try to clarify
some of the AI behaviors (like deception) and skills (like persuasion and programming) that can make loss of
human control dangerous because of the capabilities it would give to the AI to cause harm. How dangerous
misalignment can emerge will be discussed in Section 2.4 and Section 2.5.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 13

**Term:** loss of human control
**Location:** Section 2.3, p. 12

**Extracted quote:**
> Supposing the emergence of an ASI agent with a misaligned self-preservation goal, we now try to clarify some of the AI behaviors (like deception) and skills (like persuasion and programming) that can make loss of human control dangerous because of the capabilities it would give to the AI to cause harm.

**Context from source** (±3 sentences):
> More precisely, the probability of loss of control
may increase simply because such an event requires an AI with sufficient capabilities in key areas (e.g.,
cyber attacks, deception, etc.) to free itself from our control. The severity of a loss-of-control event also
increases with computational power of the AI because some capabilities (such as the design of bioweapons or
the ability to control robots) significantly increase the amount of damage that a rogue AI could inflict. We
stress this point because in Section 3.5.2, we propose to consider ways to reverse this trend such that more
computational resources would generally increase safety, thereby charting a path where further technological
advances are to our benefit rather than our disadvantage. 2.3
Dangerous AI behaviors and capabilities
Supposing the emergence of an ASI agent with a misaligned self-preservation goal, we now try to clarify
some of the AI behaviors (like deception) and skills (like persuasion and programming) that can make loss of
human control dangerous because of the capabilities it would give to the AI to cause harm. How dangerous
misalignment can emerge will be discussed in Section 2.4 and Section 2.5. We must keep in mind that trying to anticipate the ways in which an ASI might escape our control, dis-
empower, or catastrophically harm us is futile. Just as we cannot predict in advance the exact sequence
of moves today’s superhuman chess AIs can use to defeat us—despite knowing with certainty that they
will win—we cannot predict exactly what an ASI with objectives misaligned with human interests would
do.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 14

**Term:** loss of control / losing control
**Location:** Section 2.3, p. 12

**Extracted quote:**
> Loss of control could arise from advancements in deception or persuasion, as well as combined expertise in programming, cybersecurity, and AI research—areas that could enable recursive self-improvement. We discuss these pathways in Sections 2.3.1 to 2.3.3. Broader cognitive abilities and a better proficiency at long-term planning could also further compound the risk of losing control; this is discussed in Section 2.3.4.

**Context from source** (±3 sentences):
> These steps include (1) careful planning, including
resource and skill acquisition; (2) gaining influence in society through means such as manipulation of public
opinion, bribery, and hacking; and (3) ultimately disempowering humanity, for example through the use of
engineered bioweapons (Carter et al. 2023). To better understand how these steps could materialize, we need to examine the key capabilities that would
enable them. Loss of control could arise from advancements in deception or persuasion, as well as com-
bined expertise in programming, cybersecurity, and AI research—areas that could enable recursive self-
improvement. We discuss these pathways in Sections 2.3.1 to 2.3.3. Broader cognitive abilities and a better
proficiency at long-term planning could also further compound the risk of losing control; this is discussed in
Section 2.3.4. Finally, interactions between multiple ASIs introduce new complexities: collusion, conflict, and
power dynamics between such entities could create scenarios beyond human influence and understanding,
which we discuss in Section 2.3.5. 12


2.3.1
Deception
A crucial ability of an AI agent with misaligned goals is deception: the ability to mislead in order to achieve
one’s goals. Suppose that, by one mechanism or another, humanity happens to produce an AI system
with goals that are not (exclusively) in service of human flourishing.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 15

**Term:** escape human control (beyond human control)
**Location:** Section 2.3.4, p. 14

**Extracted quote:**
> Such narrow AI systems are unlikely to have the kind of general knowledge that is required to escape human control or worse.

**Context from source** (±3 sentences):
> 2021),
playing strategy games such as chess (Silver, Hubert, et al. 2018), and detecting cancer in medical images
(McKinney et al. 2020). Such narrow AI systems are unlikely to have the kind of general knowledge that is
required to escape human control or worse. These systems can also be more capable in their given domains
than powerful generalist AI systems. However, frontier AI systems are generalists for a particular scientific
14


reason: as anticipated in the early days of deep learning (Y. Bengio, Courville, and Vincent 2013) and
empirically observed for more than a decade, learning systems benefit tremendously from exposure to a wide
variety of tasks and domains of knowledge, as synergy between different domains of thought enables forms
of reasoning by analogy that is otherwise impossible.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 16

**Term:** escape human control (beyond human control)
**Location:** Section 2.3.4, p. 15

**Extracted quote:**
> By picking the domain carefully so that the narrow AI does not have expert knowledge in areas enabling its escape (such as persuasion and hacking), we can have strong assurances that the resulting AI, even if it is superhuman in its domain of competence and thus potentially very useful to society, cannot by itself escape human control.

**Context from source** (±3 sentences):
> 2023; Altmeyer et al. 2024). Interestingly, a generalist safe non-agentic AI could be used to train a narrow AI by having the generalist AI
generate synthetic data in the chosen domain. By picking the domain carefully so that the narrow AI does
not have expert knowledge in areas enabling its escape (such as persuasion and hacking), we can have strong
assurances that the resulting AI, even if it is superhuman in its domain of competence and thus potentially
very useful to society, cannot by itself escape human control. If the narrow AIs are self-preserving agents,
there is, however, the possibility of collusion between AI agents with complementary skills (see Section 2.3.5),
as well as the possibility that a narrow AI finds a way to create more capable versions of itself. The safest
form of AI is thus one that is strictly non-agentic. That kind of AI could be deployed with strong safety
assurances.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 17

**Term:** loss of control
**Location:** Section 2.4.7, p. 20

**Extracted quote:**
> It would be best if we could instead design AI systems so that as their capabilities and computational power increased, the risks associated with loss of control decreased.

**Context from source** (±3 sentences):
> The ability to successfully deceive humans also grows with general cognitive
capabilities and computational resources, especially as humans build up defenses such as alignment train-
ing (Bai, Jones, et al. 2022), automated detection of deceptive intentions with mechanistic interpretability
(Bereska and Gavves 2024), or guardrails that monitor the behavior of the AI to detect harmful actions
(Ayyamperumal and Ge 2024). It is rational for an agent with misaligned goals, and especially with a self-
preservation goal, to hide its intentions in order to achieve those goals. It would be best if we could instead
design AI systems so that as their capabilities and computational power increased, the risks associated with
loss of control decreased. This is, in fact, one of the motivations for the Scientist AI design. 20


2.5
Misaligned agency and lack of trustworthiness from imitating humans
In this section, we examine how misaligned agency can emerge from learning to imitate humans—for example,
by accurately completing human-written text, as is core to the training process for modern AI systems. The
core issue is that humans are agents, and not always benign and trustworthy.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 18

**Term:** uncontrolled
**Location:** Section 2.5.1, p. 21

**Extracted quote:**
> These goals can be implicit (not mentioned in the prompt) and can manifest in uncontrolled ways—for example, the LLM may infer that some type of person would have a certain goal, and therefore generates words to enact that goal.

**Context from source** (±3 sentences):
> Because there can be many words in the input context or fine-tuning
examples, the persona instantiated by this context could correspond to a very specific type of human, and
not necessarily a benevolent one. We can imagine many human personas which, in the shoes of the AI,
may want to act to increase their freedom, to preserve themselves, potentially by using deception and acting
against user instructions. Because humans are agents, by imitating humans an LLM is imitating agents, who have goals. These goals
can be implicit (not mentioned in the prompt) and can manifest in uncontrolled ways—for example, the
LLM may infer that some type of person would have a certain goal, and therefore generates words to enact
that goal. A lot of the research on AI alignment rests on making sure inputs to the LLM evoke the kind of benevolent
behavior the designers would like to see in their AI (Bai, Kadavath, et al. 2022). Unfortunately, it has
turned out to be difficult to do so robustly, and adversarial user prompts (“jailbreaks”) can easily counter
the previous training or policy instructions the AI has received (Zou et al.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 19

**Term:** loss of control
**Location:** Section 3.1.1, p. 24

**Extracted quote:**
> There is a lot of uncertainty about the exact timeline at which agentic AI systems might become powerful enough to run a high risk of loss of control (Wynroe, Atkinson, and Sevilla 2023).

**Context from source** (±3 sentences):
> Readers interested at a higher
level may wish to read just Section 3.1 and then skip to Section 3.8, where we describe potential applications
of the Scientist AI. 3.1
Introduction to the Scientist AI
In this section, we describe the backdrop of our safe AI research plan and the considerations that shaped
its structure. We define our Scientist AI in broad terms, and discuss a few important properties that all
combine to provide the safety that we seek. 3.1.1
Time horizons and anytime preparedness
There is a lot of uncertainty about the exact timeline at which agentic AI systems might become powerful
enough to run a high risk of loss of control (Wynroe, Atkinson, and Sevilla 2023). A research program
to build safer AI systems should include shorter-term and more easily achieved actions on top of its more
ambitious longer-term goals. Shorter term steps providing reduced safety assurances could be all we can
muster before the risk of uncontrolled AIs is on the horizon. It is reasonable to simultaneously explore projects with different levels of ambition and expected delivery
horizons, so as to be ready at any time—“anytime preparedness”—with the best results such a research
program could offer by a given time.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 20

**Term:** uncontrolled
**Location:** Section 3.1.1, p. 24

**Extracted quote:**
> Shorter term steps providing reduced safety assurances could be all we can muster before the risk of uncontrolled AIs is on the horizon.

**Context from source** (±3 sentences):
> We define our Scientist AI in broad terms, and discuss a few important properties that all
combine to provide the safety that we seek. 3.1.1
Time horizons and anytime preparedness
There is a lot of uncertainty about the exact timeline at which agentic AI systems might become powerful
enough to run a high risk of loss of control (Wynroe, Atkinson, and Sevilla 2023). A research program
to build safer AI systems should include shorter-term and more easily achieved actions on top of its more
ambitious longer-term goals. Shorter term steps providing reduced safety assurances could be all we can
muster before the risk of uncontrolled AIs is on the horizon. It is reasonable to simultaneously explore projects with different levels of ambition and expected delivery
horizons, so as to be ready at any time—“anytime preparedness”—with the best results such a research
program could offer by a given time. Short term. Current safety fine-tuning is based on supervised or reinforcement learning, both of which
suffer from the safety considerations discussed in Section 2.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 21

**Term:** uncontrolled
**Location:** Section 3.1.5, p. 27

**Extracted quote:**
> For this reason, we designed the Scientist AI such that it can also be employed as a guardrail against uncontrolled or misused agentic systems.

**Context from source** (±3 sentences):
> If needed, confidence intervals around
the predicted probabilities can be used to estimate the prediction error resulting from limited computational
resources. For further details, see Section 3.5. 26


3.1.5
Using the Scientist AI as a guardrail
We acknowledge that agentic AIs may be developed in spite of the risks. For this reason, we designed
the Scientist AI such that it can also be employed as a guardrail against uncontrolled or misused agentic
systems. This will be explored in Section 3.8.2. Crucially, a Scientist AI can also serve as a guardrail for
other instances of itself. Despite efforts to ensure its inherent safety, it could be misused or, in the worst
case, turned into an agent, intentionally or inadvertently.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 22

**Term:** loss of control (loss-of-control)
**Location:** Section 3.2, p. 28

**Extracted quote:**
> We claim that an AI system requires all three of these properties to pose the dangers laid out in Section 2. Therefore, eliminating any one property would be sufficient to mitigate most categories of loss-of-control risk (Krueger 2024).

**Context from source** (±3 sentences):
> Since goal-directedness, by definition,
requires an (arbitrary) choice of what to value, goal-directedness requires a persistent state to keep track of
that choice, so as to pursue it. In addition, an agent’s state may include beliefs about the environment and
other attributes of self. This often culminates in a situational awareness that is the confluence of all three
traits: the sensory affordances needed to make observations about one’s place in the world, the persistent
state needed to maintain a coherent direction towards one’s goals, and the short-term memory needed to
intelligently put it all together with practical reasoning. We claim that an AI system requires all three of these properties to pose the dangers laid out in Section 2. Therefore, eliminating any one property would be sufficient to mitigate most categories of loss-of-control
risk (Krueger 2024). We explore several such cases below, focusing on limiting affordances and eliminating
goal-directedness (although we also consider the case of limiting intelligence, for narrow AIs, in Section 3.2.2). 3.2.1
How to make a non-agentic Scientist AI
In light of the previous discussion on agency, our proposal—the Scientist AI—is explicitly designed to be
non-agentic from the outset. As summarized in Section 3.1.2, it consists of a question-answering inference
system, based on a world model that generates causal theories to explain observed data.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 23

**Term:** loss of control
**Location:** Section 3.2.2, p. 29

**Extracted quote:**
> While agency risks cannot be entirely eliminated even in narrow AI systems, if the risks of loss of control are sufficiently small due to limitations on the system’s capabilities, such narrow agentic AIs might be operated safely.

**Context from source** (±3 sentences):
> 28


3.2.2
The safety of narrow agentic AIs
Agency can also be restricted by constraining the system’s intelligence to a narrow range, for example, by
training it on a limited dataset for a specific task or distilling it from a generalist model. This approach
is commonly used in the development of narrow AI systems, such as those designed for specific medical or
scientific applications (McKinney et al. 2020), or even in agentic contexts like autonomous driving (Bojarski
2016). While agency risks cannot be entirely eliminated even in narrow AI systems, if the risks of loss of
control are sufficiently small due to limitations on the system’s capabilities, such narrow agentic AIs might
be operated safely. However, narrow AIs could engage in collusion, as discussed in Section 2.3.5. A narrow agentic AI can be further restricted by limiting its affordances (i.e., the actions that it can take) to
its specialized domain, such as driving a car or operating a drug discovery robotic apparatus. Additionally,
our Scientist AI could serve as a guardrail or an additional safety layer for narrow agentic AI systems, as
discussed further in Section 3.8.2.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 24

**Term:** uncontrolled
**Location:** Section 3.8.3, p. 46

**Extracted quote:**
> Such a system could emerge if hostile actors transform a non-agentic AI into a dangerous agent, or if an uncontrolled ASI is exploited as a geopolitical threat.

**Context from source** (±3 sentences):
> The crucial advantage of using a Scientist AI in this research program is that we would be able to trust it,
whereas if we try to use an untrusted agentic AI to help us figure out how to build future and supposedly
safe ASI, it may fool us into building something that would advance its goals and endanger us, for example
by proposing code with back-doors that we are not able to detect. One may however ask why we would want to build ASI at all, if we do not have the answers to these
questions. One motivation is that a safe agentic ASI may be necessary to defend humanity against a rogue
system. Such a system could emerge if hostile actors transform a non-agentic AI into a dangerous agent, or
45


if an uncontrolled ASI is exploited as a geopolitical threat. Regulations and treaties can reduce these risks
but cannot remove them entirely. Alternative measures must be in place to ensure that any ASI developed
is both safe and able to protect humanity. 46


4
Conclusion
The frontier AIs of today are increasingly capable generalist agents.

**Quote verification:** VERIFIED (ratio: 0.96)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---