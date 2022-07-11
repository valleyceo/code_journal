# Design Log Aggregation System

"""
Implement a Log Aggregation System which aggregates logs from various services in a datacenter and provides search APIs.

Design the LogAggregator class:

LogAggregator(int machines, int services) Initializes the object with machines and services representing the number of machines and services in the datacenter, respectively.
void pushLog(int logId, int machineId, int serviceId, String message) Adds a log with id logId notifying that the machine machineId sent a string message while executing the service serviceId.
List<Integer> getLogsFromMachine(int machineId) Returns a list of ids of all logs added by machine machineId.
List<Integer> getLogsOfService(int serviceId) Returns a list of ids of all logs added while running service serviceId on any machine.
List<String> search(int serviceId, String searchString) Returns a list of messages of all logs added while running service serviceId where the message of the log contains searchString as a substring.
Note that:

The entries in each list should be in the order they were added, i.e., the older logs should precede the newer logs.
A machine can run multiple services more than once. Similarly, a service can be run on multiple machines.
All logId may not be ordered.
A substring is a contiguous sequence of characters within a string.
"""

class LogAggregator:

    def __init__(self, machines: int, services: int):
        self.logMap = {}
        self.machineMap = defaultdict(list)
        self.serviceMap = defaultdict(list)

    def pushLog(self, logId: int, machineId: int, serviceId: int, message: str) -> None:
        self.machineMap[machineId].append(logId)
        self.serviceMap[serviceId].append(logId)
        self.logMap[logId] = message

    def getLogsFromMachine(self, machineId: int) -> List[int]:
        return self.machineMap[machineId]

    def getLogsOfService(self, serviceId: int) -> List[int]:
        return self.serviceMap[serviceId]

    def search(self, serviceId: int, searchString: str) -> List[str]:
        outMatch = []

        for sid, lid_list in self.serviceMap.items():
            if sid != serviceId:
                continue

            for lid in lid_list:
                msg = self.logMap[lid]

                if msg.find(searchString) != -1:
                    outMatch.append(msg)

        return outMatch

# Your LogAggregator object will be instantiated and called as such:
# obj = LogAggregator(machines, services)
# obj.pushLog(logId,machineId,serviceId,message)
# param_2 = obj.getLogsFromMachine(machineId)
# param_3 = obj.getLogsOfService(serviceId)
# param_4 = obj.search(serviceId,searchString)
