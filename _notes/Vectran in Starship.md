---
---
- This post uses a summary of somewhat recent work on inflatable stations to identify some challenges to realising large inflatable structures.
# Multilayer Inflatable Shell Structure
- It comprises five main parts, as shown in the figure below: 1) inner liner layer, 2) bladder layer, 3) restraint layer, 4) micrometeoroid/orbital debris (MMOD) protection layer, and a 5) thermal protection (MLI) layer.
- Much of the focus here will be on the restraint layer, which is main load-bearing layer for the structure and, as will be shown, in need of material innovation as the spaceship scales. There will also be some consideration on the MMOD shields as that can be the bulkiest part of the spaceship, depending on its orbit.
![](assets/imgs/spaceship-engineering/layers_of_inflatable_habitat.png)
## Restraint layer
- Vectran was used in making BEAM's restraint layer that bears loads and stresses at design pressures, which is a multiple (called "factor of safety") of the operational pressure. 14.7 psi for the ISS and presumed to be the case for any spaceship, as well.
- Now, Vectran's is five times stronger than steel and ten times stronger than aluminium while being half as dense (1400 $kg/m^3$) as aluminium, which means we can get a lot more of it into space. If made purely from Vectran, a 5000 $m^3$ [[Where is my von Braun Wheel?|von Braun wheel]] would need 7000 tons of Vectran—one such spaceship would require a crazy number of Starship launches: 70!
- Luckily, systems such as TransHab and [[BEAM video summary|BEAM]] were made from 5 layers which result in a far less dense structure when inflated (synonymous with pressurised) as per the table below from the same paper. 

![Title of table in image.](assets/imgs/spaceship-engineering/Densities_of_inflatable_habitats.png)
- So, if made from TransHab materials,  a 5000 $m^3$ von Braun wheel would be about 195 tons, which would need only 2 Starship launches and 5 launches if made from BEAM-style materials.
- A next-generation multilayer design that could fit in one Starship launch helps frame the first challenge as:
> [!Challenge] Challenge 1: Material Density Optimization
> Find an optimised material that halves the pressurised density of TransHab materials so the mass fits within one Starship launch. Given that TransHab was less dense than BEAM, this doesn't sound as outrageous on paper.

### Packaged Density 
- BEAM's density when inflated is 88 $kg/m^3$ (from above table) and, assuming it's a cylinder when deflated too, it's density is 157 $kg/m^3$. TransHAB is even more impressive with a packaged/deflated/unpressurised density of 122 $kg/m^3$.
- This also tells us that the compression ratios (pressurised to unpressurized volumes) for TransHab and BEAM are 3.12 and 1.78, respectively.

> [!Challenge] Challenge 2: Advanced Packaging of Multi-layer Inflatable Structure
> Identify a packaging method to fold said von Braun wheel into Starship's 1000 $m^3$ fairing. This is about finding a 5:1 ratio at the lower end, which might be insane before we consider 10:1 ratios (as unpressurised spaceship volumes might be of the same measure)?

## Materials
- Then there is the issue that the TransHab materials only scale to a certain diameter of about 8.2 $m$—a von Braun wheel of 75 $m$ diameter is unexplored territory but the graph suggests that novel restraint materials are needed beyond the 9 $m$ mark. This is where AI-led materials discovery will become crucial.
- The chart below shows design Categories by Complexity:
	- **Left side:** Simple bladder designs (small, low-load applications)
	- **Middle:** Combined restraint systems
	- **TransHab sits here:** "Bladder + Close Proximity Restraint" at ~20 ft diameter
- **Right side:** "Novel Restraint System" for very large structures (BA 2100)
![](assets/imgs/spaceship-engineering/Restraint-Loading.jpg)

> [!Challenge] Challenge 3: Scale-Up to 75m Diameter
> Find a material that allows more restraint layer loads and larger diameters at the design pressure.

## MMOD layer
- This layer is 68% of TransHab's mass for LEO applications, given the higher debris density, but drops to 14% in deep space (what is it for higher Earth orbits?).
- Our chosen orbit is initially assumed to be LEO—to take maximal mass to orbit using Starship's current specs—there may be a need for in-orbit assembly of Whipple Shield panels around the restraint layer. If this is the case, then perhaps operating in a higher orbit might be preferable. The study should reveal this.
	- But the orbit won't be driven by the spaceship's engineering challenges alone—market demands of a large data center or robotic factory might show that their desired orbits are more lucrative than crewed spaceships in the near-term.
- **Advanced composites:** Carbon fiber restraint layers vs. Vectran/Kevlar.
- **Hybrid design:** More efficient hard-structure to soft-goods ratios.

> [!Tip] MMOD Shield
> Should this be assembled as a panel or be a monolithic system similar to TransHab?


> [!Note] MMOD Shield
> Should this be assembled as a panel or be a monolithic system similar to TransHab?


> [!Warning] MMOD Shield
> Should this be assembled as a panel or be a monolithic system similar to TransHab?
