# "Refining SUMO Simulation Strategies for Realistic Traffic Patterns: Insights from Field Experience" paper submitted to ICSRS 2023
# Abstract
 Urbanization and the surge in vehicle numbers have posed significant
  challenges, including tackling traffic congestion, reducing ecological
  footprint, and enhancing safety. In the context of developing efficient and
  sustainable transportation technologies, this research focuses on gaining
  insights into traffic patterns, human behavior, and their impact on urban
  livability. Drawing on field experience, this study investigates the intricate
  traffic conditions in the regional shopping center of
  Saint-Quentin-en-Yvelines using advanced SUMO simulations. By refining traffic
  models and fine-tuning their parameters, the simulation strategy is gradually
  adjusted to accurately simulate the traffic dynamics. Generated data are then
  analyzed to ascertain the usefulness of the whole approach in capturing
  realistic traffic patterns. The outcomes pave the way for designing smart
  vehicular applications to improve traffic flow in comparable urban contexts. 



# Git repository
SUMO version is **v1_17_0**

**Important Note**: If you're aiming to faithfully reproduce the simulation, please avoid running any `build.bat` command. The version we used hasn't been included in the repository...

**Execution**: After cloning, within the `sumo/` directory, run the following command:

`sumo-gui --time-to-teleport -1 --junction-taz --pedestrian.model striping -c osm.sumocfg &`

**Contact**:
- Jean T. Muabila: `jean.tshibangu-muabila_at_estaca.fr`
- Sebti Mouelhi: `sebti.mouelhi_at_estaca.fr`
