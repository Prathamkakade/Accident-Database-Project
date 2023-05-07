#!/usr/bin/env python
# coding: utf-8

# # [BONUS TASK]
# ## Step- 11
# ## UI created 

# In[9]:


#pip install psycopg2-binary


# In[1]:


from tkinter import messagebox


# In[2]:


import psycopg2
from tkinter import *

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="AccidentsDB",
    user="postgres",
    password="3016"
)


# In[3]:


# Open a cursor to perform database operations
cur = conn.cursor()

# Execute the SQL command to retrieve a list of tables
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE'")
#cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'Accidents')");

# Fetch all the rows in a list of lists
table_list = cur.fetchall()

# Print the list of tables
for table in table_list:
    print(table[0])


# In[4]:


print(cur)


# In[5]:


#conn = psycopg2.connect(database="Accidents", user="AccidentsDB", password="3016", host="localhost", port="5432")


# ## INSERT, DELETE, RETRIEVE

# In[8]:


def insert_data():
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
    host="localhost",
    database="AccidentsDB",
    user="postgres",
    password="3016"
    )
    # Create a cursor
    cur = conn.cursor()
    # Get the values from the input fields
    AccidentID = AccidentID_input.get()
    Severity = Severity_input.get()
    Start_Time = Start_Time_input.get()
    End_Time = End_Time_input.get()
    Distance = Distance_input.get()
    Description = Description_input.get()
    Start_Lat = Start_Lat_input.get()
    Start_Lng = Start_Lng_input.get()
    End_Lat = End_Lat_input.get()
    End_Lng = End_Lng_input.get()
    WeatherID = WeatherID_input.get()
    StartID = StartID_input.get()
    EndID = EndID_input.get()
    Start_Lat = Start_Lat_input.get()
    Start_Lng = Start_Lng_input.get()
    End_Lat = End_Lat_input.get()
    End_Lng = End_Lng_input.get()
    print(StartID)
    if StartID=="" and EndID=="":
        try:
            print("empty")
            # Execute the insert query
            cur.execute('INSERT INTO public."Accident"("AccidentID", "Severity", "Start_Time", "End_Time", "Distance", "Description")VALUES (%s, %s, %s, %s, %s, %s)', (AccidentID, Severity, Start_Time, End_Time, Distance, Description))
            conn.commit()
            messagebox.showinfo("Inserted","Done")
            print("Inserted")
        except Exception as e:
            print("Error:", e)
            messagebox.showinfo("Error",e)
            conn.rollback()
    elif EndID=="": 
        try:
            cur.execute('INSERT INTO public."StartLocation"("AccidentID", "Start_Lat", "Start_Lng", "StartID")VALUES (%s, %s, %s, %s)', (AccidentID, Start_Lat, Start_Lng,StartID))
            conn.commit()
            messagebox.showinfo("Inserted","Done")
            print("Inserted")
        except Exception as e:
            print("Error:", e)
            messagebox.showinfo("Error",e)
            conn.rollback()
    else: 
        try:
            cur.execute('INSERT INTO public."EndLocation"("AccidentID", "End_Lat", "End_Lng", "EndID")VALUES (%s, %s, %s, %s)', (AccidentID, End_Lat, End_Lng,EndID))
            conn.commit()
            messagebox.showinfo("Inserted","Done")
            print("Inserted")
        except Exception as e:
            print("Error:", e)
            messagebox.showinfo("Error",e)
            conn.rollback()
    # Close the cursor
    cur.close()


# Define a function to delete data from the database
def delete_data():
    # Create a cursor
    cur = conn.cursor()
    # Get the value from the input field
    AccidentID = AccidentID_input.get()
    WeatherID = WeatherID_input.get()
    StartID = StartID_input.get()
    EndID = EndID_input.get()
    if StartID=="" and EndID=="":
        try:
            # Execute the delete query
            before = cur.rowcount
            print(f"Deleting record with ID {AccidentID}...")
            cur.execute('DELETE FROM public."Accident" WHERE "AccidentID" = %s;', (AccidentID,))
            conn.commit()
            after = cur.rowcount
            if after==0:
                print("Record not found.")
                messagebox.showinfo("Error", "Not Found")
            else:
                print(f"Record with ID {AccidentID} deleted.")
                messagebox.showinfo("Deleted", "Done")

        except Exception as e:
            print("Error:", e)
            messagebox.showinfo("Error","Not Found")
    elif EndID=="":
        try:
            # Execute the delete query
            before = cur.rowcount
            print(f"Deleting record with ID {AccidentID}...")
            cur.execute('DELETE FROM public."StartLocation" WHERE "AccidentID" = %s AND "StartID"= %s;', (AccidentID,StartID,))
            conn.commit()
            after = cur.rowcount
            if after==0:
                print("Record not found.")
                messagebox.showinfo("Error", "Not Found")
            else:
                print(f"Record with ID {AccidentID} deleted.")
                messagebox.showinfo("Deleted", "Done")

        except Exception as e:
            print("Error:", e)
            messagebox.showinfo("Error","Not Found")
            
            conn.rollback()
        
    else:
        try:
            # Execute the delete query
            before = cur.rowcount
            print(f"Deleting record with ID {AccidentID}...")
            cur.execute('DELETE FROM public."EndLocation" WHERE "AccidentID" = %s AND "EndID"= %s;', (AccidentID,EndID,))
            conn.commit()
            after = cur.rowcount
            if after==0:
                print("Record not found.")
                messagebox.showinfo("Error", "Not Found")
            else:
                print(f"Record with ID {AccidentID} deleted.")
                messagebox.showinfo("Deleted", "Done")

        except Exception as e:
            print("Error:", e)
            messagebox.showinfo("Error","Not Found")
            
            conn.rollback()
    # Close the cursor
    cur.close()

def retrieve_data():
    # Create a cursor
    cur = conn.cursor()
    AccidentID = AccidentID_input.get()
    WeatherID = WeatherID_input.get()
    StartID = StartID_input.get()
    EndID = EndID_input.get()
    if StartID=="" and EndID=="":

        try:
            # Execute the select query
            cur.execute('SELECT * FROM public."Accident" WHERE "AccidentID" = %s;', (AccidentID,))
            rows = cur.fetchall()
            print(rows)
            formatted_data = ""
            for item in rows:
                formatted_data += f"ID: {item[0]}\n"
                formatted_data += f"Severity: {item[1]}\n"
                formatted_data += f"Start Time: {item[2]}\n"
                formatted_data += f"End Time: {item[3]}\n"
                formatted_data += f"Distance: {item[4]}\n"
                formatted_data += f"Description: {item[5]}\n"
                #formatted_data += f"Start Latitude: {item[4]}\n"
                #formatted_data += f"Start Longitude: {item[5]}\n"
                #formatted_data += f"End Latitude: {item[6]}\n"
                #formatted_data += f"End Longitude: {item[7]}\n"
            if rows==[]:
                messagebox.showinfo("Error","Not Found")
            else:
                messagebox.showinfo("Data",formatted_data)
        except Exception as e:
            print("Error:", e)
            messagebox.showinfo("Error","Not Found")
            
    elif EndID=="":
            try:
                # Execute the select query
                cur.execute('SELECT * FROM public."StartLocation" WHERE "AccidentID" = %s AND "StartID"= %s;', (AccidentID,StartID,))
                rows = cur.fetchall()
                print(rows)
                formatted_data = ""
                for item in rows:
                    formatted_data += f"ID: {item[0]}\n"
                    formatted_data += f"Start_Lat: {item[1]}\n"
                    formatted_data += f"Start_Lng: {item[2]}\n"
                    formatted_data += f"StartID: {item[3]}\n"
                    #formatted_data += f"Distance: {item[4]}\n"
                    #formatted_data += f"Description: {item[5]}\n"
                    #formatted_data += f"Start Latitude: {item[4]}\n"
                    #formatted_data += f"Start Longitude: {item[5]}\n"
                    #formatted_data += f"End Latitude: {item[6]}\n"
                    #formatted_data += f"End Longitude: {item[7]}\n"
                if rows==[]:
                    messagebox.showinfo("Error","Not Found")
                else:
                    messagebox.showinfo("Data",formatted_data)
            except Exception as e:
                print("Error:", e)
                messagebox.showinfo("Error","Not Found")

    else:
            try:
                # Execute the select query
                cur.execute('SELECT * FROM public."EndLocation" WHERE "AccidentID" = %s AND "EndID"= %s;', (AccidentID,EndID,))
                rows = cur.fetchall()
                print(rows)
                formatted_data = ""
                for item in rows:
                    formatted_data += f"ID: {item[0]}\n"
                    formatted_data += f"End_Lat: {item[1]}\n"
                    formatted_data += f"End_Lng: {item[2]}\n"
                    formatted_data += f"EndID: {item[3]}\n"
                    #formatted_data += f"Distance: {item[4]}\n"
                    #formatted_data += f"Description: {item[5]}\n"
                    #formatted_data += f"Start Latitude: {item[4]}\n"
                    #formatted_data += f"Start Longitude: {item[5]}\n"
                    #formatted_data += f"End Latitude: {item[6]}\n"
                    #formatted_data += f"End Longitude: {item[7]}\n"
                if rows==[]:
                    messagebox.showinfo("Error","Not Found")
                else:
                    messagebox.showinfo("Data",formatted_data)
            except Exception as e:
                print("Error:", e)
                messagebox.showinfo("Error","Not Found")


    # Close the cursor and connection
    cur.close()
    
# Create the main window
root = Tk()
root.title("PostgreSQL UI")

# Create the input fields
AccidentID_input = Label(root, text="AccidentID:")
AccidentID_input.grid(row=0, column=5, padx=5, pady=5)
AccidentID_input = Entry(root)
AccidentID_input.grid(row=0, column=6, padx=5, pady=5)

Severity_input = Label(root, text="Severity:")
Severity_input.grid(row=1, column=0, padx=5, pady=5)
Severity_input = Entry(root)
Severity_input.grid(row=1, column=1, padx=5, pady=5)

Start_Time_input = Label(root, text="Start_Time:")
Start_Time_input.grid(row=2, column=0, padx=5, pady=5)
Start_Time_input = Entry(root)
Start_Time_input.grid(row=2, column=1, padx=5, pady=5)

End_Time_input = Label(root, text="End_Time:")
End_Time_input.grid(row=3, column=0, padx=5, pady=5)
End_Time_input = Entry(root)
End_Time_input.grid(row=3, column=1, padx=5, pady=5)

Distance_input = Label(root, text="Distance:")
Distance_input.grid(row=4, column=0, padx=5, pady=5)
Distance_input = Entry(root)
Distance_input.grid(row=4, column=1, padx=5, pady=5)

Description_input = Label(root, text="Description:")
Description_input.grid(row=5, column=0, padx=5, pady=5)
Description_input = Entry(root)
Description_input.grid(row=5, column=1, padx=5, pady=5)



# _________________________________________2_________________________________

Number_input = Label(root, text="Number:")
Number_input.grid(row=1, column=2, padx=5, pady=5)
Number_input = Entry(root)
Number_input.grid(row=1, column=3, padx=5, pady=5)

Street_input = Label(root, text="Street:")
Street_input.grid(row=2, column=2, padx=5, pady=5)
Street_input = Entry(root)
Street_input.grid(row=2, column=3, padx=5, pady=5)

Side_input = Label(root, text="Side:")
Side_input.grid(row=3, column=2, padx=5, pady=5)
Side_input = Entry(root)
Side_input.grid(row=3, column=3, padx=5, pady=5)

City_input = Label(root, text="City:")
City_input.grid(row=4, column=2, padx=5, pady=5)
City_input = Entry(root)
City_input.grid(row=4, column=3, padx=5, pady=5)

County_input = Label(root, text="County:")
County_input.grid(row=5, column=2, padx=5, pady=5)
County_input = Entry(root)
County_input.grid(row=5, column=3, padx=5, pady=5)

State_input = Label(root, text="State:")
State_input.grid(row=6, column=2, padx=5, pady=5)
State_input = Entry(root)
State_input.grid(row=6, column=3, padx=5, pady=5)

Zipcode_input = Label(root, text="Zipcode:")
Zipcode_input.grid(row=7, column=2, padx=5, pady=5)
Zipcode_input = Entry(root)
Zipcode_input.grid(row=7, column=3, padx=5, pady=5)

Country_input = Label(root, text="Country:")
Country_input.grid(row=8, column=2, padx=5, pady=5)
Country_input = Entry(root)
Country_input.grid(row=8, column=3, padx=5, pady=5)

Timezone_input = Label(root, text="Timezone:")
Timezone_input.grid(row=9, column=2, padx=5, pady=5)
Timezone_input = Entry(root)
Timezone_input.grid(row=9, column=3, padx=5, pady=5)

Airport_Code_input = Label(root, text="Airport_Code:")
Airport_Code_input.grid(row=10, column=2, padx=5, pady=5)
Airport_Code_input = Entry(root)
Airport_Code_input.grid(row=10, column=3, padx=5, pady=5)


Weather_Timestamp_input = Label(root, text="Weather_Timestamp:")
Weather_Timestamp_input.grid(row=11, column=2, padx=5, pady=5)
Weather_Timestamp_input = Entry(root)
Weather_Timestamp_input.grid(row=11, column=3, padx=5, pady=5)

Temperature_input = Label(root, text="Temperature(F):")
Temperature_input.grid(row=12, column=2, padx=5, pady=5)
Temperature_input = Entry(root)
Temperature_input.grid(row=12, column=3, padx=5, pady=5)

Wind_Chill_input = Label(root, text="Wind_Chill(F):")
Wind_Chill_input.grid(row=13, column=2, padx=5, pady=5)
Wind_Chill_input = Entry(root)
Wind_Chill_input.grid(row=13, column=3, padx=5, pady=5)

Humidity_input = Label(root, text="Humidity(%):")
Humidity_input.grid(row=14, column=2, padx=5, pady=5)
Humidity_input = Entry(root)
Humidity_input.grid(row=14, column=3, padx=5, pady=5)

Pressure_input = Label(root, text="Pressure(in):")
Pressure_input.grid(row=15, column=2, padx=5, pady=5)
Pressure_input = Entry(root)
Pressure_input.grid(row=15, column=3, padx=5, pady=5)

Visibility_input = Label(root, text="Visibility(mi):")
Visibility_input.grid(row=16, column=2, padx=5, pady=5)
Visibility_input = Entry(root)
Visibility_input.grid(row=16, column=3, padx=5, pady=5)

Wind_Direction_input = Label(root, text="Wind_Direction:")
Wind_Direction_input.grid(row=17, column=2, padx=5, pady=5)
Wind_Direction_input = Entry(root)
Wind_Direction_input.grid(row=17, column=3, padx=5, pady=5)

Wind_Speed_input = Label(root, text="Wind_Speed(mph):")
Wind_Speed_input.grid(row=18, column=2, padx=5, pady=5)
Wind_Speed_input = Entry(root)
Wind_Speed_input.grid(row=18, column=3, padx=5, pady=5)

Precipitation_input = Label(root, text="Precipitation(in):")
Precipitation_input.grid(row=19, column=2, padx=5, pady=5)
Precipitation_input = Entry(root)
Precipitation_input.grid(row=19, column=3, padx=5, pady=5)

Weather_Condition_input = Label(root, text="Weather_Condition:")
Weather_Condition_input.grid(row=20, column=2, padx=5, pady=5)
Weather_Condition_input = Entry(root)
Weather_Condition_input.grid(row=20, column=3, padx=5, pady=5)

WeatherID_input = Label(root, text="WeatherID:")
WeatherID_input.grid(row=21, column=2, padx=5, pady=5)
WeatherID_input = Entry(root)
WeatherID_input.grid(row=21, column=3, padx=5, pady=5)

#_________________________________3______________________________________________


Amenity_input = Label(root, text="Amenity:")
Amenity_input.grid(row=1, column=4, padx=5, pady=5)
Amenity_input = Entry(root)
Amenity_input.grid(row=1, column=5, padx=5, pady=5)

Bump_input = Label(root, text="Bump:")
Bump_input.grid(row=2, column=4, padx=5, pady=5)
Bump_input = Entry(root)
Bump_input.grid(row=2, column=5, padx=5, pady=5)

Crossing_input = Label(root, text="Crossing:")
Crossing_input.grid(row=3, column=4, padx=5, pady=5)
Crossing_input = Entry(root)
Crossing_input.grid(row=3, column=5, padx=5, pady=5)

Give_Way_input = Label(root, text="Give_Way:")
Give_Way_input.grid(row=4, column=4, padx=5, pady=5)
Give_Way_input = Entry(root)
Give_Way_input.grid(row=4, column=5, padx=5, pady=5)

Junction_input = Label(root, text="Junction:")
Junction_input.grid(row=5, column=4, padx=5, pady=5)
Junction_input = Entry(root)
Junction_input.grid(row=5, column=5, padx=5, pady=5)

No_Exit_input = Label(root, text="No_Exit:")
No_Exit_input.grid(row=6, column=4, padx=5, pady=5)
No_Exit_input = Entry(root)
No_Exit_input.grid(row=6, column=5, padx=5, pady=5)

Railway_input = Label(root, text="Railway:")
Railway_input.grid(row=7, column=4, padx=5, pady=5)
Railway_input = Entry(root)
Railway_input.grid(row=7, column=5, padx=5, pady=5)

Roundabout_input = Label(root, text="Roundabout:")
Roundabout_input.grid(row=8, column=4, padx=5, pady=5)
Roundabout_input = Entry(root)
Roundabout_input.grid(row=8, column=5, padx=5, pady=5)

Station_input = Label(root, text="Station:")
Station_input.grid(row=9, column=4, padx=5, pady=5)
Station_input = Entry(root)
Station_input.grid(row=9, column=5, padx=5, pady=5)

Stop_input = Label(root, text="Stop:")
Stop_input.grid(row=10, column=4, padx=5, pady=5)
Stop_input = Entry(root)
Stop_input.grid(row=10, column=5, padx=5, pady=5)

Traffic_Calming_input = Label(root, text="Traffic_Calming:")
Traffic_Calming_input.grid(row=11, column=4, padx=5, pady=5)
Traffic_Calming_input = Entry(root)
Traffic_Calming_input.grid(row=11, column=5, padx=5, pady=5)

Traffic_Signal_input = Label(root, text="Traffic_Signal:")
Traffic_Signal_input.grid(row=12, column=4, padx=5, pady=5)
Traffic_Signal_input = Entry(root)
Traffic_Signal_input.grid(row=12, column=5, padx=5, pady=5)

Turning_Loop_input = Label(root, text="Turning_Loop:")
Turning_Loop_input.grid(row=13, column=4, padx=5, pady=5)
Turning_Loop_input = Entry(root)
Turning_Loop_input.grid(row=13, column=5, padx=5, pady=5)



#___________________________________4________________________________________



Start_Lat_input = Label(root, text="Start_Lat:")
Start_Lat_input.grid(row=1, column=6, padx=5, pady=5)
Start_Lat_input = Entry(root)
Start_Lat_input.grid(row=1, column=7, padx=5, pady=5)

Start_Lng_input = Label(root, text="Start_Lng:")
Start_Lng_input.grid(row=2, column=6, padx=5, pady=5)
Start_Lng_input = Entry(root)
Start_Lng_input.grid(row=2, column=7, padx=5, pady=5)

StartID_input = Label(root, text="StartID:")
StartID_input.grid(row=3, column=6, padx=5, pady=5)
StartID_input = Entry(root)
StartID_input.grid(row=3, column=7, padx=5, pady=5)

#___________________________________5________________________________________



End_Lat_input = Label(root, text="End_Lat:")
End_Lat_input.grid(row=1, column=8, padx=5, pady=5)
End_Lat_input = Entry(root)
End_Lat_input.grid(row=1, column=9, padx=5, pady=5)

End_Lng_input = Label(root, text="End_Lng:")
End_Lng_input.grid(row=2, column=8, padx=5, pady=5)
End_Lng_input = Entry(root)
End_Lng_input.grid(row=2, column=9, padx=5, pady=5)

EndID_input = Label(root, text="EndID:")
EndID_input.grid(row=3, column=8, padx=5, pady=5)
EndID_input = Entry(root)
EndID_input.grid(row=3, column=9, padx=5, pady=5)
#________________________________________6_____________________________________


Severity_input = Label(root, text="Sunrise_Sunset:")
Severity_input.grid(row=1, column=10, padx=5, pady=5)
Severity_input = Entry(root)
Severity_input.grid(row=1, column=11, padx=5, pady=5)

Civil_Twilight_input = Label(root, text="Civil_Twilight:")
Civil_Twilight_input.grid(row=2, column=10, padx=5, pady=5)
Civil_Twilight_input = Entry(root)
Civil_Twilight_input.grid(row=2, column=11, padx=5, pady=5)

End_Time_input = Label(root, text="Nautical_Twilight:")
End_Time_input.grid(row=3, column=10, padx=5, pady=5)
End_Time_input = Entry(root)
End_Time_input.grid(row=3, column=11, padx=5, pady=5)

End_Time_input = Label(root, text="Astronomical_Twilight:")
End_Time_input.grid(row=3, column=10, padx=5, pady=5)
End_Time_input = Entry(root)
End_Time_input.grid(row=3, column=11, padx=5, pady=5)


# Create the buttons
insert_button = Button(root, text="Insert", command=insert_data)
insert_button.grid(row=22, column=5, padx=5, pady=5)

delete_button = Button(root, text="Delete", command=delete_data)
delete_button.grid(row=22, column=6, padx=5, pady=5)

delete_button = Button(root, text="Retrieve", command=retrieve_data)
delete_button.grid(row=22, column=7, padx=5, pady=5)

# Start the main loop
root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




