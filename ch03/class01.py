class AutoMobile:
    name = ""
    velocity = 0
    def velocityPlus(self):
        self.velocity = self.velocity + 1
        print("속도는 %d 입니다." % self.velocity)
    def velocityDw(self):
        self.velocity = self.velocity - 1
        if self.velocity < 0:
            self.velocity = 0
        print("속도는 %d 입니다." % self.velocity)
ac = AutoMobile()
ac.velocityPlus()
ac.velocity = 20
ac.velocityDw()