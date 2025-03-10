from DB.creation.db_creation import db_connection
from UI.popup import info_popup


def insert_donor(donor_data):

  connection = db_connection()

  cursor = connection.cursor()
  cursor.execute("USE autogenerated_blood_donation;")

  # for i in range(1,10):
  #   donor_data = [
  #     (i, 'Male', 'John', 'Doe', 1990,1,1,'A+', False, False, '123 Main St', 'Mumbai', 'Mumbai Suburban', 'Maharashtra', 'India', '+91', 'P@ssw0rd', 'Doe', 'Jane', 'Jon Cornor', 9876543210, 9876543210, 12345)
  #   ]

  print(donor_data)
  
  # donor_data=('123456789098', 'Male', 'fname', 'lastname', 11, 3, 2345, 'A+', True, True, 'street', 'city', 'district', 'state', 'country', '+91', '1234567', 'fname', 'mother', 'gname', 1234567890, 987654321, 1234)

  qonor_data_insert_query = """
  INSERT INTO donor (aadhaar_id, gender, first_name, last_name, dob , mob, yob, blood_type, pregnancy_status, HIV, street, city, district, state, country, country_code, password, father_name, mother_name, gaurdian_name, ph1 , ph2 , hid) 
  VALUES (           %s        , %s    , %s        , %s       , %s  , %s , %s , %s        , %s              , %s , %s    , %s  , %s      , %s   , %s     , %s          , %s      , %s         , %s         , %s           , %s  , %s , %s);
  """

  cursor.execute(qonor_data_insert_query,donor_data)

  connection.commit()


  info_popup("Donor data inserted successfully!")

  # Close the cursor and the connection
  cursor.close()
  connection.close()
