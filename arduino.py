import serial

class Arduino:
    def __init__(self, port, baud_rate=115200):
        self.port = port
        self.baud_rate = baud_rate
        self.arduino = serial.Serial(port=self.port, baudrate=self.baud_rate, timeout=0.1)

    def wait_until_ready(self):
        while self.arduino.in_waiting == 0:
            pass

    def write(self, data):
        if isinstance(data, str):
            data = bytes(data, "utf-8")
        self.arduino.write(data)

    def recv(self):
        return self.arduino.readline()

    def write_and_recv(self, data):
        self.write(data)
        self.wait_until_ready()
        print(self.recv().decode('utf-8'))
    
    def close(self):
        self.arduino.close()
