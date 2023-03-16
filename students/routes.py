from flask import Blueprint
from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
from db.queris import *
from pprint import pprint
from datetime import datetime


from students import forms


students = Blueprint('students', __name__, template_folder='templates')

@students.route('/get_students', methods=['GET', 'POST'])
def get_students():
    create_form = forms.UserForm(request.form)
    students = search_all_students()
    pprint(students)

    if request.method == 'POST':
        id = create_form.id.data 
        if not id:  # Si el formulario está vacío, devuelve todos los profesores
            students = search_all_students()
        else:
            students = search_students_(id)

    return render_template("students.html", form=create_form, students=students)


@students.route('/insert_students', methods=['GET', 'POST'])
def insert_students():
    create_form = forms.UserForm(request.form)
    name = create_form.name.data
    surname = create_form.surname.data
    email = create_form.email.data
    insert_students = None
    if request.method=='POST':
        insert_student(name, surname, email, datetime.now())
    return render_template("insert_students.html", form=create_form, insert_students=insert_students)


@students.route('/update_students', methods=['GET', 'POST'])
def update_students():
    
    create_form = forms.UserForm(request.form)
    update_students = None
    if request.method=='GET':
        id=int(request.args.get('id'))
        student=search_students_(id)
        create_form.id.data = id
        create_form.name.data = student[0]['name']
        create_form.surname.data =student[0]['surname']
        create_form.email.data = student[0]['email']
        
    if request.method=='POST':
        id = create_form.id.data 
        name = create_form.name.data
        surname = create_form.surname.data
        email = create_form.email.data
        update_student(id, name, surname, email)
    return render_template("update_students.html", form=create_form, update_students=update_students)

@students.route('/delete_students', methods=['GET', 'POST'])
def delete_students():
    
    create_form = forms.UserForm(request.form)
    delete_students = None
    if request.method=='GET':
        id=int(request.args.get('id'))
        student=search_students_(id)
        create_form.id.data = id
        create_form.name.data = student[0]['name']
        create_form.surname.data =student[0]['surname']
        create_form.email.data = student[0]['email']
        
    if request.method=='POST':
        id = create_form.id.data 
        delete_student(id)
    return render_template("delete_students.html", form=create_form, update_students=delete_students)



