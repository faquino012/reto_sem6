from re import A
from config.connection import Connection


class Alumno:
    def __init__(self):
        pass  
        # self.create_table()

    def create_table(self):
        try:
            conn = Connection('alumno')
            query = '''
                CREATE TABLE IF NOT EXISTS public.alumno
                (
                    id integer NOT NULL,
                    documento character varying(20) NOT NULL,
                    nombre character varying(100) NOT NULL,
                    fecha_de_nacimiento date NOT NULL,
                    correo character varying(50) NOT NULL,
                    estado boolean NOT NULL,
                    genero character varying(1) NOT NULL,
                    PRIMARY KEY (id)
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
    def alumno_datos(self, records):
        for record in records:
                print(f'ID: {record[0]}')
                print(f'Documento: {record[1]}')
                print(f'Nombre: {record[2]}')
                print(f'Fecha de nacimiento: {record[3]}')
                print(f'Correo: {record[4]}')
                if record[6]=="V":
                    print(f'Genero: Varon')
                elif record[6]=="M":
                    print("Genero: Mujer")    
                if str(record[5])=="True":
                    print(f'Estado: Activo')
                elif str(record[5])=="False":
                    print(f'Estado: Inactivo')
    def all_alumnos(self):

        try:
            conn = Connection('alumno')
            records = conn.select([])

            for record in records:
                print(f'ID: {record[0]}')
                print(f'Documento: {record[1]}')
                print(f'Nombre: {record[2]}')
                print(f'Fecha de nacimiento: {record[3]}')
                print(f'Correo: {record[4]}')
                if record[6]=="V":
                    print(f'Genero: Varon')
                elif record[6]=="M":
                    print("Genero: Mujer")    
                if str(record[5])=="True":
                    print(f'Estado: Activo')
                elif str(record[5])=="False":
                    print(f'Estado: Inactivo')
                print('=====================')
        except Exception as e:
            print(e)
    def agregar_datos_alumno(self):
        try:
            print("Ingrese el documento del alumno")
            documento=input("> ")
            print("Ingrese el nombre del alumno")
            nombre=input("> ")
            print("Ingrese la fecha de nacimiento del alumno (dia/mes/año)")
            fecha_de_nacimiento=input("> ")
            print("Ingrese el correo del alumno")
            correo=input("> ")
            while True:
                print("Ingrese el genero del alumno (V = Varón / M = Mujer)")
                genero=input("> ")
                if genero == "V" or genero =="M":
                    break
                else:
                    print("Error, ingrese una opción válida")
            while True:
                print("Ingrese el estado del alumno (A = Activo / I = Inactivo)")
                estado=input("> ")
                if estado =="A":
                    estado=True
                    break
                elif estado=="I":
                    estado=False
                    break
                else:
                    print("Error, escriba una opción válida")
            self.insert_alumno(documento,nombre, fecha_de_nacimiento,correo, estado, genero)
        except Exception as e:
            print(e)
    def insert_alumno(self, documento, nombre, fecha_de_nacimiento,correo,estado, genero):
        try:
            conn = Connection('alumno')
            conn.insert({
                'documento': documento,
                'nombre': nombre,
                'fecha_de_nacimiento': fecha_de_nacimiento,
                'correo':correo,
                'estado':estado,
                'genero':genero
            })

        except Exception as e:
            print(e)
    def delete_alumno(self):
        conn = Connection('alumno')
        while True:
            
            records=conn.select(['id'])
            print("Ingrese el id del alumno que quiere eliminar")
            id_alumno=input("> ")
            validacion=False
            for record in records:
                for recor in record:
                    if str(recor)==id_alumno:
                        validacion=True
            if validacion==True:
               break
            else:
                print("Error, id no existente")

        records=conn.select_id(id_alumno)
        print("datos actuales del alumno")
        self.alumno_datos(records)
        print("¿Esta seguro que quiere eliminar los datos de este alumno? (1= si / 2 = no)")
        validacion=input("> ")
        while True:
            if validacion=="1":
               conn.delete_id(id_alumno)
               print("Se eliminaron los datos del alumno")
               break
            elif validacion=="2":
                print("Volviendo...")
                break
            else :
                print("ingrese una opcion valida") 

    def new_method(self, conn, id_alumno):
        conn.delete_id(id_alumno)   

    def update_alumno(self):
        try:
           
            while True:
                conn = Connection('alumno')
                records=conn.select(['id'])
                print("Ingrese el id del alumno")
                id_alumno=input("> ")
                validacion=False
                for record in records:
                    for recor in record:
                        if str(recor)==id_alumno:
                            validacion=True
                if validacion==True:
                   break
                else:
                    print("Error, id no existente")

            records=conn.select_id(id_alumno)
            print("datos actuales del alumno")
            self.alumno_datos(records)
            print("¿Que dato deseas cambiar?")
            v2=False
            while True:    

                print("1 = documento")
                print("2 = nombre")
                print("3 = fecha de nacimiento")
                print("4 = correo")
                print("5 = genero")
                print("6 = estado")
                if v2== False:
                    print("7 = Salir")
                else:
                    print("7 = No")
                dato_cambio=input("> ")

                if dato_cambio=="1":
                    print("Ingrese el nuevo documento del alumno")
                    documento=input("> ")
                    conn.update({'id': id_alumno,}, {'documento':str(documento)})
                    v=True
                elif dato_cambio=="2":
                    print("Ingrese el nuevo nombre del alumno")
                    nombre=input("> ")
                    conn.update({'id': id_alumno,}, {'nombre':str(nombre)})
                    v=True
                elif dato_cambio=="3":
                    print("Ingrese la nueva fecha de nacimiento del alumno (dia/mes/año)")
                    fecha_de_nacimiento=input("> ")
                    conn.update({'id': id_alumno,}, {'fecha_de_nacimiento':str(fecha_de_nacimiento)})
                    v=True
                elif dato_cambio=="4":
                    print("Ingrese el correo del alumno")
                    correo=input("> ")
                    conn.update({'id': id_alumno,}, {'correo':str(correo)})
                    v=True
                elif dato_cambio=="5":
                    while True:
                        print("Ingrese el genero del alumno (V = Varón / M = Mujer)")
                        genero=input("> ")
                        if genero == "V" or genero =="M":
                            break
                        else:
                            print("Error, ingrese una opción válida")
                    conn.update({'id': id_alumno,}, {'genero':str(genero)})
                    v=True
                elif dato_cambio=="6":
                    while True:
                       print("Ingrese el nuevo estado del alumno (A = Activo / I = Inactivo)")
                       estado=input("> ")
                       if estado =="A":
                           estado=True
                           break
                       elif estado=="I":
                           estado=False
                           break
                       else:
                           print("Error, escriba una opción válida")
                    conn.update({'id': id_alumno,}, {'estado':str(estado)})
                    v=True
                elif dato_cambio=="7":
                    print("Volviendo...")
                    break
                else:
                    print("Error, escriba una opcion valida")
                
                if v==True:
                    print("Nuevos datos del alumno")
                    records2=conn.select_id(id_alumno)
                    self.alumno_datos(records2)
                    print("¿Desea cambiar otro dato?")
                    v2=True
                    v=False


        except Exception as e:
            print(e)
            
    def crud_alumno(self):
        try:
            while True:
                print("¿Que desea hacer?")
                print("1: Ver alumnos")
                print("2: Agregar alumno")
                print("3: Actualizar datos de alumno")
                print("4: Eliminar alumno")
                print("5: volver a menu")
                opcion=input("> ")
                if opcion=="1":
                    self.all_alumnos()
                elif opcion=="2":
                    self.agregar_datos_alumno()
                elif opcion=="3":
                    self.update_alumno()
                elif opcion=="4":
                    self.delete_alumno()
                elif opcion=="5":
                    break
                else:
                    print("Error, ingrese una opcion válida")
        except Exception as e:
            print (e)


prueba=Alumno()
prueba.crud_alumno()

