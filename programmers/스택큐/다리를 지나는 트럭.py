from collections import  deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    onBridge = deque()
    onBridgeWeight = 0
    time = 0
    inTime = 0

    for i in range(len(truck_weights)):
        while not (len(onBridge) < bridge_length and onBridgeWeight + truck_weights[i] <= weight):
            curTruckIndex, inTime = onBridge.popleft()
            onBridgeWeight -= truck_weights[curTruckIndex]

        if inTime > 0:
            time = inTime + bridge_length
            while onBridge and time <= onBridge[-1][1]:
                time += 1
            inTime = 0
        else:
            time = time + 1
        onBridge.append((i,time))
        onBridgeWeight += truck_weights[i]


    while onBridge:
        curTruckIndex, inTime = onBridge.popleft()
        time = inTime + bridge_length


    return time


def solution2(bridge_length, weight, truck_weights):

    onBridge = deque([0] * bridge_length)
    onBridgeWeight = 0
    onBridgeCount = 0

    i = 0
    time = 0
    while onBridge and i < len(truck_weights):
        popWeight = onBridge.popleft()
        onBridgeWeight -= popWeight

        if len(onBridge) < bridge_length and onBridgeWeight + truck_weights[i] <= weight:
            onBridge.append(truck_weights[i])
            onBridgeWeight += truck_weights[i]
            i += 1
        else:
            onBridge.append(0)

        time += 1


    while onBridge:
        onBridge.popleft()
        time += 1

    return time



assert solution2(10,100,[50, 30, 10, 10, 30, 10, 40]) == 23
assert solution2(2,10,[7,4,5,6]) == 8
assert solution2(100,100,[10]) == 101
assert solution2(100,100,[10,10,10,10,10,10,10,10,10,10]	) == 110
