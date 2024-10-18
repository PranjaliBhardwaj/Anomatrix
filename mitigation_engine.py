import socket
import threading
import time

class MitigationEngine:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.attack_count = 0
        self.last_mitigation_time = time.time()

    def mitigate_attack(self):
        print("Mitigating attack from IP:", self.ip, "on port:", self.port)
        self.attack_count += 1
        current_time = time.time()

        # agar last 10 seconds me 1000 se jyada req aati hai, then drop connections from attacker IP
        if self.attack_count > 1000 and current_time - self.last_mitigation_time < 10:
            print("Rate limiting - dropping connections from attacker's IP:", self.ip)
            self.attack_count = 0
            self.last_mitigation_time = current_time
        elif current_time - self.last_mitigation_time >= 10:
            # Attack count and mitigation ko reset krdega taki process dubara start ho
            self.attack_count = 0
            self.last_mitigation_time = current_time

# Creating an instance of MitigationEngine
a = MitigationEngine("175.176.187.102", 80)

# Calling the mitigate_attack method
a.mitigate_attack()





