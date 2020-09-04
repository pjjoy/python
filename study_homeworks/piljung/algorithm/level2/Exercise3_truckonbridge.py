# 3. 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    bridge=[0]*bridge_length#[0 for x in range(bridge_lenght)]
    time = 0
    while bridge:
        time += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return time