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

The von Braun wheel design assumes a torus with major radius R = 37.5 m and minor radius r = 3 m.

**Internal volume:** Using the standard torus volume formula:

$$
V = 2π²Rr² = 2π²(37.5)(3²) ≈ 6,650 m³
$$

**Surface area:** The surface area for a torus with the same dimensions:

$$
A_s = 4\pi^2 R r = 4\pi^2(37.5)(3) \approx 4,440 \, \text{m}^2
$$

# Air Mass Requirements
At standard atmospheric conditions, air has a density of approximately 1.2 kg/m³. Therefore, the total air mass required to pressurize the habitat to Earth-like atmospheric pressure (1 bar) is:

$$
m_{air} = 6,650 m³ × 1.2 kg/m³ ≈ 8,000 kg = 8 \, tonnes
$$

[[Delivering air at this scale in a compressed form sounds logical but would likely require novel solutions.]]

# Using BEAM as a Scaling Baseline

![The Bigelow Expandable Activity Module](assets/imgs/WiP1/BEAM.png)

To estimate the fabric mass for our wheel, we use the  [Bigelow Expandable Activity Module (BEAM)](https://www.nasa.gov/wp-content/uploads/2015/06/2016-march-beam-factsheet-508.pdf)  as a reference point. BEAM represents the most flight-proven inflatable habitat technology available.

## BEAM's Key Specifications

BEAM weighs 1,360 kg total and consists of:
- **Two metal bulkheads:** 400 kg total ([200 kg](https://en.wikipedia.org/wiki/Common_Berthing_Mechanism) each) - these provide docking interfaces, called [Passive Common Berthing Mechanisms (PCBMs)](https://www.sierraspace.com/wp-content/uploads/2024/01/DOCKING-AND-BERTHING-SYSTEMS-Passive-Common-Berthing-Mechanism-PCBM.pdf) for attaching incoming spacecraft to the International Space Station (ISS).
- **Multi-layer fabric shell:** 960 kg—this includes all soft materials and structural spines that provide hard points to integrate sensors, radiation monitors, and other fixtures.

For our analysis, we focus on the 960 kg fabric mass since a von Braun wheel wouldn't need the same bulkhead configuration.

## BEAM's Physical Properties

When deployed, BEAM measures:
- **Length:** 4.0 m
- **Diameter:** 3.2 m
- **Surface area:** ~57 m²
- **Usable volume:** 16 m³

When stowed for launch:
- **Length:** 2.1 m
- **Diameter:** 2.36 m
- **Stowed volume:** ~9.5 m³

From these numbers, we can calculate BEAM's **packing efficiency** - how much deployed surface area fits into a given stowed volume:
$$
\text{Packing efficiency}=\frac{57\,m^2}{9.5\,m^3}​\approx6\,m^2/m^3
$$

# Fabric Mass Scenarios

The mass of an inflatable habitat's fabric depends heavily on the space environment as the risk of colliding with micrometeoroids and orbital debris (MMOD) varies between orbit. We examine three scenarios:

## Scenario 1: Low Earth Orbit (High Debris)

In Low Earth Orbit, orbital debris is abundant. Based on TransHab studies, approximately 68% of an inflatable habitat's fabric mass consists of MMOD shielding (Page 5 in [Litteken et al., 2019](https://www.researchgate.net/profile/Douglas-Litteken/publication/333919095_System_Integration_Comparison_Between_Inflatable_and_Metallic_Spacecraft_Structures/links/5e75387392851cf2719a389c/System-Integration-Comparison-Between-Inflatable-and-Metallic-Spacecraft-Structures.pdf?__cf_chl_tk=pDGvn9SayN3u94_S2IxijTtcfUUkhKg0khQn23ldwPY-1735002576-1.0.1.1-tXvyxaLfG.lXVagYY.rMLfOHHkqRP9DP3HAh.jXshUY)).

**Calculation steps:**

1. BEAM's mass per surface area: 960 kg ÷ 57 m² = 16.8 kg/m²
2. Von Braun wheel fabric mass: 4,440 m² × 16.8 kg/m² = **75 tonnes**
3. Stowed volume: 4,440 m² ÷ 6 m²/m³ = 740 m³

**Result:** 75 tonnes fabric mass, fitting in one Starship launch

## Scenario 2: Low Debris Orbits

In low debris environments (higher orbits, lunar vicinity, Lagrange points), orbital debris is minimal. MMOD shielding drops to only ~14% of total fabric mass (Page 5 in [Litteken et al., 2019](https://www.researchgate.net/profile/Douglas-Litteken/publication/333919095_System_Integration_Comparison_Between_Inflatable_and_Metallic_Spacecraft_Structures/links/5e75387392851cf2719a389c/System-Integration-Comparison-Between-Inflatable-and-Metallic-Spacecraft-Structures.pdf?__cf_chl_tk=pDGvn9SayN3u94_S2IxijTtcfUUkhKg0khQn23ldwPY-1735002576-1.0.1.1-tXvyxaLfG.lXVagYY.rMLfOHHkqRP9DP3HAh.jXshUY)).

**Calculation steps:**

1. Non-shielding fabric mass (constant): 32% of BEAM's 960 kg = 307 kg
2. In low debris orbits, this 307 kg represents 86% of total fabric mass
3. Total BEAM mass in this case: 307 kg ÷ 0.86 = 357 kg
4. Mass per surface area: 357 kg ÷ 57 m² = 6.3 kg/m²
5. Von Braun wheel fabric mass: 4,440 m² × 6.3 kg/m² = **28 tonnes**
6. Stowed volume: 4,440 m² ÷ 9 m²/m³ = 490 m³. Note that we assume better packing efficiency in low debris  environments (9 m²/m³). 

**Result:** 28 tonnes fabric mass, easily fitting in one Starship launch

## Scenario 3: Conservative LEO Estimate

This scenario uses BEAM's full 1,360 kg mass (including bulkheads) to provide a conservative upper bound.

**Calculation steps:**

1. Total mass per surface area: 1,360 kg ÷ 57 m² = 23.9 kg/m²
2. Von Braun wheel total mass: 4,440 m² × 23.9 kg/m² = **106 tonnes**
3. Stowed volume: Same as Scenario 1 = 740 m³

**Result:** 106 tonnes total mass, requiring two Starship launches

# Summary

| Scenario | Environment       | Assumptions                                  | Fabric Mass | Volume | Starship Launches |
| -------- | ----------------- | -------------------------------------------- | ----------- | ------ | ----------------- |
| 1        | LEO (high debris) | Full MMOD protection, no bulkhead            | 75 tonnes   | 740 m³ | 1                 |
| 2        | Low debris orbits | Minimal MMOD protection, no bulkhead<br>     | 28 tonnes   | 490 m³ | 1                 |
| 3        | LEO (high debris) | Full MMOD protection, bulkhead mass included | 106 tonnes  | 740 m³ | 2                 |

These estimates demonstrate the significant mass savings possible through careful orbital environment selection and highlight how MMOD protection requirements drive inflatable habitat design.

**Important limitations:** These estimates offer a first-order understanding of how inflatable station mass might scale with area and orbit. They are not engineering specifications, but they help illustrate the architectural trade space for future rotating habitats—and point toward the role of materials and environment in mission feasibility.