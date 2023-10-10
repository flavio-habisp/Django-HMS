from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from accounts.models import *
from room.models import *
from hotel.models import *
from hotel.templatetags.custom_filter import *

from django.http import JsonResponse
from datetime import date

def ajax_view(request):
    param = request.GET.get('param') 
    data = {'message': 'Out 01 to Out 07'}
    return JsonResponse(data)


@login_required(login_url='login')
def week(request, day = ''):
    if day == '' :
        day = (date.today() - timedelta(days=date.today().weekday()+1)
        ).strftime('%Y-%m-%d')
    current_path = request.path.lower()
    date_obj = datetime.strptime(day, '%Y-%m-%d')
    if 'previous' in current_path :  
        date_obj = date_obj + timedelta(days=-7)
    if 'next' in current_path:
        date_obj = date_obj + timedelta(days=7)      

    role = str(request.user.groups.all()[0])
    path = role + "/"
    week_schedules =  date_obj.strftime('%b %d') + ' to ' + (date_obj + timedelta(days=int(6))).strftime('%b %d')
    schedules = [{'date':date_obj.strftime('%Y-%m-%d'),'hotel_id':'02', 'place': 'SERV. RMS. HGI', 'totalpercent' : 95.7, 'sun' : 81, 'mon' : 65, 'tue' : 57, 'wed' : 122, 'thu' : 133, 'fri' : 127, 'sat' : 70},
        {'date':date_obj.strftime('%Y-%m-%d'),'hotel_id':'03','place': 'SERV. RMS. HWS', 'totalpercent' : 89.8,'sun' : 87,  'mon' : 69, 'tue' : 88, 'wed' : 102, 'thu' :	103, 'fri' : 90, 'sat' : 89}]
    room_services = RoomServices.objects.all()
    context = {
        "role": role,
        "room_services": room_services,
        "schedules" : schedules,
        "week_schedules" : week_schedules,
        "date" : date_obj.strftime('%Y-%m-%d')
    }
    return render(request, path + "week.html", context)

    
@login_required(login_url='login')
def attendance(request, day = ''):
    if day == '' :
        day = (date.today() - timedelta(days=date.today().weekday()+1)
        ).strftime('%Y-%m-%d')
    current_path = request.path.lower()
    date_obj = datetime.strptime(day, '%Y-%m-%d')
    if 'previous' in current_path :  
        date_obj = date_obj + timedelta(days=-7)
    if 'next' in current_path:
        date_obj = date_obj + timedelta(days=7)      

    role = str(request.user.groups.all()[0])
    path = role + "/"
    week_schedules =  date_obj.strftime('%b %d') + ' to ' + (date_obj + timedelta(days=int(6))).strftime('%b %d')
    schedules =[ 
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 1, 'name': 'SHAMELY', 'position': 'FULL TIME', 'role': 'HOUSEKEEPERS', 'days': 4, 'sun': 'N/A', 'mon': 'N/A', 'tue': '8:00', 'wed': '8:00', 'thu': '8:00', 'fri': '8:00', 'sat': 'CF' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 2, 'name': 'ANNE JUDITH', 'position': 'FULL TIME', 'role': 'HOUSEKEEPERS', 'days': 0, 'sun': 'MAT', 'mon': 'MAT', 'tue': 'MAT', 'wed': 'MAT', 'thu': 'MAT', 'fri': 'MAT', 'sat': 'MAT' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 3, 'name': 'MARCIA', 'position': 'FULL TIME', 'role': 'HOUSEKEEPERS', 'days': 4, 'sun': '8:00', 'mon': '7:00', 'tue': '7:00', 'wed': '7:00', 'thu': 'N/A', 'fri': 'N/A', 'sat': 'N/A' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 4, 'name': 'COREEN', 'position': 'FULL TIME', 'role': 'HOUSEKEEPERS', 'days': 3, 'sun': 'N/A', 'mon': 'N/A', 'tue': '8:00', 'wed': '8:00', 'thu': '8:00', 'fri': 'N/A', 'sat': 'N/A' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 5, 'name': 'NAZARII', 'position': 'FULL TIME', 'role': 'HOUSEKEEPERS', 'days': 5, 'sun': '9:00', 'mon': '8:00', 'tue': '8:00', 'wed': '8:00', 'thu': '8:00', 'fri': 'N/A', 'sat': 'N/A' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 6, 'name': 'VITA PAVLOVYCH', 'position': 'FULL TIME', 'role': 'HOUSEKEEPERS', 'days': 5, 'sun': 'N/A', 'mon': '8:00', 'tue': '8:00', 'wed': '8:00', 'thu': 'N/A', 'fri': '8:00', 'sat': '9:00' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 7, 'name': 'NADIIA SRYPNYK', 'position': 'FULL TIME', 'role': 'HOUSEKEEPERS', 'days': 0, 'sun': 'SUP', 'mon': 'SUP', 'tue': 'SUP', 'wed': 'CF', 'thu': 'N/A', 'fri': 'N/A', 'sat': 'SUP' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 8, 'name': 'DIANA RAMIREZ', 'position': 'FULL TIME', 'role': 'HOUSEKEEPERS', 'days': 5, 'sun': '10:00', 'mon': 'N/A', 'tue': 'N/A', 'wed': '8:00', 'thu': '10:00', 'fri': '8:00', 'sat': '9:00' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 10, 'name': 'OLENA', 'position': 'FULL TIME', 'role': 'HOUSEKEEPERS', 'days': 5, 'sun': 'N/A', 'mon': '8:00', 'tue': '8:00', 'wed': '8:00', 'thu': 'N/A', 'fri': '8:00', 'sat': '9:00' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 11, 'name': 'EKATERYNA', 'position': 'FULL TIME', 'role': 'HOUSEKEEPERS', 'days': 5, 'sun': '9:00', 'mon': '8:00', 'tue': '8:00', 'wed': 'N/A', 'thu': 'N/A', 'fri': '8:00', 'sat': '9:00' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 12, 'name': 'RUBENS', 'position': 'FULL TIME', 'role': 'HOUSEKEEPERS', 'days': 5, 'sun': '9:00', 'mon': '8:00', 'tue': 'N/A', 'wed': '8:00', 'thu': '8:00', 'fri': '8:00', 'sat': 'N/A' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 13, 'name': 'NATALIIA', 'position': 'FULL TIME', 'role': 'HOUSEKEEPERS', 'days': 5, 'sun': 'N/A', 'mon': '8:00', 'tue': '8:00', 'wed': '8:00', 'thu': 'N/A', 'fri': '8:00', 'sat': '9:00' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 14, 'name': 'NADIIA', 'position': 'FULL TIME', 'role': 'HOUSEKEEPERS', 'days': 5, 'sun': '9:00', 'mon': '8:00', 'tue': 'N/A', 'wed': 'N/A', 'thu': '8:00', 'fri': '8:00', 'sat': '9:00' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 15, 'name': 'LAMIA', 'position': 'FULL TIME', 'role': 'HOUSEKEEPERS', 'days': 5, 'sun': 'N/A', 'mon': '8:00', 'tue': '8:00', 'wed': '8:00', 'thu': '8:00', 'fri': '8:00', 'sat': 'N/A' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 16, 'name': 'IVAN', 'position': 'FULL TIME', 'role': 'HOUSEKEEPERS', 'days': 5, 'sun': '9:00', 'mon': 'N/A', 'tue': 'N/A', 'wed': '8:00', 'thu': '8:00', 'fri': '8:00', 'sat': '9:00' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 17, 'name': 'ANASTASIA', 'position': 'FULL TIME', 'role': 'HOUSEKEEPERS', 'days': 5, 'sun': '9:00', 'mon': 'N/A', 'tue': 'N/A', 'wed': '8:00', 'thu': '8:00', 'fri': '8:00', 'sat': '9:00' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 18, 'name': 'SABRINA HADDOUCHE', 'position': 'FULL TIME', 'role': 'HOUSEKEEPERS', 'days': 5, 'sun': 'N/A', 'mon': '8:00', 'tue': '8:00', 'wed': '8:00', 'thu': '8:00', 'fri': '8:00', 'sat': 'N/A' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 19, 'name': 'YANET MARAVILLA', 'position': 'FULL TIME', 'role': 'HOUSEKEEPERS', 'days': 4, 'sun': 'N/A', 'mon': '8:00', 'tue': '8:00', 'wed': '8:00', 'thu': '8:00', 'fri': 'N/A', 'sat': 'N/A' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 20, 'name': 'NATALIIA TESLAVA', 'position': 'FULL TIME', 'role': 'HOUSEKEEPERS', 'days': 5, 'sun': '9:00', 'mon': '8:00', 'tue': '8:00', 'wed': 'N/A', 'thu': '8:00', 'fri': 'N/A', 'sat': '9:00' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 21, 'name': 'LEIDY', 'position': 'FULL TIME', 'role': 'HOUSEKEEPERS', 'days': 5, 'sun': '9:00', 'mon': '8:00', 'tue': '8:00', 'wed': 'N/A', 'thu': '8:00', 'fri': 'N/A', 'sat': '9:00' },

 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 21, 'name': 'TETIANA MALINOVOSKA', 'position': 'PART TIME', 'role': 'HOUSEKEEPERS', 'days': 2, 'sun': '9:00', 'mon': 'N/A', 'tue': 'N/A', 'wed': 'N/A', 'thu': 'N/A', 'fri': 'N/A', 'sat': '9:00' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 22, 'name': 'JHOSELINE', 'position': 'PART TIME', 'role': 'HOUSEKEEPERS', 'days': 2, 'sun': '9:00', 'mon': 'N/A', 'tue': 'N/A', 'wed': 'N/A', 'thu': 'N/A', 'fri': 'N/A', 'sat': '9:00' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 23, 'name': 'CLAUDIA', 'position': 'PART TIME', 'role': 'HOUSEKEEPERS', 'days': 3, 'sun': 'N/A', 'mon': '10:00', 'tue': '8:00', 'wed': 'N/A', 'thu': '8:00', 'fri': 'N/A', 'sat': 'N/A' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 24, 'name': 'TATIANA BARRETO', 'position': 'PART TIME', 'role': 'HOUSEKEEPERS', 'days': 1, 'sun': 'N/A', 'mon': 'N/A', 'tue': 'N/A', 'wed': 'N/A', 'thu': 'N/A', 'fri': 'N/A', 'sat': '12:00' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 25, 'name': 'PILAR', 'position': 'PART TIME', 'role': 'HOUSEKEEPERS', 'days': 0, 'sun': 'N/A', 'mon': 'N/A', 'tue': 'N/A', 'wed': 'N/A', 'thu': 'N/A', 'fri': 'N/A', 'sat': 'N/A' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 26, 'name': 'FATIMA', 'position': 'PART TIME', 'role': 'HOUSEKEEPERS', 'days': 1, 'sun': '11:30', 'mon': 'N/A', 'tue': 'N/A', 'wed': 'N/A', 'thu': 'N/A', 'fri': 'N/A', 'sat': 'N/A' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 28, 'name': 'NICOL', 'position': 'PART TIME', 'role': 'HOUSEKEEPERS', 'days': 2, 'sun': '9:00', 'mon': 'N/A', 'tue': 'N/A', 'wed': 'N/A', 'thu': 'N/A', 'fri': 'N/A', 'sat': '9:00' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 29, 'name': 'BIANCA', 'position': 'PART TIME', 'role': 'HOUSEKEEPERS', 'days': 3, 'sun': 'N/A', 'mon': '8:00', 'tue': 'N/A', 'wed': 'N/A', 'thu': '8:00', 'fri': '8:00', 'sat': 'N/A' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 30, 'name': 'MARCELI', 'position': 'PART TIME', 'role': 'HOUSEKEEPERS', 'days': '', 'sun': '9:00', 'mon': 'N/A', 'tue': 'N/A', 'wed': 'N/A', 'thu': 'N/A', 'fri': 'SUP', 'sat': 'SUP' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 1, 'name': 'LUISITO', 'position': 'PART TIME', 'role': 'HOUSEMAN', 'days': 4, 'sun': 'N/A', 'mon': 'CF', 'tue': '6:45', 'wed': '6:45', 'thu': '6:45', 'fri': '6:45', 'sat': 'N/A' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 2, 'name': 'JEAN PAUL', 'position': 'PART TIME', 'role': 'HOUSEMAN', 'days': 2, 'sun': '15:00', 'mon': 'N/A', 'tue': 'N/A', 'wed': 'N/A', 'thu': 'N/A', 'fri': 'N/A', 'sat': '15:00' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 3, 'name': 'KALUTA', 'position': 'PART TIME', 'role': 'HOUSEMAN', 'days': 4, 'sun': 'N/A', 'mon': '23:00', 'tue': '23:00', 'wed': '23:00', 'thu': '23:00', 'fri': 'N/A', 'sat': 'N/A' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 4, 'name': 'BRUNO', 'position': 'PART TIME', 'role': 'HOUSEMAN', 'days': 3, 'sun': '7:00', 'mon': '7:00', 'tue': 'N/A', 'wed': 'N/A', 'thu': 'N/A', 'fri': 'N/A', 'sat': '7:00' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 5, 'name': 'HUGO', 'position': 'PART TIME', 'role': 'HOUSEMAN', 'days': 3, 'sun': '7:00', 'mon': 'N/A', 'tue': 'N/A', 'wed': 'N/A', 'thu': 'N/A', 'fri': '7:00', 'sat': '7:00' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 6, 'name': 'MYROSLAV', 'position': 'PART TIME', 'role': 'HOUSEMAN', 'days': 5, 'sun': 'N/A', 'mon': '11:00', 'tue': '11:00', 'wed': '11:00', 'thu': '11:00', 'fri': '15:00', 'sat': 'N/A' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 8, 'name': 'GUILHERME', 'position': 'PART TIME', 'role': 'HOUSEMAN', 'days': 2, 'sun': '15:00', 'mon': 'N/A', 'tue': 'N/A', 'wed': 'N/A', 'thu': 'N/A', 'fri': 'N/A', 'sat': '15:00' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 9, 'name': 'VITALII', 'position': 'PART TIME', 'role': 'HOUSEMAN', 'days': 3, 'sun': '23:00', 'mon': 'N/A', 'tue': 'N/A', 'wed': 'N/A', 'thu': 'N/A', 'fri': '23:00', 'sat': '23:00' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 10, 'name': 'STANISLAV', 'position': 'PART TIME', 'role': 'HOUSEMAN', 'days': 5, 'sun': '7:00', 'mon': '15:00', 'tue': '15:00', 'wed': '15:00', 'thu': '15:00', 'fri': '15:00', 'sat': 'N/A' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 11, 'name': 'AKIN', 'position': 'PART TIME', 'role': 'HOUSEMAN', 'days': '', 'sun': '23:00', 'mon': '23:00', 'tue': 'N/A', 'wed': 'N/A', 'thu': 'N/A', 'fri': '23:00', 'sat': '23:00' },
 
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 1, 'name': 'THAYANNE', 'position': '', 'role': 'SUPERVISEURS', 'days': 5, 'sun': '7:30', 'mon': '6:30', 'tue': '6:30', 'wed': '6:30', 'thu': '6:30', 'fri': 'N/A', 'sat': 'N/A' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 2, 'name': 'ELIZA R', 'position': '', 'role': 'SUPERVISEURS', 'days': 4, 'sun': 'N/A', 'mon': 'N/A', 'tue': '10:00', 'wed': '10:00', 'thu': '10:00', 'fri': '9:00', 'sat': 'CF' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 3, 'name': 'TARAS', 'position': '', 'role': 'SUPERVISEURS', 'days': 5, 'sun': '10:00', 'mon': '10:00', 'tue': 'N/A', 'wed': 'N/A', 'thu': '9:30', 'fri': '6:30', 'sat': '7:30' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 4, 'name': 'VIVIAN', 'position': '', 'role': 'SUPERVISEURS', 'days': 0, 'sun': 'N/A', 'mon': 'N/A', 'tue': 'N/A', 'wed': 'N/A', 'thu': 'N/A', 'fri': 'N/A', 'sat': 'N/A' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 6, 'name': 'NADIIA S', 'position': '', 'role': 'SUPERVISEURS', 'days': 4, 'sun': '10:00', 'mon': '9:30', 'tue': '10:00', 'wed': 'CF', 'thu': 'N/A', 'fri': 'N/A', 'sat': '10:00' },
 {'date':date_obj.strftime('%Y-%m-%d'),'schedules_id': 5, 'name': 'MARCELI DELBONI', 'position': '', 'role': 'SUPERVISEURS', 'days': 2, 'sun': 'housekeeper', 'mon': 'N/A', 'tue': 'N/A', 'wed': 'N/A', 'thu': 'N/A', 'fri': '10:00', 'sat': '10:00' },
 ]
    room_services = RoomServices.objects.all()
    context = {
        "role": role,
        "room_services": room_services,
        "schedules" : schedules,
        "week_schedules" : week_schedules,
        "date" : date_obj.strftime('%Y-%m-%d')
    }
    return render(request, path + "attendance.html", context)



    SUPERVISEURS
    HOUSEKEEPERS
    HOUSEMAN 

