'''
@Author: WANG Maonan
@Date: 2023-04-11 13:47:23
@Description: 获得车道的信息
1. traci.edge.getLastStepMeanSpeed()，车道平均速度；
2. traci.edge.getCO2Emission()，车道上车辆的二氧化碳排放；
@LastEditTime: 2023-04-19 19:20:29
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

# 仿真直到路网中没有车辆
while traci.simulation.getMinExpectedNumber() > 0:
    for edge_id in traci.edge.getIDList(): # 获得所有车道的 id
        veh_num = traci.edge.getLastStepVehicleNumber(edge_id)
        if veh_num > 0:
            avg_speed = traci.edge.getLastStepMeanSpeed(edge_id)
            avg_co2 = traci.edge.getCO2Emission(edge_id)
            print(edge_id, avg_speed, avg_co2)
    print('-')
    traci.simulationStep()

traci.close()