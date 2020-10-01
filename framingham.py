class Framingham:

    def __init__(self, gender, age, diabetes, smoker, bloodPersore, totalCholesterol, Hdl, treatedBloodPressure):
        self.gender = gender
        self.age = age
        self.diabetes = diabetes
        self.smoker = smoker
        self.bloodPersore = bloodPersore
        self.totalCholesterol = totalCholesterol
        self.Hdl = Hdl
        self.treatedBloodPressure = treatedBloodPressure

    def FraminghamRisk(self):
        RiskScore = []

        if self.gender == 0:
            # age
            if self.age <= 34:
                RiskScore.append(0)
            elif 34 < self.age <= 39:
                RiskScore.append(2)
            elif 39 < self.age <= 44:
                RiskScore.append(5)
            elif 44 < self.age <= 49:
                RiskScore.append(7)
            elif 49 < self.age <= 54:
                RiskScore.append(8)
            elif 54 < self.age <= 59:
                RiskScore.append(10)
            elif 59 < self.age <= 64:
                RiskScore.append(11)
            elif 64 < self.age <= 69:
                RiskScore.append(12)
            elif 69 < self.age <= 74:
                RiskScore.append(14)
            elif 74 < self.age:
                RiskScore.append(15)

            # diabetes
            if self.diabetes == 0:
                RiskScore.append(4)
            else:
                RiskScore.append(0)
            # Smoker
            if self.smoker == 1:
                RiskScore.append(4)
            else:
                RiskScore.append(0)

            # BP
            if self.treatedBloodPressure == 0:  # BP Treated

                if self.bloodPersore <= 120:
                    RiskScore.append(0)
                elif 120 < self.bloodPersore <= 129:
                    RiskScore.append(2)
                elif 129 < self.bloodPersore <= 139:
                    RiskScore.append(3)
                elif 139 < self.bloodPersore <= 149:
                    RiskScore.append(4)
                elif 149 < self.bloodPersore <= 159:
                    RiskScore.append(4)
                elif 159 < self.bloodPersore:
                    RiskScore.append(5)

            if self.treatedBloodPressure == 1:  # BP  Not Treated
                if self.bloodPersore <= 120:
                    RiskScore.append(-2)
                elif 120 < self.bloodPersore <= 129:
                    RiskScore.append(0)
                elif 129 < self.bloodPersore <= 139:
                    RiskScore.append(1)
                elif 139 < self.bloodPersore <= 149:
                    RiskScore.append(2)
                elif 149 < self.bloodPersore <= 159:
                    RiskScore.append(2)
                elif 159 < self.bloodPersore:
                    RiskScore.append(3)
            # totalCholesterol
            if self.totalCholesterol <= 74:
                RiskScore.append(0)
            elif 74 < self.totalCholesterol <= 94:
                RiskScore.append(1)
            elif 94 < self.totalCholesterol <= 112:
                RiskScore.append(2)
            elif 112 < self.totalCholesterol <= 130:
                RiskScore.append(3)
            elif self.totalCholesterol > 130:
                RiskScore.append(4)
            # Hdl
            if self.Hdl <= 16:
                RiskScore.append(2)
            elif 16 < self.Hdl <= 21:
                RiskScore.append(1)
            elif 21 < self.Hdl <= 24:
                RiskScore.append(0)
            elif 24 < self.Hdl <= 30:
                RiskScore.append(-1)
            elif 30 < self.Hdl:
                RiskScore.append(-2)

            totalRisk = sum(RiskScore)
            Score = []

            if totalRisk <= (-2):
                Score.append(1)
            elif - 2 < totalRisk <= -1:
                Score.append(1.1)
            elif -1 < totalRisk <= 0:
                Score.append(1.4)
            elif 0 < totalRisk <= 1:
                Score.append(1.6)
            elif 1 < totalRisk <= 2:
                Score.append(1.9)
            elif 2 < totalRisk <= 3:
                Score.append(2.3)
            elif 3 < totalRisk <= 4:
                Score.append(2.8)
            elif 4 < totalRisk <= 5:
                Score.append(3.3)
            elif 5 < totalRisk <= 6:
                Score.append(3.9)
            elif 6 < totalRisk <= 7:
                Score.append(4.7)
            elif 7 < totalRisk <= 8:
                Score.append(5.6)
            elif 8 < totalRisk <= 9:
                Score.append(6.7)
            elif 9 < totalRisk <= 10:
                Score.append(7.9)
            elif 10 < totalRisk <= 11:
                Score.append(9.4)
            elif 11 < totalRisk <= 12:
                Score.append(11.2)
            elif 12 < totalRisk <= 13:
                Score.append(13.3)
            elif 13 < totalRisk <= 14:
                Score.append(15.6)
            elif 14 < totalRisk <= 15:
                Score.append(18.4)
            elif 15 < totalRisk <= 16:
                Score.append(18.4)
            elif 16 < totalRisk <= 17:
                Score.append(21.6)
            elif 17 < totalRisk <= 18:
                Score.append(25.3)
            elif 18 < totalRisk <= 19:
                Score.append(29.4)
            elif 19 < totalRisk <= 20:
                Score.append(30)
            elif totalRisk >= 21:
                Score.append(30)
        if self.gender == 1:
            if self.age <= 34:
                RiskScore.append(0)
            elif 34 < self.age <= 39:
                RiskScore.append(2)
            elif 39 < self.age <= 44:
                RiskScore.append(4)
            elif 44 < self.age <= 49:
                RiskScore.append(5)
            elif 49 < self.age <= 54:
                RiskScore.append(7)
            elif 54 < self.age <= 59:
                RiskScore.append(8)
            elif 59 < self.age <= 64:
                RiskScore.append(9)
            elif 64 < self.age <= 69:
                RiskScore.append(10)
            elif 69 < self.age <= 74:
                RiskScore.append(11)
            elif 74 < self.age <= 120:
                RiskScore.append(12)

            if self.Hdl <= 16:
                RiskScore.append(2)
            elif 16 < self.Hdl <= 21:
                RiskScore.append(1)
            elif 21 < self.Hdl <= 24:
                RiskScore.append(0)
            elif 24 < self.Hdl <= 30:
                RiskScore.append(-1)
            elif 30 < self.Hdl:
                RiskScore.append(-2)

            if self.totalCholesterol <= 74:
                RiskScore.append(0)
            elif 74 < self.totalCholesterol <= 94:
                RiskScore.append(1)
            elif 94 < self.totalCholesterol <= 112:
                RiskScore.append(3)
            elif 112 < self.totalCholesterol <= 130:
                RiskScore.append(4)
            elif self.totalCholesterol > 130:
                RiskScore.append(5)

            # BP Treated
            if self.treatedBloodPressure == 1:
                if self.bloodPersore <= 120:
                    RiskScore.append(-1)
                elif 120 < self.bloodPersore <= 129:
                    RiskScore.append(2)
                elif 129 < self.bloodPersore <= 139:
                    RiskScore.append(3)
                elif 139 < self.bloodPersore <= 149:
                    RiskScore.append(5)
                elif 149 < self.bloodPersore <= 159:
                    RiskScore.append(6)
                elif 159 < self.bloodPersore:
                    RiskScore.append(7)

            if self.treatedBloodPressure == 0:
                # BP  Not Treated
                if self.bloodPersore <= 120:
                    RiskScore.append(-3)
                elif 120 < self.bloodPersore <= 129:
                    RiskScore.append(0)
                elif 129 < self.bloodPersore <= 139:
                    RiskScore.append(1)
                elif 139 < self.bloodPersore <= 149:
                    RiskScore.append(2)
                elif 149 < self.bloodPersore <= 159:
                    RiskScore.append(4)
                elif 159 < self.bloodPersore:
                    RiskScore.append(5)

            # smoker

            if self.smoker == 1:
                RiskScore.append(3)
            else:
                RiskScore.append(0)
                # print(risk_v)

            # diabetes

            if self.diabetes == 0:
                RiskScore.append(4)
            else:
                RiskScore.append(0)
                # print(risk_v)

            totalRisk = sum(RiskScore)
            score = []

            if totalRisk <= -2:
                score.append(1)
            elif -2 < totalRisk <= -1:
                score.append(1.2)
            elif -1 < totalRisk <= 0:
                score.append(1.5)
            elif 0 < totalRisk <= 1:
                score.append(1.7)
            elif 1 < totalRisk <= 2:
                score.append(2)
            elif 2 < totalRisk <= 3:
                score.append(2.4)
            elif 3 < totalRisk <= 4:
                score.append(2.8)
            elif 4 < totalRisk <= 5:
                score.append(3.3)
            elif 5 < totalRisk <= 6:
                score.append(3.9)
            elif 6 < totalRisk <= 7:
                score.append(4.5)
            elif 7 < totalRisk <= 8:
                score.append(5.3)
            elif 8 < totalRisk <= 9:
                score.append(6.3)
            elif 9 < totalRisk <= 10:
                score.append(7.3)
            elif 10 < totalRisk <= 11:
                score.append(8.6)
            elif 11 < totalRisk <= 12:
                score.append(10.0)
            elif 12 < totalRisk <= 13:
                score.append(11.7)
            elif 13 < totalRisk <= 14:
                score.append(13.7)
            elif 14 < totalRisk <= 15:
                score.append(15.9)
            elif 15 < totalRisk <= 16:
                score.append(15.9)
            elif 16 < totalRisk <= 17:
                score.append(18.51)
            elif 17 < totalRisk <= 18:
                score.append(21.5)
            elif 18 < totalRisk <= 19:
                score.append(24.8)
            elif 19 < totalRisk <= 20:
                score.append(27.5)
            elif totalRisk >= 21:
                score.append(30)
        return float(score[0])

