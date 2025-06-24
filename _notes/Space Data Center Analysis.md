---
title: Space Data Center
created: 2025-06-19
published: 2025-06-20
tags:
  - space
  - WiP
permalink: /space-data-centers-1
top_of_mind: "true"
completion_score: 25
image:
companion music:
subtitle:
---
# Abstract

Starcloud have claimed that a single 100-ton Starship launch could suffice to create a 40 MW space data centre (SDC) for $8.2 M. My analysis finds that this could be feasibly within a single launch with existing roll-out solar panels used on the ISS. However, this is based on speculative numbers on the iROSA's stowed volume. This single launch feasiblity could change as sizing radiators and MMOD/radiation shielding is pending. Considerations for fuel requirements for in-space assembly will also significantly affect launch numbers—this requires specifications and mission architectures that are not publicly available. On the note of launch costs, the whitepaper's (erroneous) assumed launch cost is $30/kg. This makes their comparative economic analysis to terrestrial data centers unmoored from reality in the near term; even if launch comes down to $500/kg{%sidenote "owid-launch-cost" "In [2021 dollars](https://ourworldindata.org/grapher/cost-space-launches-low-earth-orbit), a Falcon-9 launch costs $2600/kg and a Falcon Heavy's at $1500/kg. So, even $500/kg is also a fairly optimistic estimate."%}, one launch would result in an overall cost of $53.2M, not the purported $8.2M. Some experts speculate that $1000/kg would be an optimistic launch cost, which means $100M per launch and a total cost of $103.2M. If a second launch is needed, then the worst case number is $200M making it more than their reported cost of running a terrestrial data center (TDC).


> [!warning]This is a work-in-progress
> This block is to warn you that everything below should be considered a draft as there is more analysis to be completed. This block will be removed once I feel my analysis is complete and fully documented below. So, please treat everything below as potentially inaccurate as this is just my explorations of working in public.

# Introduction

On Earth, data centers run on the existing electricity grid that, crudely put, use a combination of fossil fuels or terrestrial solar. So, technologists and entrepreneurs have recently talked up data centres in space to resolve three issues with terrestrial data centers (TDC):
1. Data centers require tremendous amounts of energy, which is plentiful and "free" in space. There, 24/7 solar power is unhindered by day/night cycles, weather, and atmospheric losses (attenuation).
2. A lot of waste heat is generated running TDCs, which bodes poorly for climate change—so migrating to space would alleviate the toll on Earth's thermal budget. This seems like a compelling environmental argument. TDCs already consume about [1-1.5% of global electricity](https://www.iea.org/energy-system/buildings/data-centres-and-data-transmission-networks) and it's safe to assume that this will only grow in the pursuit of AGI.
3. Real estate for data centers is a massive bottleneck and this land could be used for other purposes.

Now, Sam Altman has also talked up nuclear energy as a solution, which I suspect is maybe a more desirable solution from an energy and climate angle but the regulatory barriers need resolution. So, space, in theory, sounds like a speedier answer from a regulatory framework—as a space person, I'd love nothing more than for there to be a strong economic case for space[^1]. But to deliver GW-scale SDCs require engineering solar arrays in the km scale, which will not be easy. Even the 40 MW system, that Starcloud used to benchmark against TDCs, would need a square of side 357m. This would far exceed the span of largest space structure ever built—the ISS is about 100 m.

So, there's now at least one YCombinator-backed company, Starcloud Inc., working on building SDCs—they released a white paper on this and I decided to dive in (with Claude to speedrun my analysis, of course). They begin by pointing us to some of the unique benefits of space solar, the main one being its 95%+ [capacity factor](https://en.wikipedia.org/wiki/Capacity_factor) versus just a median capacity factor of 24% for US terrestrial solar (under 10% in northern Europe). They continue to say that combined with 40% higher peak power due to no atmospheric losses, you get over 5x the energy output from the same solar array. This is not exactly my forte so I am not fact-checking these claims—let's accept them as true.

## My qualifications

If I can claim a bit of domain expertise, it's on the space side. Reading Starcloud's whitepaper, I felt I could use my limited expertise from [designing mission for in-space assembled large space telescopes and analysing them](https://www.sciencedirect.com/science/article/pii/S0094576524004612) to understand their techno-economic analysis.

## Space challenges

Now, in-space assembly of large space structures, like large aperture telescopes, comes with its own challenges. For the sake of this analysis, I will classify them in the same three categories as I did at the start for TDCs but present them in reverse order:
1. Real estate: Starcloud's target is to achieve a 5 GW cluster spanning, with solar arrays spanning 4 km by 4 km—this would comfortably become the largest structure in space—which will need in-space assembly. This is, in some sense, equivalent to real estate.
2. Cooling (aka Thermal Management): On Earth, data centers use air (convection) and water cooling (conduction) but in space, thermal management requires radiation, which is less efficient—convection is impossible in a vacuum and while water could extract heat from the center, cooling that heated up water would then pose another problem.
3. Finally, we could also think about if/when the carbon footprint of launches offset the benefits of a SDC. But the report suggests that achieving AGI could need 1 GW centers but large hyperscale Earth-based data centers today reach 100 megawatts (MW) meaning they "do not scale well or sustainably to gigawatt (GW) sizes".

Now, I will treat that last item as speculative mostly because it is out of my wheelhouse. However, if it is true, then we will need some alternative (either nuclear or space-based data centers) but by examining the first two aspects, I imagine we will know how well the business case of this company adds up.
# Starcloud's Business Case
While one could begin by asking how much compute workload should be moved to space to make a meaningful dent on the climate—a really good reason to do so—economic incentives that lead to large returns on investment are what appeal to private at the end of the day which is why Starcloud exist but space agencies haven't invested here. So, my analysis begins by examining [[starcloud-wp.pdf|Starcloud]]'s numbers to justify their business case for SDC.

Their whitepaper presents a table where the total costs of running a 40MW data centre cluster over ten years is determined to be $167M on Earth versus $8.2M for space; launch is the largest contributor to Starcloud's total costs and they presume that one launch shall be enough, which I was skeptical about.

The costs for TDCs and SDCs are broken down as follows:
**Terrestrial:**
- Energy: $140M (@ $0.04/kWh)
- Cooling: $7M (@ 5% of power usage)
- Water: 1.7M tons (@ 0.5L/kWh)
- Backup power: $20M
- **Total: $167M**
	  
**Space:**
- Energy: $2M (cost of solar array)
- Launch: $5M (single launch)
- Radiation shielding: $1.2M
- **Total: $8.2M**

Now this means their projected energy cost is $0.002/kWh in space versus $0.045-0.17/kWh terrestrially—this is between 22 to 85 times cheaper. This raises questions about feasibility.

# Solar Arrays: Launch Numbers from First Principles

To determine the cost of launch requires knowledge of number of launches. There are number of ways we can go about doing this: the traditional approach would involve determining the mass of the SDC—this assumes to be how Starcloud make their single launch claim but there is no clarity on how their system could be 100 tonnes which requires some initial SDC design.

After a mass-based estimate of launches, one can further refine the first-order designs to determine revised launch numbers that account for how the SDC structure fits into a rocket{%sidenote "architecture-launch-numbers" "Here, one essentially breaks the large space system into its smaller elements and works out if/how their geometries can be made to fit into the volume of a launcher's fairing. So, even if the mass estimates indicate the SDC fits into a single launcher, its parts might not necessarily be as accommodating."%}.

As Starcloud haven't publicly shared their mass breakdown or component-level design documentation—could either be proprietary information or they are still figuring this out—it is hard to verify their mass claims. I hope to derive this in a future update to this post{%sidenote 'telescope-assembly-overlap' "I see many overlapping architectural challenges here based on my earlier work into in-space assembly of space telescopes"%}. But there is another way for us to determine the number of launches- from their SDC's assumed power density (i.e., power output by a solar array per unit area). I will present that after a short detour to illustrate an issue with the math in their whitepaper.

> [!warning]White paper math is incongruous
> The whitepaper states $5M to launch a 100-tonne Starship to Low Earth Orbit (LEO) Sun-Synchronous Orbit (SSO). This works out to a $50/kg to reach orbit but the whitepaper says that this translates to $30/kg—this is in two locations so I am unsure why this is the case. With their claimed per kg cost, the mass of the SDC is 167 tonnes. This means two 100-tonne Starship launches or, it could be a single 200-ton Starship launch, which is on SpaceX's roadmap. This means their launch cost just went up by $3M or $5M—though, as I say in the abstract, a single launch would cost $50M {%sidenote 'optimistic-thousand-per-kg' "This could even be $100M per 100-tonne launch as some have said $1000/kg to orbit is also a reasonable cost."%}.

## Desired Packaging Densities

Their long-term goal is to build a 5 GW system which they state needs solar arrays spanning an area of 4km × 4km. This is a power density of 312 W/m², which we will denote as $$P_{\text{solar}}$$. Using the same power density, their smaller 40 MW SDC needs 128,000 m² of solar panels. This would need to be packed into a single launch Starship, which has a fairing volume of 1000 m³. We now define areal packing density, which is the area of these arrays divided by the Starship's fairing volume; this works out to 128 m²/m³.

$$
\begin{align}
{(Packing \, density)}_{desired} &=\frac{128,000}{1000}\\ &= 128 \, m^2/m^3
\end{align}
$$

This means that we would need to fit 128 m² into a  m³ of Starship. This is a quite optimistic estimate as every little bit of volume is being used; but such efficiency is impractical. A more realistic estimate would be that 80% of the available 1000 m³ can be used; the areal packing density then becomes **160 m²/m³**.

To estimate if this is feasible based on current technologies, I will examine the performance of two space-proven designs for deployable solar arrays (of the three options that Starcloud propose to use as per their whitepaper). The first design is the **Z-folds arrays** which are the legacy design used on the ISS's Solar Array Wings (SAW) and the second, called roll-out solar arrays (ROSA), augmented to the SAW's and are set to become its next-generation replacements; this ISS variant is called iROSA.

## Analysis of Solar Array Wings (SAW)

The image below shows a ROSA and against one wing of the ISS Solar Array Win (SAW).

![ISS SAW is a LOT larger than the early ROSA.](assets/imgs/space-data-centers/Rosa-SAW.png)

The ISS has 8 such (SAWs) attached to trusses; four each on its port and starboard side—which explains why the trusses names are prefixed with P's and S's (e.g., P-6 and S-6). Altogether, the eight solar array wings generate about 240 kilowatts in direct sunlight, or about 84 to 120 kilowatts average power (cycling between sunlight and shade).

Each wing generates nearly 31 kilowatts (kW) of direct current power from two solar "blankets". When fully extended, the pair span 35 metres in length and 12 metres in width. These are the largest ever deployed in space and weighing well 1,100 kg. Now, the power density based on this wing span works out to about 71.43  W/m² but a more accurate estimate is possible. Each photovoltaic blanket comprises 16,400 cells of 8-cm by 8-cm; this gives the real actual light collecting area of each blanket and multiplying by two results in that for a single SAW.
### Power Density

So the power density of a wing with two blankets works out to 147.7  W/m² from:

$$
\begin{align}
{(Power \, Density)}_{SAW} &= \frac{Power}{Area} \\
&= \frac{31000W}{32800 \times .08^2} \\
&= 147.7 \, W/m^2
\end{align}
$$

So, to achieve Starcloud's assumed power density of 312 W/m², solar technology would need to be **2.1x more efficient** than SAW's 147.7 W/m².

### Packing Density

To determine the packing density of one SAW module (i.e., a pair of deployable blankets), we use the stowed volume of this single module that fit within a launched vehicle. The data suggest that this is a cuboid of square face of 4.57 m and 0.51 m thick—the result is a packing density of

$$
\begin{align}
{(Packing \, density)}_{SAW} &= \frac{35 \times 12}{4.57^2 \times 0.51}\\ &= 39.43 \, m^2/m^3
\end{align}
$$

This density is far lower than the packing density needed by Starcloud. Therefore, to determine the number of launches, we would just need to comput the ratio of the Starcloud and SAW packing densities—a dimensionless number. This is 3.24 which means we would need nearly 4 launches with SAW technology. If we used the more realistic estimate packing density (160 m²/m³), it might need 5 launches.
## Analysis of ISS Roll-Out Solar Array (iROSA)

![iROSAs are half the length and width of the SAW but much larger than the early ROSAs developed for other missions.](assets/imgs/space-data-centers/irosa.png)

The ISS Roll Out Solar Arrays (iROSA) were launched in two pairs in June 2021 and November 2022 to augment to the first SAWs, launched in 2000 and 2006 and attached to the P6 and P4 Trusses. These SAWs were noticeably degrading towards the end of their 15-year life. Six of the intended 8 iROSAs have been added in [following sequence](https://en.wikipedia.org/wiki/Integrated_Truss_Structure#Solar_arrays):
- iROSA 1 and 2 was added in front of Old 4B and 2B solar arrays on P6 truss in June 2021;
- iROSA 3 and 4 was added in front of Old 3A and 4A solar arrays on S4 and P4 truss in December 2022;
- iROSA 5 was added in front of Old 1A solar array on S4 truss in June 2023; and
- and iROSA 6 was added in front of Old 1B solar array on S6 truss in June 2023.
The seventh and eighth, are planned to be installed on the 2A and 3B power channels on the P4 and S6 truss segments in 2025.

### Power Density

Each iROSA generates nearly 20 kilowatts (kW) of direct current power from two rolled-up solar blankets. When fully extended, the pair span 18.3 metres in length and 6 metres in width. The gap between the blankets is not in the public domain but appears to be more negligible than between a pair of SAW blankets; the specifications of the solar cells and their arrangement are also known. So, the power density here is based purely on the wing span, which works out to about 255 W/m² from:

$$
\begin{align}
{(Power \, Density)}_{iROSA} &= \frac{Power}{Area}\\ &= \frac{20000}{18.3 \times 6}\\ &= 182.1 \, W/m^2
\end{align}
$$

So, to achieve Starcloud's assumed power density of 312 W/m², solar technology would need to be **1.71x more efficient** than iROSA's 255 W/m².

### Packing Density

{% marginfigure 'mf-id-1' 'assets/imgs/space-data-centers/iROSA-dragon.jpg' "iROSA canisters stowed in cargo Dragon's trunk. [Source](https://en.wikipedia.org/wiki/File:Crs-28-sep-1024x576.jpg)"  %}

As done with the SAW module analysis (i.e., a pair of deployable blankets), we can use the stowed volume of an iROSA module to compute the number of launches. Sadly, this data is also not public but estimates can be made by examining its imagers stowed in a cargo Dragon as well as alongside humans for scale. The iROSAs packed into a cargo Dragon trunk and each blanket packed into a canister; the length of this canister can be assumed to be 3 m, a dimension that remains unchanged for either blanket as it rolls out. Each blanket's 18.3 m deployed span can be assumed to pack into a canister of diameter of 0.3 m. So two such canisters per iROSA leads to a packing density of 

$$
\begin{align}
{(Packing \, Density)}_{iROSA} &= \frac{18.3 \times 6}{2\pi \times 0.15^2 \times 3} \\&= 258.78 \, m^2/m^3
\end{align}
$$

Again, one can determine the number of launches for the SDC's solar panels by computing the ratio of the Starcloud and iROSA packing densities. At 0.49, this is well under a single Starship launch but, if the canister canister diameter increases to 0.5 m, 2 launches become necessary. The iROSA canisters diameter could fall anywhere in this range.

## Summary of Launches

Our calculations thus far are summarised below, where the pessimistic launch cost is based on a $100M Starship launch and an optimistic cost uses Starcloud's $5M launch cost assumption:

{%marginnote 'table' "Improvement on preceding solar technologies and related launch numbers" %}

| Array Design | Launches | Optimistic cost ($) | Pessimisitic cost ($) |
| ------------ | -------- | ------------------- | --------------------- |
| **Z-fold**   | 4 to 5   | 20M-25M             | 400M-500M             |
| **Roll-out** | 1 to 3   | 5M-15M              | 100M-300M             |

The above is not to say that SDCs have no value but the answer for space commercialisation is unlikely to be found through economic analysis through overly optimistic launch costs.

So this begs the question if it is possible to build the radiators in the remaining margin retained by the areal density—this will need to be repeated for the in-space assembly requirements. This will be explored in the future.

# Radiator Efficiency and Launch Analysis

To reject the full 40 MW thermal load generated by the data center, radiative cooling in deep space is required. Since space lacks convective and conductive heat transfer, **all waste heat must be radiated**, this is typically done via deployable surfaces.

Starcloud propose a passive radiator system operating near **20 °C**, facing deep space at ~3 K. Its theoretical limit is governed by the **Stefan–Boltzmann Law**, which tell us that

$$
P_{\text{body}} = 2 \cdot \varepsilon \cdot \sigma \cdot T^4
$$

where, Emissivity, $$\varepsilon = 1 $$ for a black body (Starcloud assumes this to be 0.92 for their radiators), the Stefan-Boltzmann constant ($$\sigma=5.67 \times 10^{-8} \, \text{W}\text{m}^{−2}\text{K}^{−4}$$) and radiator temperature ($$ T = 293.15\,\text{K} $$) so we can determine

$$P_{\text{radiator}} = 770.48\,\text{W}$$

as the heat radiated from both sides of a $$1 \text{m}^2$$ plate. So, with practical adjustments for real materials and environmental exposure, the net heat radiated by the plate in practice depends on the heat absorbed from the Sun $$(P_{\text{Sun}})$$ and Earth $$(P_{\text{Earth}})$$and is given by:

$$
P_{\text{net}} = P_{\text{radiator}} - (P_{\text{Sun}} + P_{\text{Earth}})
$$

One side of the radiator is in direct sunlight so the heat it absorbs is calculated as:

$$ \begin{align} P_{\text{Sun}} &= (\alpha \cdot S) \\ &= 0.09 \cdot 1366 \\ &= 122.94 , \text{W/m}^2 \end{align} $$

, where the plate's absorptivity is $$ \alpha = 0.09 $$, and solar irradiance in space is $$
S = 1366 \text{W}/\text{m}^2$$.

The thermal energy absorbed by the plate from the Earth’s albedo and blackbody radiation, is determined from:

$$
\begin{align}
P_{\text{Earth}} &= \alpha \cdot F \cdot (Al \cdot S + \sigma \cdot T_{\text{earth}}^4) \\
%%  %%&= 0.09 \cdot 0.25 \cdot (0.3 \cdot 1366 + 5.67 \times 10^{-8} \cdot (273.15 - 20)^4) \\
&= 14.46 \,\text{W/m}^2 \end{align}
$$

where, we have some additional terms such as the view factor $$(F = 0.25)$$, Earth's black body temperature $$(T_{Earth} = -20 °C)$$, and Earth's albedo $$(Al = 0.3)$$. Thus, the net radiative power per square meter of a passive radiator system operating near **20 °C** is therefore:

$$
\begin{align}
P_{\text{rad, net}} &= \underbrace{770.48}_{\text{Radiated (both sides)}} - \underbrace{122.94}_{\text{Sun absorbed}} - \underbrace{14.46}_{\text{Earth absorbed}}\\ &= \boxed{633.08\,\text{W/m}^2}
\end{align}
$$

## Radiator Area Required

This can be used to compute the area needed to radiate 40 MW of waste heat (assuming as much heat is generated as electricity is produced):

$$
A_{\text{rad}} = \frac{40{,}000{,}000}{633.08} \approx \boxed{63{,}190\,\text{m}^2}
$$

This is roughly **0.063 km²** of radiator surface that their whitepaper claims also needs packing in  the same Starship's fairing volume of 1000 m³. The areal packing density is 63.2 m²/m³.

$$
\begin{align}
{(Packing \, density)}_{desired} &=\frac{63{,}190}{1000}\\ &= 63{.}19 \, m^2/m^3
\end{align}
$$

A more realistic estimate would be based on 80% of the fairing volume being available. In this case, the areal packing density is **79 m²/m³**.
## Clarifications of white paper on radiator performance

Previously, we calculated the **solar power density** as:

$$
P_{\text{solar}} = \boxed{312.5\,\text{W/m}^2}
$$

and determined the area of solar arrays required for a 40MW cluster as $$A_{\text{solar}}=128{,}000\,\text{m}^2$$. The area ratio of solar to radiator is then:

$$
\frac{A_{\text{solar}}}{A_{\text{rad}}} = \frac{128{,}000}{63{,}190} \approx 1.94
$$

which is in agreement with Starcloud's claims that radiator area needed is roughly half that of the solar array. However, examining the power density ratio of the radiator to solar  arrays tells us that the performance of the radiator is just about twice better than the power generation capacity of the solar panels. For an idealized two-sided blackbody plate's power denity, this ratio is 2.68; this is closer to the paper's statement of "roughly three times the electricity generated per square meter by solar panels". Thus, it is important to clarify that under Starcloud’s assumed radiator and environmental parameters, the whitepaper's commentary could be strengthened by focusing on a radiator system's heat rejection capability being approximately **twice**, not three times, the power per square meter as the solar array generates electricity.

## ISS radiators
[The station's systems and experiments consume a large amount of electrical power, almost all of which is converted to heat.](https://en.wikipedia.org/wiki/International_Space_Station#:~:text=The%20station%27s%20systems%20and%20experiments%20consume%20a%20large%20amount%20of%20electrical%20power%2C%20almost%20all%20of%20which%20is%20converted%20to%20heat). To achieve thermal control and maintain components at acceptable temperatures, this heat must be transferred to space. An Active Thermal Control System (ATCS) achieves this heat rejection function when the combination of the ISS external environment and the generated heat loads exceeds the capabilities of the [Passive Thermal Control System (PTCS)](https://ntrs.nasa.gov/api/citations/20180004456/downloads/20180004456.pdf) to maintain temperatures. The PTCS is made of external surface materials, insulation such as MLI, and heat pipes.

The [ATCS Overview](https://www.nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf) essentially tells us that it comprises equipment and subsystems that provide thermal conditioning via fluid flow, e.g. ammonia and water, and includes pumps, radiators, heat exchangers, tanks, and cold plates. In principle, there are two kinds of heat that need to be radiated—one generated directly by the solar arrays and another generated from inside the ISS. The former is radiated by the External Active Thermal Control System (EATCS) and the latter by the Photovoltaic Thermal Control System (PVTCS). An ATCS mechanically pumps fluid in closed-loop circuits to perform three tasks: collect heat, transport heat, and reject heat. Waste heat can be removed via two structures—cold plates and heat exchangers—both cooled by a circulating ammonia loops on the outside of the station. The heated ammonia circulates through large radiators located on the exterior of the Space Station, releasing the heat by radiation to space that cools the ammonia as it flows through the radiators. The two heat rejection systems are discussed further below:
### **EATCS (External Active Thermal Control System) Radiators**

The EATCS consists of an internal, non-toxic, water coolant loop used to cool and dehumidify the atmosphere the Internal Active Thermal Control System (IATCS). It transfers collected excess heat from electronic and experiment equipment and distributes it to the Interface Heat Exchangers. From these heat exchangers, ammonia is pumped into external radiators—the External Active Thermal Control System (EATCS)—that emit heat as infrared radiation and this ammonia cycles [back to the station](https://web.archive.org/web/20230203012526/https://science.nasa.gov/science-news/science-at-nasa/2001/ast21mar_1/). In this way, the EATCS cools the US modules, Kibō, Columbus, and also the main power distribution electronics of the S0, S1 and P1 trusses. It can reject up to 70 kW, which is more than the 14 kW of the Early EATCS (or EEATCS).

![ISS SAW is a LOT larger than the early ROSA.](assets/imgs/space-data-centers/EATCS.png)

