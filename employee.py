"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name
        self.contractType = None
        self.contractDetails = None
        self.commissionType = None
        self.commissionDetails = None

    def setMonthly(self, salary):
        self.contractType = "monthly"
        self.contractDetails = salary

    def setHourly(self, hoursWorked, hourlyRate):
        self.contractType = "hourly"
        self.contractDetails = {"hoursWorked": hoursWorked, "hourlyRate": hourlyRate}

    def setBonus(self, bonusAmount):
        self.commissionType = "bonus"
        self.commissionDetails = bonusAmount

    def setContract(self, numContracts, commissionPerContract):
        self.commissionType = "contract"
        self.commissionDetails = {"numContracts": numContracts, "commissionPerContract": commissionPerContract}

    def get_pay(self):
        if self.contractType == "monthly":
            contractPay = self.contractDetails
        elif self.contractType == "hourly":
            contractPay = self.contractDetails["hoursWorked"] * self.contractDetails["hourlyRate"]
        else:
            contractPay = 0

        if self.commissionType == "bonus":
            commissionPay = self.commissionDetails
        elif self.commissionType == "contract":
            commissionPay = self.commissionDetails["numContracts"] * self.commissionDetails["commissionPerContract"]
        else:
            commissionPay = 0

        return contractPay + commissionPay

    def __str__(self):
        contractInfo = ""
        commissionInfo = ""

        if self.contractType == "monthly":
            contractInfo = f"works on a monthly salary of {self.contractDetails}"
        elif self.contractType == "hourly":
            contractInfo = f"works on a contract of {self.contractDetails['hoursWorked']} hours at {self.contractDetails['hourlyRate']}/hour"

        if self.commissionType == "bonus":
            commissionInfo = f"receives a bonus commission of {self.commissionDetails}"
        elif self.commissionType == "contract":
            commissionInfo = f"receives a commission for {self.commissionDetails['numContracts']} contract(s) at {self.commissionDetails['commissionPerContract']}/contract"

        totalPay = self.get_pay()
        if commissionInfo:
            return f"{self.name} {contractInfo} and {commissionInfo}. Their total pay is {totalPay}."
        return f"{self.name} {contractInfo}. Their total pay is {totalPay}."


billie = Employee('Billie')
billie.setMonthly(4000)

charlie = Employee('Charlie')
charlie.setHourly(100, 25)

renee = Employee('Renee')
renee.setMonthly(3000)
renee.setContract(4, 200)

jan = Employee('Jan')
jan.setHourly(150, 25)
jan.setContract(3, 220)

robbie = Employee('Robbie')
robbie.setMonthly(2000)
robbie.setBonus(1500)

ariel = Employee('Ariel')
ariel.setHourly(120, 30)
ariel.setBonus(600)