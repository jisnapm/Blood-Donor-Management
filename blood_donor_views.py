from datetime import datetime

import mysql.connector

class BloodDonorManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user= 'root',
            password= 'Jis12#na',
            database= 'blood_db'
        )
        print("Connected Successfully!")

    def get_object(self, id=None):
        try:
            self.cursor = self.connection.cursor()
            q = 'select * from donor where id = %s'
            value = (id, )
            self.cursor.execute(q, value)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            return None

    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()
            q = 'insert into donor(name, blood_group, phone, city, last_donation) values(%s, %s, %s, %s, %s)'
            values = [v for v in kwargs.values()]
            self.cursor.execute(q, values)
            self.connection.commit()
            # print("Donor Added Successfully!")
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.cursor = self.connection.cursor()
            q = 'select * from donor'
            self.cursor.execute(q)
            records = self.cursor.fetchall()
            # for data in records:
            #     print(data)
            return records
        except Exception as e:
            print(e)

    def retrieve(self, id= None):
        try:
            record = self.get_object(id)
            if record != None:
                print("- - - DONOR DETAILS - - -")
                print(record)
            else:
                print("Donor Not Found!")
        except Exception as e:
            print(e)

    def delete(self, id= None):
        try:
            record = self.get_object(id)
            if record != None:
                q = 'delete from donor where id = %s'
                value = (id, )
                self.cursor.execute(q, value)
                self.connection.commit()
                print("Donor Deleted!")
            else:
                print("Donor Not Found!")
        except Exception as e:
            print(e)

    def put(self, id= None, **kwargs):
        try:
            record = self.get_object(id)
            if record != None:
                self.cursor = self.connection.cursor()
                placeholder = ''
                # for k,v in kwargs.items():
                #     placeholder += k + "='" + v + "', "
                # placeholder = placeholder.rstrip(", ")
                # q = f"update donor set {placeholder} where id = %s"
                # values = (id, )
                for k in kwargs.keys():
                    placeholder += k + "=%s, "
                placeholder = placeholder.rstrip(", ")
                q = f"update donor set {placeholder} where id = %s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(q, values)
                self.connection.commit()
                print("Donor Details Updated!")
            else:
                print("Donor Not Found!")
        except Exception as e:
            print(e)


# donor_instance = BloodDonorManager()
# # donor_instance.post(name= "Sai", blood_group= "A+", phone="8562641050", city="Calicut", last_donation= datetime.today())
# donor_instance.get()
# # donor_instance.retrieve(5)
# donor_instance.delete(9)
# donor_instance.put(5, name= "Jismi")
# donor_instance.get()