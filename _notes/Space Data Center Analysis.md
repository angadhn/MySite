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
Starcloud have claimed that a single 100-ton Starship launch could create a 40 MW space data centre (SDC) for $8.2 M. My analysis shows that, even with their assumed power density of 312 W/m², there is no chance this could be achieved in a single launch. The math shows that this needs five 100-ton Starship launches, at least. This is only to get the solar panels int orbit—I haven't even looked at sizing the radiator, MMOD and radiation shielding, or in-space assembly fuel requirements yet!

Further, their (erroneously calculated) envisioned launch cost of $30/kg makes their comparative economic analysis to terrestrial data centers unmoored from reality; even if launch comes down to $500/kg{%sidenote "owid-launch-cost" "In [2021 dollars](https://ourworldindata.org/grapher/cost-space-launches-low-earth-orbit), Falcon-9 launches cost $2600/kg and a Falcon Heavy's at $1500/kg. So, I'd say even $500/kg is an optimistic estimate."%}, five launches would result in an overall cost of $253.2M, not the purported $8.2M.

This is not to say that SDCs have no value—the answer for space commercialisation will not be found through their economic analysis.

> [!warning]This is a work-in-progress
> This block is to warn you that this is a draft article. This block will be removed once I my analysis and comments are complete. This involves migrating my analysis into this write-up. So, if you stumble on this, treat everything below as inaccurate in math but principled in reasoning. The numbers in the abstract are accurate.

# Introduction
On Earth, data centers run on the existing electricity grid that, crudely put, use a combination of fossil fuels or terrestrial solar. So, technologists and entrepreneurs have recently talked up data centres in space to resolve three issues with terrestrial data centers (TDC):
1. Data centers require tremendous amounts of energy, which is plentiful and "free" in space. There, 24/7 solar power is unhindered by day/night cycles, weather, and atmospheric losses (attenuation).
2. A lot of waste heat is generated running TDCs, which bodes poorly for climate change—so migrating to space would alleviate the toll on Earth's thermal budget. This seems like a compelling environmental argument. ==TDCs already consume about 1% of global electricity {%sidenote 'verified-1' "TBV."%} ==, and it's safe to assume that this will only grow in the pursuit of AGI.
3. Real estate for data centers is a massive bottleneck and this land could be used for other purposes.

Now, Sam Altman has also talked up nuclear energy as a solution, which I suspect is maybe an easier technological solution from an energy and climate angle but the regulatory barriers need resolution. So, space, in theory, sounds like a speedier answer too—as a space person, I'd love nothing more than for there to be a strong economic case for space. My only gripe is that SDC remains data-related, which we know is proven to work well with GPSand satellite communications.

So, there's now at least one YCombinator-backed company, Starcloud Inc., working on building SDCs—they released a white paper on this and I decided to dive in (with Claude to speedrun my analysis, of course). They begin by pointing us to some of the unique benefits of space solar, the main one being its 95%+ [capacity factor](https://en.wikipedia.org/wiki/Capacity_factor) versus just a median capacity factor of 24% for US terrestrial solar (under 10% in northern Europe. They continue to say that combined with 40% higher peak power due to no atmospheric losses, you get over 5x the energy output from the same solar array. This is not exactly my forte so I am not fact-checking these claims—let's accept them as true.

If I can claim a bit of domain expertise, it's on the space side. Reading Starcloud's whitepaper, I felt I could use my limited expertise from [designing mission for in-space assembled large space telescopes and analysing them]() to understand their techno-economic analysis.

Now, from my time working on that project, I have come to understand that space has its own challenges. For the sake of this analysis, I will classify them in the same three categories as I did at the start for Earth data centers but present them in reverse order:
1. Real estate: Starcloud's target is to achieve a 5 GW cluster spanning, with solar arrays spanning 4 km by 4 km—this would comfortably become the largest structure in space—which will need in-space assembly. This is, in some sense, equivalent to real estate.
2. Cooling (aka Thermal Management): On Earth, data centers use air (convection) and water cooling (conduction) but in space, thermal management requires radiation, which is less efficient—convection is impossible in a vacuum and while water could extract heat from the center, cooling that heated up water would then pose another problem.
3. Finally, we could also think about if/when the carbon footprint of launches offset the benefits of a SDC. But the report suggests that achieving AGI could need 1 GW centers but large hyperscale Earth-based data centers today reach 100 megawatts (MW) meaning they "do not scale well or sustainably to gigawatt (GW) sizes".

Now, I will treat that last item as speculative mostly because it is out of my wheelhouse. However, if it is true, then we will need some alternative (either nuclear or space-based data centers) but by examining the first two aspects, I imagine we will know how well the business case of this company adds up.

%% After examining their numbers, I will try to unpack a very simple architecture to building such data centers—I have done something similar for large aperture space telescopes in the past. %%
# Analysis of Starcloud's whitepaper
While one could begin by asking how much compute workload should be moved to space to make a meaningful dent on the climate—a really good reason to do so—economic incentives that lead to large returns on investment are what appeal to private at the end of the day which is why Starcloud exist but space agencies haven't invested here. So, my analysis begins by examining [[starcloud-wp.pdf|Starcloud]]'s numbers to justify their business case for SDC.

Their whitepaper presents a table where the total costs of running a 40MW data centre cluster over ten years is determined to be $167M on Earth versus $8.2M for space. This is broken down as follows:
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

 Now this means their projected energy cost is $0.002/kWh in space versus $0.045-0.17/kWh terrestrially—this is between 22 to 85 times cheaper. Remarkable! Is this realistic?

## Calculating Launch Costs from First Principles
To determine the cost of launch requires knowledge of number of launches. There are number of ways we can go about doing this: the traditional approach would involve determining the mass of the SDC—this assumes to be how Starcloud make their single launch claim but there is no clarity on how their system could be 100 tonnes which requires some initial SDC design.

After a mass-based estimate of launches, one can further refine the first-order designs to determine revised launch numbers that account for how the SDC structure fits into a rocket{%sidenote "architecture-launch-numbers" "Here, one essentially breaks the large space system into its smaller elements and works out if/how their geometries can be made to fit into the volume of a launcher's fairing. So, even if the mass estimates indicate the SDC fits into a single launcher, its parts might not necessarily be as accommodating."%}.

As Starcloud haven't publicly shared their mass breakdown or component-level design documentation—could either be proprietary information or they are still figuring this out—it is hard to verify their mass claims. I hope to derive this in a future update to this post{%sidenote 'telescope-assembly-overlap' "I see many overlapping architectural challenges here based on my earlier work into [[|in-space assembly of space telescopes]]"%}. But there is another way for us to determine the number of launches- from their SDC's assumed power density (i.e., power output by a solar array per unit area). I will present that after a short detour to illustrate an issue with the math in their whitepaper.
###  Whitepaper Math is Incongruous
The whitepaper states $5M to launch a 100-tonne Starship ith a payload capacity of 100 tons to Low Earth Orbit (LEO) Sun-Synchronous Orbit (SSO). This works out to a (measly) $50/kg to get to orbit but the whitepaper says that this translates to $30/kg. Now, the latter per kg cost actually then tells us that this is 167 tonnes for a SDC—so two Starship launches, which means their launch cost just went up by $3-$5M. Or, it could be a single 200-ton Starship launch, which is on SpaceX's roadmap.

#### Number of launches
- Launch is the largest contributor to Starcloud's total costs and they presume that one launch shall be enough—for me, these ring some alarm bells. Can we really pack everything into one Starship launch for even the 40 MW system? Let's see if I can work this out.
- For a 5 GW system, they state that 4km × 4km solar arrays are needed; this is a power density of 312 W/m². For the smaller 40 MW that they benchmarked, they would need approximately 128,000 m² of solar panels. If arranged as a large square, this would be roughly 357 m × 357 m. Now, as they suggest, one can go with either Z-fold or roll-out arrays{%sidenote 'picframe' 'The report also mentions picture frame panels but roll-outs are were added recently to the ISS. [Z-folds have also been used before via the Solar Alpha Rotary Joints (SARJs)](https://x.com/raffaeledipalma/status/1368672410522820612).'%}. I suspect that the former alludes to something similar to the [Solar Array Wings (SAW)](https://en.wikipedia.org/wiki/Electrical_system_of_the_International_Space_Station#Solar_array_wing) of the ISS, which works by panels that can fold up (and unfold) like an accordion, whereas the latter is probably based on the [Roll Out Solar Array (ROSA](https://en.wikipedia.org/wiki/Roll_Out_Solar_Array) that augment to the oldest wings. Data and calculations of the SAW and ROSA in an ISS context can be found [[|here]], which shows that iROSA are 1.7x better for power density than the SAWs.
  ![basic ROSA](assets/imgs/space-data-centers/Rosa-SAW.png)
![](assets/imgs/space-data-centers/irosa.png)
- Whichever option is used must fit in Starship's fairing, whose diameter is ~9 meters. So let's get some sizing estimates:
	- **Z-folds**: To fit within Starship’s 9-meter fairing, solar panels must be modular. Allowing for a 0.125-meter clearance on each side, the largest practical square tile is **8.75 m × 8.75 m**, or **76.56 m²**. To reach the full **127,449 m²** required for 40 MW, we need approximately **1,665 tiles**.
	  The International Space Station’s legacy solar arrays follow a Z-fold architecture. Each array “wing” consists of **two solar blankets**, with an estimated deployed width of **4.5 m** each and a **3 m gap** between them, totalling ~**315 m²** of effective solar collecting area per wing. Each wing folds into a cuboidal stowage volume of **4.57 m × 4.57 m × 0.51 m = ~10.65 m³**.
	  Thus the **packing density** of a Z-fold wing is thus **~29.6 m²/m³** (315 m² ÷ 10.65 m³). For Starcloud's sake we will make the generous assumption that Starship’s **1,000 m³** payload bay can be fully utilized. So, one launch could carry **~29,600 m²** of deployed solar area. To reach **127,449 m²**, we would therefore require **~4.3 launches**, or **5 launches conservatively**. This means each launch would carry approximately **333 Z-fold tiles** (1,665 ÷ 5).
		- Although the total area of the ISS's deployed wing is **~420 m²** (including structural gaps), the **actual structural area** is **315 m²**. The **actual light-collecting area** of ~**210 m²** contains **16,400 solar cells**, each measuring **8 cm × 8 cm**. The difference is due to structural supports, wiring, and non-collecting surfaces. Therefore, the wing’s **true optical power density** is about **147.7 W/m²**, despite a lower apparent geometric density of ~98 W/m².
	- **ROSA Module Flight Example**: The ROSA module flown on the ISS's numbers are less concrete—it deployed into a ~**6 m × 18.3 m (~110 m²)** array and let's assume it outputs 25 kW power for a power density of **227.7 W/m²**. While its stowed dimensions are not available in the open literature, there is an image of a pair of the iROSAs in the cargo Dragon trunk; I will assume that each of the pair is approximately **0.6 m diameter × 3 m length** to yield a total volume for the pair as  . But to analyse Starcloud's assumption, let's work with the assumed power density of 315 W/ m² that yielded the total solar area of 128,000 m².
	  
	  This yields a **packing density of ~37.7 m²/m³**, but accounting for structure, deployment hardware, and thermal margins, we conservatively round this down to **35 m²/m³**.
	  Assuming a generous **100% fill efficiency** of Starship’s **~1,000 m³** payload volume, this gives **35,000 m²** of deployable solar per launch — about **27.4%** of the **127,449 m²** needed for a 40 MW system.
	  If we assume **300 W/m²** power density, that’s **~10.5 MW** per launch. Therefore, we estimate **4 launches** to deploy the full system with current ROSA-like roll-out arrays.
- Take-away: With today’s **roll-out array technologies**, we estimate the 40 MW system could be launched in **~4 Starship missions**. Z-folds, while simpler and space-proven, would require **~20 launches**. This strongly favors roll-out technologies for mass deployment — but note: **radiators, truss structures, and power electronics** will still add significant volume/mass, and should be factored in separately.
- Comment: I haven't even begun to factor in a truss, which would be needed for such a structure. Its architecture might end up being such that it would need a separate launch of its own.
Core takeaway: At 4 launches, they would still pay $20 million. But as I have shown that their mass calculation could be off. This means they would need twice as many 100-ton launches resulting in a total of 8 launches. This brings their optimistic launch cost to $80 million.

However, if we go with my less optimistic numbers of $83.5M per 100 tonne launch, then we are talking about $334M or $668M in launch costs. Let's say I am pessimistic and they are optimistic and go down the middle—this becomes $167M or $334M.

Either way, just for the solar panels alone, I don't think we are looking at a single launch system.

### Cooling: Passive Radiative
passive radiative cooling
## What this misses?
- Assembly challenges unaddressed:
	- Propellant use and costs
	- 
- **No risk pricing:** Could space hardware fails at much higher rates. No mention of this in costs.
- Even without failure, there is the cost of maintenance/repair/servicing.
	- They use $0.04/kWh for terrestrial but claim $0.002/kWh for space. The space number assumes perfect 10-year amortization with no maintenance, failures, or financing costs.
# Space challenges
The three reasons I have stated above are issues that we face on space. But challenges in space also fall under the same three categories. These are best worked backwards:
1. Real estate: Large solar panels need to be assembled in space for energy collection; this is equivalent to real estate. One company is saying they would need 4 km by 4 km—easily the largest structure we would have ever built. 
2. Cooling (aka Thermal Management): On Earth, data centers use air (convection) and water cooling (conduction). In space, thermal management is a bigger engineering challenge as we can only rely on radiation, which is less efficient.
3. And does the carbon footprint of launches offset the benefits?



Are these omissions are intentional optimism or genuine blindspots?