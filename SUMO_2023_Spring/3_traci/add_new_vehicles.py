'''
@Author: WANG Maonan
@Date: 2023-04-11 13:47:23
@Description: 添加新的右转车辆
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

traci.route.add('r_turn', ['1125695391#0', '238823566', '219060439#2'])
for i in range(10):
    traci.vehicle.add(str(i), 'r_turn', depart=i+20, departLane='free')

while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()

traci.close()