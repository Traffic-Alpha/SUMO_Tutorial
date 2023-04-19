'''
@Author: WANG Maonan
@Date: 2023-04-11 13:47:23
@Description: 获得车辆的信息
1. traci.vehicle.getPosition()，车辆位置；
2. traci.vehicle.getSpeed()，车辆速度；
3. traci.vehicle.getWaitingTime()，车辆等待时间；
@LastEditTime: 2023-04-19 19:10:57
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
    time = traci.simulation.getTime()
    for vehID in traci.vehicle.getIDList(): # 获得所有，车辆的 ID
        pos = traci.vehicle.getPosition(vehID)
        speed = traci.vehicle.getSpeed(vehID)
        time_loss = traci.vehicle.getWaitingTime(vehID)
        print(time, vehID, pos, speed, time_loss)
    print('-')
    traci.simulationStep()

traci.close()