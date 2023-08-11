# Git repository for "Refining SUMO Simulation Strategies for Realistic Traffic Patterns: Insights from Field Experience" paper submitted to ICSRS 2023

SUMO version is v1_17_0

<span style="color: red;">Warning, if you would like to reproduce exactly the
same simulation under SUMO please don't run `build.bat` </span>

One cloned, under the folder `sumo/`, run this command:

`sumo-gui --time-to-teleport -1 --junction-taz --pedestrian.model striping -c osm.sumocfg &`

Contact:
- Jean T. Muabila: jean.tshibangu-muabila@estaca.fr
- Sebti Mouelhi: sebti.mouelhi@estaca.fr
