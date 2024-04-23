data = [
    ["Good", "High", "A", "Pass"],
    ["Good", "Low", "B", "Pass"],
    ["Poor", "High", "C", "Fail"],
    ["Poor", "Low", "B", "Fail"],
    ["Good", "Low", "A", "Pass"],
    ["Good", "High", "C", "Pass"],
]
P_PASS = 0.0
P_FAIL = 0.0
def computeProbabilities():
    passCount = 0
    failCount = 0
    totalStudents = len(data)
    for row in data:
        study, sports, grade, result = row[0], row[1], row[2], row[3]
        if result == "Pass":
            passCount += 1
        else:
            failCount += 1
    global P_PASS, P_FAIL
    P_PASS = passCount / totalStudents
    P_FAIL = failCount / totalStudents
def testClassifier():
    input_str = input("Enter comma-separated test tuple (e.g., 'Good,High,A'): ")
    test = input_str.split(",")
    pPass = P_PASS
    pFail = P_FAIL
    for row in data:
        study, sports, grade, result = row[0], row[1], row[2], row[3]
        if study == test[0] and sports == test[1] and grade == test[2]:
            if result == "Pass":
                pPass += 1
            else:
                pFail += 1
    pPass /= (P_PASS + P_FAIL)
    pFail /= (P_PASS + P_FAIL)
    print("Probability of Passing:", pPass)
    print("Probability of Failing:", pFail)
    if pPass > pFail:
        print("Prediction: Pass")
    else:
        print("Prediction: Fail")
if __name__ == "__main__":
    computeProbabilities()
    testClassifier()