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
Starcloud have claimed that a single 100-ton Starship launch could create a 40 MW space data centre (SDC) for $8.2 M. My analysis finds that there is a slim chance this could be achieved within a single launch. The math currently shows that their solar panels could be achieved for in one 100-ton Starship launch with existing roll-out solar panels used on the ISS. **This could change as I haven't looked at sizing the radiator, MMOD/radiation shielding, or in-space assembly fuel requirements yet.**

However, their whitepaper's (erroneous) envisioned launch cost of $30/kg makes their comparative economic analysis to terrestrial data centers unmoored from reality in the near term; even if launch comes down to $500/kg{%sidenote "owid-launch-cost" "In [2021 dollars](https://ourworldindata.org/grapher/cost-space-launches-low-earth-orbit), Falcon-9 launches cost $2600/kg and a Falcon Heavy's at $1500/kg. So, $500/kg is also a fairly optimistic estimate."%}, one launch would result in an overall cost of $53.2M, not the purported $8.2M. Some experts speculate that $1000/kg would be an optimistic launch cost, which means $100M per launch and a total cost of $103.2M. If a second launch is needed, then the worst case number is $200M making it more than their reported cost of running a terrestrial data center (TDC). 

This is not to say that SDCs have no value—the answer for space commercialisation will not be found through their economic analysis.

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

# Analysis of Starcloud's whitepaper
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

 Now this means their projected energy cost is $0.002/kWh in space versus $0.045-0.17/kWh terrestrially—this is between 22 to 85 times cheaper. Remarkable! Is this realistic?
## Calculating Launch Costs from First Principles
To determine the cost of launch requires knowledge of number of launches. There are number of ways we can go about doing this: the traditional approach would involve determining the mass of the SDC—this assumes to be how Starcloud make their single launch claim but there is no clarity on how their system could be 100 tonnes which requires some initial SDC design.

After a mass-based estimate of launches, one can further refine the first-order designs to determine revised launch numbers that account for how the SDC structure fits into a rocket{%sidenote "architecture-launch-numbers" "Here, one essentially breaks the large space system into its smaller elements and works out if/how their geometries can be made to fit into the volume of a launcher's fairing. So, even if the mass estimates indicate the SDC fits into a single launcher, its parts might not necessarily be as accommodating."%}.

As Starcloud haven't publicly shared their mass breakdown or component-level design documentation—could either be proprietary information or they are still figuring this out—it is hard to verify their mass claims. I hope to derive this in a future update to this post{%sidenote 'telescope-assembly-overlap' "I see many overlapping architectural challenges here based on my earlier work into in-space assembly of space telescopes"%}. But there is another way for us to determine the number of launches- from their SDC's assumed power density (i.e., power output by a solar array per unit area). I will present that after a short detour to illustrate an issue with the math in their whitepaper.
###  Whitepaper Math is Incongruous
The whitepaper states $5M to launch a 100-tonne Starship to Low Earth Orbit (LEO) Sun-Synchronous Orbit (SSO). This works out to a (measly) $50/kg to reach orbit but the whitepaper says that this translates to $30/kg—this is in two locations so I am unsure why this is the case. With their claimed per kg cost, the mass of the SDC is 167 tonnes. This means two 100-tonne Starship launches or, it could be a single 200-ton Starship launch, which is on SpaceX's roadmap. This means their launch cost just went up by $3M or $5M—though, as I say in the abstract, a single launch would cost $50M {%sidenote 'optimistic-thousand-per-kg' "This could even be $100M per 100-tonne launch as some have said $1000/kg to orbit is also a reasonable cost."%}.



%% After examining their numbers, I will try to unpack a very simple architecture to building such data centers—I have done something similar for large aperture space telescopes in the past. %%




### Deriving Number of launches from Packing Densities
Their long-term goal is to build a 5 GW system which they state needs solar arrays spanning an area of 4km × 4km. This is a power density of 312 W/m². Using the same power density, their smaller 40 MW SDC needs 128,000 m² of solar panels. This would need to be packed into a single launch Starship, which has a fairing volume of 1000 m³. We now define areal packing density, which is the area of these arrays divided by the Starship's fairing volume; this works out to 128 m²/m³.

$$
Starcloud \quad areal \quad packing \quad density =\frac{128,000 m²}{1000 m³} = 128 m²/m³
$$
This means that we would need to fit 128 m² into a  m³ of Starship. This is a quite optimistic estimate as every little bit of volume is being used; but such efficiency is impractical. A more realistic estimate would be that we use 80% of the available 1000 m³; the areal packing density then becomes **160 m²/m³**.

To estimate if this is feasible based on current technologies, I will examine the performance of two space-proven designs for deployable solar arrays (of the three options that Starcloud propose to use as per their whitepaper). The first design is the **Z-folds arrays** which are the legacy design used on the ISS's Solar Array Wings (SAW) and the second, called roll-out solar arrays (ROSA), augmented to the SAW's and are set to become its next-generation replacements; this ISS variant is called iROSA.

### SAW
The image below shows a ROSA and against one wing of the ISS Solar Array Win (SAW).

![basic ROSA](assets/imgs/space-data-centers/Rosa-SAW.png)

The ISS has 8 such (SAWs) attached to trusses; four each on its port and starboard side—which explains why the trusses names are prefixed with P's and S's (e.g., P-6 and S-6). Altogether, the eight solar array wings generate about 240 kilowatts in direct sunlight, or about 84 to 120 kilowatts average power (cycling between sunlight and shade).

 Each wing generates nearly 31 kilowatts (kW) of direct current power from two solar "blankets". When fully extended, the pair span 35 metres in length and 12 metres in width. These are the largest ever deployed in space and weighing well 1,100 kg. Now, the power density based on this wing span works out to about 71.43  W/m² but a more accurate estimate is possible. Each photovoltaic blanket comprises 16,400 cells of 8-cm by 8-cm; this gives the real actual light collecting area of each blanket and multiplying by two results in that for a single SAW.
#### Power Density
 So the power density of a wing with two blankets works out to 147.7  W/m² from:

$$
SAW \quad Power \quad Density = \frac{Power}{Light \quad collecting \quad area} = \frac{31000W}{32800*8cm*8cm} = 147.7 W/m^2
$$

So, to achieve Starcloud's assumed power density of 312 W/m², solar technology would need to be **2.1x more efficient** than SAW's 147.7 W/m².
#### Packing Density
To determine the packing density of one SAW module (i.e., a pair of deployable blankets), we use the stowed volume of this single module that fit within a launched vehicle. The data suggest that this is a cuboid of square face of 4.57 m and 0.51 m thick—the result is a packing density of

$$
SAW \quad areal \quad packing \quad density = \frac{32800*8cm*8cm}{4.57m*4.57m*0.51m} = 19.7 m²/m³
$$

This density is far lower than the packing density needed by Starcloud. Therefore, to determine the number of launches, we would just need to comput the ratio of the Starcloud and SAW packing densities—a dimensionless number. This is 6.49 which means we would need nearly 7 launches with SAW technology. If we used the more realistic estimate packing density (160 m²/m³), we need about 9 launches.
#### iROSA

![iROSA compared to tech demo ROSAs that were built prior.](assets/imgs/space-data-centers/irosa.png)

The ISS Roll Out Solar Arrays (iROSA) were launched in two pairs in June 2021 and November 2022 to augment to the first SAWs, launched in 2000 and 2006 and attached to the P6 and P4 Trusses. These SAWs were noticeably degrading towards the end of their 15-year life. Six of the intended 8 iROSAs have been added in [following sequence](https://en.wikipedia.org/wiki/Integrated_Truss_Structure#Solar_arrays):
- iROSA 1 and 2 was added in front of Old 4B and 2B solar arrays on P6 truss in June 2021;
- iROSA 3 and 4 was added in front of Old 3A and 4A solar arrays on S4 and P4 truss in December 2022;
- iROSA 5 was added in front of Old 1A solar array on S4 truss in June 2023; and
- and iROSA 6 was added in front of Old 1B solar array on S6 truss in June 2023.
The seventh and eighth, are planned to be installed on the 2A and 3B power channels on the P4 and S6 truss segments in 2025.
#### Power Density
Each iROSA generates nearly 20 kilowatts (kW) of direct current power from two rolled-up solar blankets. When fully extended, the pair span 18.3 metres in length and 6 metres in width. The gap between the blankets is not in the public domain but appears to be more negligible than between a pair of SAW blankets; the specifications of the solar cells and their arrangement are also known. So, the power density here is based purely on the wing span, which works out to about 255 W/m² from:

$$
iROSA \quad Power \quad Density = \frac{Power}{Light \quad collecting \quad area} = \frac{20000W}{18.3m*6m} = 182.1 W/m^2
$$

So, to achieve Starcloud's assumed power density of 312 W/m², solar technology would need to be **1.71x more efficient** than iROSA's 255 W/m².
#### Packing Density

{% marginfigure 'mf-id-1' 'assets/imgs/space-data-centers/iROSA-dragon.jpg' 'Stowed canisters.'  %}

As done with the SAW module analysis (i.e., a pair of deployable blankets), we can use the stowed volume of an iROSA module to compute the number of launches. Sadly, this data is also not public but estimates can be made by examining its imagers stowed in a cargo Dragon as well as alongside humans for scale. The iROSAs packed into a cargo Dragon trunk and each blanket packed into a canister; the length of this canister can be assumed to be 3 m, a dimension that remains unchanged for either blanket as it rolls out. Each blanket's 18.3 m deployed span can be assumed to pack into a canister of diameter of 0.3 m. So two such canisters per iROSA leads to a packing density of 

$$
iROSA \quad areal \quad packing \quad density = \frac{18.3m*6m}{2(\pi*(0.15m)^2*3m)} = 258.78 m²/m³
$$

Again, one can determine the number of launches for the SDC's solar panels by computing the ratio of the Starcloud and iROSA packing densities. At 0.49, this is well under a single Starship launch but, if the canister canister diameter increases to 0.5 m, 2 launches become necessary. The iROSA canisters diameter could fall anywhere in this range.

Our calculations thus far are summarised below:

{%marginnote 'table' "Imprveoment on preceding solar technologies and related launch numbers" %}

|       | Power  density | Launch numbers | Launch Cost ($5M/launch) | Launch Cost ($50M/launch) | Launch Cost ($100M/launch) |
| ----- | -------------- | -------------- | ------------------------ | ------------------------- | -------------------------- |
| SAW   | 2.1x           | 7 to 9         | 35M-45M                  | 350M-450M                 | 700M-900M                  |
| iROSA | 1.71x          | 1 to 3         | 5M-15M                   | 50M-150M                  | 100M-750M                  |

So this begs the question if it is possible to build the radiators in the remaining margin retained by the areal density—this will need to be repeated for the in-space assembly requirements. This will be explored in the future.


> [!warning]This is a work-in-progress
> This block is to warn you that everything below is in draft mode. This block will be removed once my analysis is complete and documented below. So, if you have reached this far, treat everything below as inaccurate explorations for myself.


[[Other stuff]]
# Space challenges
The three reasons I have stated above are issues that we face on space. But challenges in space also fall under the same three categories. These are best worked backwards:
1. Real estate: Large solar panels need to be assembled in space for energy collection; this is equivalent to real estate. One company is saying they would need 4 km by 4 km—easily the largest structure we would have ever built. 
2. Cooling (aka Thermal Management): On Earth, data centers use air (convection) and water cooling (conduction). In space, thermal management is a bigger engineering challenge as we can only rely on radiation, which is less efficient.
3. And does the carbon footprint of launches offset the benefits?



Are these omissions are intentional optimism or genuine blindspots?