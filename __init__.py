from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft import MycroftSkill, intent_file_handler
import date



class CafeteriaMenu(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder("").require("monday.menu"))
    def handle_monday_menu(self):
        mone = self.settings.get("mone")
        mons = self.settings.get("mons")
        mond = self.settings.get("mond")
        self.speak_dialog("monday.menu", data={"mone": mone, "mons": mons, "mond": mond})

    @intent_handler(IntentBuilder("").require("tuesday.menu"))
    def handle_tuesday_menu(self):
        tuee = self.settings.get("tuee")
        tues = self.settings.get("tues")
        tued = self.settings.get("tued")
        self.speak_dialog("tuesday.menu", data={"tuee": tuee, "tues": tues, "tued": tued})

    @intent_handler(IntentBuilder("").require("wednesday.menu"))
    def handle_wednesday_menu(self):
        wede = self.settings.get("wede")
        weds = self.settings.get("weds")
        wedd = self.settings.get("wedd")
        self.speak_dialog("wednesday.menu", data={"wede": wede, "weds": weds, "wedd": wedd})

    @intent_handler(IntentBuilder("").require("thursday.menu"))
    def handle_thursday_menu(self):
        thue= self.settings.get("thue")
        thus = self.settings.get("thus")
        thud = self.settings.get("thud")
        self.speak_dialog("thursday.menu", data={"thue": thue, "thus": thus, "thud": thud})

    @intent_handler(IntentBuilder("").require("friday.menu"))
    def handle_friday_menu(self):
        frie = self.settings.get("frie")
        fris = self.settings.get("fris")
        frid = self.settings.get("frid")
        self.speak_dialog("friday.menu", data={"frie": frie, "fris": fris, "frid": frid})

    @intent_handler(IntentBuilder("").require("today.menu"))
    def handle_friday_menu(self):
        today = self.get_weekday()
        if today == "monday":
            mone = self.settings.get("mone")
            mons = self.settings.get("mons")
            mond = self.settings.get("mond")
            self.speak_dialog("monday.menu", data={"mone": mone, "mons": mons, "mond": mond})
        elif today == "tuesday":
            tuee = self.settings.get("tuee")
            tues = self.settings.get("tues")
            tued = self.settings.get("tued")
            self.speak_dialog("tuesday.menu", data={"tuee": tuee, "tues": tues, "tued": tued})
        elif today == "wednesday":
            wede = self.settings.get("wede")
            weds = self.settings.get("weds")
            wedd = self.settings.get("wedd")
            self.speak_dialog("wednesday.menu", data={"wede": wede, "weds": weds, "wedd": wedd})
        elif today == "thursday":
            thue = self.settings.get("thue")
            thus = self.settings.get("thus")
            thud = self.settings.get("thud")
            self.speak_dialog("thursday.menu", data={"thue": thue, "thus": thus, "thud": thud})
        elif today == "friday":
            frie = self.settings.get("frie")
            fris = self.settings.get("fris")
            frid = self.settings.get("frid")
            self.speak_dialog("friday.menu", data={"frie": frie, "fris": fris, "frid": frid})

def create_skill():
    return CafeteriaMenu()
