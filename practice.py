import itertools
import numpy


def minCost(sensor_Range, sensors):
    first_sensor = numpy.array((sensors[0][0], sensors[0][1]))
    answer = [sensors[0]]
    #iterate through the sensors list
    for ii in range(1, len(sensors)):
        b = numpy.array((sensors[ii][0], sensors[ii][1]))
        dist = numpy.linalg.norm(first_sensor - b)
        #chcek if it is within range of the first sensor
        if dist <= sensor_Range:
            passed = True
            #iterate through current best run
            for jj in range(0, len(answer)):
                c = numpy.array((answer[jj][0], answer[jj][1]))
                dist = numpy.linalg.norm(c - b)
                #check if it is within range of all the sensors in current best run
                if dist > sensor_Range:
                    passed = False
            if passed:
                answer.append(sensors[ii])
    return answer
        #euclidean distance between starting sensor and sensor[i]
        #check if the euclidean distance is <= sensor_Range, if so save it and return an array of the sensors


with open("amazon.txt") as textFile:
    text_file = [line.split() for line in textFile]
temp = list(itertools.chain.from_iterable(text_file))
cases = []
num_Sensors = []
sensor_Range = []
sensors = []
final_answer = []
#iterate through the textfile and sort it
while temp:
    temp_Num_Sensors = int(temp.pop(0))
    num_Sensors.append(temp_Num_Sensors)
    sensor_Range.append(int(temp.pop(0)))
    for i in range(0, temp_Num_Sensors*2):
        sensors.append(int(temp.pop(0)))
#iterate each problem
for i in range (0, len(num_Sensors)):
    current_sensors = []
    best_run_count = float('-inf')
    #iterate through current problems sensors
    for j in range (0, num_Sensors[i]):
        temp = []
        temp.append(sensors.pop(0))
        temp.append(sensors.pop(0))
        temp.append(j+1)
        current_sensors.append(temp)
    sensor_permutations = list(itertools.permutations(current_sensors))
    #iterate through current problems sensor permutations
    for k in range(0, len(sensor_permutations)):
        current_run = minCost(sensor_Range[i], sensor_permutations[k])
        #find the best run
        if len(current_run) > best_run_count:
            best_run_count = len(current_run)
            best_run = current_run
    final_answer.append(best_run)
#print the answer
for v in range (0, len(final_answer)):
    print len(final_answer[v])
    answer = ""
    for vv in range (0, len(final_answer[v])):
        answer = answer + str(final_answer[v][vv][2]) + " "
    print answer

#feed it into the minCost
#take the return array and keep the largest one cus you know that ones the best
#append the best one to the final answers array
#do it again until you are out of num_sensors