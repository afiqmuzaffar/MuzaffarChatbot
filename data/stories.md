## fallback story
* out_of_scope
 - utter_fallback
 - action_default_fallback

## normal path1
* greet
 - utter_greet
* feedback
 - user_form
 - form{"name":"user_form"}
 - form{"name": null}
 - utter_submit
* affirm 
 - action_submit
 - action_restart

## deny path
* deny
 - utter_goodbye
 - action_restart

## search path 1 (give me all your names) only time in the first statement
* greet
 - utter_greet
* search_names{"keyin_time":"9:02 AM","keyin_date":"13/10/2020","type_timeoff":"ooo"}
 - action_search_names_keyin_time
 
## search path 2 (give me all your names) only time in the first statement
* greet
 - utter_greet
* search_names{"keyin_time":"9:02 AM","type_timeoff":"ooo"}
 - action_search_names_keyin_time

## search path 3 (give me all your names) only time in the first statement
* greet
 - utter_greet
* search_names{"keyin_time":"9:02 AM","keyin_date":"13/10/2020"}
 - action_search_names_keyin_time


## search based on names part 1
* greet
 - utter_greet
* search_names{"names":"natasya"}
 - utter_ask_keyindate
* keyin_date_type{"keyin_date":"13/10/2020"}
 - utter_ask_date_confirmation
* affirm
 - utter_give
 - action_search_names_keyin_date_type_timeoff
 - utter_goodbye
 - action_restart

## search based on names part 2
* greet
 - utter_greet
* search_names{"names":"natasya"}
 - utter_ask_keyindate
* keyin_time_type{"keyin_date":"13/10/2020"}
 - utter_ask_date_confirmation
* deny
 - utter_goodbye
 - action_restart

## search based on names and type_timeoff code
* greet
 - utter_greet
* search_names{"names":"natasya","type_timeoff":"ooo","keyin_date":"13/10/2020"}
 - action_search_names_type_timeoff
 - utter_goodbye
 - action_restart

## search based on names and keyin_time
* greet
 - utter_greet
* search_names{"names":"natasya","keyin_time":"9:02 AM"}
 - action_search_names_keyin_time
 - utter_goodbye
 - action_restart

## search based on names and keyin_date
* greet
 - utter_greet
* search_names{"type_timeoff":"ooo","keyin_date":"13/10/2020"}
 - action_search_names_keyin_date
 - utter_goodbye
 - action_restart
 
 ## search based on type_timeoff and keyin_time and keyin_date
* greet
 - utter_greet
* search_names{"keyin_time":"9:02 AM","type_timeoff":"ooo","keyin_date":"13/10/2020"}
 - action_search_names_keyin_time
 - utter_goodbye
 - action_restart
 
 ## list people 1
* greet
 - utter_greet
* bismillah{"type_timeoff":"ooo","keyin_date":"19/10/2020","keyin_time":"9:02 AM"}
 - action_search_type_timeoff
 - utter_goodbye
 - action_restart
 
 ## list people 2
* greet
 - utter_greet
* bismillah{"type_timeoff":"ooo","keyin_date":"19/10/2020"}
 - action_search_type_timeoff
 - utter_goodbye
 - action_restart
 
 ## list people 3
* greet
 - utter_greet
* bismillah{"type_timeoff":"ooo"}
 - action_search_type_timeoff
 - utter_goodbye
 - action_restart
 