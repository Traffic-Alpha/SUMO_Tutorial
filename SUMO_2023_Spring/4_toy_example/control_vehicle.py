'''
@Author: WANG Maonan
@Date: 2023-04-11 13:47:23
@Description: 根据等待时间，控制车辆行驶或停止；
1. 拿到四个 edge 上的车辆等待时间；
2. 将等待时间长的 edge 上车辆速度设置为 20,变为白色；
3. 将等待时间短的 edge 上车辆速度设置为 4,变为绿色；
@LastEditTime: 2023-04-11 14:12:54
'''
import traci
import sumolib
import numpy as np

sumoBinary = sumolib.checkBinary('sumo-gui')
traci.start(
    [sumoBinary, 
     "-c", './sumo_net/sumo.sumocfg'
    ], 
    label='0'
)

edge_ids = {
    '1125695390#0':0, '1125695391#1':0,
    '1125691753#2':0, '1125684496#2':0
}
upstream_edge = {
    '1125695390#0':'1125678574', '1125695391#1':'1125695391#0',
    '1125691753#2':'1125691753#1', '1125684496#2':'1125684496#1'
}
while traci.simulation.getMinExpectedNumber() > 0:
    # Update Avg Time Loss for each Edge
    for edge_id in edge_ids.keys():
        veh_nums = traci.edge.getLastStepVehicleNumber(edge_id)
        time_loss = traci.edge.getWaitingTime(edge_id)
        avg_time_loss = time_loss/veh_nums if veh_nums!=0 else 0
        edge_ids[edge_id] = avg_time_loss
    
    # Change Speed
    avg_edge_time_loss = np.mean(list(edge_ids.values()))
    for edge_id, avg_time_loss in edge_ids.items():
        for veh_id in traci.edge.getLastStepVehicleIDs(edge_id):
            traci.vehicle.setColor(veh_id, (255,255,0)) # yellow
            traci.vehicle.setSpeed(veh_id, 14)
            traci.vehicle.setSpeedMode(veh_id, 5)

        if avg_time_loss >= avg_edge_time_loss:
            for veh_id in traci.edge.getLastStepVehicleIDs(upstream_edge[edge_id]):
                traci.vehicle.setColor(veh_id, (255,255,255)) # white
                traci.vehicle.setSpeed(veh_id, 14)
        else:
            for veh_id in traci.edge.getLastStepVehicleIDs(upstream_edge[edge_id]):
                traci.vehicle.setColor(veh_id, (255,0,255)) # purple
                traci.vehicle.setSpeed(veh_id, 0.5)
    traci.simulationStep()

traci.close()