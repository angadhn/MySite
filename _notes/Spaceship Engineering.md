---
title: What is a Spaceship?
created: 2025-06-10
published: 2025-06-15
tags:
  - spaceships
  - essays
permalink: /spaceship-1
top_of_mind: "false"
completion_score: 30
image:
companion music: https://soundcloud.com/adamfreeland/adam-freeland-pale-blue-dot-dj
subtitle: And how to make them
---

Even over a millenium ago, Vikings did not build longships by cobbling together a bunch of smaller boats. In principle, this is how we have built the ISS—by joining several smaller "space boats" together to get something bigger than its parts. This architectural issue is why we are stuck with single-digit occupancy space stations[^1]. The crew sizes of these 11th-century longships were also double-digit—ranging from 30-40.

These fundamental facts made me revisit a plot{% sidenote `plot` 'Recreated below with clearer categories and more example systems'%} from [[Where is my von Braun Wheel?]], where I examine  real, planned, and conceptual space stations. This time ,I saw more than the architectural/technical issues with modular construction, crew sizes, and comfort.

I saw issues with terminology. For far too long I had used the *space station* misnomer for all of these systems too. This is common, where too often we tend to refer to any of these pressure vessels by other loosely defined terms like spacecraft or satellites. These are all correct terms but there is something imprecise about them.

After all, a boat is not also called a ship.

A kayak is also not mistaken for a ship even if some classify them (correctly) as boats.

It was time to stop cringing when using the word "spaceship" and instead better define these systems {%sidenote `spaceship` 'The term is implied in science fiction but again, I am not sure what it actually conveys in my limited reading. Maybe someone has been more precise and I am poorly read—let me know, if so. '%} that I want to (and we should) be engineering.

The more I examined this plot and reflected on Langley's work as an activity similar to ship-building—covered in [[Where is my von Braun Wheel?]]—it was increasingly apparent that these engineers should have referred to their creations as *spaceships* and eschewed calling them _[[Where is my von Braun Wheel?#A pre-Apollo solution unitised stations|unitised space stations]]_.

Their approach for making large space structures in a non-modular fashion, well before Apollo, also leads into a need for recognising a field of _spaceship engineering_ as one distinct from _spacecraft_ or _satellite engineering_ to convey both a difference in scale but also of building approaches. Much like how naval architecture focues on shipbuilding.
# What is a Spaceship?

To help you see what I did, I present an updated plot with three regions classifying space pressure vessels as *space stations* (what we have built so far), *superstructures* (what we wish to build), and *spaceships* (what we need to build next) as the step between. To me, this is also now allowing a first-order conceptualisation of how we might build spaceships in the near-term; indeed, I am hoping to bias more people away from the modular architectures we have seen so far and migrate towards the "unitised" philosophy of Langley (which we have clearly lost). So let's look at the plot.

<div class="plot-container">
  <iframe src="/assets/plots/spaceship-engineering/spaceship-region.html" frameborder="0"></iframe>
  <div class="marginal-caption">Spaceships are different from Space Stations and Superstructures</div>
</div>

A little more on the chart above and the logic of better defining spaceships:
- I use *space stations* for everything that we have flown so far that we have called a "space station" but allow for crew sizes of upto 25 (arbitrarily chosen but I think this is generous).
- Next, I placed the outlandish (outworldish?) conceptual designs like the _Stanford Torus_ and _O'Neill Cylinders_ to fall under this category and call this region as _space superstructures_{% sidenote 'superstructures-1' 'I have kept adding to the list from the earlier post and can see where certain systems fall (like the *Bernal Sphere* and *Kalpana One*).' %} .
  Now, something the plot doesn't convey but is important to note is that these superstructures inherently assumed needing space resources for their construction. This is untrue for _space stations_.
- *Spaceship* territory then is the region between these two categories. In my short-term vision, the need for space resource use in their creation is not a requirement and, to keep things real, should be avoided-however, spaceships are (or should become) platforms from where we launch a variety of missions to asteroids for space resource extraction, which there is no dearth of ideas for so I won't go into this. As we will see shortly in how to build spaceships, even with terrestrial resources, a lot of R&D to invent/discover new materials is (likely) needed.
The delineation between the three categories should not be seen as a precise definition of any of them but purely as a first-principles (or crude?) attempt to define a *spaceship* by contextualising it as a bridge between reality (*space stations*) and what is currently fantasy (*superstructures*). Perhaps, it will permit more precise definitions—this will, I think, only help us think of newer ways to approach how we build larger orbiting structures.
## Clarifcation on Spaceship Uses
- A risk of defining the "ideal spaceship" as one with artificial gravity and deriving its specs from human factors (*habitable volume per person* and *crew sizes*) might suggest that I see spaceships primarily for human occupation. This is not the case. Human factors help us define pressurised volumes that we should be engineering towards; in this case, roughly 6000 $$m^3$$. If we focus on engineering the right geometries (like a torus), we can get microgravity stations without spinning them up—we can then explore modular bolt-on solutions to spin them up once we have figured out how to build larger (non-spinning) volumes.
- In other words, I am saying we should be thinking of engineering spaceships to be large enough to be adaptive to various uses.
- Now, by plotting *habitable volume per person* and *crew sizes* and then introducing the notion of an _ideal spaceship_ with artificial gravity, one may conclude that spaceships are fundamentally only much larger habitats. But that is not the case. Instead, one should see the ideal spaceship case as one from which we derive requirements for creating a volume large enough to, say, host seventy people but also of use for other emerging microgravity applications, like space data centers and pharmaceutical manufacturing.
  The key engineering idea then is to recommen a focus on create the kind of technology that leads to rapid and low-cost large volume deployments in Low Earth Orbit, that we will find multiple lucrative uses.

we can see that some conceptual spaceships (like the _Space Base_ and even the _von Braun wheel_) would be as comfortable as current space stations and that we should be veering towards more capacious designs. Indeed, what we see is that 

# How to (maybe) make them?
This post uses a summary of somewhat recent work on inflatable stations to identify some challenges to realising large inflatable structures.
## Multilayer Inflatable Shell Structure
### Shell Challenges
- It comprises five main parts, as shown in the figure below: 1) inner liner layer, 2) bladder layer, 3) restraint layer, 4) micrometeoroid/orbital debris (MMOD) protection layer, and a 5) thermal protection (MLI) layer.
- Much of the focus here will be on the restraint layer, which is main load-bearing layer for the structure and, as will be shown, in need of material innovation as the spaceship scales. There will also be some consideration on the MMOD shields as that can be the bulkiest part of the spaceship, depending on its orbit.
![](assets/imgs/spaceship-engineering/layers_of_inflatable_habitat.png)

- Vectran was used in making BEAM's restraint layer that bears loads and stresses at design pressures, which is a multiple (called "factor of safety") of the operational pressure. 14.7 psi for the ISS and presumed to be the case for any spaceship, as well.
- Now, Vectran's is five times stronger than steel and ten times stronger than aluminium while being half as dense (1400 $$kg/m^3$$) as aluminium, which means we can get a lot more of it into space. If made purely from Vectran, a 5000 $$m^3$$ [[Where is my von Braun Wheel?|von Braun wheel]] would need 7000 tons of Vectran—one such spaceship would require a crazy number of Starship launches: 70!
- Luckily, systems such as TransHab and [[BEAM video summary|BEAM]] were made from 5 layers which result in a far less dense structure when inflated (synonymous with pressurised) as per the table below from the same paper. 

![Title of table in image.](assets/imgs/spaceship-engineering/Densities_of_inflatable_habitats.png)
- So, if made from TransHab materials,  a 5000 $$m^3$$ von Braun wheel would be about 195 tons, which would need only 2 Starship launches and 5 launches if made from BEAM-style materials.
- A next-generation multilayer design that could fit in one Starship launch helps frame the first challenge as:

> [!Challenge] Challenge 1: Material Density Optimization
> Find an optimised material that halves the pressurised density of TransHab materials so the mass fits within one Starship launch. Given that TransHab was less dense than BEAM, this doesn't sound as outrageous on paper.

- BEAM's density when inflated is 88 $$kg/m^3$$ (from above table) and, assuming it's a cylinder when deflated too, it's density is 157 $$kg/m^3$$. TransHAB is even more impressive with a packaged/deflated/unpressurised density of 122 $$kg/m^3$$.
- This also tells us that the compression ratios (pressurised to unpressurized volumes) for TransHab and BEAM are 3.12 and 1.78, respectively.

> [!Challenge] Challenge 2: Advanced Packaging of Multi-layer Inflatable Structure
> Identify a packaging method to fold said von Braun wheel into Starship's 1000 $$m^3$$ fairing. This is about finding a 5:1 ratio at the lower end, which might be insane before we consider 10:1 ratios (as unpressurised spaceship volumes might be of the same measure)?

### Restraint layer materials
- Then there is the issue that the TransHab materials only scale to a certain diameter of about 8.2 $$m$$—a von Braun wheel of 75 $$m$$ diameter is unexplored territory but the graph suggests that novel restraint materials are needed beyond the 9 $$m$$ mark. This is where AI-led materials discovery will become crucial.
- The chart below shows design Categories by Complexity:
	- **Left side:** Simple bladder designs (small, low-load applications)
	- **Middle:** Combined restraint systems
	- **TransHab sits here:** "Bladder + Close Proximity Restraint" at ~20 ft diameter
- **Right side:** "Novel Restraint System" for very large structures (BA 2100)
![](assets/imgs/spaceship-engineering/Restraint-Loading.jpg)

> [!Challenge] Challenge 3: Scaling Restraint Materials towards 75m-100m Diameter
> Find a material that allows more restraint layer loads and larger diameters at the design pressure.

### MMOD layer
- This layer is 68% of TransHab's mass for LEO applications, given the higher debris density, but drops to 14% in deep space (what is it for higher Earth orbits?).
- Our chosen orbit is initially assumed to be LEO—to take maximal mass to orbit using Starship's current specs—there may be a need for in-orbit assembly of Whipple Shield panels around the restraint layer. If this is the case, then perhaps operating in a higher orbit might be preferable. The study should reveal this.
	- But the orbit won't be driven by the spaceship's engineering challenges alone—market demands of a large data center or robotic factory might show that their desired orbits are more lucrative than crewed spaceships in the near-term.
- **Advanced composites:** Carbon fiber restraint layers vs. Vectran/Kevlar.
- **Hybrid design:** More efficient hard-structure to soft-goods ratios.

> [!Challenge] Challenge 4: MMOD Shield Assembly
> Should this be assembled as a panel from a separate launch or can it be unitised to the main restraint structure system similar to TransHab and existing designs?

[^1]: A different analogue might have been with aircraft construction—we don't build an Airbus A380 by stitching together several Cessnas—but I sense there is something more evocative about comparing to a 1000-year old approach to building. Also, several boats are more likely to float but several Cessnas will never leave the tarmac.
