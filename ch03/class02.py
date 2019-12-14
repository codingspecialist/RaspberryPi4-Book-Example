class AutoMobile:
    name = ""
    velocity = 0
    def __init__(self, str):
        self.name = str
    def velocityPlus(self):
        self.velocity = self.velocity + 1
    def velocityDw(self):
        self.velocity = self.velocity - 1
        if self.velocity < 0:
            self.velocity = 0
ac = AutoMobile("소나타")
ac.velocity = 20
ac.velocityPlus()
print(ac.name+"의 속도는 %d 입니다." % ac.velocity)