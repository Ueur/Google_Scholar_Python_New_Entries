# This program is to check all newly published papers by a group of scholars selected by the person who runs this program
# Due to the limitations of Google Search, the program will take about 40 seconds to get result from one scholar, so the
# time will be very long if dozens of scholars need to be checked. Since Google Scholar does not automatically identify
# scholars with same names but different scholar IDs, therefore results from selected scholars with same names may not be
# able to be obtained. 

import scholarly
from datetime import date
import os.path


# Search history list file and list, include all dates in which search was performed
Search_History_File = 'search_history.txt'
Search_History_List = list()

# Scholar list file and list, contain all selected scholar names and Google Scholar IDs
# For each line in this scholar_List.txt, it has to be a scholar's name plus a comma and
# a space, then plus the scholar's Google Scholar ID
Scholar_List_File = 'scholar_list.txt'
Scholar_List = list()

# File and list contain all newly added papers
New_Add_Result_File = 'new_add_result.txt'
New_Search_Result_List = list()

# List contains all papers for an individual scholar
Each_Scholar_Paper_List = list()

# List contains all papers obtained from the previous search
Previous_Papers_List = list()

# Current search result (all paper list) file name, this will be previous file for future searches
now_t = date.today()
Current_Search_Result_File = str(now_t) + '.txt'


# Get search history data, return a list contains all previous dates in which search was performed
def Read_Search_History(Search_History_File):
    file_exists = os.path.isfile(Search_History_File)
    SH_List = list()
    if file_exists:
        with open(Search_History_File, 'r', encoding='utf-8-sig') as f1:
            while True:
                Str1 = f1.readline()
                if Str1 == '\n' or Str1 == '':
                    break
                else:
                    if Str1[-1] == '\n':
                        Str2 = Str1[:-1]
                    else:
                        Str2 = Str1
                                         
                    SH_List.append(Str2)
    else:
        with open(Search_History_File, 'w', encoding='utf-8') as f1:
            now_t = date.today()
            s1 = str(now_t) + '\n'
            f1.write(s1)
    return SH_List


# Get a list contains all selected scholar name and corresponding Google Scholar IDs, return a large list with
# all small lists containing name and ID pairs of all selected scholars. You can change scholar_list.txt file
# to add or remove scholars.

def Read_Scholar_List(Scholar_List_File):
    file_exists = os.path.isfile(Scholar_List_File)
    SC_List = list()
    if file_exists:
        with open(Scholar_List_File, 'r', encoding='utf-8-sig') as f1:
            while True:
                Str1 = f1.readline()
                if Str1 == '\n' or Str1 == '':
                    break
                else:
                    if Str1[-1] == '\n':
                        Str2 = Str1[:-1]
                    else:
                        Str2 = Str1
                    Str3 = Str2.split(", ")
                    SC_List.append(Str3)
    else:
        print('The file doex not exist')
        SC_List = none

    return SC_List       

# Get all papers from a previous search result file,return a big list containing all paper IDs
def Read_Previous_Papers(Previous_Search_File_Name):
    PP_List = list()
    Str_List = list()

    file_exists = os.path.isfile(Previous_Search_File_Name)

    if file_exists:
        with open(Previous_Search_File_Name, 'r', encoding='utf-8-sig') as f1:
            while True:
                Str1 = f1.readline()
                if Str1 == '\n' or Str1 == '':
                    break
                else:
                    if Str1[-1] == '\n':
                        Str2 = Str1[:-1]
                    else:
                        Str2 = Str1
                    PP_List.append(Str2)
    else:
        print('The file doex not exist')

    return PP_List

# Obtain all papers publised by an individual scholar, return a list containing all papers published by the scholar.

def Each_Scholar_Papers(Name_ID, Previous_Papers_List, Current_Search_Result_File, New_Add_Result_File):
    Paper_List = list()
    Paper_Str_List = list()
         
    S_Author = Name_ID[0]
    search_query = scholarly.search_author(S_Author)
    author = next(search_query).fill()
    
    if author.id == Name_ID[1]:
        Paper_List = author.publications
        with open(Current_Search_Result_File, 'a', encoding='utf-8') as f1:
            for pap in Paper_List:
                s1 = pap.bib['title']
                Paper_Str_List.append(s1)
                f1.write(s1 + '\n')
    else:
        print('There are more than one ', Name_ID[0], ' in Google Scholar, this program cannot perform search correctly, please check manually')
       
    ToTal = len(Paper_Str_List)

    CoUnt = 0
    while CoUnt < ToTal:

        if Paper_Str_List[CoUnt] in Previous_Papers_List:
            sfornothing = 1
        else:
            s3 = Name_ID[0] + '--' + Name_ID[1] + ': ' + Paper_List[CoUnt].bib['title'] + '\n'
            with open(New_Add_Result_File, 'a', encoding='utf-8') as f2:
                f2.write(s3) 
        CoUnt = CoUnt + 1


Search_History_List = Read_Search_History(Search_History_File)

# This is the txt file containing the latest search results

Previous_Search_File_Name = Search_History_List[-1] + '.txt'

print('The previous search date is: ', Search_History_List[-1])

with open(Search_History_File, 'a', encoding='utf-8') as file1:
    file1.write(str(now_t) + '\n')

Scholar_List = Read_Scholar_List(Scholar_List_File)

Previous_Papers_List = Read_Previous_Papers(Previous_Search_File_Name)

Run_time_number = len(Scholar_List)*40/60

print(f'Please be patient, this program will take about {Run_time_number: .3f} minutes')


with open(Current_Search_Result_File, 'w', encoding='utf-8') as f1:
    s1 = ''
    f1.write(s1)

with open(New_Add_Result_File, 'w', encoding='utf-8') as f2:
    s2 = ''
    f2.write(s2)
    
for Scholar in Scholar_List:
    Each_Scholar_Papers(Scholar, Previous_Papers_List, Current_Search_Result_File, New_Add_Result_File)

print('It is done, please check new_add_Result.txt file to see the results. If the file is empty, it means no newly added papers since last search date. Thanks for your patience!')

