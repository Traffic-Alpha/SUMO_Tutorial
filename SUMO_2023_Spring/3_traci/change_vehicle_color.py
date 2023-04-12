'''
@Author: WANG Maonan
@Date: 2023-04-11 13:47:23
@Description: 修改车辆的信息
- 如果等待时间超过 10s，则修改颜色；
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
    time = traci.simulation.getTime()
    for vehID in traci.vehicle.getIDList():
        time_loss = traci.vehicle.getWaitingTime(vehID)
        if time_loss > 10:
            traci.vehicle.setColor(vehID, (255,255,255))
    traci.simulationStep()

traci.close()