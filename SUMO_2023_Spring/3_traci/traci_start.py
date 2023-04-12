'''
@Author: WANG Maonan
@Date: 2023-04-11 13:47:23
@Description: 使用 Traci 开启仿真
@LastEditTime: 2023-04-11 14:12:54
'''
import traci
import sumolib

sumoBinary = sumolib.checkBinary('sumo-gui')
traci.start(
    [sumoBinary, 
     "-c", './sumo_net/sumo.sumocfg'
    ], 
    label='0'
)


while traci.simulation.getMinExpectedNumber() > 0:
   traci.simulationStep()

traci.close()