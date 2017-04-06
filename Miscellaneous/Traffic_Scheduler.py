import time

total_traffic_time = 180

lane_weight = [1, 1, 1, 1]
weight_delta = 0.2

print(" ------ Welcome to Traffic Scheduler ------- ")
print(" Total Traffic Signal Time :", total_traffic_time)


while True:

    print("\n\n ------------ New Traffic Round ------------ ")

    # Calculate time for each lane
    lane_time = [ total_traffic_time*weight/sum(lane_weight) for weight in lane_weight]
    print("Lane Weights :", lane_weight)

    # Simulation
    for i in range(len(lane_time)):
        print("\nLane", i+1,"green signal for", lane_time[i],"sec")
        time.sleep(lane_time[i]/20);
        print("Stopping lane", i+1)

    
    # Convert input from string to list of string to list of int
    inc_lanes = input("\n\nEnter lanes that have more traffic now (1-4) :");
    inc_lanes = list(map(int, inc_lanes.split()))
    
    for lane in inc_lanes:
        if lane >=1 and lane<=4:
            lane_weight[lane-1] = min( 5, lane_weight[lane-1] + weight_delta);
        else:
            print("Invalid Lane", lane)

    dec_lanes = input("Enter lanes that have less traffic now (1-4) :");
    dec_lanes = list(map(int, dec_lanes.split()))
    for lane in dec_lanes:
        if lane >=1 and lane<=4:
            lane_weight[lane-1] = max( 0.1, lane_weight[lane-1] - weight_delta);
        else:
            print("Invalid Lane", lane)

        
    
    




    

    

    
    
