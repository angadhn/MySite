---
title: "Appendix: Mass estimate of an inflatable von Braun wheel"
created: 2025-07-04
published: 2025-07-04
tags:
  - WiP
permalink: /WiP-piece-math-inflatable-space-station
top_of_mind: "false"
completion_score:
image:
companion music:
subtitle: Appendix to Works in Progress piece
discussion:
hideFromHomePage: "true"
---
This appendix provides the detailed methodology used to estimate the mass and volume requirements for components of an inflatable space station—most notably the pressurizing air supply and inflatable fabric shell. It supports the main arguments presented in the Works in Progress piece and is based on a von Braun-style toroidal habitat concept.

# Von Braun Wheel Design Parameters

The von Braun wheel design assumes a torus with major radius R = 37.5 m and minor radius r = 3 m. The internal volume is calculated using the standard torus volume formula:

$$
V = 2π²Rr² = 2π²(37.5)(3²) ≈ 6,650 m³
$$

For a torus with the same dimensions, the surface area is: Surface area = 4π²Rr = 4π²(37.5)(3) ≈ 4,440 m²

# Air Mass Requirements
At standard atmospheric conditions, air has a density of approximately 1.2 kg/m³. Therefore, the total air mass required is:

$$
m_{air} = 6,650 m³ × 1.2 kg/m³ ≈ 8,000 kg = 8 \, tonnes
$$

This represents the equivalent mass of air needed to pressurize the habitat to Earth-like atmospheric pressure (1 bar). [[Delivering compress air would require new solutions]]

# Using BEAM as a Scaling Baseline

![The Bigelow Expandable Activity Module](assets/imgs/WiP1/BEAM.png)

We use data from [NASA's documentation](https://www.nasa.gov/wp-content/uploads/2015/06/2016-march-beam-factsheet-508.pdf)  on the Bigelow Expandable Activity Module (BEAM) as a scaling baseline to derive the potential multi-layer inflatable fabric mass needed for a von Braun wheel.

BEAM weighs 1,360 kg and comprises two main parts:
- a pair of metal bulkheads—called [Passive Common Berthing Mechanisms (PCBMs)](https://www.sierraspace.com/wp-content/uploads/2024/01/DOCKING-AND-BERTHING-SYSTEMS-Passive-Common-Berthing-Mechanism-PCBM.pdf)—each weighing [200 kg](https://en.wikipedia.org/wiki/Common_Berthing_Mechanism) . They serve as mechanical and structural interfaces for berthing incoming spacecraft to the International Space Station (ISS); and
- multiple layers of soft fabric—including Vectran for bearing the internal pressurisation loads—with an aluminium spine structure that provides hard points to integrate other sensors, radiation monitors, and other fixtures.

BEAM's bulkheads would not feature in the same manner in a von Braun wheel so we discard them and use 960 kg as BEAM’s structural mass. For the sake of estimation, we assume the entire 960 kg remaining mass is attributable to the multilayer fabric shell assuming the spine structure contributes negligibly to overall mass (likely <5%) {% sidenote "BEAMfabricspine-1" "Specific data on the fabric with spines and equipment masses is not public but this could be under 5%." %}. BEAM's stows into and deploys as a cylinder and its dimensions are known in both cases. When stowed, it is 2.16 m long and 2.36 m in diameter and the deployed length and diameter are 4 m and 3.2 m, respectively. Its stated usable volume is 16 m³. Note that the total geometric volume is approximately 32 m³, while the usable pressurized volume is specified as 16 m³.

With this data, this we can then determine that its:
- fully deployed surface area is ~57 m²
  
  $$
  A = 2\pi r^2 + 2\pi r h = 2\pi (1.615)^2 + 2\pi (1.615)(4.01) ≈ 57.1 \, \text{m}^2
  $$
  
  and
  
- stowed volume is 9.46 m³ from:
  
  $$
  π × (2.36/2)² × 2.16 = π × 1.18² × 2.16 ≈ 9.46 m³
	  $$

These BEAM parameters can now be used to determine the mass of the von Braun wheel. We examine these under several scenarios, as described below.

# Fabric Mass and Launch Numbers

Here, we aim to estimate the fabric mass comprising both MMOD shielding and other layers of the multilayer fabric in BEAM with spines.

**Scenario 1: Low Earth Orbit (High Debris Environment)**

In Low Earth Orbit, approximately 68% of an inflatable habitat's fabric mass is from its micrometeoroid and orbital debris (MMOD) shielding (Page 5 in [Litteken et al., 2019](https://www.researchgate.net/profile/Douglas-Litteken/publication/333919095_System_Integration_Comparison_Between_Inflatable_and_Metallic_Spacecraft_Structures/links/5e75387392851cf2719a389c/System-Integration-Comparison-Between-Inflatable-and-Metallic-Spacecraft-Structures.pdf?__cf_chl_tk=pDGvn9SayN3u94_S2IxijTtcfUUkhKg0khQn23ldwPY-1735002576-1.0.1.1-tXvyxaLfG.lXVagYY.rMLfOHHkqRP9DP3HAh.jXshUY)). In such a scenario, a von Braun wheel weighs 75 tonnes. This is based on the following BEAM's:
- Mass per surface area = 960 kg ÷ 57 m² = 16.84 kg/m²
- Von Braun wheel mass = 4,440 m² ×  16.84 kg/m² ≈ **74 tonnes**

This would fit within the payload volume and mass capacity of a single Starship launch, which we determine from the notion of "packing efficiency of BEAM" (defined as) we define an effective packing density as deployed surface area per unit stowed volume, which for BEAM is approximately 5.9 m²/m³ (i.e. 57 m² ÷ 9.46 m³). Dividing this packing efficiency from the surface area of the 75 m von Braun wheel gives its stowed volume as 733 m³ packed (4,440m² ÷ 6 m²/m³).

**Scenario 2: Deep Space/Low Debris Environment**

In environments with sparse debris (higher Earth orbits, deep space, lunar orbit, Lagrange points), MMOD shielding drops to only ~14% of fabric mass  (Page 5 in [Litteken et al., 2019](https://www.researchgate.net/profile/Douglas-Litteken/publication/333919095_System_Integration_Comparison_Between_Inflatable_and_Metallic_Spacecraft_Structures/links/5e75387392851cf2719a389c/System-Integration-Comparison-Between-Inflatable-and-Metallic-Spacecraft-Structures.pdf?__cf_chl_tk=pDGvn9SayN3u94_S2IxijTtcfUUkhKg0khQn23ldwPY-1735002576-1.0.1.1-tXvyxaLfG.lXVagYY.rMLfOHHkqRP9DP3HAh.jXshUY)). So, assuming that the remaining non-shielding related fabric mass is constant, we can determine the mass of a von Braun wheel as 29 tonnes. This is worked out as follows:
- **Step 1:** If MMOD represents 68% in LEO, then the remaining 32% is other layers of fabric and spines. i.e. Structural components: 32% × 960 kg = 307 kg.
- **Step 2:** In low debris environments, this contributes to 86% of total fabric mass, which we can solve for as:
		  307 kg ÷ 0.86 ≈ 357 kg 
- **Step 3:**   Then, we can compute mass per surface area of this deep space BEAM as:
	  357 kg ÷ 57 m² = 6.26 kg/m² 
  to get a Von Braun wheel mass of  (4,440 m² × 6.26 kg/m² )≈ **27.5 tonnes**

Now, we could anticipate that such a deep space BEAM might stow more compactly—here, I assume about 6 m³. If so, this would fit even more easily in one Starship as the new "packing efficiency of a deep space BEAM" is 9.3 m²/m³ (i.e. 57 m² ÷ 6 m³). Dividing this packing efficiency from the surface area of the 75 m von Braun wheel gives its stowed volume as 463 m³ packed (4,440m² ÷ 9.3 m²/m³).

**Scenario 3: Low Earth Orbit (High Debris Environment)**

In this case, repeat the calculations from scenario 1 but using BEAM's reported total mass of 1,360 kg, including bulkheads. This gives us a total mass the von Braun wheel at over 100 tonnes, indicating we need two Starship launches; as none of the areal and volumetric properies change from scenario 1, its stowed volume remains the same at 733 m³.
- Mass per surface area = 1,360 kg ÷ 57 m² = 23.85 kg/m²
- Von Braun wheel mass = 4,440 m² × 23.85 kg/m² ≈ **105 tonnes**

**Summary of Mass Estimates:**
The following table summarizes the structural mass and stowage volume across three orbital scenarios, illustrating the tradeoff between environmental shielding needs and habitat scalability.

| Scenario | Environment       | Assumptions                                  | Fabric Mass | Volume | Starship Launches |
| -------- | ----------------- | -------------------------------------------- | ----------- | ------ | ----------------- |
| 1        | LEO (high debris) | Full MMOD protection, no bulkhead            | 74 tonnes   | 733 m³ | 1                 |
| 2        | Deep space        | Minimal MMOD protection, no bulkhead<br>     | 27.5 tonnes | 463 m³ | 1                 |
| 3        | LEO (high debris) | Full MMOD protection, bulkhead mass included | 105 tonnes  | 733 m³ | 2                 |

These estimates highlight the significant mass savings achievable through orbital environment selection and demonstrate the importance of early architectural assumptions in space station design.