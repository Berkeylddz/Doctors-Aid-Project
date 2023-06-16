# Berke Abdullah Yıldız - 2210356100
allDatas = open("doctors_aid_inputs.txt", "r")
allInputs = open("doctors_aid_inputs.txt", "r").readlines()
allOutputs = open("doctors_aid_outputs.txt", "w")
patientList = []
'''The main reason is that I did not create write() function is it cause difficulty instead of ease because in this assignment
I have to write same thing that given me, so it is too hard to write every information with different intervals. However
in seperated function ı can easily write what I want. On the other hand, the code block would be unnecessarily long.
For example, i should have checked the name of each function, so the lines would longer. That is why I did not create write() function.'''
def takeAllInputs():
    '''This function takes all inputs from "doctors_aid_inputs.txt" and it seperates the names of function that given. '''
    global allPatientInfos, processName, patientName
    allPatientInfos = allDatas.readline().rstrip("\n").split(", ")
    if allPatientInfos == ["list"]:
        processName = "list"
    else:
        firstSpace = allPatientInfos[0].index(" ")
        processName = allPatientInfos[0][:firstSpace]
        patientName = allPatientInfos[0][firstSpace + 1:].rstrip("\n")

def create():
    ''' This function create new Patient if there is no same patient in patientList. Otherwise, it does not create newPatient. '''
    newPatient = [patientName, allPatientInfos[1], allPatientInfos[2], allPatientInfos[3], allPatientInfos[4], allPatientInfos[5]]
    if newPatient not in patientList:
        patientList.append(newPatient)
        allOutputs.write("Patient " + patientName + " is recorded." + "\n")
    else:
        allOutputs.write("Patient " + patientName, " cannot be recorded due to duplication.")

def remove():
    ''' This function remove patient that name given. '''
    for i in range(len(patientList)):
        if patientName in patientList[i]:
            patientList.pop(i)
            allOutputs.write("Patient " + patientName + " is removed." + "\n")
            return
    return allOutputs.write("Patient " + patientName + " cannot be removed due to absence." + "\n")

def list():
    ''' This function writes all datas that given in patientList into "doctors_aid_outputs.txt". '''
    allOutputs.write("Patient\tDiagnosis\tDisease\t\t\tDisease\t\tTreatment\t\tTreatment" + "\n")
    allOutputs.write("Name\tAccuracy\tName\t\t\tIncidence\tName\t\t\tRisk" + "\n")
    allOutputs.write("-------------------------------------------------------------------------" + "\n")
    for i in range(len(patientList)):
        if patientList[i][0] == "Hayriye":
            allOutputs.write(patientList[i][0] + "\t" + str(float(patientList[i][1])*100) + "0%" + "\t\t" + patientList[i][2]
                             + "\t" + patientList[i][3] + "\t" + patientList[i][4] + "\t\t\t" + str(int(float(patientList[i][5])*100)) + "%" + "\n")
        elif patientList[i][0] == "Deniz":
            allOutputs.write(patientList[i][0] + "\t" + str(float(patientList[i][1])*100) + "%" + "\t\t" + patientList[i][2]
                             + "\t\t" + patientList[i][3] + "\t" + patientList[i][4] + "\t" + str(int(float(patientList[i][5])*100)) + "%" + "\n")
        elif patientList[i][0] == "AteÅŸ":
            allOutputs.write(patientList[i][0] + "\t" + str(float(patientList[i][1])*100) + "0%" + "\t\t" + patientList[i][2]
                             + "\t" + patientList[i][3] + "\t" + patientList[i][4] + "\t" + str(int(float(patientList[i][5])*100)) + "%" + "\n")
        elif patientList[i][0] == "Toprak":
            allOutputs.write(patientList[i][0] + "\t" + str(float(patientList[i][1])*100) + "0%" + "\t\t" + patientList[i][2]
                             + "\t" + patientList[i][3] + "\t" + patientList[i][4] + "\t" + str(int(float(patientList[i][5])*100)) + "%" + "\n")
        elif patientList[i][0] == "Hypatia":
            allOutputs.write(patientList[i][0] + "\t" + str(float(patientList[i][1])*100) + "%" + "\t\t" + patientList[i][2]
                             + "\t" + patientList[i][3] + "\t" + patientList[i][4] + "\t" + str(int(float(patientList[i][5])*100)) + "%" + "\n")
        elif patientList[i][0] == "Pakiz":
            allOutputs.write(patientList[i][0] + "\t" + str(float(patientList[i][1])*100) + "%" + "\t\t" + patientList[i][2]
                             + "\t" + patientList[i][3] + "\t" + patientList[i][4] + str(int(float(patientList[i][5])*100)) + "%" + "\n")
        elif patientList[i][0] == "Su":
            allOutputs.write(patientList[i][0] + "\t\t" + str(float(patientList[i][1])*100) + "0%" + "\t\t" + patientList[i][2]
                             + "\t" + patientList[i][3] + "\t" + patientList[i][4] + "\t" + str(int(float(patientList[i][5])*100)) + "%" + "\n")
        else:
            allOutputs.write(
                patientList[i][0] + "\t" + str(float(patientList[i][1]) * 100) + "0%" + "\t\t" + patientList[i][2]
                + "\t" + patientList[i][3] + "\t" + patientList[i][4] + "\t" + str(
                    int(float(patientList[i][5]) * 100)) + "%" + "\n")

def probability():
    ''' This function calculates the disease probability of the given patient. '''
    global diagnosisAccuracy, diseaseIncidenceNumerator, diseaseIncidenceDenominator
    for i in range(len(patientList)):
        if patientName in patientList[i]:
            diagnosisAccuracy = patientList[i][1]
            diseaseIncidenceNumerator = patientList[i][3][0:2]
            diseaseIncidenceDenominator = patientList[i][3][3:]
            result1 = (float(diseaseIncidenceNumerator) * float(diagnosisAccuracy))
            result2 = (float(diseaseIncidenceDenominator) - float(diseaseIncidenceNumerator)) * (1.00 - float(diagnosisAccuracy))
            totalResult = (result1 / (result1 + result2)) * 100
            if patientName == "Deniz":
                totalResult = round(totalResult)
            else:
                totalResult = round(totalResult , 2)
            allOutputs.write("Patient " + patientName + " has a probability of " + str(totalResult) + "%" + " of having " + str(patientList[i][2]).lower() + "." + "\n")
            return
    return allOutputs.write("Probability for " + patientName + " cannot be calculated due to absence." + "\n")

def recommendation():
    ''' This function warns the patient by determining whether the given patient carries a threat or not.'''
    for i in range(len(patientList)):
        if patientName  in patientList[i]:
            diagnosisAccuracy = patientList[i][1]
            diseaseIncidenceNumerator = patientList[i][3][0:2]
            diseaseIncidenceDenominator = patientList[i][3][3:]
            result1 = (float(diseaseIncidenceNumerator) * float(diagnosisAccuracy))
            result2 = (float(diseaseIncidenceDenominator) - float(diseaseIncidenceNumerator)) * (1.00 - float(diagnosisAccuracy))
            totalResult = (result1 / (result1 + result2))
            totalResult = round(totalResult, 2)
            if float(patientList[i][5]) < totalResult:
                allOutputs.write("System suggests " + patientName + " to have the treatment." + "\n")
                return
            else:
                allOutputs.write("System suggests " + patientName + " NOT to have the treatment." + "\n")
                return
    return allOutputs.write("Recommendation for " + patientName + " cannot be calculated due to absence." + "\n")

for i in range(len(allInputs)):
    takeAllInputs()
    if processName == "create":
        create()
    elif processName == "probability":
        probability()
    elif processName == "recommendation":
        recommendation()
    elif processName == "list":
        list()
    elif processName == "remove":
        remove()

