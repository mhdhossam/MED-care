from .models import patientLogin
from .models import medicallogin

#check for medicalproviders
def checkData1(request,email,email1,password,password1 ):
    id = medicallogin.getID()
    for i in range(0,len(email)):
      if email[i][0] == email1 and password[i][0] == password1 :
        return id[i][0]
      elif email[len(email)-1][0] != email1 :
        return False
        break

#check for patient
def checkData(request,email,email1,password,password1 ):
    id = patientLogin.getID()
    for i in range(0,len(email)):
      if email[i][0] == email1 and password[i][0] == password1 :
        return id[i][0]
      elif email[len(email)-1][0] != email1 :
        return False
        break

