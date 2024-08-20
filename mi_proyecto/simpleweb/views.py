from django.shortcuts import render,redirect

from django.http import HttpResponse, HttpRequest
# Create your views here.
import mysql.connector as mcdb
conn = mcdb.connect(host="db", user="root", passwd="12345678", database='ejemplo_db',port=3306)
print('Successfully connected to database')
cur = conn.cursor()

def home(request):
    return  render(request,'home.html')


def categorylisting(request):
    cur.execute("SELECT * FROM `tb_category`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'view.html', {'categories': data})   


def categorycreate(request):
    return render(request, 'add.html')   


def categoryaddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        catname = request.POST['txt1']
        cur.execute("INSERT INTO `tb_category`(`category_name`,`is_deleted`) VALUES ('{}',{})".format(catname,12))
        conn.commit()
        return redirect(categorycreate) 
    else:
        return redirect(categorycreate)


def categorydelete(request,id):
     
    #id = request.GET['id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("delete from `tb_category` where `category_id` = {}".format(id))
    conn.commit()
    return redirect(categorylisting) 


def categoryedit(request,id):
     
    print(id)
    cur.execute("select * from `tb_category` where `category_id` = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request, 'edit.html', {'categories': data})   


def categoryupdate(request):
    if request.method == 'POST':
        print(request.POST)
        catid = request.POST['txt1']
        catname = request.POST['txt2']
        cur.execute("update `tb_category` set `category_name` ='{}' where `category_id`='{}'".format(catname,catid))
        conn.commit()
        return redirect(categorylisting) 
    else:
        return redirect(categorylisting)
    

##MIS CRUDS
def alumnos_listing(request):
    cur.execute("SELECT * FROM Alumnos")
    data = cur.fetchall()
    print(list(data))
    return render(request, 'view_alumnos.html', {'alumnos': data})   

def alumnos_create(request):
    return render(request, 'add.html')   


def alumnos_addprocess(request):
    if request.method == 'POST':
        print(request.POST)
        nombre=request.POST.get('nombre')
        apellido=request.POST.get('apellido')
        dni=request.POST.get('dni')
        telefono=request.POST.get('telefono')
        cur.execute("INSERT INTO Alumnos (nombre, apellido, dni, telefono) VALUES (%s,%s,%s,%s)",(nombre,apellido,dni,telefono))
        conn.commit()
        return redirect(alumnos_create) 
    else:
        return redirect(alumnos_create)
    
def alumnos_delete(request, id):
     
    print(id)
    cur.execute("delete from Alumnos where id_alumno = %s", (id,))
    conn.commit()
    return redirect(alumnos_listing)

def alumnos_edit(request, id):
     
    print(id)
    cur.execute("select * from Alumnos where id_alumno = %s", (id,))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request, 'edit_alumnos.html', {'alumnos': data})   


def alumnos_update(request):
    if request.method == 'POST':
        print(request.POST)
        catid = request.POST['txt1']
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni= request.POST.get('dni')
        telefono=request.POST.get('telefono')
        cur.execute("update Alumnos set nombre = %s, apellido = %s, dni =%s , telefono =%s where id_alumno=%s", (nombre,apellido,dni,telefono,catid))
        conn.commit()
        return redirect(alumnos_listing) 
    else:
        return redirect(alumnos_listing)