from django.shortcuts import render
import pickle
#import numpy as np
def home(request):
    return render(request,'index.html')
def getdata(sex,cp,restecg,exang,oldpeak,slope,ca,thal,fbs,thalach):
   # X=np.array([sex,cp,restecg,exang,oldpeak,slope,ca,])
    model=pickle.load(open('static\Heart_Disease_Prediction_NB.py','rb'))
    prediction=model.predict([[sex,cp,restecg,exang,oldpeak,slope,ca,thal,fbs,thalach]])
    if prediction==0:
        return "Congrats! No Heart Disease Found"
    elif prediction==1:
        return "Heart Disease Found! Kindly Contact To Your Doctor ASAP!"
    else:
        return "Error"
def result(request):
    sex=int(request.POST.get('sex',False))
    cp=int(request.POST.get('cp',False))
    restecg=int(request.POST.get('restecg',False))
    exang=int(request.POST.get('exang',False))
    oldpeak=float(request.POST.get('oldpeak',False))
    slope=int(request.POST.get('slope',False))
    ca=int(request.POST.get('ca',False))
    thal=int(request.POST.get('thal',1))
    fbs=int(request.POST.get('fbs',False))
    thalach=int(request.POST.get('thalach',72))
    result=getdata(sex,cp,restecg,exang,oldpeak,slope,ca,thal,fbs,thalach)
    return render(request,'result.html',{'result':result})