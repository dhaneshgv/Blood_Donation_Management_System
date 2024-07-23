from DB.creation.db_creation import db_connection
from UI.popup import info_popup


def insert_admin(admin_data):

    connection = db_connection()

    cursor = connection.cursor()
    cursor.execute("USE autogenerated_blood_donation;")

    # admin_data = [
    #     ('dhanesh',1234, 'Pbks2023Cup'),
    #     ('karthi',5678, 'K@rth1rOcks')
    # ]
    

    admin_data_insert_query = """
        INSERT INTO admin (admin_name, admin_id, password)
        VALUES (           %s        ,%s       ,%s);
    """

    cursor.execute(admin_data_insert_query,admin_data)
    connection.commit()

    info_popup("Admin data inserted successfully!")

    cursor.close()
    connection.close()


# sample insertion queries

# INSERT INTO admin (admin_name, admin_id, password)
#         VALUES ("admin1",1,"password1");
# INSERT INTO admin (admin_name, admin_id, password)
#         VALUES ("admin2",2,"password2");
# INSERT INTO admin (admin_name, admin_id, password)
#         VALUES ("admin3",3,"password3");
# INSERT INTO admin (admin_name, admin_id, password)
#         VALUES ("admin4",4,"password4");
# INSERT INTO admin (admin_name, admin_id, password)
#         VALUES ("admin5",5,"password5");