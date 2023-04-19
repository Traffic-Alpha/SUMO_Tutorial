'''
@Author: WANG Maonan
@Date: 2023-04-11 13:47:23
@Description: 使用 Traci 开启仿真
@ sumo-gui -c xxx.sumocfg
@LastEditTime: 2023-04-19 19:09:27
'''
import traci
import sumolib

sumoBinary = sumolib.checkBinary('sumo-gui') # sumo-gui 是可以打开界面; sumo 不打开界面
traci.start(
    [sumoBinary, 
     "-c", './sumo_net/sumo.sumocfg'
    ], 
    label='0'
)

# 进行仿真
while traci.simulation.getMinExpectedNumber() > 0: # 判断路网中是否有车
   traci.simulationStep()

traci.close()