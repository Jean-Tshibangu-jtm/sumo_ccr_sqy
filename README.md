# Git repository for "Refining SUMO Simulation Strategies for Realistic Traffic Patterns: Insights from Field Experience" paper submitted to ICSRS 2023

SUMO version is **v1_17_0**

**Important Note**: If you're aiming to faithfully reproduce the simulation, please avoid running any `build.bat` command. The version we used hasn't been included in the repository...

**Execution**: After cloning, within the `sumo/` directory, run the following command:

`sumo-gui --time-to-teleport -1 --junction-taz --pedestrian.model striping -c osm.sumocfg &`

**Contact**:
- Jean T. Muabila: `jean.tshibangu-muabila_at_estaca.fr`
- Sebti Mouelhi: `sebti.mouelhi_at_estaca.fr`
