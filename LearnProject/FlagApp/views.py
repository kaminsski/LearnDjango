from django.shortcuts import render, redirect
import random
from django.contrib import messages

from .models import *
from UserApp.models import *


def flag(request):
    if request.method == "POST":
        answer = request.POST.get("selected")
        user = request.user
        last = user.userLastNumber
        answer_exist = FlagModel.objects.filter(_id=last).first()

        if answer:
            if answer_exist.name == answer:
                if len(list(user.userListeElemani.all())) > 1:
                    messages.add_message(request, messages.INFO,"Correct!")
                user.userListeElemani.remove(last)
                user.gamePoint += answer_exist.flagPoint
                user.pointTotal += answer_exist.flagPoint
                user.save(update_fields=['gamePoint', "pointTotal"])

                return redirect("flag")
            else:
                if len(list(user.userListeElemani.all())) > 1:

                    messages.add_message(request, messages.WARNING, f"Wrong! Correct answer is: {answer_exist.name}")

                user.userListeElemani.remove(last)
                user.gamePoint = user.gamePoint - (5 - answer_exist.flagPoint)
                user.pointTotal = user.pointTotal - (5 - answer_exist.flagPoint)
                user.save(update_fields=['gamePoint', "pointTotal"])

                return redirect("flag")
        
        
    else:    
        user = request.user
        degerler_listesi = list(user.userListeElemani.all())
        degerler = [eleman.userListeElemaniMany for eleman in degerler_listesi]
        
        if degerler_listesi == []:
            if request.user.firstStep == False:
                request.user.firstStep = True
                request.user.save()
                for i in range(1, 201):
                    user.userListeElemani.add(i)
                return redirect("flag")
                
            Records.objects.create(
                user=request.user,
                score = user.gamePoint)
            
            for i in range(1, 201):
                user.userListeElemani.add(i)

            
            messages.add_message(request, messages.WARNING, f"Your Score: {user.gamePoint}")

            user.gamePoint = 0
            user.userLastNumber = None
            user.save()
            return redirect("records")
        
        liste = ListeElemaniUser.objects.all()
        allList = [obje.userListeElemaniMany for obje in liste]

        
        last = user.userLastNumber
        lastFlag = FlagModel.objects.filter(_id=last).first()
        
        randomId = random.choice(degerler)
        singleFlag = FlagModel.objects.get(id=randomId)
        singleFlag1 = FlagModel.objects.get(id=randomId)
        
        user.userLastNumber = randomId
        user.save()

        score = user.gamePoint
        
        
        randomId1 = randomId
        randomId2 = randomId
        
        while randomId == randomId1 or randomId == randomId2 or randomId1 == randomId2:
            randomId1 = random.choice(allList)
            randomId2 = random.choice(allList)
      
        randomFlag1 = FlagModel.objects.filter(id=randomId1).first()        
        randomFlag2 = FlagModel.objects.filter(id=randomId2).first()        
        
        randomList = [randomFlag2, randomFlag1, singleFlag1]
        random.shuffle(randomList)
        a = randomList[0]
        b = randomList[1]
        c = randomList[2]
        
        remain = len(degerler)
        allObj = len(allList)
        
        context = {
            "flag": singleFlag,
            "randomFlag": a,
            "randomFlag1": b,
            "randomFlag2": c,
            "lastFlag": lastFlag,
            "gameScore": score,
            "remain": remain,
            "allObj": allObj,
        }
        return render(request, "flagapp/flag.html", context)
    

            
def records(request):
    records = Records.objects.all().order_by("-score")[:5]
    totalRecords = Records1.objects.all().order_by("-score")[:5]
    realTotal = CustomUser.objects.all().order_by("-pointTotal")[:5]
    context={
        "records": records,
        "total": totalRecords,
        "realTotal": realTotal
    }

    return render(request,"flagapp/records.html",context)
          
    
