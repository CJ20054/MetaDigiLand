import os
from Tkinter import *

desc_obj_library = []

class description_popup:
    def __init__(self, desc_text):
        
        self.desc_window_popup = Toplevel() # spawn a new window for the fix subject tools
        Label(self.desc_window_popup, bg="#359A35", foreground="white", text=desc_text, anchor=W, justify=LEFT).grid(row=1, column=1)
    def cleanup(self):
        try:
            self.desc_window_popup.destroy()
        except (TclError):
            pass

def look_at_description(desc_text):
    for obj in desc_obj_library: # destroy any other add subject windows that are present before creating a new one, only one at a time people!
        obj.cleanup()
    del desc_obj_library[:] # delete all object instance references to avoid duplicate attempts to destroy them
    desc_obj_library.append(description_popup(desc_text))

	
# hash for holding the paths
apps = { 
    'manifestMods': '"' + "S:\Digital Projects\Administrative\scripts\Metadata\manifestMods.pl" + '"',
    'GUI_makeMods': '"' + "S:\Digital Projects\Administrative\scripts\Metadata\makeMods\GUI_makeMods.pl" + '"',
    'getSubjects': '"' + "S:\Digital Projects\Administrative\scripts\Metadata\getSubjects.py" + '"',
    'DB_SubjectTagging': '"' + "S:\Digital Projects\Administrative\scripts\Metadata\DB_SubjectTagging.pl" + '"',
    'DB_SubjectReplace': '"' + "S:\Digital Projects\Administrative\scripts\Metadata\DB_SubjectReplace.pl" + '"',
    'GUI_subsToDbase': '"' + "S:\Digital Projects\Administrative\scripts\Metadata\GUI_subsToDbase.pl" + '"',
    'checkImages': '"' + "S:\Digital Projects\Administrative\scripts\qc\checkImages.pl" + '"',
    'filenamesAndDupes': '"' + "S:\Digital Projects\Administrative\scripts\qc\\filenamesAndDupes.pl" + '"', # \f (in python) resolves to \x0c which is the expressable character notation for form feed. this path has a \f at the begigning of the file name so the slash needed to be escaped
    'fixfits': '"' + "S:\Digital Projects\Administrative\scripts\qc\\fixfits.pl" + '"',
    'MassContentCheck': '"' + "S:\Digital Projects\Administrative\scripts\qc\MassContentCheck.pl" + '"',
    'qc_list': '"' + "S:\Digital Projects\Administrative\scripts\qc\qc_list.py" + '"',
    'ScrapbookCheck': '"' + "S:\Digital Projects\Administrative\scripts\qc\ScrapbookCheck.pl" + '"',
    'getNames': '"' + "S:\Digital Projects\Administrative\scripts\Metadata\getNames.py" + '"',
    'DB_NameTagging': '"' + "S:\Digital Projects\Administrative\scripts\Metadata\DB_NameTagging.pl" + '"',
    'Scans_Mover_GUI': '"' + "S:\Digital Projects\Administrative\scripts\Scans_Mover\Scans_Mover_GUI.pl" + '"',
    'ExcelConverter': '"' + "S:\Digital Projects\Administrative\scripts\ExcelConverter\ExcelConverter.pl" + '"',
    'pull_it': '"' + "S:\Digital Projects\Administrative\scripts\image_puller\pull_it.py" + '"',
    }
# generic function for calling scripts
def call_launcher(script_name):
    os.startfile(apps[script_name])


# start of the GUI ----------------------------------------------
root = Tk()
root.wm_title("Metadata and Digital Services Toolbox")

background_image = PhotoImage(file="winner-taco.gif")
background_label = Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Mods frame ----------------------------------------------
mods_tools = LabelFrame(root, text="MODS Tools", font = "Helvetica 16 bold", width=150, height=400, bd=5, padx=10, pady=10) # jeremiah
mods_tools.grid(row=0, column=0)
mods_tools.config(bg="#359A35")
#app buttons
Button(mods_tools, text='manifestMods', command=lambda : call_launcher("manifestMods"), height=2, font="bold", foreground="red2").grid(row=1, column=0, padx=5, pady=5)
Button(mods_tools, text='GUI_makeMods', command=lambda : call_launcher("GUI_makeMods"), height=2, font="bold", foreground="red2").grid(row=2, column=0, padx=5, pady=5)
#desc button
Button(mods_tools, text='What do these scripts do?', command=lambda : look_at_description("Script Name\t\t Required\t\t\t\t\tDescription\t\t\t\t\t\t\t\t\tOutput\n\nmanifestMods\t\t Requires: MODS files.\t\t\t\tFunction: generates a mods manifest for use with xmlspy in validating mods\t\tOutput: manifest file\nGUI_makeMods\t\t Requires: Metadata Spreadsheet exported to text file.\tFunction: Creates finalized MODS files\t\t\t\t\t\tOutput: MODS files"), height=1, foreground="red2").grid(row=10, column=0, padx=5, pady=5)

# Subject frame ----------------------------------------------
subjects_tools = LabelFrame(root, text="Subject Tools", font = "Helvetica 16 bold", width=150, height=130, bd=5, padx=10, pady=10) # corinne
subjects_tools.grid(row=0, column=2)
subjects_tools.config(bg="#359A35")

Button(subjects_tools, text='GetSubjects', command=lambda : call_launcher("getSubjects"), height=2, font="bold", foreground="DarkSlateBlue").grid(row=2, column=2, padx=5, pady=5)
Button(subjects_tools, text='DB_SubjectTagging', command=lambda : call_launcher("DB_SubjectTagging"), height=2, font="bold", foreground="DarkSlateBlue").grid(row=3, column=2, padx=5, pady=5)
Button(subjects_tools, text='DB_SubjectReplace', command=lambda : call_launcher("DB_SubjectReplace"), height=2, font="bold", foreground="DarkSlateBlue").grid(row=4, column=2, padx=5, pady=5)
Button(subjects_tools, text='GUI_subsToDbase', command=lambda : call_launcher("GUI_subsToDbase"), height=2, font="bold", foreground="DarkSlateBlue").grid(row=5, column=2, padx=5, pady=5)

Button(subjects_tools, text='What do these scripts do?', command=lambda : look_at_description("Script Name\t\t Required\t\t\t\t\tDescription\t\t\t\t\t\t\t\t\tOutput\n\ngetSubjects\t\t Requires: Nothing.\t\t\t\tFunction: Search the subjects database for tagged subjects\t\t\t\tOutput: Results of search\nDB_SubjectTagging\t Requires: Metadata Spreadsheet exported to text file.\tFunction: Compares the untagged subjects in the spreadsheet to those in the database.\tOutput: A list of subjects that are in the spreadsheet and not in the database\nGUI_subsToDbase\t\t Requires: Text file of subjects in correct format.\tFunction: Adds multiple subjects to the subjects database\t\t\t\tOutput: Error file\nDB_SubjectReplace\t Requires: Metadata Spreadsheet exported to text file\tFunction: Replaces untagged subjects from spreadsheet with their tagged version\t\tOutput: A list of subjects that are in the spreadsheet and not in the database\n"), height=1, foreground="DarkSlateBlue").grid(row=10, column=2, padx=5, pady=5)


# Names frame ----------------------------------------------
names_tools = LabelFrame(root, text="Names Tools", font = "Helvetica 16 bold", width=150, height=400, bd=5, padx=10, pady=10) # claire
names_tools.grid(row=0, column=1)
names_tools.config(bg="#359A35")

Button(names_tools, text='getNames', command=lambda : call_launcher("getNames"), height=2, font="bold", foreground="#666699").grid(row=1, column=1, padx=5, pady=5)
Button(names_tools, text='DB_NameTagging', command=lambda : call_launcher("DB_NameTagging"), height=2, font="bold", foreground="#666699").grid(row=2, column=1, padx=5, pady=5)

Button(names_tools, text='What do these scripts do?', command=lambda : look_at_description("Script Name\t\t Required\t\t\t\t\tDescription\t\t\t\t\t\t\t\t\tOutput\n\ngetNames\t\t Requires: Nothing.\t\t\t\tFunction: Search the names database for tagged names\t\t\t\tOutput: Results of search\nDB_NameTagging\t Requires: Metadata Spreadsheet exported to text file.\tFunction: Compares the untagged names in the spreadsheet to those in the database.\tOutput: A list of names that are in the spreadsheet and not in the database\n"), height=1, foreground="DarkSlateBlue").grid(row=3, column=1, padx=5, pady=5)


# QC frame ----------------------------------------------
qc_tools = LabelFrame(root, text="QC Tools", font = "Helvetica 16 bold", width=150, height=130, bd=5, padx=10, pady=10) # alissa
qc_tools.grid(row=0, column=4)
qc_tools.config(bg="#359A35")

Button(qc_tools, text='filenamesAndDupes', command=lambda : call_launcher("filenamesAndDupes"), height=2, font="bold", foreground="dark green").grid(row=1, column=3, padx=5, pady=5)
Button(qc_tools, text='MassContentCheck', command=lambda : call_launcher("MassContentCheck"), height=2, font="bold", foreground="dark green").grid(row=2, column=3, padx=5, pady=5)
Button(qc_tools, text='qc_list', command=lambda : call_launcher("qc_list"), height=2, font="bold", foreground="dark green").grid(row=3, column=3, padx=5, pady=5)
Button(qc_tools, text='ScrapbookCheck', command=lambda : call_launcher("ScrapbookCheck"), height=2, font="bold", foreground="dark green").grid(row=4, column=3, padx=5, pady=5)

Button(qc_tools, text='What do these scripts do?', command=lambda : look_at_description("Script Name\t\t Required\t\t\t\t\tDescription\t\t\t\t\t\t\t\t\t\tOutput\n\nfilenamesAndDupes\t Requires: Nothing.\t\t\t\tFunction: Checks for bad filenames, duplications, and wrong directories.\t\t\t\tOutput: Details of errors found.\nMassContentCheck\t Requires: Metadata Spreadsheet exported to text file.\tFunction: Checks Mass content for bad filenames, out of sequence IDs, and missing OCR files.\tOutput: Details of errors found.\nqc_list\t\t\t Requires: Nothing.\t\t\t\tFunction: Creates a list of problems and item IDs found during QC.\t\t\t\tOutput: Compiled list.\nScrapbookCheck\t\t Requires: Log file exported to text file.\t\tFunction: Checks Scrapbooks for bad filenames and out of sequence items, pages, and subpages.\tOutput: Details of errors found.\n"), height=1, foreground="dark green").grid(row=10, column=3, padx=5, pady=5)

# Other frame ----------------------------------------------
other_tools = LabelFrame(root, text="Other Tools", font = "Helvetica 16 bold", width=150, height=400, bd=5, padx=10, pady=10) 
other_tools.grid(row=0, column=5)
other_tools.config(bg="#359A35")

Button(other_tools, text='ExcelConverter', command=lambda : call_launcher("ExcelConverter"), height=2, font="bold", foreground="#666699").grid(row=1, column=1, padx=5, pady=5)
Button(other_tools, text='Scans_Mover_GUI', command=lambda : call_launcher("Scans_Mover_GUI"), height=2, font="bold", foreground="#666699").grid(row=2, column=1, padx=5, pady=5)
Button(other_tools, text='pull_it', command=lambda : call_launcher("pull_it"), height=2, font="bold", foreground="#666699").grid(row=3, column=1, padx=5, pady=5)

Button(other_tools, text='What do these scripts do?', command=lambda : look_at_description("Script Name\t\t Required\t\t\t\t\tDescription\t\t\t\t\t\t\t\t\t\tOutput\n\nExcelConverter\t\t Requires: .xlsx file.\t\t\t\tFunction: converts  a .xlsx file into a tab delimited file and manages diacritics and encoding.\tOutput: tab delimited .txt file.\nScans_mover\t\t Requires: directory full of tiffs \t\t\tFunction: moves and folderizes tiff files for the item level onto the S drive\t\t\tOutput: Folderized tiffs\n"), height=1, foreground="dark green").grid(row=10, column=1, padx=5, pady=5)

mainloop()