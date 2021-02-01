# This files contains your custom actions which can be used to run
# custom Python code.

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_core_sdk.events import Restarted
import pymysql

class ActionCuisineC(Action): 
# search based on names -> type_timeoff
    def name(self) -> Text: 
        #Unique identifier of the form
        return "action_search_names_type_timeoff" #done

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 

        names = tracker.get_slot("names")
        messages = tracker.get_slot("type_timeoff")
        keyin_date = tracker.get_slot("keyin_date")

        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="skymind123",
            database="rasa_feedback"
        )
        cur = conn.cursor()
        sql = 'SELECT * FROM dt_historical WHERE names LIKE "%{}%" AND (messages LIKE "%{}%" OR keyin_date LIKE "%{}%")'.format(names, messages, keyin_date)
        cur.execute(sql)
        result = cur.fetchall()
        if len(result) > 0:
            for row in result:
                print('action_search_names_type_timeoff', row[0])
                a = row[0]
                b = row[2]
                c = row[3]

                dispatcher.utter_message("Here is the information\nName: {}\nTime Off: {}\nLeft Messages: {}\n\n".format(a, b, c)) #cun melecun lihat stories memudahkan kerja sambil lihat database query
        else:
            dispatcher.utter_message("No data found in the database, please try again.")
        conn.close()
        return []

class ActionCuisineB(Action): 
# search based on names -> keyin_date
    def name(self) -> Text: 
        #Unique identifier of the form
        return "action_search_names_keyin_date"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 

        names = tracker.get_slot("names")
        keyin_date = tracker.get_slot("keyin_date")

        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="skymind123",
            database="rasa_feedback"
        )
        cur = conn.cursor()
        sql = 'SELECT * FROM dt_historical WHERE keyin_date LIKE "%{}%" OR names LIKE "%{}%"'.format(keyin_date, names) #updated on november 4/11/2020
        cur.execute(sql)
        result = cur.fetchall()
        if len(result) > 0:
            for row in result:
                print('action_search_names_keyin_date', row[0])
                a = row[0]
                b = row[1]
                c = row[2]
                d = row[3]

                dispatcher.utter_message("Here is the information\nName: {}\nKeyin-Time: {}\nKeyin-Date: {}\nTime-Off Messages: {}\n\n".format(a, b, c, d))
        else:
            dispatcher.utter_message("No data found in the database, please try again.")
        conn.close()
        return []


class ActionCuisineA(Action): 
# search based on names -> keyin_time
    def name(self) -> Text: 
        #Unique identifier of the form
        return "action_search_names_keyin_time"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 


        keyin_time = tracker.get_slot("keyin_time")
        messages = tracker.get_slot("type_timeoff")
        keyin_date = tracker.get_slot("keyin_date")

        conn = pymysql.connect(
            host="localhost", 
            user="root",
            password="skymind123",
            database="rasa_feedback"
        )
        cur = conn.cursor()
        #sql = 'SELECT names FROM dt_historical WHERE keyin_time LIKE "%9:02 AM%" AND (keyin_date LIKE "%13/10/2020%" OR messages LIKE "%ooo%")'.format(messages, keyin_time, keyin_date)
        sql = 'SELECT names FROM dt_historical WHERE keyin_time LIKE "%{}%" AND (messages LIKE "%{}%" OR keyin_date LIKE "%{}%")'.format(keyin_time, messages, keyin_date) #terbaik boh lihat di stories untuk guide
        cur.execute(sql)
        result = cur.fetchall()
        if len(result) > 0:
            for row in result:
                print('action_search_names_keyin_time', row[0])
                a = row[0]
                # b = row[1]
                # c = row[2]
                # d = row[3]

#BERHASIL YANG NI MENJADI
                dispatcher.utter_message("Here is the information\nName: {}".format(a))
        else:
            dispatcher.utter_message("No data found in the database, please try again.")
        conn.close()
        return []






# class ActionCuisine(Action):
# # search based on names -> keyin_time and type_timeoff
#     def name(self) -> Text:
#         #Unique identifier of the form
#         return "action_search_names_keyin_time_type_timeoff"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         names = tracker.get_slot("names")
#         type_timeoff = tracker.get_slot("type_timeoff")
#         keyin_time= tracker.get_slot("keyin_time")
#         print(names, type_timeoff, keyin_time)
#
#         conn = pymysql.connect(
#             host="localhost",
#             user="root",
#             password="skymind123",
#             database="rasa_feedback"
#         )
#         cur = conn.cursor()
#         sql = 'SELECT * FROM dt_historical WHERE names LIKE "%{}%" AND messages LIKE "%{}%" AND keyin_time LIKE "%{}%"'.format(names, type_timeoff, keyin_time)
#         cur.execute(sql)
#         result = cur.fetchall()
#         if len(result) > 0:
#             for row in result:
#                 print('action_search_names_keyin_time_type_timeoff', row[0])
#                 a = row[0]
#                 b = row[1]
#                 c = row[3]
#
#                 dispatcher.utter_message("Here is the information\nName: {}\nTime: {}\nMessages: {}\n\n".format(a, b, c))
#         else:
#             dispatcher.utter_message("No data found in the database, please try again.")
#         conn.close()
#         return []

class ActionCuisine(Action):
# search based on names -> type_timeoff
    def name(self) -> Text:
        #Unique identifier of the form
        return "action_search_names_keyin_date_type_timeoff"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        names = tracker.get_slot("names")
        messages = tracker.get_slot("type_timeoff")
        keyin_time = tracker.get_slot("keyin_time")
        keyin_date = tracker.get_slot("keyin_date")

        print(names, messages, keyin_time, keyin_date)

        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="skymind123",
            database="rasa_feedback"
        )
        cur = conn.cursor()
        sql = 'SELECT * FROM dt_historical WHERE names LIKE "%{}%" AND (messages LIKE "%{}%" OR keyin_date LIKE "%{}%")'.format(names, messages, keyin_date)
        cur.execute(sql)
        result = cur.fetchall()
        if len(result) > 0:
            for row in result:
                print('action_search_names_keyin_date_type_timeoff', row[0])
                a = row[0]
                b = row[1]
                c = row[2]
                d = row[3]
                dispatcher.utter_message("Here is the information\nNames: {}\nKey In Time: {}\nKey In Date: {}\nLeft Messages: {}\n\n".format(a, b, c, d))
        else:
            dispatcher.utter_message("No data found in the database, please try again.")
        conn.close()
        return []

        

class ActionSearch(Action): 

    def name(self) -> Text: 
        #Unique identifier of the form
        return "action_search_type_timeoff" #done

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        names = tracker.get_slot("names")
        keyin_time = tracker.get_slot("keyin_time")
        messages = tracker.get_slot("type_timeoff")
        keyin_date = tracker.get_slot("keyin_date")


        conn = pymysql.connect(
            host="localhost", 
            user="root",
            password="skymind123",
            database="rasa_feedback"
        )
        cur = conn.cursor()
        sql = 'SELECT * FROM dt_historical WHERE messages LIKE "%{}%"'.format(messages)
        #sql = 'SELECT * FROM dt_historical WHERE messages LIKE "%ooo%" AND (keyin_date LIKE "%19/10/2020%" OR keyin_time LIKE "%9:02 AM%")'.format(messages, keyin_date, keyin_time)
        cur.execute(sql)
        result = cur.fetchall()
        if len(result) > 0:
            for row in result:
                print('action_search_type_timeoff', row[0])
                a = row[0]
                b = row[1]
                c = row[2]
                d = row[3]

                dispatcher.utter_message("Here is the information\nNames: {}\nKey In Time: {}\nKey In Date: {}\nLeft Messages: {}\n\n".format(a, b, c, d))
        else:
            dispatcher.utter_message("No data found in the database, please try again.")
        conn.close()
        return []

class ActionSubmit(Action): 

    def name(self) -> Text: 
        #Unique identifier of the form
        return "action_submit"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
            
        Name = tracker.get_slot("name")
        Gender = tracker.get_slot("gender") 

        conn = pymysql.connect(
            host="localhost", 
            user="root",
            password="skymind123",
            database="rasa_feedback"
        )
        cur = conn.cursor()
        sql='INSERT INTO user_info (name, gender) VALUES ("{}","{}");'.format(Name, Gender)
        #sql='INSERT INTO user_info (name, gender, age, phonenumber) VALUES ("Ali","male","22","123");'
        cur.execute(sql) 
        conn.commit()
        # some other statments  with the help of cursor
        conn.close()
        print("Success!")
        dispatcher.utter_message("Thanks for the valuable feedback. ") 
        return []

class ActionForm(FormAction):

    def name(self) -> Text:
        return "user_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        return["name","gender"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        # Pick up slot
        return {
        "name":[
            self.from_entity(entity="name"),
        ], 
        "gender":[
            self.from_entity(entity="gender"),
        ],
        }

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[Dict]:
        # utter submit template
        dispatcher.utter_message(responses="utter_slots_value",)
        return []

class SomeAction(Action):
    def name(self):
        return "action_restart"

    def run(self, dispatcher, tracker, domain):
        # do something here

        return [Restarted()]