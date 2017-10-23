import pandas as pd
import numpy as np

#ENIGMA BiPolar Data Sorting and Merging (MEP)
#see CodeDictionary_Enigma_Study_MEP for coding 
  
#####Begin Site 1_Cardiff####
Cardiff_FA = pd.read_csv('/home/melissa/Desktop/OriginalFiles/Cardiff_Original/Original_Cardiff_combinedROItable.csv')

#Add Columns 
Cardiff_FA.insert(0, 'Site', 'Cardiff')
Cardiff_FA.insert(1, 'Site_ID', 1)

#Rename columns
Cardiff_FA.rename(columns={'subjectID':'Subject_ID', 
                           'age':'Age_at_ToS', 
                           'diagnosis':'HC_Pat', 
                           'sex':'Sex'}, inplace=True)

#Change Coding
Cardiff_FA['Sex'].replace([2],[0],inplace=True)
Cardiff_FA['HC_Pat'].replace([1],[0],inplace=True)
Cardiff_FA['HC_Pat'].replace([2],[1],inplace=True)

#Look for duplicate subjects
pd.options.display.max_rows = (500)
print(Cardiff_FA.duplicated('Subject_ID'))

Cardiff_Clinical = pd.read_csv('/home/melissa/Desktop/OriginalFiles/Cardiff_Original/Original_Cardiff_VariableTableEnigmaBDStudy_subjectNos_wDX.csv')


#Change column names
Cardiff_Clinical.rename(columns={'Subject ID': 'Subject_ID', 
                                 'Age of Onset':'Age_of_Onset', 
                                 'Diagnosis (BP1, BP2, Control)':'Full_Diagnosis', 
                                 'Mood Phase at Time of Scan':'Mood_Phase_ToS', 
                                 'Depression Scale':'Depression_Scale', 
                                 'Depression Score at Time of Scan':'Depression_Score_ToS', 
                                 'Number of Depressive Episodes':'No_Depressive_Ep', 
                                 'Mania Scale':'Mania_Scale', 
                                 'Mania Score at time of Scan':'Mania_Score_ToS', 
                                 'Number of Manic Episodes':'No_Manic_Ep', 
                                 'Psychotic Features (Y/N – throughout Lifetime)':'Psychotic_Feat', 
                                 'Suicide Attempt  (Y/N – throughout Lifetime)':'Suicide_Attempt', 
                                 'On Medication at Time of Scan (Y/N)':'On_Med_ToS', 
                                 'Meds, Antipsychotics':'Meds_Antipsychotics', 
                                 'Length of Time on Antipsychotics':'Time_on_Antipsychotics', 
                                 'Meds, Antidepressants':'Meds_Antidepressants', 
                                 'Length of Time on Antidepressants':'Time_on_Antidepressants', 
                                 'Meds, Anticonvulsants':'Meds_Anticonvulsants', 
                                 'Length of Time on Anticonvulsants':'Time_on_Anticonvulsants', 
                                 'Lithium (y/n)':'Meds_Lithium', 
                                 'Length of Time on Lithium':'Time_on_Lithium', 
                                 'History of Alcohol Dependence (Y/N)':'Hx_Alcohol_Dep', 
                                 'Rapid Cycling (Y/N)':'Rapid_Cycling'}, inplace=True)

#Change coding 
Cardiff_Clinical.replace({'Mood_Phase_ToS' : {'euthymic' : 0}}, inplace=True)
Cardiff_Clinical.replace({'Psychotic_Feat' : {'Y' : 1, 'N' : 0}}, inplace=True)
Cardiff_Clinical.replace({'On_Med_ToS' : {'Y' : 1, 'N' : 0}}, inplace=True)

#Delete columns (checked previously for agreement between datasets, for all sites)
Cardiff_Clinical.drop(['Age at Time of Scan', 'Sex'], axis=1, inplace=True)

#Merge Recoded FA df and Clinical data frame
Cardiff_MergedFAClinical = pd.merge(Cardiff_FA, Cardiff_Clinical, how='left', on=['Subject_ID'])

####Begin Site 2_Columbia####
Columbia_FA = pd.read_csv('/home/melissa/Desktop/OriginalFiles/Columbia_Original/Original_Columbia_FA_combinedROItable.csv')

#Add Columns 
Columbia_FA.insert(0, 'Site', 'Columbia')
Columbia_FA.insert(1, 'Site_ID', 2)
Columbia_FA.insert(3, 'HC_Pat', 1)

#Standardize site names
Columbia_FA.rename(columns={'subjectID':'Subject_ID', 
                               'Age':'Age_at_ToS'}, inplace=True)

#Change Coding
Columbia_FA['Sex'].replace([2],[0],inplace=True)

#Look for duplicate subjects
pd.options.display.max_rows = (500)
print(Columbia_FA.duplicated('Subject_ID'))

Columbia_Clinical = pd.read_csv('/home/melissa/Desktop/OriginalFiles/Columbia_Original/Original_VariableTableEnigmaBDStudy_ColombiaGroup.csv') 
#subject TAB_P057 has no clinical data 

#Change Column Names
Columbia_Clinical.rename(columns={'Subject ID': 'Subject_ID', 
                                  'Age of Onset':'Age_of_Onset', 
                                  'Diagnosis (BP1, BP2, Control)':'Full_Diagnosis', 
                                  'Mood Phase at Time of Scan':'Mood_Phase_ToS', 
                                  'Depression Scale':'Depression_Scale', 
                                  'Depression Score at Time of Scan':'Depression_Score_ToS', 
                                  'Number of Depressive Episodes':'No_Depressive_Ep', 
                                  'Mania Scale':'Mania_Scale',
                                  'Mania Score at time of Scan':'Mania_Score_ToS',
                                  'Number of Manic Episodes':'No_Manic_Ep', 
                                  'Psychotic Features (Y/N – throughout Lifetime)':'Psychotic_Feat', 
                                  'Suicide Attempt  (Y/N – throughout Lifetime)':'Suicide_Attempt', 
                                  'On Medication at Time of Scan (Y/N)':'On_Med_ToS', 
                                  'Meds, Antipsychotics':'Meds_Antipsychotics', 
                                  'Length of Time on Antipsychotics':'Time_on_Antipsychotics', 
                                  'Meds, Antidepressants':'Meds_Antidepressants', 
                                  'Length of Time on Antidepressants':'Time_on_Antidepressants', 
                                  'Meds, Anticonvulsants':'Meds_Anticonvulsants', 
                                  'Length of Time on Anticonvulsants':'Time_on_Anticonvulsants', 
                                  'Lithium (y/n)':'Meds_Lithium', 
                                  'Length of Time on Lithium':'Time_on_Lithium', 
                                  'History of Alcohol Dependence (Y/N)':'Hx_Alcohol_Dep', 
                                  'Rapid Cycling (Y/N)':'Rapid_Cycling'}, inplace=True)

#Change Coding
Columbia_Clinical.replace({'Full_Diagnosis' : {'BP1' : 1, 'BP2' : 2}}, inplace=True)
Columbia_Clinical.replace({'Mood_Phase_ToS' : {'Euthymia ' : 0, 'Depression' : 1, 'Depression with mixed symptons' : 3}}, inplace=True)
Columbia_Clinical.replace({'Psychotic_Feat' : {'Y' : 1, ' Y' : 1, 'N' : 0, ' N' : 0}}, inplace=True)
Columbia_Clinical.replace({'Suicide_Attempt' : {'Y' : 1, 'N' : 0}}, inplace=True)
Columbia_Clinical.replace({'On_Med_ToS' : {'Y' : 1, 'N' : 0}}, inplace=True)
Columbia_Clinical.replace({'Meds_Antipsychotics' : {'Y' : 1, 'N' : 0}}, inplace=True)
Columbia_Clinical.replace({'Meds_Antidepressants' : {'Y' : 1, 'N' : 0}}, inplace=True)
Columbia_Clinical.replace({'Meds_Anticonvulsants' : {'Y' : 1, 'N' : 0}}, inplace=True)
Columbia_Clinical.replace({'Meds_Lithium' : {'Y' : 1, 'N' : 0}}, inplace=True)
Columbia_Clinical.replace({'Hx_Alcohol_Dep' : {'Y' : 1, 'N' : 0}}, inplace=True)
Columbia_Clinical.replace({'Rapid_Cycling' : {'Y' : 1, 'N' : 0}}, inplace=True)
#Remove Age_of_Onset where it is greater than the age at time of scan, age at time of scan matches for clinical and FA data
Columbia_Clinical.ix[53, 'Age_of_Onset']= np.nan 

#Delete columns
Columbia_Clinical.drop(['Age at Time of Scan', 'Sex'], axis=1, inplace=True)



#Merge FA and Clinical data frames, merged left as it is a patient only population 
Columbia_MergedFAClinical = pd.merge(Columbia_Clinical, Columbia_FA, how='left', on=['Subject_ID'])

####Begin Site 3_Creteil####
Creteil_FA = pd.read_csv('/home/melissa/Desktop/OriginalFiles/Creteil_Original/FA_3_Creteil_RTA.csv')

#Add Columns to Identify Site
Creteil_FA.insert(0, 'Site', 'Creteil')
Creteil_FA.insert(1, 'Site_ID', 3)

#Standardize site names
Creteil_FA.rename(columns={'subjectID':'Subject_ID', 
                              'Age':'Age_at_ToS', 
                              'DX':'HC_Pat'}, inplace=True)

#Dropped subjects ip100526 and ip100558 during DTI processing due to a renaming mistake (renamed identically) 
Creteil_Clinical = pd.read_csv('/home/melissa/Desktop/OriginalFiles/Creteil_Original/Original_Creteil_VIP_TOTAL_FITTEE3_WithID.csv')

#Standardize site names
Creteil_Clinical.rename(columns={'ID2': 'Subject_ID'}, inplace=True)

#Modify subject name if necessary to match format of FA file
Creteil_Clinical['Subject_ID'] = 'creteil__' + Creteil_Clinical['Subject_ID'].astype(str)
Creteil_Clinical['Subject_ID'] = Creteil_Clinical['Subject_ID'].astype(str).str[:-2]

#Delete columns  
Creteil_Clinical.drop(['AGEATMRI','SEX', 'ID', 'BD_HC', 'HANDEDNESS', 'SYMPTOMATIQUE', 'BRAIN_NORMALIZED',
                       'GM_NORMALIZED', 'WM_NORMALIZED', 'R_HIPP_mm3', 'L_HIPP_mm3', 'SCANNER', 
                       'HANDEDNESS',  'OH_POS_LT_SUBGROUP','BMRMS_UDINE', 'HRS17TOT', 'HRS25TOT', 
                       'TOT#PSYCHOTROP','LITHIUM_LIFETIME', 'LITHIUM_AAO_vip', 'LITH_DUR_JOSS', 
                       'DDN', 'DATE_INC'],axis=1, inplace=True)

#Note According to MRInotes, cl1004 was miscoded in clinical data as a HC

#Rename columns
Creteil_Clinical = Creteil_Clinical.rename(columns={'ID2':'Subject_ID', 
                                                    'ONSET_TYPE':'Full_Diagnosis',
                                                    'PF':'Psychotic_Feat',
                                                    'MADRS':'Depression_Score_ToS',
                                                    'YMRS':'Mania_Score_ToS', 
                                                    'AGE_AT_ONSET':'Age_of_Onset',
                                                    'ANTIPSYCH':'Meds_Antipsychotics', 
                                                    'MOODSTAB':'Meds_Anticonvulsants', 
                                                    'ANTIDEP':'Meds_Antidepressants', 
                                                    'LITHIUM':'Meds_Lithium',
                                                    'LITHIUM_DURATION_VIP':'Time_on_Lithium',
                                                    'TS':'Suicide_Attempt'})
#Removed value since flagged for verification 
Creteil_Clinical.ix[11, 'Meds_Lithium']= np.nan 

#Add columns
Creteil_Clinical.insert(0, 'Depression_Scale', 'MADRS')
Creteil_Clinical.insert(1, 'Mania_Scale', 'YMRS')
Creteil_Clinical = Creteil_Clinical.convert_objects(convert_numeric=True)
Creteil_Clinical = Creteil_Clinical.reindex(columns = np.append(Creteil_Clinical.columns.values,[
        'Mood_Phase_ToS','No_Depressive_Ep', 'No_Manic_Ep', 'On_Med_ToS', 
        'Time_on_Antipsychotics', 'Time_on_Antidepressants', 'Time_on_Anticonvulsants', 'Hx_Alcohol_Dep', 
        'Rapid_Cycling',]))

for i, row in Creteil_Clinical.iterrows():
    if row['Meds_Antipsychotics' or 'Meds_Anticonvulsants' or 'Meds_Antidepressants' or 'Meds_Lithium'] == 1:
        Creteil_Clinical.ix[i,'On_Med_ToS']=1
    elif row['Meds_Antipsychotics' or 'Meds_Anticonvulsants' or 'Meds_Antidepressants' or 'Meds_Lithium'] == 0:
        Creteil_Clinical.ix[i,'On_Med_ToS']=0
    else: Creteil_Clinical.ix[i,'On_Med_ToS']=np.nan

Creteil_MergedFAClinical = pd.merge(Creteil_Clinical, Creteil_FA, how='right', on= 'Subject_ID')

#Populate cells 
Creteil_MergedFAClinical['Age_of_Onset'] = Creteil_MergedFAClinical['Age_at_ToS'] - Creteil_MergedFAClinical['Illness_Duration']
Creteil_MergedFAClinical.drop('Illness_Duration', axis=1, inplace=True)

####----Begin Site 4_Edinburgh----####
#Deleted subjects SF099 (SZ dx), SF060, SF076 and SF096 (BP-NOS) prior to script

Edinburgh_FA = pd.read_csv('/home/melissa/Desktop/OriginalFiles/Edinburgh_Original/Originanl_Edinburgh_4_combinedROItablew_sexIncluded.csv')

#Add Columns to Identify Site
Edinburgh_FA.insert(0, 'Site', 'Edinburgh')
Edinburgh_FA.insert(1, 'Site_ID', 4)

#Standardize site names
Edinburgh_FA.rename(columns={'subjectID':'Subject_ID', 
                             'Age':'Age_at_ToS', 
                             'Diagnosis':'HC_Pat', 
                             'Gender':'Sex'}, inplace=True)

#Delete subjects not meeting inclusion criteria 
Edinburgh_FA = Edinburgh_FA[(Edinburgh_FA.Age_at_ToS < 66) & (Edinburgh_FA.Age_at_ToS > 18)]

#Change Coding  
Edinburgh_FA.replace({'Sex' : {'F' : 0, ' F' : 0, 'M' : 0, ' M' : 1}}, inplace=True)

#Look for duplicate subjects
pd.options.display.max_rows = (500)
print(Edinburgh_FA.duplicated('Subject_ID'))

#Recoded medicines to proper categories, left blank where there were ? prior to scripting
Edinburgh_Clinical = pd.read_csv('/home/melissa/Desktop/OriginalFiles/Edinburgh_Original/Edinburgh_4_CombinedVariableTableEnigmaBDStudy_MedsRecoded_FullDx.csv')

#Delete columns 
Edinburgh_Clinical.drop(['Age at Time of Scan', 'Sex'], axis=1, inplace=True)

#Change Relevant Column Names
Edinburgh_Clinical.rename(columns={'Subject ID': 'Subject_ID', 
                                   'Age of Onset':'Age_of_Onset', 
                                   'Diagnosis (BP1, BP2, Control)':'Full_Diagnosis', 
                                   'Mood Phase at Time of Scan':'Mood_Phase_ToS', 
                                   'Depression Scale':'Depression_Scale', 
                                   'Depression Score at Time of Scan':'Depression_Score_ToS', 
                                   'Number of Depressive Episodes':'No_Depressive_Ep', 
                                   'Mania Scale':'Mania_Scale', 
                                   'Mania Score at time of Scan':'Mania_Score_ToS', 
                                   'Number of Manic Episodes':'No_Manic_Ep', 
                                   'Psychotic Features (Y/N – throughout Lifetime)':'Psychotic_Feat', 
                                   'Suicide Attempt  (Y/N – throughout Lifetime)':'Suicide_Attempt', 
                                   'On Medication at Time of Scan (Y/N)':'On_Med_ToS', 
                                   'Meds, Antipsychotics':'Meds_Antipsychotics', 
                                   'Length of Time on Antipsychotics':'Time_on_Antipsychotics', 
                                   'Meds, Antidepressants':'Meds_Antidepressants', 
                                   'Length of Time on Antidepressants':'Time_on_Antidepressants', 
                                   'Meds, Anticonvulsants':'Meds_Anticonvulsants', 
                                   'Length of Time on Anticonvulsants':'Time_on_Anticonvulsants', 
                                   'Lithium (y/n)':'Meds_Lithium', 
                                   'Length of Time on Lithium':'Time_on_Lithium', 
                                   'History of Alcohol Dependence (Y/N)':'Hx_Alcohol_Dep', 
                                    'Rapid Cycling (Y/N)':'Rapid_Cycling'}, inplace=True)

#Change Coding 
Edinburgh_Clinical.replace({'Full_Diagnosis' : {'Control': 0, 'BP1': 1}}, inplace=True)
Edinburgh_Clinical.replace({'On_Med_ToS' : {'Y' : 1, 'N' : 0}}, inplace=True)

#replace N 
Edinburgh_Clinical['Depression_Score_ToS']= Edinburgh_Clinical['Depression_Score_ToS'].replace('N', np.nan)

#Merge Recoded FA and Clinical data frames
Edinburgh_MergedFAClinical = pd.merge(Edinburgh_Clinical, Edinburgh_FA, how='right', on='Subject_ID')

####Begin Site 5_EdinburghSiteE####
EdinburghSiteE_FA = pd.read_csv('/home/melissa/Desktop/OriginalFiles/Edinburgh_Original/Original_Edinburgh_5_emotion_results_Clara_Alloza.csv')

#Add Columns to Identify Site
EdinburghSiteE_FA.insert(0, 'Site', 'EdinburghSiteE')
EdinburghSiteE_FA.insert(1, 'Site_ID', 5)

#Change Relevant Column Names
EdinburghSiteE_FA.rename(columns={'subjectID':'Subject_ID', 'age':'Age_at_ToS', 'diagnosis':'HC_Pat', 
                                  'sex': 'Sex'}, inplace=True)

#Round up age 
EdinburghSiteE_FA['Age_at_ToS'] = np.ceil(EdinburghSiteE_FA['Age_at_ToS'])

#Delete any subjects not meeting inclusion criteria
EdinburghSiteE_FA = EdinburghSiteE_FA[(EdinburghSiteE_FA.Age_at_ToS < 66) & (EdinburghSiteE_FA.Age_at_ToS > 17)]

#Change Coding 
EdinburghSiteE_FA['Sex'].replace([1],[0],inplace=True)
EdinburghSiteE_FA['Sex'].replace([0],[1],inplace=True)

#Look for duplicate subjects
pd.options.display.max_rows = (500)
print(EdinburghSiteE_FA.duplicated('Subject_ID'))

EdinburghSiteE_Clinical = pd.read_csv('/home/melissa/Desktop/OriginalFiles/Edinburgh_Original/Edinburgh_5_CombinedVariableTableEnigmaBDStudy_MedsRecoded_FullDx.csv')

#Delete columns 
EdinburghSiteE_Clinical.drop(['Age at Time of Scan', 'Sex'], axis=1, inplace=True)

EdinburghSiteE_Clinical.rename(columns={'Subject ID':'Subject_ID', 
                                        'Age of Onset':'Age_of_Onset', 
                                        'Diagnosis (BP1, BP2, Control)':'Full_Diagnosis', 
                                        'Mood Phase at Time of Scan':'Mood_Phase_ToS', 
                                        'Depression Scale':'Depression_Scale', 
                                        'Depression Score at Time of Scan':'Depression_Score_ToS', 
                                        'Number of Depressive Episodes':'No_Depressive_Ep', 
                                        'Mania Scale':'Mania_Scale', 
                                        'Mania Score at time of Scan':'Mania_Score_ToS', 
                                        'Number of Manic Episodes':'No_Manic_Ep', 
                                        'Psychotic Features (Y/N – throughout Lifetime)':'Psychotic_Feat', 
                                        'Suicide Attempt  (Y/N – throughout Lifetime)':'Suicide_Attempt', 
                                        'On Medication at Time of Scan (Y/N)':'On_Med_ToS', 
                                        'Meds, Antipsychotics':'Meds_Antipsychotics', 
                                        'Length of Time on Antipsychotics':'Time_on_Antipsychotics', 
                                        'Meds, Antidepressants':'Meds_Antidepressants', 
                                        'Length of Time on Antidepressants':'Time_on_Antidepressants', 
                                        'Meds, Anticonvulsants':'Meds_Anticonvulsants', 
                                        'Length of Time on Anticonvulsants':'Time_on_Anticonvulsants', 
                                        'Lithium (y/n)':'Meds_Lithium', 
                                        'Length of Time on Lithium':'Time_on_Lithium', 
                                        'History of Alcohol Dependence (Y/N)':'Hx_Alcohol_Dep', 
                                        'Rapid Cycling (Y/N)':'Rapid_Cycling'}, inplace=True)

#Change Coding 
EdinburghSiteE_Clinical.replace({'Full_Diagnosis' : {'Control': 0, 'BP1': 1}}, inplace=True)
EdinburghSiteE_Clinical.replace({'On_Med_ToS' : {'Y' : 1, 'N' : 0}}, inplace=True)
EdinburghSiteE_Clinical['Depression_Score_ToS']= EdinburghSiteE_Clinical['Depression_Score_ToS'].replace('N', np.nan)

#Merge FA and Clinical data frames
EdinburghSiteE_MergedFAClinical = pd.merge(EdinburghSiteE_Clinical, EdinburghSiteE_FA, how='left', on='Subject_ID')

####Begin Site 6_FIDMAG####
FIDMAG_FA = pd.read_csv('/home/melissa/Desktop/OriginalFiles/FIDMAG_Original/Original_FIDMAG_enigma_combinedROItable_FA_pomarol-clotet.csv')

#Add Columns to Identify Site
FIDMAG_FA.insert(0, 'Site', 'FIDMAG')
FIDMAG_FA.insert(1, 'Site_ID', 6)

#Standardize site names
FIDMAG_FA.rename(columns={'subjectID':'Subject_ID', 
                          'Age':'Age_at_ToS', 
                          'Dx':'HC_Pat', 
                          'Sex':'Sex'}, inplace=True)

#Change Coding 
FIDMAG_FA['Sex'].replace([2],[0],inplace=True)

#Look for duplicate subjects
pd.options.display.max_rows = (500)
print(FIDMAG_FA.duplicated('Subject_ID'))

FIDMAG_Clinical = pd.read_csv('/home/melissa/Desktop/OriginalFiles/FIDMAG_Original/Original_FIDMAG_enigma_dti_paris_clinicalvariables .csv')

#Delete columns 
FIDMAG_Clinical.drop(['Age at Time of Scan', 'Sex'], axis=1, inplace=True)

#Change Relevant Column Names
FIDMAG_Clinical.rename(columns={'subjectID':'Subject_ID', 
                                'Age of Onset':'Age_of_Onset', 
                                'Diagnosis':'Full_Diagnosis', 
                                'Mood Phase at Time of Scan':'Mood_Phase_ToS', 
                                'Depression Scale':'Depression_Scale', 
                                'Depression Score at Time of Scan':'Depression_Score_ToS', 
                                'Number of Depressive Episodes':'No_Depressive_Ep', 
                                'Mania Scale':'Mania_Scale', 
                                'Mania Score at time of Scan':'Mania_Score_ToS', 
                                'Number of Manic Episodes':'No_Manic_Ep', 
                                'Psychotic Features (Y/N – throughout Lifetime)':'Psychotic_Feat', 
                                'Suicide Attempt  (Y/N – throughout Lifetime)':'Suicide_Attempt', 
                                'On Medication at Time of Scan (Y/N)':'On_Med_ToS', 
                                'Meds, Antipsychotics':'Meds_Antipsychotics', 
                                'Length of Time on Antipsychotics':'Time_on_Antipsychotics', 
                                'Meds, Antidepressants':'Meds_Antidepressants', 
                                'Length of Time on Antidepressants':'Time_on_Antidepressants', 
                                'Meds, Anticonvulsants':'Meds_Anticonvulsants',
                                'Length of Time on Anticonvulsants':'Time_on_Anticonvulsants',
                                'Lithium (y/n)':'Meds_Lithium',
                                'Length of Time on Lithium':'Time_on_Lithium',
                                'History of Alcohol Dependence (Y/N)':'Hx_Alcohol_Dep', 
                                'Rapid Cycling (Y/N)':'Rapid_Cycling'}, inplace=True)

#Change Coding
FIDMAG_Clinical.replace({'Full_Diagnosis' : {'Control' : 0, 'BP1' : 1, 'BP2' : 2}}, inplace=True)
FIDMAG_Clinical.replace({'Mood_Phase_ToS' : {'Euthymia' : 0}}, inplace=True)
FIDMAG_Clinical.replace({'Psychotic_Feat' : {'Y' : 1, 'N' : 0}}, inplace=True)
FIDMAG_Clinical.replace({'On_Med_ToS' : {'Y' : 1, 'N' : 0}}, inplace=True)
FIDMAG_Clinical.replace({'Meds_Antipsychotics' : {'Y' : 1, 'N' : 0}}, inplace=True)
FIDMAG_Clinical.replace({'Meds_Antidepressants' : {'Y' : 1, 'N' : 0}}, inplace=True)
FIDMAG_Clinical.replace({'Meds_Anticonvulsants' : {'Y' : 1, 'N' : 0}}, inplace=True)
FIDMAG_Clinical.replace({'Meds_Lithium' : {'Y' : 1, 'N' : 0}}, inplace=True)
FIDMAG_Clinical.replace({'Rapid_Cycling' : {'Y' : 1, 'N' : 0}}, inplace=True)
#CodedDepressive episodes with estimate as exact number not known, may want to drop later 
FIDMAG_Clinical = FIDMAG_Clinical.replace('>10', 15)
FIDMAG_Clinical = FIDMAG_Clinical.replace('6-10(>5<11)', 8)
FIDMAG_Clinical = FIDMAG_Clinical.replace('missing', np.nan)
FIDMAG_Clinical = FIDMAG_Clinical.replace('no info', np.nan)
FIDMAG_Clinical.convert_objects(convert_numeric=True)

FIDMAG_MergedFAClinical = pd.merge(FIDMAG_FA, FIDMAG_Clinical, on='Subject_ID')

####Begin Site 7_Grenoble####
Grenoble_FA = pd.read_csv('/home/melissa/Desktop/OriginalFiles/Grenoble_Original/FA_7_grenoblePhillips_RTA.csv')

#Add Columns to Identify Site
Grenoble_FA.insert(0, 'Site', 'Grenoble')
Grenoble_FA.insert(1, 'Site_ID', 7)

#Standardize site names
Grenoble_FA.rename(columns={'subjectID':'Subject_ID', 'Age':'Age_at_ToS', 'DX':'HC_Pat', 'Sex':'Sex'}, inplace=True)

#Look for duplicate subjects
pd.options.display.max_rows = (500)
print(Grenoble_FA.duplicated('Subject_ID'))

Grenoble_Clinical = pd.read_csv('/home/melissa/Desktop/OriginalFiles/Grenoble_Original/Original_GrenobleClinicalVariables_wMeds_delsubj.csv')

#Delete columns 
Grenoble_Clinical.drop(['Age', 'Sexe', 'Patient','Groupe','Machine','Comorbidités','Durée moy maladie', 'Traitement','QIDS1',
                        'Altman1', 'Nb Hypomaniques'], axis=1, inplace=True)

#Change Relevant Column Names
Grenoble_Clinical.rename(columns={'N°':'Subject_ID', 
                                  'Type':'Full_Diagnosis', 
                                  'Age 1er épisode':'Age_of_Onset', 
                                  'Nb EDM':'No_Depressive_Ep', 
                                  'Nb Maniaques':'No_Manic_Ep',
                                  'Symptômes psychotiques ':'Psychotic_Feat', 
                                  'MADRS1':'Depression_Score_ToS', 
                                  'YMRS1':'Mania_Score_ToS', 
                                  'On Meds at Time of Scan' :'On_Med_ToS', 
                                  'Antipsychotic':'Meds_Antipsychotics', 
                                  'Antidepressant':'Meds_Antidepressants', 
                                  'Anticonvulsivant':'Meds_Anticonvulsants', 
                                  'Lithium':'Meds_Lithium'}, inplace=True)

#Add missing columns
Grenoble_Clinical = Grenoble_Clinical.reindex(columns = np.append(Grenoble_Clinical.columns.values,[
        'Mood_Phase_ToS', 'Suicide_Attempt', 'Time_on_Antipsychotics','Time_on_Antidepressants', 
        'Time_on_Anticonvulsants', 'Time_on_Lithium', 'Hx_Alcohol_Dep', 'Rapid_Cycling']))
Grenoble_Clinical.insert(0, 'Depression_Scale', 'HDRS21')
Grenoble_Clinical.insert(1, 'Mania_Scale', 'YMRS')

#Replace missing, Not applicable, not completed etc. values with NaN
Grenoble_Clinical = Grenoble_Clinical.replace('?', np.nan)
Grenoble_Clinical = Grenoble_Clinical.convert_objects(convert_numeric=True)

#Merge FA and Clinical data frames
Grenoble_MergedFAClinical = pd.merge(Grenoble_Clinical, Grenoble_FA, how='right', on='Subject_ID')

####Begin Site 8_Institute0fLiving####
#no clinical variables sent (via email informed all BP1)
IoL13_FA = pd.read_csv('/home/melissa/Desktop/OriginalFiles/InstituteOfLiving_Original/InstituteOfLiving13_Original_combinedROItable_FA_HC_BP.csv')

#Add Columns to Identify Site
IoL13_FA.insert(0, 'Site', 'Institute_Of_Living13')
IoL13_FA.insert(1, 'Site_ID', 8)

#Delete columns
IoL13_FA.drop('DTI_directions', axis=1, inplace=True)

#Standardize site names
IoL13_FA.rename(columns={'SubjID':'Subject_ID', 
                         'Age':'Age_at_ToS', 
                         'Dx':'HC_Pat', 
                         'Sex':'Sex'}, inplace=True)

#Round up age 
IoL13_FA['Age_at_ToS'] = np.ceil(IoL13_FA['Age_at_ToS'])

#Delete subjects not meeting inclusion criteria 
IoL13_FA = IoL13_FA[(IoL13_FA.Age_at_ToS < 66) & (IoL13_FA.Age_at_ToS > 17)]

#Change Coding 
IoL13_FA['Sex'].replace([2],[0],inplace=True)

#Look for duplicate subjects
pd.options.display.max_rows = (500)
print(IoL13_FA.duplicated('Subject_ID'))

#Create clinical database
IoL13_MergedFAClinical = IoL13_FA.copy()

#add missing columns
def Full_Diagnosis(c):
  if c['HC_Pat'] == 1:
    return 1
  else:
    return 0

IoL13_MergedFAClinical['Full_Diagnosis'] = IoL13_MergedFAClinical.apply(Full_Diagnosis, axis=1)
IoL13_MergedFAClinical = IoL13_MergedFAClinical.reindex(columns = np.append(IoL13_MergedFAClinical.columns.values,[
        'Age_of_Onset', 'Mood_Phase_ToS', 'Depression_Scale', 'Depression_Score_ToS', 'No_Depressive_Ep', 
        'Mania_Scale', 'Mania_Score_ToS', 'No_Manic_Ep', 'Psychotic_Feat', 'Suicide_Attempt', 'On_Med_ToS', 
        'Meds_Antipsychotics', 'Time_on_Antipsychotics', 'Meds_Antidepressants', 'Time_on_Antidepressants', 
        'Meds_Anticonvulsants', 'Time_on_Anticonvulsants', 'Meds_Lithium', 'Time_on_Lithium', 'Hx_Alcohol_Dep', 
        'Rapid_Cycling']))

# Subjects removed, too many controls
IoL13_toremove =('S1260WTI','S2779GCK','S8392NUP','S2411YRE','S9594NUM','S9891SUD','S9164QNP','S8167RWF','S6874XAB',
                 'S2912DAK','S8853CUS','S8252CRG','S1892OCW','S7931SQF','S2974TST','S6259XGT','S3376HWB','S8141MTQ',
                 'S6561XSB','S8857VBM','S5469TCN','S6129OKP','S2618SQH','S5550MCJ','S9615FEQ','S0541IWS','S7762HMP',
                 'S6043GRM','S9849QJP','S5845LGL','S6179FPC','S7454EUD','S7007XNF','S5541BCJ','S1210DLO','S9490SSR',
                 'S8411FIT','S4196BOL','S5446BQT','S8576PIY','S2622WKG','S1572VCJ','S6760LPC','S9578NRP','S5546BHB',
                 'S4091FIF','S7683GTJ','S0081BSS','S4638JVN','S8842WMC','S2123BFU','S5201MEI','S8300YIO','S3719HID',
                 'S3242OBA','S1915TUF')

IoL13_FA_SubjRemoved = IoL13_FA.copy()
IoL13_FA_SubjRemoved = IoL13_FA_SubjRemoved[~IoL13_FA_SubjRemoved.Subject_ID.isin(IoL13_toremove)]

####Begin Site 9_Institute0fLiving####
#no clinical variables sent (via email informed all BP1)
IoL33_FA = pd.read_csv('/home/melissa/Desktop/OriginalFiles/InstituteOfLiving_Original/InstituteOfLiving33_Original_combinedROItable_FA_HC_BP.csv')

#Add Columns to Identify Site
IoL33_FA.insert(0, 'Site', 'Institute_Of_Living33')
IoL33_FA.insert(1, 'Site_ID', 9)

#Delete Columns
IoL33_FA.drop('DTI_directions', axis=1, inplace=True)

#Standardize site names
IoL33_FA.rename(columns={'SubjID':'Subject_ID', 
                         'Age':'Age_at_ToS', 
                         'Dx':'HC_Pat', 
                         'Sex':'Sex'}, inplace=True)

#Round up age 
IoL33_FA['Age_at_ToS'] = np.ceil(IoL33_FA['Age_at_ToS'])

#Delete any subjects not meeting inclusion criteria 
IoL33_FA = IoL33_FA[(IoL33_FA.Age_at_ToS < 66) & (IoL33_FA.Age_at_ToS > 17)]

#Change Coding for Sex 
IoL33_FA['Sex'].replace([2],[0],inplace=True)

#Look for duplicate subjects
pd.options.display.max_rows = (500)
print(IoL33_FA.duplicated('Subject_ID'))

#delete duplicate
IoL33_FA.drop(75, inplace=True)

#Create Clinical database
IoL33_MergedFAClinical = IoL33_FA.copy()
 
#add missing columns
def Full_Diagnosis(c):
  if c['HC_Pat'] == 1:
    return 1
  else:
    return 0
IoL33_MergedFAClinical['Full_Diagnosis'] = IoL33_MergedFAClinical.apply(Full_Diagnosis, axis=1)
IoL33_MergedFAClinical = IoL33_MergedFAClinical.reindex(columns = np.append(IoL33_MergedFAClinical.columns.values,[
        'Age_of_Onset', 'Mood_Phase_ToS', 'Depression_Scale', 'Depression_Score_ToS', 'No_Depressive_Ep', 
        'Mania_Scale', 'Mania_Score_ToS', 'No_Manic_Ep', 'Psychotic_Feat', 'Suicide_Attempt', 'On_Med_ToS', 
        'Meds_Antipsychotics', 'Time_on_Antipsychotics', 'Meds_Antidepressants', 'Time_on_Antidepressants', 
        'Meds_Anticonvulsants', 'Time_on_Anticonvulsants', 'Meds_Lithium', 'Time_on_Lithium', 'Hx_Alcohol_Dep', 
        'Rapid_Cycling']))

# Subjects removed for case_control analysis, too many controls
IoL33_toremove = ('S0389LIM','S3469ISO','S0159AUC','S0647WBY','S1269OEQ','S9247DXR','S6934WON','S5819PJA',
                  'S1018ITD','S7093LJB','S3802KJL','S4229JBX','S4943ZOF','S2201XMU','S6900JCB','S6217NJG',
                  'S3378AKT','S5018RSS','S5935UGF','S2360CUJ','S1488NWV','S3711USN','S5079RNF','S2526ICQ',
                  'S9684VWA','S6775PBB','S2182YRV','S4618MNB','S0878FHW','S2838OUO','S3711USN','S3804KNQ',
                  'S7111TQA','S1427UVC','S8126VTN','S1905ZJZ','S1900OAM','S2327QOB','S2729XJY','S4839NKG',
                  'S5718HNK','S7990EIK','S3468SYK','S9290GKG','S9164NLS','S8962KPV','S7876QKD','S9444EXN',
                  'S8947SHJ','S9166ASM','S5267JXD','S4156MHN','S9379GPQ','S7940LAO','S0603HBA','S4286VMA',
                  'S0439YVY','S1275GPL','S7786UUR','S8183KRJ','S9124JRS','S0827GHX','S6508TMJ','S7915HAP',
                  'S6578UWX','S9028KLS','S7130BYS','S7678QZY','S2604GVG','S1296COO','S6429ETK','S3947AQI',
                  'S9093HMV','S9611DVF','S2167PIJ','S3904JTO','S7314KOV','S8858GKD','S2778IBY','S6727OFM',
                  'S8726FNA','S8244XWY','S9923CLE','S6368KOU','S5545LLM','S0124EZU','S6399FUN','S4153AUB',
                  'S5439VSF','S1656CFQ','S6410WWN','S8156OYE','S3556API','S1185KUS','S8891QRR','S4170MOW',
                  'S1584SYP','S9350VNS','S8900JLD','S3749DMX','S7696TMK','S9776EET','S2491ITM','S4759JUG',
                  'S2764BCQ','S6691OOE','S6508YJC','S3459KUP','S7903AIX','S7922RIC','S9059XNO','S9910MZF',
                  'S7151BAG','S4946KTR','S6837OLP','S0510LYX','S5214DDN','S5208PVK','S2993THI','S8072RYL',
                  'S7517JYD','S1164ITV','S2580MVH','S9861XOL','S1423AKL','S4406FDQ','S2270NGY','S3310OJM',
                  'S7686EPB','S6800KAG','S7977FOT','S3814IAH','S7070DWQ','S3273PKY','S6357HHF','S7357OZI',
                  'S7558SYT','S6448SDD','S1705QXD','S3703UGY','S7765SJH','S0868FEI','S5373TBZ','S1755UVS',
                  'S7890KXD','S9718JDB','S6937JKF','S5858RDW','S6070YAK','S8262IWP','S4833LYS','S4069QIE',
                  'S7560LRV','S0732MME','S3591OWB','S6003CLT','S7469DFU','S6835JEL','S1344GIO','S2751KTE',
                  'S4756HAI','S9377JWE','S7464HIO','S5713USL')

IoL33_FA_SubjRemoved = IoL33_FA.copy()
IoL33_FA_SubjRemoved = IoL33_FA_SubjRemoved[~IoL33_FA_SubjRemoved.Subject_ID.isin(IoL33_toremove)]

####Begin Site 10_Institute0fLiving####
#no clinical variables sent (via email informed all BP1)
IoL58_FA = pd.read_csv('/home/melissa/Desktop/OriginalFiles/InstituteOfLiving_Original/InstituteOfLiving58_Original_combinedROItable_FA_HC_BP.csv')

#Add Columns to Identify Site
IoL58_FA.insert(0, 'Site', 'Institute_Of_Living58')
IoL58_FA.insert(1, 'Site_ID', 10)

#Standardize site names
IoL58_FA.rename(columns={'SubjID':'Subject_ID', 
                         'Age':'Age_at_ToS', 
                         'Dx':'HC_Pat', 
                         'Sex':'Sex'}, inplace=True)

#Round up age 
IoL58_FA['Age_at_ToS'] = np.ceil(IoL58_FA['Age_at_ToS'])

#Delete subjects not meeting inclusion criteria 
IoL58_FA = IoL58_FA[(IoL58_FA.Age_at_ToS < 66) & (IoL58_FA.Age_at_ToS > 17)]

#Change Coding 
IoL58_FA['Sex'].replace([2],[0],inplace=True)

#Delete unnecessary columns
IoL58_FA.drop('DTI_directions', axis=1, inplace=True)

#Look for duplicate subjects
pd.options.display.max_rows = (500)
print(IoL58_FA.duplicated('Subject_ID'))

#Create Clinical database
IoL58_MergedFAClinical = IoL58_FA.copy()
 
#add missing columns
def Full_Diagnosis(c):
  if c['HC_Pat'] == 1:
    return 1
  else:
    return 0

IoL58_MergedFAClinical['Full_Diagnosis'] = IoL58_MergedFAClinical.apply(Full_Diagnosis, axis=1)
IoL58_MergedFAClinical = IoL58_MergedFAClinical.reindex(columns = np.append(IoL58_MergedFAClinical.columns.values,[
        'Age_of_Onset', 'Mood_Phase_ToS', 'Depression_Scale', 'Depression_Score_ToS', 'No_Depressive_Ep', 
        'Mania_Scale', 'Mania_Score_ToS', 'No_Manic_Ep', 'Psychotic_Feat', 'Suicide_Attempt', 'On_Med_ToS', 
        'Meds_Antipsychotics', 'Time_on_Antipsychotics', 'Meds_Antidepressants', 'Time_on_Antidepressants', 
        'Meds_Anticonvulsants', 'Time_on_Anticonvulsants', 'Meds_Lithium', 'Time_on_Lithium', 'Hx_Alcohol_Dep', 
        'Rapid_Cycling']))

####Begin Site 11_KI####
KI_FA = pd.read_csv("/home/melissa/Desktop/OriginalFiles/KI_Original/Original_KI_SBPcombinedROItable_covars.csv")

#Add Columns to Identify Site
KI_FA.insert(0, 'Site', 'KI')
KI_FA.insert(1, 'Site_ID', 11)

#Standardize site names
KI_FA.rename(columns={'ENIGMA_DTI_Subj_code':'Subject_ID', 
                      'Age':'Age_at_ToS', 
                      'Patient':'HC_Pat'}, inplace=True)

#Delete any subjects not meeting inclusion criteria 
KI_FA = KI_FA[(KI_FA.Age_at_ToS < 66) & (KI_FA.Age_at_ToS > 17)]
KI_FA = KI_FA.ix[~(KI_FA['Diag'] == 'other')]

#Delete columns 
KI_FA.drop(['ICV_L', 'Diag'], axis=1, inplace=True)

#Look for duplicate subjects
pd.options.display.max_rows = (500)
print(KI_FA.duplicated('Subject_ID'))

KI_Clinical = pd.read_csv('/home/melissa/Desktop/OriginalFiles/KI_Original/Original_KI_VariableTableEnigmaBPStudy_SBP_FOLLOWUP_FINAL_shared.csv')

#Delete subjects not meeting inclusion criteria 
KI_Clinical = KI_Clinical.ix[~(KI_Clinical['Diagnosis (BP1, BP2, Control)'] == 'other')]

#Delete columns 
KI_Clinical.drop(['Age at Time of Scan', 'Sex'], axis=1, inplace=True)

#Change Relevant Column Names
KI_Clinical.rename(columns={'Subject ID ENIGMA': 'Subject_ID', 
                            'Age of Onset':'Age_of_Onset', 
                            'Diagnosis (BP1, BP2, Control)':'Full_Diagnosis', 
                            'Mood Phase at Time of Scan':'Mood_Phase_ToS', 
                            'Depression Scale':'Depression_Scale', 
                            'Depression Score at Time of Scan':'Depression_Score_ToS', 
                            'Number of Depressive Episodes':'No_Depressive_Ep', 
                            'Mania Scale':'Mania_Scale', 
                            'Mania Score at time of Scan':'Mania_Score_ToS', 
                            'Number of Manic Episodes':'No_Manic_Ep', 
                            'Psychotic Features (Y/N – throughout Lifetime)':'Psychotic_Feat', 
                            'Suicide Attempt  (Y/N – throughout Lifetime)':'Suicide_Attempt', 
                            'On Medication at Time of Scan (Y/N)':'On_Med_ToS', 
                            'Meds, Antipsychotics':'Meds_Antipsychotics', 
                            'Length of Time on Antipsychotics':'Time_on_Antipsychotics', 
                            'Meds, Antidepressants':'Meds_Antidepressants', 
                            'Length of Time on Antidepressants':'Time_on_Antidepressants', 
                            'Meds, Anticonvulsants':'Meds_Anticonvulsants', 
                            'Length of Time on Anticonvulsants':'Time_on_Anticonvulsants', 
                            'Lithium (y/n)':'Meds_Lithium', 
                            'Length of Time on Lithium':'Time_on_Lithium', 
                            'History of Alcohol Dependence (Y/N)':'Hx_Alcohol_Dep', 
                            'Rapid Cycling (Y/N)':'Rapid_Cycling'}, inplace=True)

#Change coding 
KI_Clinical.replace({'Full_Diagnosis' : {'Control' : 0, 'BP1' : 1, 'BP2' : 2}}, inplace=True)
KI_Clinical.replace({'Mood_Phase_ToS' : {'euthymia' : 0}}, inplace=True)
KI_Clinical.replace({'Psychotic_Feat' : {'Y' : 1, 'N' : 0}}, inplace=True)
KI_Clinical.replace({'On_Med_ToS' : {'Y' : 1, 'N' : 0}}, inplace=True)
KI_Clinical.replace({'Meds_Antipsychotics' : {'Y' : 1, 'N' : 0}}, inplace=True)
KI_Clinical.replace({'Meds_Antidepressants' :{'Y' : 1, 'N' : 0}}, inplace=True)
KI_Clinical.replace({'Meds_Anticonvulsants' : {'Y' : 1, 'N' : 0}}, inplace=True)
KI_Clinical.replace({'Meds_Lithium' : {'Y' : 1, 'N' : 0}}, inplace=True)
KI_Clinical.replace({'Hx_Alcohol_Dep' : {'Y' : 1, 'N' : 0}}, inplace=True)
KI_Clinical.replace({'Rapid_Cycling' : {'Y' : 1, 'N' : 0}}, inplace=True)
#Remove Age_of_Onset where it is greater than the age at time of scan, age at time of scan matches for clinical and FA data
KI_Clinical.ix[(94, 88, 76, 74, 68, 58, 33), 'Age_of_Onset']= np.nan 


#Merge FA and Clinical data frames
KI_MergedFAClinical = pd.merge(KI_Clinical, KI_FA, how='right', on='Subject_ID')


#Subjects removed for case_control analysis, too many patients
KI_toremove = (49,43,74,79,65,19,26,56,91,62,31,25,47,57,18,34,93,27,87,61,71,101,75,66,32,48,39,20,103,78,76,38,102,
               24,44,28,29,92,70)

KI_FA_SubjRemoved = KI_FA
KI_FA_SubjRemoved = KI_FA_SubjRemoved[~KI_FA_SubjRemoved.Subject_ID.isin(KI_toremove)]

#Start Site 13 Muenster
Muenster_FA = pd.read_csv('/home/melissa/Desktop/OriginalFiles/Muenster_Original/Original_muenster_combinedROItable.csv')

#Add Columns to Identify Site
Muenster_FA.insert(0, 'Site', 'Muenster')
Muenster_FA.insert(1, 'Site_ID', 13)

#Standardize site names
Muenster_FA.rename(columns={'subjectID':'Subject_ID', 
                            'Age':'Age_at_ToS', 
                            'Sex':'Sex', 
                            'AffectionStatus' :'HC_Pat'}, inplace=True)

#Delete subjects not meeting inclusion criteria 
Muenster_FA = Muenster_FA[(Muenster_FA.Age_at_ToS < 66) & (Muenster_FA.Age_at_ToS > 17)]

#Change Coding 
Muenster_FA['Sex'].replace([2],[0],inplace=True)

#Look for duplicate subjects
pd.options.display.max_rows = (500)
print(Muenster_FA.duplicated('Subject_ID'))

Muenster_Clinical = pd.read_csv('/home/melissa/Desktop/OriginalFiles/Muenster_Original/Original_Covariates_Muenster_fixed.csv')

#Modify subject_ID to match format of FA file
Muenster_Clinical['Subject ID'] = Muenster_Clinical['Subject ID'].astype(str).str[0:5]+ '_FA'

#Change Relevant Column Names
Muenster_Clinical.rename(columns={'Subject ID':'Subject_ID', 
                                  'Age of Onset ':'Age_of_Onset', 
                                  'Diagnosis (BP1, BP2, Control)':'Full_Diagnosis', 
                                  'Mood Phase at Time of Scan':'Mood_Phase_ToS', 
                                  'Depression Scale ':'Depression_Scale', 
                                  'Depression Score at Time of Scan':'Depression_Score_ToS', 
                                  'Number of Depressive Episodes ':'No_Depressive_Ep', 
                                  'Mania Scale':'Mania_Scale', 
                                  'Mania Score at time of Scan':'Mania_Score_ToS', 
                                  'Number of Manic Episodes ':'No_Manic_Ep', 
                                  'Psychotic Features (Y/N – throughout Lifetime)':'Psychotic_Feat', 
                                  'Suicide Attempt  (Y/N – throughout Lifetime)':'Suicide_Attempt', 
                                  'On Medication at Time of Scan (Y/N)':'On_Med_ToS', 
                                  'Meds, Antipsychotics ':'Meds_Antipsychotics', 
                                  'Length of Time on Antipsychotics':'Time_on_Antipsychotics', 
                                  'Meds, Antidepressants ':'Meds_Antidepressants', 
                                  'Length of Time on Antidepressants':'Time_on_Antidepressants', 
                                  'Meds, Anticonvulsants ':'Meds_Anticonvulsants', 
                                  'Length of Time on Anticonvulsants':'Time_on_Anticonvulsants', 
                                  'Lithium (y/n)':'Meds_Lithium',
                                  'Length of Time on Lithium':'Time_on_Lithium', 
                                  'History of Alcohol Dependence (Y/N)':'Hx_Alcohol_Dep', 
                                  'Rapid Cycling (Y/N)':'Rapid_Cycling'}, inplace=True)

#Delete columns  
Muenster_Clinical.drop(['Age at Time of Scan ', 'Sex'], axis=1, inplace=True)

#Change Coding 
Muenster_Clinical = Muenster_Clinical.fillna({'Full_Diagnosis': 0}, inplace=True)
Muenster_Clinical.replace({'Full_Diagnosis' : {'BP1' : 1, 'BP2' : 2}}, inplace=True)
Muenster_Clinical['Full_Diagnosis']= Muenster_Clinical['Full_Diagnosis'].replace('NotApplic', np.nan)
Muenster_Clinical.replace({'Mood_Phase_ToS' : {'dep' : 1}}, inplace=True)
Muenster_Clinical = Muenster_Clinical.fillna({"Depression_Scale": 'HDRS21'}, inplace=True)
Muenster_Clinical = Muenster_Clinical.fillna({"Mania_Scale": "YMRS"}, inplace=True)

#Merge Recoded FA and Clinical data 
Muenster_MergedFAClinical = pd.merge(Muenster_Clinical, Muenster_FA, how='right', on='Subject_ID')

#Subjects removed, too many controls
Muenster_toremove = ('N0832_FA','N4344_FA','N0826_FA','N0810_FA','N4214_FA','N0805_FA','N0809_FA','N6701_FA',
                     'N4300_FA','N4212_FA','N5713_FA','N0909_FA','N0858_FA','N0865_FA','N0854_FA','N4264_FA',
                     'N0823_FA','N4295_FA','N0761_FA','N0831_FA','N0968_FA','N5740_FA','N4353_FA','N4352_FA',
                     'N4372_FA','N4359_FA','N5736_FA','N4206_FA','N4337_FA','N6703_FA','N4335_FA','N4379_FA',
                     'N4378_FA','N0904_FA','N0857_FA','N0964_FA','N4312_FA','N4203_FA','N4302_FA','N6711_FA',
                     'N4237_FA','N4323_FA','N0867_FA','N4241_FA','N0920_FA','N4209_FA','N4377_FA','N4370_FA',
                     'N0896_FA','N0827_FA','N6712_FA','N0942_FA','N4306_FA','N4381_FA','N4271_FA','N4278_FA',
                     'N0899_FA','N5737_FA','N4274_FA','N4321_FA','N4219_FA','N5704_FA','N4374_FA','N0981_FA',
                     'N0879_FA','N5728_FA','N0983_FA','N4333_FA','N6729_FA','N0997_FA','N4316_FA','N0802_FA',
                     'N0930_FA','N0866_FA','N0876_FA','N6708_FA','N4361_FA','N0932_FA','N4259_FA','N0914_FA',
                     'N4256_FA','N4244_FA','N0822_FA','N4303_FA','N4311_FA','N4236_FA','N0919_FA','N0872_FA',
                     'N4287_FA','N0851_FA','N4318_FA','N4226_FA','N0961_FA','N0889_FA','N4211_FA','N0860_FA',
                     'N0801_FA','N6718_FA','N0829_FA','N0884_FA','N6725_FA','N4218_FA','N4249_FA','N4225_FA',
                     'N0807_FA','N0898_FA','N4339_FA','N5729_FA','N4351_FA','N0962_FA','N0972_FA','N0978_FA',
                     'N4356_FA','N4272_FA','N5703_FA','N4294_FA','N0900_FA','N5715_FA','N4220_FA','N4281_FA',
                     'N4273_FA','N4240_FA','N6722_FA','N4354_FA','N0960_FA','N0841_FA','N0952_FA','N5733_FA',
                     'N5711_FA','N4325_FA','N0971_FA','N0821_FA','N0943_FA','N0965_FA','N0892_FA','N6713_FA',
                     'N4229_FA','N4239_FA','N0883_FA','N4230_FA','N4291_FA','N0856_FA','N4355_FA','N4282_FA',
                     'N0929_FA','N4360_FA','N0830_FA','N0989_FA','N0910_FA','N4205_FA','N4289_FA','N0882_FA',
                     'N5732_FA','N0907_FA','N4228_FA','N0849_FA','N4317_FA','N4268_FA','N0913_FA','N0885_FA',
                     'N4358_FA','N4367_FA','N4343_FA','N0998_FA','N0980_FA','N4285_FA','N6723_FA','N4088_FA',
                     'N0947_FA','N5707_FA','N4324_FA','N4243_FA','N0843_FA','N4364_FA','N0933_FA','N0813_FA',
                     'N0924_FA','N0973_FA','N1000_FA','N4383_FA','N6715_FA','N0934_FA','N4320_FA','N0870_FA',
                     'N4296_FA','N4347_FA','N4373_FA','N0835_FA','N4375_FA','N4223_FA','N0863_FA','N4251_FA',
                     'N0902_FA','N4231_FA','N0949_FA','N4216_FA','N5739_FA','N0803_FA','N0984_FA','N4307_FA',
                     'N0850_FA','N5742_FA','N0893_FA','N4301_FA','N6709_FA','N0838_FA','N0925_FA','N0756_FA',
                     'N0969_FA','N0836_FA','N4309_FA','N4369_FA','N0967_FA','N4091_FA','N5741_FA','N0847_FA',
                     'N6730_FA','N4284_FA','N5726_FA','N4342_FA','N4263_FA','N4227_FA','N0818_FA','N0825_FA',
                     'N4331_FA','N0881_FA','N0941_FA','N4290_FA','N4202_FA','N4255_FA','N4257_FA','N0816_FA',
                     'N0987_FA','N4254_FA','N6707_FA','N4267_FA','N0886_FA','N0873_FA','N4336_FA','N0951_FA',
                     'N4283_FA','N4215_FA','N4298_FA','N4258_FA','N0912_FA','N6710_FA','N0927_FA','N0741_FA',
                     'N5730_FA','N5720_FA','N4368_FA','N0999_FA','N0996_FA','N4207_FA','N0915_FA','N4329_FA',
                     'N4308_FA','N0955_FA','N0891_FA','N4245_FA','N0911_FA','N5725_FA','N0901_FA','N4363_FA',
                     'N4204_FA','N4310_FA','N0880_FA','N4247_FA','N0992_FA','N0894_FA','N4297_FA','N4322_FA',
                     'N5735_FA','N4092_FA','N0928_FA','N0868_FA','N0958_FA','N4213_FA','N4292_FA','N0975_FA',
                     'N4275_FA','N4313_FA','N4348_FA','N0995_FA','N6702_FA','N6717_FA','N0931_FA','N0916_FA',
                     'N4210_FA','N4232_FA','N0957_FA','N0954_FA','N6705_FA','N4269_FA','N0988_FA','N0974_FA',
                     'N0888_FA','N4346_FA','N5723_FA','N4270_FA','N0833_FA','N4315_FA','N4345_FA','N0897_FA',
                     'N4233_FA','N0953_FA','N0877_FA','N4253_FA','N4341_FA')

Muenster_FA_SubjRemoved = Muenster_FA.copy()
Muenster_FA_SubjRemoved = Muenster_FA_SubjRemoved[~Muenster_FA_SubjRemoved.Subject_ID.isin(Muenster_toremove)]

####Begin Site 14_OsloMalt####
#Combine Demographics and FA data into one document
OsloMalt_FA_Dem = pd.read_csv('/home/melissa/Desktop/OriginalFiles/TOP_Oslo_Malt_Original/Oslo-Malt/Covariates_Oslo-Malt.csv')
OsloMalt_FAonly = pd.read_csv('/home/melissa/Desktop/OriginalFiles/TOP_Oslo_Malt_Original/Oslo-Malt/combinedROItable_FA.csv')

#Standardize column names
OsloMalt_FA_Dem.rename(columns={'id': 'Subject_ID'}, inplace=True) 
OsloMalt_FAonly.rename(columns={'subjectID': 'Subject_ID'}, inplace=True) 

OsloMalt_FA = pd.merge(OsloMalt_FA_Dem, OsloMalt_FAonly, on=['Subject_ID'])

#Add Columns to Identify Site
OsloMalt_FA.insert(0, 'Site', 'OsloMalt')
OsloMalt_FA.insert(1, 'Site_ID', 14)

#Standardize column names
OsloMalt_FA.rename(columns={'AGE (TP1 or TP2)':'Age_at_ToS', 'GENDER (0=F) ':'Sex', 
                               'DIAGNOSIS (0=HC)':'HC_Pat'}, inplace=True)

#Round up age if decimal
OsloMalt_FA['Age_at_ToS'] = np.ceil(OsloMalt_FA['Age_at_ToS'])

#Delete subjects not meeting inclusion criteria
OsloMalt_FA = OsloMalt_FA[(OsloMalt_FA.Age_at_ToS < 66) & (OsloMalt_FA.Age_at_ToS > 17)]

#Look for duplicate subjects
pd.options.display.max_rows = (500)
print(OsloMalt_FA.duplicated('Subject_ID'))

OsloMalt_Clinical = pd.read_csv('/home/melissa/Desktop/OriginalFiles/TOP_Oslo_Malt_Original/Oslo-Malt/Original_ OsloMAlt_ENIGMA_DTI_Clin_Variables_Sent MelissaP_290317.csv')

#Delete columns 
OsloMalt_Clinical.drop(['AGE AT THE TIME OF SCAN', 'GENDER (0=F) ', 'FAMILY HISTORY OF BD (YES=1)', 
                           'HYPOMANIC EPISODE; YES=1; NO=0; HC=2', 'DEPRESSIVE EPISODE; YES=1; NO=0; HC=2', 
                           'MED FREE PAT=0, MEDICATED PAT=1, HC=2.1'], axis=1, inplace=True)

#Change Relevant Column Names
OsloMalt_Clinical.rename(columns={'SubjectId': 'Subject_ID', 
                                  'AGE OF ONSET (NA=HC)':'Age_of_Onset', 
                                  'DIAGNOSIS (0=HC; 1=BDII)':'Full_Diagnosis', 
                                  'MADRS SCORE':'Depression_Score_ToS',
                                  'YMRS SCORE ':'Mania_Score_ToS', 
                                  'MED FREE PAT=0, MEDICATED PAT=1, HC=2':'On_Med_ToS', 
                                  'ANTIPSYCHOTICS FREE PAT=0, USING PAT=1, HC=2':'Meds_Antipsychotics', 
                                  'ANTIDEPRESSANTS FREE PAT=0, USING PAT=1, HC=2':'Meds_Antidepressants', 
                                  'ANTIEPILEPTICS FREE PAT=0, USING PAT=1, HC=2':'Meds_Anticonvulsants',  
                                  'LITHIUM FREE PAT=0, USING PAT=1, HC=2':'Meds_Lithium'}, inplace=True)

#Add missing columns
OsloMalt_Clinical = OsloMalt_Clinical.reindex(columns = np.append(OsloMalt_Clinical.columns.values,[
        'Mood_Phase_ToS', 'No_Depressive_Ep', 'No_Manic_Ep', 'Psychotic_Feat', 'Suicide_Attempt', 
        'Time_on_Antipsychotics','Time_on_Antidepressants', 'Time_on_Anticonvulsants', 'Time_on_Lithium', 
        'Hx_Alcohol_Dep', 'Rapid_Cycling']))
    
OsloMalt_Clinical.insert(0, 'Depression_Scale', 'HDRS21')
OsloMalt_Clinical.insert(1, 'Mania_Scale', 'YMRS')

#Change Coding
OsloMalt_Clinical['Full_Diagnosis'].replace([2],[1],inplace=True)
OsloMalt_Clinical['On_Med_ToS'].replace([2],[0],inplace=True)
OsloMalt_Clinical['Meds_Antipsychotics'].replace([2],[0],inplace=True)
OsloMalt_Clinical['Meds_Antidepressants'].replace([2],[0],inplace=True)
OsloMalt_Clinical['Meds_Anticonvulsants'].replace([2],[0],inplace=True)
OsloMalt_Clinical['Meds_Lithium'].replace([2],[0],inplace=True)


#Replace missing, Not applicable, not completed etc. values with NaN
OsloMalt_Clinical = OsloMalt_Clinical.replace('Missing data', np.nan)
OsloMalt_Clinical = OsloMalt_Clinical.convert_objects(convert_numeric=True)

#Merge FA and Clinical data frames
OsloMalt_MergedFAClinical = pd.merge(OsloMalt_FA, OsloMalt_Clinical, how='right', on='Subject_ID')

####Begin Site 12_Mannheim###"
Mannheim_FA = pd.read_csv('/home/melissa/Desktop/OriginalFiles/Mannheim_Original/FA_12_mannheim_RTA.csv')

#Add Columns to Identify Site
Mannheim_FA.insert(0, 'Site', 'Mannheim')
Mannheim_FA.insert(1, 'Site_ID', 12)

#Standardize site names
Mannheim_FA.rename(columns={'subjectID':'Subject_ID', 
                            'Age':'Age_at_ToS', 
                            'DX':'HC_Pat', 
                            'Sex':'Sex'}, inplace=True) #Delete any subjects not meeting 

#Delete subjects not meeting inclusion criteria 
Mannheim_FA = Mannheim_FA[(Mannheim_FA.Age_at_ToS < 66) & (Mannheim_FA.Age_at_ToS > 17)]

#Look for duplicate subjects
pd.options.display.max_rows = (500)
print(Mannheim_FA.duplicated('Subject_ID'))

Mannheim_Clinical = pd.read_csv('/home/melissa/Desktop/OriginalFiles/Mannheim_Original/MannheimClinicalVariables.csv')

#Modify subject name if necessary to match format of FA file
Mannheim_Clinical['Current ID'] = 'mannheim__' + Mannheim_Clinical['Current ID'].astype(str)

#Delete columns 
Mannheim_Clinical.drop(['ID_Original','AGE', 'SEX', 'BD_HC', 'HANDEDNESS','BMRMS','HRS17','HRS25','SYMPTOMATIQUE',
                        'ILLNESS_DURATION', 'TOTAL_PSYCHOTROP','LITHIUM_LIFETIME'], axis=1, inplace=True)

#Rename columns
Mannheim_Clinical = Mannheim_Clinical.rename(columns={'Current ID':'Subject_ID',
                                                      'OH_DEPENDENCE':'Hx_Alcohol_Dep',
                                                      'MADRS':'Depression_Score_ToS',
                                                      'YMRS':'Mania_Score_ToS',
                                                      'AAO':'Age_of_Onset', 
                                                      'ANTIDEP':'Meds_Antidepressants', 
                                                      'ANTIPSYCH':'Meds_Antipsychotics', 
                                                      'MOODSTAB':'Meds_Anticonvulsants', 
                                                      'LITHIUM':'Meds_Lithium', 
                                                      'LITHIUM_DURATION_YEARS':'Time_on_Lithium'})

#Add columns
Mannheim_Clinical = Mannheim_Clinical.reindex(columns = np.append(Mannheim_Clinical.columns.values,[
        'Psychotic_Feat', 'Full_Diagnosis','Time_on_Antipsychotics',  'Time_on_Antidepressants', 
        'Time_on_Anticonvulsants', 'Mood_Phase_ToS', 'No_Depressive_Ep', 'No_Manic_Ep', 'Suicide_Attempt', 
        'Rapid_Cycling']))

#Change coding
Mannheim_Clinical.replace({'Meds_Antipsychotics' :{'yes' : 1, 'no' : 0}}, inplace=True)
Mannheim_Clinical.replace({'Meds_Antidepressants' :{'yes' : 1, 'no' : 0}}, inplace=True)
Mannheim_Clinical.replace({'Meds_Anticonvulsants' : {'yes' : 1, 'no' : 0}}, inplace=True)
Mannheim_Clinical.replace({'Meds_Lithium' : {'yes' : 1, 'no' : 0}}, inplace=True)
Mannheim_Clinical.replace({'Hx_Alcohol_Dep' : {'yes' : 1, 'no' : 0}}, inplace=True)
Mannheim_Clinical.insert(2, 'Depression_Scale', 'MASDRS')
Mannheim_Clinical.insert(3, 'Mania_Scale', 'YMRS')
Mannheim_Clinical = Mannheim_Clinical.replace('#NULL!', np.nan)
Mannheim_Clinical = Mannheim_Clinical.replace('=', np.nan)
Mannheim_Clinical = Mannheim_Clinical.convert_objects(convert_numeric=True)
for i, row in Mannheim_Clinical.iterrows():
    if row['Meds_Antipsychotics' or 'Meds_Anticonvulsants' or 'Meds_Antidepressants' or 'Meds_Lithium'] == 1:
        Mannheim_Clinical.ix[i,'On_Med_ToS']=1
    elif row['Meds_Antipsychotics' or 'Meds_Anticonvulsants' or 'Meds_Antidepressants' or 'Meds_Lithium'] == 0:
        Mannheim_Clinical.ix[i,'On_Med_ToS']=0
    else: Mannheim_Clinical.ix[i,'On_Med_ToS']=np.nan

 
 
#Merge Recoded FA df and Clinical data frame
Mannheim_MergedFAClinical = pd.merge(Mannheim_Clinical, Mannheim_FA, how='right', on=['Subject_ID'])

####Start Site 15_Pittsburgh####
Pittsburgh_FA = pd.read_csv('/home/melissa/Documents/cleaning/Finalcsvs/FA_20_pittsburgh_figures/FA_20_pittsburgh_RTA.csv')

#Add Columns to Identify Site
Pittsburgh_FA.insert(0, 'Site', 'Pittsburgh')
Pittsburgh_FA.insert(1, 'Site_ID', 15)

#Rename columns
Pittsburgh_FA.rename(columns={'subjectID':'Subject_ID', 
                              'Age':'Age_at_ToS', 
                              'DX':'HC_Pat'}, inplace=True)

#Look for duplicate subjects
pd.options.display.max_rows = (500)
print(Pittsburgh_FA.duplicated('Subject_ID'))

#Define data type of ID to maintain subject_IDs with leading 0s
dtype_dic= {'ID': str}
Pittsburgh_Clinical = pd.read_csv('/home/melissa/Desktop/OriginalFiles/Pittsburgh_Original/Original_task21e_dtimulti_all_PITT_Lith.csv', dtype=dtype_dic)

#Modify subject name if necessary to match format of FA file
Pittsburgh_Clinical['ID'] = 'pittsburgh__' + Pittsburgh_Clinical['ID'].astype(str)

#Rename columns
Pittsburgh_Clinical.rename(columns={'Lithium':'Meds_Lithium', 
                                    'ID':'Subject_ID', 
                                    'HRS17TOT':'Depression_Score_ToS', 
                                    'YOUNGTOT':'Mania_Score_ToS', 
                                    'Illness_AgeatOnset':'Age_of_Onset', 
                                    'Dep_Episodes':'No_Depressive_Ep',
                                    'Mania_Episodes':'No_Manic_Ep',
                                    'AntiDep':'Meds_Antidepressants', 
                                    'AntiPsych':'Meds_Antipsychotics', 
                                    'MoodStab':'Meds_Anticonvulsants'}, inplace=True)

#Add columns
Pittsburgh_Clinical = Pittsburgh_Clinical.replace('#NULL!', np.nan)
Pittsburgh_Clinical.insert(0, 'Depression_Scale', 'MADRS')
Pittsburgh_Clinical.insert(1, 'Mania_Scale', 'YMRS')
Pittsburgh_Clinical = Pittsburgh_Clinical.reindex(columns = np.append(Pittsburgh_Clinical.columns.values,[
        'Psychotic_Feat', 'Mood_Phase_ToS', 'Time_on_Lithium', 'Suicide_Attempt', 'Time_on_Antipsychotics', 
        'Time_on_Antidepressants', 'Time_on_Anticonvulsants', 'Hx_Alcohol_Dep', 'Rapid_Cycling']))
Pittsburgh_Clinical = Pittsburgh_Clinical.convert_objects(convert_numeric=True)
    
for i, row in Pittsburgh_Clinical.iterrows():
    if row['Meds_Antipsychotics' or 'Meds_Anticonvulsants' or 'Meds_Antidepressants' or 'Meds_Lithium'] == 1:
        Pittsburgh_Clinical.ix[i,'On_Med_ToS']= 1
    elif row['Meds_Antipsychotics' or 'Meds_Anticonvulsants' or 'Meds_Antidepressants' or 'Meds_Lithium'] == 0:
        Pittsburgh_Clinical.ix[i,'On_Med_ToS']= 0
    else: Pittsburgh_Clinical.ix[i,'On_Med_ToS']=np.nan

#Change coding
for i, row in Pittsburgh_Clinical.iterrows():
    if row['COHORT2'] == 1:
        Pittsburgh_Clinical.ix[i,'Full_Diagnosis']= 0
        Pittsburgh_Clinical.ix[i,'Mood_Phase_ToS']= np.nan
    elif row['COHORT2'] == 4:
        Pittsburgh_Clinical.ix[i,'Full_Diagnosis']= 1
        Pittsburgh_Clinical.ix[i,'Mood_Phase_ToS']= 1
    elif row['COHORT2'] == 5:
        Pittsburgh_Clinical.ix[i,'Full_Diagnosis']= 1
        Pittsburgh_Clinical.ix[i,'Mood_Phase_ToS']= 0
        
#Delete columns  
Pittsburgh_Clinical.drop(['Hypomania_Episodes', 'Sex', 'AgeatMRI', 'COHORT','COHORT2',
                          'MRI_DATE','DOB','HRS25TOT', 'Mania_AgeatOnset', 'Dep_AgeatOnset','DSMIV','Duration_Dep',
                          'Illness_Duration', 'PMD_Episodes','Total#_Psychotropics','MEDLOAD_TOTAL', 'Benzo', 
                          'NART_FullScaleIQ', 'Level_Education', 'LPBIPOL1', 'LPBIPOL2', 'LPBPOTHR', 'BIPSPECTRUM',
                          'DYSTYMC','LPDEPNOS', 'DELTHNK', 'HALUCN','PsychFx_DuringMood', 'LPETOH', 'LPSEDATV',
                          'LPCANNAB','LPSTIMUL','LPOPIOD','LPCOCANE','LPHALPCP','LPPOLY','LPOTHSUB','CoAlcDrug',
                          'LPPANIC','LPAGORA','LPSOCIAL','LPSPECIF', 'LPOBESS','LPPSTRES','LPACSTRS','LPGENANX',
                          'LPANXNOS','LPANXDEP','CoANXIETY','CoSomatoform','CoEatingDisorder','LPADJUST',
                          'LPOTHER','SCANNAME1','SCANNAME1_COMMENT','SCANNAME2','SCANNAME2_COMMENT',
                          'VISIT2_COMMENT', '@1_MEDCLASS', '@1_MEDLOAD', '@1_DRUGNAME', '@1_DOSE', 
                          '@1_DOSETYPE', '@2_MEDCLASS', '@2_MEDLOAD', '@2_DRUGNAME', '@2_DOSE', '@2_DOSETYPE', 
                          '@3_MEDCLASS', '@3_MEDLOAD', '@3_DRUGNAME', '@3_DOSE', '@3_DOSETYPE', '@4_MEDCLASS', 
                          '@4_MEDLOAD', '@4_DRUGNAME', '@4_DOSE', '@4_DOSETYPE', '@5_MEDCLASS', '@5_MEDLOAD', 
                          '@5_DRUGNAME', '@5_DOSE', '@5_DOSETYPE', 'Duration_Mania'], axis=1, inplace=True)

#Merge FA and Clinical data frames
Pittsburgh_MergedFAClinical = pd.merge(Pittsburgh_Clinical, Pittsburgh_FA, how='right', on= 'Subject_ID')

#Start Site 16_SaoPaulo
#Combine demographic and FA data 
SaoPaulo_FA_Dem = pd.read_csv('/home/melissa/Desktop/OriginalFiles/Sao_Paulo_Original/Original_SaoPaulo_covariates_basic.csv')
SaoPaulo_FAonly = pd.read_csv('/home/melissa/Desktop/OriginalFiles/Sao_Paulo_Original/Original_SaoPaulo_FA.csv') 
SaoPaulo_FA = pd.merge(SaoPaulo_FA_Dem, SaoPaulo_FAonly, how= 'right', on=['SubjID'])

#Add Columns 
SaoPaulo_FA.insert(0, 'Site', 'SaoPaulo')
SaoPaulo_FA.insert(1, 'Site_ID', 16)

#Standardize site names
SaoPaulo_FA.rename(columns={'SubjID':'Subject_ID', 
                            'Age':'Age_at_ToS', 
                            'Dx':'HC_Pat'}, inplace=True)

#Delete subjects 
SaoPaulo_FA = SaoPaulo_FA[(SaoPaulo_FA.Age_at_ToS < 66) & (SaoPaulo_FA.Age_at_ToS > 17)]

#Change Coding 
SaoPaulo_FA['Sex'].replace([2],[0],inplace=True)
SaoPaulo_FA['HC_Pat'].replace([2],[0],inplace=True)

#Look for duplicate subjects
pd.options.display.max_rows = (500)
print(SaoPaulo_FA.duplicated('Subject_ID'))

SaoPaulo_Clinical = pd.read_csv('/home/melissa/Desktop/OriginalFiles/Sao_Paulo_Original/Original_SaoPaulo_covariates_nokey.csv')

#Add missing columns
SaoPaulo_Clinical = SaoPaulo_Clinical.reindex(columns = np.append(SaoPaulo_Clinical.columns.values,[
        'Mood_Phase_ToS', 'Depression_Scale', 'Depression_Score_ToS', 'No_Depressive_Ep', 'Mania_Scale', 
        'Mania_Score_ToS', 'No_Manic_Ep', 'Suicide_Attempt', 'On_Med_ToS', 'Time_on_Antipsychotics', 
        'Time_on_Antidepressants', 'Time_on_Anticonvulsants', 'Time_on_Lithium', 'Hx_Alcohol_Dep', 'Rapid_Cycling']))

#Delete columns
SaoPaulo_Clinical.drop(['Age', 'Sex', 'Dx', 'FGA','HAND'], axis=1, inplace=True)

#Change Relevant Column Names
SaoPaulo_Clinical.rename(columns={'SubjID': 'Subject_ID', 
                                  'Age-of-onset':'Age_of_Onset',
                                  'BD Type':'Full_Diagnosis',
                                  'Psychosis history':'Psychotic_Feat', 
                                  'SGA':'Meds_Antipsychotics', 
                                  'AD':'Meds_Antidepressants', 
                                  'MS':'Meds_Anticonvulsants', 
                                  'Lithium':'Meds_Lithium'}, inplace=True)

#Change Coding 
SaoPaulo_Clinical = SaoPaulo_Clinical.fillna({"Full_Diagnosis": 0}, inplace=True)
SaoPaulo_Clinical['Psychotic_Feat'].replace([2],[0],inplace=True)
SaoPaulo_Clinical['Meds_Antipsychotics'].replace([2],[0],inplace=True)
SaoPaulo_Clinical['Meds_Antidepressants'].replace([2],[0],inplace=True)
SaoPaulo_Clinical['Meds_Anticonvulsants'].replace([2],[0],inplace=True)

#Merge FA and Clinical data frames
SaoPaulo_MergedFAClinical = pd.merge(SaoPaulo_Clinical, SaoPaulo_FA, how='right', on='Subject_ID')

####Begin Site 17_TOP####
TOP_FA_Dem = pd.read_csv('/home/melissa/Desktop/OriginalFiles/TOP_Oslo_Malt_Original/TOP/Covariates_TOP.csv')
TOP_FAonly = pd.read_csv('/home/melissa/Desktop/OriginalFiles/TOP_Oslo_Malt_Original/TOP/combinedROItable_FA.csv') 

TOP_FA = pd.merge(TOP_FA_Dem, TOP_FAonly, on='subjectID')


#Add Columns to Identify Site
TOP_FA.insert(0, 'Site', 'Top')
TOP_FA.insert(1, 'Site_ID', 17)

#Standardize site names
TOP_FA.rename(columns={'subjectID':'Subject_ID', 
                       'age':'Age_at_ToS', 
                       'sex':'Sex', 
                       'dx':'HC_Pat'}, inplace=True)

#Round up age 
TOP_FA['Age_at_ToS'] = np.ceil(TOP_FA['Age_at_ToS'])

#Delete subjects not meeting inclusion criteria 
TOP_FA = TOP_FA[(TOP_FA.Age_at_ToS < 66) & (TOP_FA.Age_at_ToS > 17)]

#Change Coding
TOP_FA['Sex'].replace(['female'],[0],inplace=True)
TOP_FA['Sex'].replace(['male'],[1],inplace=True)
TOP_FA['HC_Pat'].replace(['ctr'],[0],inplace=True)
TOP_FA['HC_Pat'].replace(['bd'],[1],inplace=True)

#Look for duplicate subjects
pd.options.display.max_rows = (500)
print(TOP_FA.duplicated('Subject_ID'))

#remove outlier, previously identified
TOP_FA = TOP_FA[~TOP_FA.Subject_ID.str.contains("O3550")]

#Remove subjects, too many controls 
TOP_toremove = ('O3000','O3006','O3036','O3004','O3010','O3037','O3039','O3040','O3051','O3059','O3064','O3068',
                'O3073','O3074','O3079','O3082','O3083','O3109','O3115','O3116','O3121','O3129','O3142','O3153',
                'O3158','O3161','O3167','O3168','O3171','O3172','O3176','O3194','O3199','O3201','O3207','O3211',
                'O3213','O3218','O3229','O3230','O3236','O3237','O3240','O3241','O3245','O3246','O3247','O3251',
                'O3252','O3253','O3272','O3274','O3275','O3282','O3287','O3312','O3313','O3325','O3326','O3333',
                'O3334','O3337','O3345','O3346','O3353','O3358','O3361','O3364','O3374','O3378','O3380','O3382',
                'O3386','O3393','O3395','O3415','O3431','O3442','O3450','O3466','O3470','O3481','O3489','O3525',
                'O3528','O3530','O3547','O3557','O3567','O3579','O3580','O3584','O3591','O3596','O3608','O3613',
                'O3615','O3621','O3624','O3629','O3630','O3631','O3633','O3635')

TOP_FA_SubjRemoved = TOP_FA.copy()
TOP_FA_SubjRemoved = TOP_FA_SubjRemoved[~TOP_FA_SubjRemoved.Subject_ID.isin(TOP_toremove)]

#Create clinical data frame, no clinical data sent
TOP_MergedFAClinical = TOP_FA.copy()

#add missing columns
TOP_MergedFAClinical = TOP_MergedFAClinical.reindex(columns = np.append(TOP_MergedFAClinical.columns.values,[
        'Age_of_Onset', 'Full_Diagnosis', 'Mood_Phase_ToS', 'Depression_Scale', 'Depression_Score_ToS', 
        'No_Depressive_Ep', 'Mania_Scale', 'Mania_Score_ToS', 'No_Manic_Ep', 'Psychotic_Feat', 'Suicide_Attempt', 
        'On_Med_ToS', 'Meds_Antipsychotics', 'Time_on_Antipsychotics', 'Meds_Antidepressants', 
        'Time_on_Antidepressants', 'Meds_Anticonvulsants', 'Time_on_Anticonvulsants', 'Meds_Lithium', 
        'Time_on_Lithium', 'Hx_Alcohol_Dep', 'Rapid_Cycling']))

####Begin Site 18_UCSD####
UCSD_FA = pd.read_csv('/home/melissa/Desktop/OriginalFiles/UCSD_Original/FA_16_UCSD_RTA.csv')

#Add Columns to Identify Site
UCSD_FA.insert(0, 'Site', 'UCSD')
UCSD_FA.insert(1, 'Site_ID', 18)

#Standardize site names
UCSD_FA.rename(columns={'subjectID':'Subject_ID', 
                        'Age':'Age_at_ToS', 
                        'Diagnosis':'HC_Pat', 
                        'Sex':'Sex'}, inplace=True)

#Modify subject_ID to match Clinical data
UCSD_FA['Subject_ID'] = UCSD_FA['Subject_ID'].str[15:18]

#Look for duplicate subjects
pd.options.display.max_rows = (500)
print(UCSD_FA.duplicated('Subject_ID'))

UCSD_Clinical = pd.read_csv('/home/melissa/Desktop/OriginalFiles/UCSD_Original/UCSD_VariableTableEnigmaBDStudy_Eyler_050117_MedsRecoded.csv')

#Delete columns 
UCSD_Clinical.drop(['Meds, Anti-anxiety', 'Length of Time on Anti-anxiety', 'Age at Time of Scan', 'Sex', 'Notes', 
                    'Other', 'Length of time on Other', 'History of ECT'], axis=1, inplace=True)

#Change Relevant Column Names
UCSD_Clinical.rename(columns={'Subject ID': 'Subject_ID', 
                              'Age of Onset':'Age_of_Onset', 
                              'Diagnosis (BP1, BP2, Control)':'Full_Diagnosis', 
                              'Mood Phase at Time of Scan':'Mood_Phase_ToS', 
                              'Depression Scale':'Depression_Scale', 
                              'Depression Score at Time of Scan':'Depression_Score_ToS', 
                              'Number of Depressive Episodes':'No_Depressive_Ep', 
                              'Mania Scale':'Mania_Scale', 
                              'Mania Score at time of Scan':'Mania_Score_ToS', 
                              'Number of Manic Episodes':'No_Manic_Ep', 
                              'Psychotic Features (Y/N – throughout Lifetime)':'Psychotic_Feat', 
                              'Suicide Attempt  (Y/N – throughout Lifetime)':'Suicide_Attempt', 
                              'On Medication at Time of Scan (Y/N)':'On_Med_ToS', 
                              'Meds, Antipsychotics':'Meds_Antipsychotics', 
                              'Length of Time on Antipsychotics (weeks)':'Time_on_Antipsychotics', 
                              'Meds, Antidepressants':'Meds_Antidepressants', 
                              'Length of Time on Antidepressants (weeks)':'Time_on_Antidepressants', 
                              'Meds, Anticonvulsants':'Meds_Anticonvulsants', 
                              'Length of Time on Anticonvulsants':'Time_on_Anticonvulsants', 
                              'Lithium (y/n)':'Meds_Lithium',
                              'Length of Time on Lithium':'Time_on_Lithium', 
                              'History of Alcohol Dependence (Y/N)':'Hx_Alcohol_Dep', 
                              'Rapid Cycling (Y/N)':'Rapid_Cycling'}, inplace=True)

#Modify subject_ID to match FA data
UCSD_Clinical['Subject_ID'] = UCSD_Clinical['Subject_ID'].str[3:5]

#Change Coding 
#all patients bipolar one, communicated via email
UCSD_Clinical.replace({'Full_Diagnosis' : {'BD' : 1, 'HC' : 0}}, inplace=True)
UCSD_Clinical.replace({'Mood_Phase_ToS' : {'Euthymic' : 0}}, inplace=True)
UCSD_Clinical.replace({'Psychotic_Feat' : {'Y' : 1, 'N' : 0}}, inplace=True)
UCSD_Clinical.replace({'Suicide_Attempt' : {'Y' : 1, 'N' : 0}}, inplace=True)
UCSD_Clinical.replace({'On_Med_ToS' : {'Y' : 1, 'N' : 0}}, inplace=True)
UCSD_Clinical.replace({'Meds_Lithium' : {'Y' : 1, 'N' : 0}}, inplace=True)
UCSD_Clinical.replace({'Hx_Alcohol_Dep' : {'Y' : 1, 'N' : 0}}, inplace=True)
UCSD_Clinical.replace({'Rapid_Cycling' : {'Y' : 1, 'N' : 0, 'y' : 1}}, inplace=True)
UCSD_Clinical= UCSD_Clinical.replace('?', np.nan)

#Replace missing, Not applicable, not completed etc. values with NaN
UCSD_Clinical = UCSD_Clinical.replace('-9', np.nan)
UCSD_Clinical = UCSD_Clinical.replace('-8', np.NaN)



#Merge FA and Clinical data frames
UCSD_MergedFAClinical = pd.merge(UCSD_Clinical, UCSD_FA, how='right', on='Subject_ID')

###Begin Site 19_UCT####
UCT_FA = pd.read_csv('/home/melissa/Desktop/OriginalFiles/UCT_Original/Original_UCT_CombinedROItable_FA.csv')

#Add Columns to Identify Site
UCT_FA.insert(0, 'Site', 'UCT')
UCT_FA.insert(1, 'Site_ID', 19)

#Add HC_Pat column, using data from ID column
UCT_FA['HC_Pat'] = np.where(UCT_FA.subjectID.str.contains('CON'), 0, 1)

#Standardize site names
UCT_FA.rename(columns={'subjectID':'Subject_ID', 
                       'Age' :'Age_at_ToS'}, inplace=True)

#Change Coding 
UCT_FA['Sex'].replace([0],[1],inplace=True)
UCT_FA['Sex'].replace([1],[0],inplace=True)

#remove outlier, previously identified
UCT_FA = UCT_FA[~UCT_FA.Subject_ID.str.contains("CIAM_BIP_03")]

#Look for duplicate subjects
pd.options.display.max_rows = (500)
print(UCT_FA.duplicated('Subject_ID'))

UCT_Clinical = pd.read_csv('/home/melissa/Desktop/OriginalFiles/UCT_Original/Original_UCT_BPDDTIwithClincial_09_03_2017.csv')

#Delete columns 
UCT_Clinical.drop(['Age at Time of Scan', 'Sex', 'History Drug Dependence'], axis=1, inplace=True)

#Change Relevant Column Names
UCT_Clinical.rename(columns={'ID': 'Subject_ID', 
                             'Age of Onset':'Age_of_Onset', 
                             'Diagnosis (BP1, BP2, Control)':'Full_Diagnosis', 
                             'Mood Phase at Time of Scan':'Mood_Phase_ToS', 
                             'Depression Scale':'Depression_Scale', 
                             'Depression Score at Time of Scan':'Depression_Score_ToS', 
                             'Number of Depressive Episodes':'No_Depressive_Ep', 
                             'Mania Scale':'Mania_Scale', 
                             'Mania Score at time of Scan':'Mania_Score_ToS',
                             'Number of Manic Episodes':'No_Manic_Ep', 
                             'Psychotic Features (Y/N, throughout Lifetime)':'Psychotic_Feat', 
                             'Suicide Attempt  (Y/N,  throughout Lifetime)':'Suicide_Attempt', 
                             'On Medication at Time of Scan (Y/N)':'On_Med_ToS', 
                             'Meds, Antipsychotics':'Meds_Antipsychotics', 
                             'Length of Time on Antipsychotics':'Time_on_Antipsychotics', 
                             'Meds, Antidepressants':'Meds_Antidepressants', 
                             'Length of Time on Antidepressants':'Time_on_Antidepressants', 
                             'Meds, Anticonvulsants':'Meds_Anticonvulsants', 
                             'Length of Time on Anticonvulsants':'Time_on_Anticonvulsants', 
                             'Lithium (y/n)':'Meds_Lithium',
                             'Length of Time on Lithium':'Time_on_Lithium', 
                             'History of Alcohol Dependence (Y/N)':'Hx_Alcohol_Dep', 
                             'Rapid Cycling (Y/N)':'Rapid_Cycling'}, inplace=True)
 
#Round up age 
UCT_Clinical['Age_of_Onset']= UCT_Clinical['Age_of_Onset'].round()

#Change Coding 
UCT_Clinical.replace({'Full_Diagnosis' : {'Bipolar I HX psychosis' : 1}}, inplace=True)
UCT_Clinical.replace({'Mood_Phase_ToS' : {'euthymic' : 0}}, inplace=True)
UCT_Clinical.replace({'Psychotic_Feat' : {'significant history' : 1, 'N' : 0}}, inplace=True)
UCT_Clinical.replace({'On_Med_ToS' : {'Y' : 1, 'N' : 0}}, inplace=True)
UCT_Clinical.replace({'Meds_Antipsychotics' :{'Y' : 1, 'Y ' : 1, 'N ' : 0, 'N' : 0}}, inplace=True)
UCT_Clinical.replace({'Meds_Antidepressants' :{'Y' : 1, 'N ' : 0, 'N' : 0}}, inplace=True)
UCT_Clinical.replace({'Meds_Anticonvulsants' : {'Y' : 1, 'N' : 0}}, inplace=True)
UCT_Clinical.replace({'Meds_Lithium' : {'Y' : 1, 'N' : 0}}, inplace=True)
UCT_Clinical.replace({'Hx_Alcohol_Dep' : {'Y' : 1, 'N' : 0}}, inplace=True)
UCT_Clinical.replace({'Mania_Scale' : {'N' : 'YMRS'}}, inplace=True)
UCT_Clinical['Mania_Score_ToS']= UCT_Clinical['Mania_Score_ToS'].replace('N', np.NaN)
UCT_Clinical = UCT_Clinical.fillna({'Full_Diagnosis': 0}, inplace=True)
UCT_Clinical = UCT_Clinical.fillna({'Depression_Scale': 'HAMD'}, inplace=True)

#remove outlier, previously identified
UCT_Clinical = UCT_Clinical[~UCT_Clinical.Subject_ID.str.contains('CIAM_BIP_03')]

#Merge Recoded FA and Cov files into one
UCT_MergedFAClinical = pd.merge(UCT_FA, UCT_Clinical, how='right', on='Subject_ID')

####Begin Site 20_UMCU_UMCLA####
#Combine Demographics and FA data into one document
UMCA_UCLA_FA_Dem = pd.read_csv('/home/melissa/Desktop/OriginalFiles/UMCU_UCLA_Original/UMCU_UCLA_ALL_Subject_Info.csv')
UMCA_UCLA_FAonly = pd.read_csv('/home/melissa/Desktop/OriginalFiles/UMCU_UCLA_Original/UMCU_UCLA_combinedROItable.csv') 

UMCA_UCLA_FA = pd.merge(UMCA_UCLA_FA_Dem, UMCA_UCLA_FAonly, on=['subjectID', 'Age', 'Sex'])

#Add Columns to Identify Site
UMCA_UCLA_FA.insert(0, 'Site', 'UMCU_UCLA')
UMCA_UCLA_FA.insert(1, 'Site_ID', 20)

#Standardize site names
UMCA_UCLA_FA.rename(columns={'subjectID':'Subject_ID', 
                             'Age':'Age_at_ToS',
                             'Diagnosis':'HC_Pat'}, inplace=True)

#Tidy subject names, to match clinical data
UMCA_UCLA_FA['Subject_ID'] = UMCA_UCLA_FA['Subject_ID'].astype(str).str[:-10]

#Round up age 
UMCA_UCLA_FA['Age_at_ToS'] = np.ceil(UMCA_UCLA_FA['Age_at_ToS'])

#Delete subjects not meeting inclusion criteria 
UMCA_UCLA_FA = UMCA_UCLA_FA[(UMCA_UCLA_FA.Age_at_ToS < 66) & (UMCA_UCLA_FA.Age_at_ToS > 17)]

#Change Coding 
UMCA_UCLA_FA['Sex'].replace([2],[0],inplace=True)
UMCA_UCLA_FA['HC_Pat'].replace([2],[0],inplace=True)

#Look for duplicate subjects
pd.options.display.max_rows = (500)
print(UMCA_UCLA_FA.duplicated('Subject_ID'))

UMCA_UCLA_Clinical = pd.read_csv('/home/melissa/Desktop/OriginalFiles/UMCU_UCLA_Original/UMCU_UCLA_covariates_1.csv')

#Change Relevant Column Names
UMCA_UCLA_Clinical.rename(columns={'MRIcode':'Subject_ID',
                                   'FullDx':'Full_Diagnosis', 
                                   'MoodState':'Mood_Phase_ToS',
                                   'HistoryPsychosis':'Psychotic_Feat',
                                   'AntiEpileptic':'Meds_Anticonvulsants', 
                                   'AntiDep':'Meds_Antidepressants', 
                                   'Li':'Meds_Lithium', 
                                   'AgeofOnset':'Age_of_Onset'}, inplace=True)

#Add columns
UMCA_UCLA_Clinical['Meds_Antipsychotics'] = UMCA_UCLA_Clinical['Gen1AntiPsych'] + UMCA_UCLA_Clinical['Gen2AntiPsych']
UMCA_UCLA_Clinical['Meds_Antipsychotics'].replace([2],[1])
UMCA_UCLA_Clinical = UMCA_UCLA_Clinical.reindex(columns = np.append(UMCA_UCLA_Clinical.columns.values,[
        'Depression_Scale', 'Depression_Score_ToS', 'No_Depressive_Ep', 'Mania_Scale', 'Mania_Score_ToS', 
        'No_Manic_Ep', 'Suicide_Attempt', 'On_Med_ToS', 'Time_on_Antipsychotics', 'Time_on_Antidepressants', 
        'Time_on_Anticonvulsants', 'Time_on_Lithium', 'Hx_Alcohol_Dep', 'Rapid_Cycling']))
    
for i, row in UMCA_UCLA_Clinical.iterrows():
    if row['Meds_Antipsychotics' or 'Meds_Anticonvulsants' or 'Meds_Antidepressants' or 'Meds_Lithium'] == 1:
        UMCA_UCLA_Clinical.ix[i,'On_Med_ToS']=1
    elif row['Meds_Antipsychotics' or 'Meds_Anticonvulsants' or 'Meds_Antidepressants' or 'Meds_Lithium'] == 0:
        UMCA_UCLA_Clinical.ix[i,'On_Med_ToS']=0
    else: UMCA_UCLA_Clinical.ix[i,'On_Med_ToS']=np.nan

#Drop columns
UMCA_UCLA_Clinical.drop(['Age', 'Sex', 'Dx', 'Gen1AntiPsych', 'Gen2AntiPsych'], axis=1, inplace=True)

#Merge Recoded FA and Cov files into one
UMCA_UCLA_MergedFAClinical = pd.merge(UMCA_UCLA_Clinical, UMCA_UCLA_FA, how='right', on= 'Subject_ID')

####Begin  21_UNC_Phillips#### 
UNC_Phillips_FA = pd.read_csv('/home/melissa/Desktop/OriginalFiles/UNC_Original/Original_UNC_texas_combinedROItable_noFamily_Phillips_SexCorrected.csv')

#Add Columns to Identify 
UNC_Phillips_FA.insert(0, 'Site', 'UNC_Phillips')
UNC_Phillips_FA.insert(1, 'Site_ID', 21)

#Delete columns 
UNC_Phillips_FA.drop(['BP_I', 'BP_II', 'BP_NOS', 'magnet', 'scan_site'], axis=1, inplace=True)

#Standardize  names
UNC_Phillips_FA.rename(columns={'subjectID':'Subject_ID', 
                                'AGE':'Age_at_ToS', 
                                'BP':'HC_Pat', 
                                'SEX0M1F':'Sex'}, inplace=True)

#Change Coding 
UNC_Phillips_FA['Sex'].replace([1],[0],inplace=True)
UNC_Phillips_FA['Sex'].replace([0],[1],inplace=True)

#Look for duplicate subjects
pd.options.display.max_rows = (500)
print(UNC_Phillips_FA.duplicated('Subject_ID'))

#Create clinical data frame, no clinical data sent
UNC_Phillips_MergedFAClinical = UNC_Phillips_FA.copy()

#add missing columns
UNC_Phillips_MergedFAClinical = UNC_Phillips_MergedFAClinical.reindex(columns = np.append(UNC_Phillips_MergedFAClinical.columns.values,[
        'Age_of_Onset', 'Full_Diagnosis', 'Mood_Phase_ToS', 'Depression_Scale', 'Depression_Score_ToS', 
        'No_Depressive_Ep', 'Mania_Scale', 'Mania_Score_ToS', 'No_Manic_Ep', 'Psychotic_Feat', 'Suicide_Attempt', 
        'On_Med_ToS', 'Meds_Antipsychotics', 'Time_on_Antipsychotics', 'Meds_Antidepressants', 
        'Time_on_Antidepressants', 'Meds_Anticonvulsants', 'Time_on_Anticonvulsants', 'Meds_Lithium', 
        'Time_on_Lithium', 'Hx_Alcohol_Dep', 'Rapid_Cycling']))

###Begin Site 22_UNC_Seimens
UNC_Seimens_FA = pd.read_csv('/home/melissa/Desktop/OriginalFiles/UNC_Original/Original_UNC_Seimens_texas_combinedROItable_noFamily_SexCorrected.csv')

#Add Columns to Identify Site
UNC_Seimens_FA.insert(0, 'Site', 'UNC_Seimens')
UNC_Seimens_FA.insert(1, 'Site_ID', 22)

#Standardize site names
UNC_Seimens_FA.rename(columns={'subjectID':'Subject_ID', 
                               'AGE':'Age_at_ToS', 
                               'BP':'HC_Pat', 
                               'SEX0M1F':'Sex'}, inplace=True)

#Delete subjects not meeting inclusion criteria 
UNC_Seimens_FA = UNC_Seimens_FA[(UNC_Seimens_FA.Age_at_ToS < 66) & (UNC_Seimens_FA.Age_at_ToS > 17)]
UNC_Seimens_FA = UNC_Seimens_FA[UNC_Seimens_FA['BP_NOS'] == 0]

#Change Coding 
UNC_Seimens_FA['Sex'].replace([1],[0],inplace=True)
UNC_Seimens_FA['Sex'].replace([0],[1],inplace=True)

#Delete columns
UNC_Seimens_FA.drop(['BP_I', 'BP_II', 'BP_NOS', 'scan_site', 'magnet'], axis=1, inplace=True)

#Look for duplicate subjects
pd.options.display.max_rows = (500)
print(UNC_Seimens_FA.duplicated('Subject_ID'))

UNC_Seimens_Clinical = pd.read_csv('/home/melissa/Desktop/OriginalFiles/UNC_Original/Original_UNC_Seimens_NewVariableTableEnigmaBPStudy_SexCorrected.csv')

#Change Relevant Column Names
UNC_Seimens_Clinical.rename(columns={'Label': 'Subject_ID', 
                                     'Group':'Full_Diagnosis', 
                                     'SCID_current_mood':'Mood_Phase_ToS', 
                                     'MADRAS_Total':'Depression_Score_ToS',
                                     'SCID_number_Of_depressive_Disorders':'No_Depressive_Ep', 
                                     'YMRS_Total':'Mania_Score_ToS', 
                                     'SCID_number_Of_manic_Episodes':'No_Manic_Ep', 
                                     'SCID_ever_psychotic':'Psychotic_Feat', 
                                     'SCID_current_medication':'On_Med_ToS', 
                                     'Meds, Antipsychotics':'Meds_Antipsychotics', 
                                     'SCID_current_antidepressants':'Meds_Antidepressants', 
                                     'SCID_current_anticonv':'Meds_Anticonvulsants',
                                     'SCID_current_lithium':'Meds_Lithium', 
                                     'SCID_curr_lithium_duration':'Time_on_Lithium', 
                                     'Alcohol_BP':'Hx_Alcohol_Dep',
                                     'SCID.rapid_cycling':'Rapid_Cycling'}, inplace=True)

#Delete subjects not meeting inclusion criteria
UNC_Seimens_Clinical = UNC_Seimens_Clinical[UNC_Seimens_Clinical.Full_Diagnosis.str.contains('BD NOS') == False]
UNC_Seimens_Clinical = UNC_Seimens_Clinical[UNC_Seimens_Clinical.Full_Diagnosis.str.contains('6') == False]

#Change Coding 
UNC_Seimens_Clinical.replace({'Full_Diagnosis' : {'Control' : 0, 'BD I' : 1, 'BD II' : 2}}, inplace=True)
UNC_Seimens_Clinical['Mood_Phase_ToS'].replace([1],[0],inplace=True)
UNC_Seimens_Clinical['Mood_Phase_ToS'].replace([2],[1],inplace=True)
UNC_Seimens_Clinical['Mood_Phase_ToS'].replace([3],[2],inplace=True)
UNC_Seimens_Clinical['Mood_Phase_ToS'].replace([4],[2],inplace=True)
#Coded hypomanic as manic 
UNC_Seimens_Clinical['Mood_Phase_ToS'].replace([5],[3],inplace=True)
UNC_Seimens_Clinical = UNC_Seimens_Clinical.replace(-99, np.NaN)
#'99' in No_Depressive_Ep and No_Manic_Ep means too many to list

#Add columns
UNC_Seimens_Clinical.insert(0, 'Depression_Scale', 'MADRAS')
UNC_Seimens_Clinical.insert(1, 'Mania_Scale', 'YMRS')
UNC_Seimens_Clinical['Meds_Antipsychotics'] = UNC_Seimens_Clinical['SCID_current_typical_Antipsychotics'] + UNC_Seimens_Clinical['SCID_current_Atypical_Antipsychotics']
#One patient had a one in both categories
UNC_Seimens_Clinical['Meds_Antipsychotics'].replace([2],[1],inplace=True)
UNC_Seimens_Clinical = UNC_Seimens_Clinical.reindex(columns = np.append(UNC_Seimens_Clinical.columns.values, [
        'Time_on_Antipsychotics', 'Time_on_Antidepressants', 'Time_on_Anticonvulsants', 'Age_of_Onset', 
        'Suicide_Attempt']))

#Delete columns
UNC_Seimens_Clinical.drop(['Age', 'M/F', 'Scanner', 'SCID_Dep_current_suicidal', 'SCID_Dep_type_suicidal', 
                           'SCID_curr_lithium_dose', 'SCID_curr_stimulants', 'SCID_current_BZD', 
                           'SCID_age_anxiety_sym', 'SCID.age_ptsd_symptoms', 'SCID.age_drug_sym', 
                           'SCID.age_First_manic_episode', 'SCID.age_First_threshold_Level_depressive_episode', 
                           'SCID.age_first_Stabilizer_treatment', 'SCID.age_first_psycho_episode', 
                           'SCID.age_first_alcohol_symptoms', 'SCID_current_typical_Antipsychotics', 
                           'SCID_current_Atypical_Antipsychotics'], axis=1, inplace=True)

#Merge Recoded FA and Cov files into one
UNC_Seimens_MergedFAClinical = pd.merge(UNC_Seimens_Clinical, UNC_Seimens_FA, how='right', on='Subject_ID')

#Begin Site 23_UNSW
UNSW_FA = pd.read_csv('/home/melissa/Desktop/OriginalFiles/UNSW_Original/Original_UNSW_bipolar_combinedROItable_EHP_checked.csv')

#Add Columns to Identify Site
UNSW_FA.insert(0, 'Site', 'UNSW')
UNSW_FA.insert(1, 'Site_ID', 23)

#Standardize site names
UNSW_FA.rename(columns={'subjectID': 'Subject_ID', 'Age' : 'Age_at_ToS', 'Sex':'Sex',
                        'Category' : 'HC_Pat'}, inplace=True)

#Round up age 
UNSW_FA['Age_at_ToS'] = np.ceil(UNSW_FA['Age_at_ToS'])

#Delete subjects not meeting inclusion criteria 
UNSW_FA = UNSW_FA[(UNSW_FA.Age_at_ToS < 66) & (UNSW_FA.Age_at_ToS > 17)]

#Delete at risk subjects
UNSW_FA=UNSW_FA.ix[~(UNSW_FA['HC_Pat'] == 1)]

#Change coding 
UNSW_FA['Sex'].replace([1],[0],inplace=True) 
UNSW_FA['Sex'].replace([2],[1],inplace=True) 
UNSW_FA['HC_Pat'].replace([3],[0],inplace=True)
UNSW_FA['HC_Pat'].replace([2],[1],inplace=True)

#Delete Columns
UNSW_FA.drop('Bipolar Type ', axis=1, inplace=True)

UNSW_Clinical = pd.read_csv('/home/melissa/Desktop/OriginalFiles/UNSW_Original/Original_UNSW_ENIGMA_TBSS_with_clinical_1March17.csv')

#Add Columns 
UNSW_Clinical.insert(2, 'Depression_Scale', 'MASDRS')
UNSW_Clinical.insert(3, 'Mania_Scale', 'YMRS')
UNSW_Clinical = UNSW_Clinical.reindex(columns = np.append(UNSW_Clinical.columns.values,[
        'Time_on_Antipsychotics',  'Time_on_Antidepressants', 'Time_on_Anticonvulsants', 'Time_on_Lithium']))
#Delete columns
UNSW_Clinical.drop(['Age at the Time of Scan ', 'Sex', 'Number of Hypomanic Episodes'], axis=1, inplace=True)

#Change relevant column Names
UNSW_Clinical.rename(columns={'Subject ID':'Subject_ID', 
                              'Age of Onset':'Age_of_Onset', 
                              'Diagnosis (BP1, BP2, Control)':'Full_Diagnosis', 
                              'Mood Phase at Time of Scan (Depressive/Manic/Neither)':'Mood_Phase_ToS', 
                              'Depression_Scale ':'Depression_Scale', 
                              'Depression Score at Time of Scan (MASDRS)':'Depression_Score_ToS', 
                              'Number of Depressive Episodes':'No_Depressive_Ep', 
                              'Mania_Scale':'Mania_Scale', 
                              'Mania Score at time of Scan (YMRS)':'Mania_Score_ToS', 
                              'No_Manic_Ep':'Number of Manic Episodes',
                              'Psychotic Features':'Psychotic_Feat', 
                              'Suicide Attempt':'Suicide_Attempt', 
                              'On Medication at Time of Scan':'On_Med_ToS', 
                              'Meds, Antipsychotics':'Meds_Antipsychotics', 
                              'Length of Time on Antipsychotics':'Time_on_Antipsychotics', 
                              'Meds, Antidepressants':'Meds_Antidepressants', 
                              'Length of Time on Antidepressants':'Time_on_Antidepressants', 
                              'Meds, Anticonvulsants':'Meds_Anticonvulsants', 
                              'Length of Time on Anticonvulsants':'Time_on_Anticonvulsants', 
                              'Lithium ':'Meds_Lithium', 
                              'Length of Time on Lithium':'Time_on_Lithium', 
                              'Alcohol Dependence':'Hx_Alcohol_Dep', 
                              'Rapid Cycling':'Rapid_Cycling'}, inplace=True)

#Modify subject_ID to match format of FA file
UNSW_Clinical['Subject_ID'] = UNSW_Clinical['Subject_ID'].astype(str).str[0:3]+ '_1_dti'

#Round up 
UNSW_Clinical['Age_of_Onset'] = np.ceil(UNSW_Clinical['Age_of_Onset'])

#Modify subject_ID to match format of FA file
UNSW_Clinical['Subject_ID'] = UNSW_Clinical['Subject_ID'].astype(str).str[0:3]+ '_1_dti'

#Change Coding 
UNSW_Clinical = UNSW_Clinical.fillna({'Full_Diagnosis': 0}, inplace=True)
UNSW_Clinical.replace({'Full_Diagnosis' : {'Control' : 0, 'Bipolar I' : 1, 'Bipolar II' : 2}}, inplace=True)
UNSW_Clinical.replace({'Mood_Phase_ToS' : {'Neither' : 0, 'Depressive' : 1, 'Manic' : 2}}, inplace=True)
UNSW_Clinical.replace({'Psychotic_Feat' : {'No' : 0, 'Yes' : 1}}, inplace=True)
UNSW_Clinical.replace({'Suicide_Attempt' : {'No' : 0, 'Yes' : 1}}, inplace=True)
UNSW_Clinical.replace({'On_Med_ToS' : {'No' : 0, 'Yes' : 1}}, inplace=True)
UNSW_Clinical.replace({'Meds_Antipsychotics' : {'No' : 0, 'Yes' : 1}}, inplace=True)
UNSW_Clinical.replace({'Meds_Antidepressants' : {'No' : 0, 'Yes' : 1}}, inplace=True)
UNSW_Clinical.replace({'Meds_Anticonvulsants' : {'No' : 0, 'Yes' : 1}}, inplace=True)
UNSW_Clinical.replace({'Meds_Lithium' : {'No' : 0, 'Yes' : 1}}, inplace=True)
UNSW_Clinical.replace({'Hx_Alcohol_Dep' : {'Yes' : 1}}, inplace=True)
UNSW_Clinical.replace({'Rapid_Cycling' : {'No' : 0, 'Yes' : 1}}, inplace=True)
#Replace missing, Not applicable, not completed etc. values with NaN
UNSW_Clinical = UNSW_Clinical.replace('-99', np.nan)
UNSW_Clinical = UNSW_Clinical.replace('-98', np.nan)
UNSW_Clinical = UNSW_Clinical.replace('-96', np.nan)

#Merge Recoded FA and Cov files into one
UNSW_MergedFAClinical = pd.merge(UNSW_Clinical, UNSW_FA, how='right', on='Subject_ID')

####Begin Site 24_VitaSalute
VitaSalute_FA = pd.read_csv('/home/melissa/Desktop/OriginalFiles/VitaSalute_Original/Original_VitaSalute_combinedROItable_wDX.csv')

#Add Columns to Identify Site
VitaSalute_FA.insert(0, 'Site', 'VitaSalute')
VitaSalute_FA.insert(1, 'Site_ID', 24)

#Standardize site names
VitaSalute_FA.rename(columns={'subjectID':'Subject_ID', 
                              'Age':'Age_at_ToS', 
                              'Diagnosis':'HC_Pat'}, inplace=True)

#Deletesubjects not meeting inclusion criteria 
VitaSalute_FA = VitaSalute_FA[(VitaSalute_FA.Age_at_ToS < 66) & (VitaSalute_FA.Age_at_ToS > 17)]

#Look for duplicate subjects
pd.options.display.max_rows = (500)
print(VitaSalute_FA.duplicated('Subject_ID'))

VitaSalute_Clinical = pd.read_csv('/home/melissa/Desktop/OriginalFiles/VitaSalute_Original/Original_VitaSalute_ALL_Subject_Info.csv')

#Delete columns
VitaSalute_Clinical.drop(['Age', 'Sex', 'Diagnosis', 'Ill_dur', 'Epi_dur', 'Tot_epi'], axis=1, inplace=True)

#Change Relevant Column Names
VitaSalute_Clinical.rename(columns={'SubjID':'Subject_ID',
                                    'N_dep':'No_Depressive_Ep', 
                                    'N_man':'No_Manic_Ep','Onset':'Age_of_Onset',
                                    'Delus':'Psychotic_Feat', 
                                    'SA':'Suicide_Attempt', 
                                    'Phase':'Mood_Phase_ToS'}, inplace=True)

#Change Coding 
VitaSalute_Clinical.replace({'Full_Diagnosis' : {'Control': 0, 'BP1': 1}}, inplace=True)
VitaSalute_Clinical.replace({'On_Med_ToS' : {'Y' : 1, 'N' : 0}}, inplace=True)
VitaSalute_Clinical.replace({'Suicide_Attempt' : {2 : 1, 3 : 1}}, inplace=True)

#add missing columns
VitaSalute_Clinical = VitaSalute_Clinical.reindex(columns = np.append(VitaSalute_Clinical.columns.values,[
        'Full_Diagnosis', 'Depression_Scale', 'Depression_Score_ToS', 'Mania_Scale', 'Mania_Score_ToS', 
        'On_Med_ToS', 'Meds_Antipsychotics', 'Time_on_Antipsychotics', 'Meds_Antidepressants', 
        'Time_on_Antidepressants', 'Meds_Anticonvulsants', 'Time_on_Anticonvulsants', 'Meds_Lithium', 
        'Time_on_Lithium', 'Hx_Alcohol_Dep', 'Rapid_Cycling']))

#Merge FA and Clinical data frames
VitaSalute_MergedFAClinical = pd.merge(VitaSalute_Clinical, VitaSalute_FA, how='right', on='Subject_ID')

#COMBINE DATA FRAMES, Master Data Frame, all subjects, all columns, with FA data and their clinical info, including controls
Clinical_FA_AllSubjects = ([Cardiff_MergedFAClinical, Columbia_MergedFAClinical, Creteil_MergedFAClinical, 
                            EdinburghSiteE_MergedFAClinical, Edinburgh_MergedFAClinical, FIDMAG_MergedFAClinical,
                            Grenoble_MergedFAClinical, IoL13_MergedFAClinical, IoL33_MergedFAClinical, IoL58_MergedFAClinical, 
                            KI_MergedFAClinical, Mannheim_MergedFAClinical, Muenster_MergedFAClinical,
                            OsloMalt_MergedFAClinical, Pittsburgh_MergedFAClinical, SaoPaulo_MergedFAClinical, 
                            TOP_MergedFAClinical, UCSD_MergedFAClinical, UCT_MergedFAClinical, UMCA_UCLA_MergedFAClinical, 
                            UNC_Phillips_MergedFAClinical, UNC_Seimens_MergedFAClinical, UNSW_MergedFAClinical, 
                            VitaSalute_MergedFAClinical]) 

Clinical_FA_AllSubjects = pd.concat(Clinical_FA_AllSubjects)
#Reset index
Clinical_FA_AllSubjects = Clinical_FA_AllSubjects.reset_index(drop=True)

#Replace / and - with _ in column names
Clinical_FA_AllSubjects.columns = Clinical_FA_AllSubjects.columns.str.replace('-', '_')
Clinical_FA_AllSubjects.columns = Clinical_FA_AllSubjects.columns.str.replace('/', '_')

#Reorder dataframe 
Clinical_FA_AllSubjects = Clinical_FA_AllSubjects[['Site', 'Site_ID', 'Subject_ID', 'Age_at_ToS', 'Age_of_Onset', 'Sex', 
                                                   'HC_Pat', 'Full_Diagnosis', 'Mood_Phase_ToS', 'Depression_Scale', 
                                                   'Depression_Score_ToS', 'No_Depressive_Ep', 'Mania_Scale', 'Mania_Score_ToS',
                                                   'No_Manic_Ep', 'Psychotic_Feat', 'Suicide_Attempt', 'On_Med_ToS', 
                                                   'Meds_Antipsychotics', 'Time_on_Antipsychotics', 'Meds_Antidepressants', 
                                                   'Time_on_Antidepressants', 'Meds_Anticonvulsants', 'Time_on_Anticonvulsants',
                                                   'Meds_Lithium', 'Time_on_Lithium', 'Hx_Alcohol_Dep', 'Rapid_Cycling', 
                                                   'ACR', 'ACR_L', 'ACR_R', 'ALIC', 'ALIC_L', 'ALIC_R', 'AverageFA', 'BCC', 
                                                   'CC', 'CGC', 'CGC_L', 'CGC_R', 'CGH', 'CGH_L', 'CGH_R', 'CR', 'CR_L', 
                                                   'CR_R', 'CST', 'CST_L', 'CST_R', 'EC', 'EC_L', 'EC_R', 'FX', 'FX_ST_L', 
                                                   'FX_ST_R', 'FXST', 'GCC', 'IC', 'IC_L', 'IC_R', 'IFO', 'IFO_L', 'IFO_R', 
                                                   'PCR', 'PCR_L', 'PCR_R', 'PLIC', 'PLIC_L', 'PLIC_R', 'PTR', 'PTR_L', 
                                                   'PTR_R', 'RLIC', 'RLIC_L', 'RLIC_R', 'SCC', 'SCR', 'SCR_L', 'SCR_R', 
                                                   'SFO', 'SFO_L', 'SFO_R', 'SLF', 'SLF_L', 'SLF_R', 'SS', 'SS_L', 'SS_R', 
                                                   'UNC', 'UNC_L', 'UNC_R']]

Clinical_FA_AllSubjects.to_csv('ENIGMA_FA_Clinical_Merged_Data_AllSubjects.csv', index=False)

#Clinical and FA data for patients only, it includes Columbia which is a patient only sample and patietns removed from KI due to their being more patients than controls 
Clinical_FA_PatientsOnly = Clinical_FA_AllSubjects.copy()
#Reset index
Clinical_FA_PatientsOnly = Clinical_FA_PatientsOnly.reset_index(drop=True)

Clinical_FA_PatientsOnly = Clinical_FA_PatientsOnly[Clinical_FA_PatientsOnly['HC_Pat'] == 1]

#Drop columns where not enough data is present for analysis
Clinical_FA_PatientsOnly.drop(['Time_on_Antipsychotics', 'Time_on_Antidepressants', 'Time_on_Anticonvulsants', 
                               'Time_on_Lithium', 'Hx_Alcohol_Dep', 'Rapid_Cycling'], axis=1, inplace=True)

Clinical_FA_PatientsOnly['No_Manic_Ep'] = Clinical_FA_PatientsOnly['No_Manic_Ep'].convert_objects(convert_numeric=True)
Clinical_FA_PatientsOnly['No_Depressive_Ep'] = Clinical_FA_PatientsOnly['No_Depressive_Ep'].convert_objects(convert_numeric=True)

#Add columns
Clinical_FA_PatientsOnly['Illness_Duration'] = Clinical_FA_PatientsOnly['Age_at_ToS'] - Clinical_FA_PatientsOnly['Age_of_Onset']     
    
#Creeate column for age of onset category, young, late and expected
for i, row in Clinical_FA_PatientsOnly.iterrows():
    if row['Age_of_Onset'] < 19:
      Clinical_FA_PatientsOnly.ix[i,'Onset_Category']= 1
    elif row['Age_of_Onset'] > 44:
      Clinical_FA_PatientsOnly.ix[i,'Onset_Category']= 2
    elif (row['Age_of_Onset'] > 18) & (row['Age_of_Onset'] < 45):
      Clinical_FA_PatientsOnly.ix[i,'Onset_Category']= 0 
    else: Clinical_FA_PatientsOnly.ix[i,'Onset_Category']= np.nan
    
#Create column for number of manic and depressive episodes, less than 10 and greater than 10   
for i, row in Clinical_FA_PatientsOnly.iterrows():
    if (row['No_Manic_Ep'] >= 1) & (row['No_Manic_Ep'] <=10): 
      Clinical_FA_PatientsOnly.ix[i,'Manic_Ep_Categorical']= 1
    elif row['No_Manic_Ep'] >= 11:
      Clinical_FA_PatientsOnly.ix[i,'Manic_Ep_Categorical']= 2 
    elif row['No_Manic_Ep'] == 0:
      Clinical_FA_PatientsOnly.ix[i,'Manic_Ep_Categorical']= 0
    else: Clinical_FA_PatientsOnly.ix[i,'Manic_Ep_Categorical']= np.nan
    
for i, row in Clinical_FA_PatientsOnly.iterrows():
    if (row['No_Depressive_Ep'] >= 1) & (row['No_Depressive_Ep'] <=10): 
      Clinical_FA_PatientsOnly.ix[i,'Depressive_Ep_Categorical']= 1
    elif row['No_Depressive_Ep'] >= 11:
      Clinical_FA_PatientsOnly.ix[i,'Depressive_Ep_Categorical']= 2 
    elif row['No_Depressive_Ep'] == 0:
      Clinical_FA_PatientsOnly.ix[i,'Depressive_Ep_Categorical']= 0
    else: Clinical_FA_PatientsOnly.ix[i,'Depressive_Ep_Categorical']= np.nan    
    
#Reorder dataframe 
Clinical_FA_PatientsOnly = Clinical_FA_PatientsOnly[['Site', 'Site_ID', 'Subject_ID', 'Age_at_ToS', 'Age_of_Onset', 
                                                     'Onset_Category', 'Illness_Duration', 'Sex','HC_Pat', 'Full_Diagnosis', 
                                                     'Mood_Phase_ToS', 'Depression_Scale', 'Depression_Score_ToS', 
                                                     'No_Depressive_Ep', 'Depressive_Ep_Categorical', 'Mania_Scale', 
                                                     'Mania_Score_ToS', 'No_Manic_Ep', 'Manic_Ep_Categorical', 
                                                     'Psychotic_Feat', 'Suicide_Attempt', 'On_Med_ToS','Meds_Antipsychotics',
                                                     'Meds_Antidepressants', 'Meds_Anticonvulsants', 'Meds_Lithium', 
                                                     'ACR', 'ACR_L', 'ACR_R', 'ALIC', 'ALIC_L', 'ALIC_R', 'AverageFA', 'BCC', 
                                                     'CC', 'CGC', 'CGC_L', 'CGC_R', 'CGH', 'CGH_L', 'CGH_R', 'CR', 'CR_L', 
                                                     'CR_R', 'CST', 'CST_L', 'CST_R', 'EC', 'EC_L', 'EC_R', 'FX', 'FX_ST_L', 
                                                     'FX_ST_R', 'FXST', 'GCC', 'IC', 'IC_L', 'IC_R', 'IFO', 'IFO_L', 'IFO_R', 
                                                     'PCR', 'PCR_L', 'PCR_R', 'PLIC', 'PLIC_L', 'PLIC_R', 'PTR', 'PTR_L', 
                                                     'PTR_R', 'RLIC', 'RLIC_L', 'RLIC_R', 'SCC', 'SCR', 'SCR_L', 'SCR_R', 
                                                     'SFO', 'SFO_L', 'SFO_R', 'SLF', 'SLF_L', 'SLF_R', 'SS', 'SS_L', 'SS_R', 
                                                     'UNC', 'UNC_L', 'UNC_R']]

Clinical_FA_PatientsOnly.to_csv('ENIGMA_FA_Clinical_Merged_PatientsOnly.csv', index=False)

#Combine data frames, all sites with patients and controls and  each has a 3:1 ration of contols to patients and vice versa
FA_CaseControl = [UMCA_UCLA_FA, UCT_FA, UCSD_FA, TOP_FA_SubjRemoved, SaoPaulo_FA, Pittsburgh_FA, OsloMalt_FA, 
                  Muenster_FA_SubjRemoved, Mannheim_FA, FIDMAG_FA, Grenoble_FA, UNC_Phillips_FA, Edinburgh_FA, 
                  EdinburghSiteE_FA, Creteil_FA, IoL13_FA_SubjRemoved, IoL33_FA_SubjRemoved, IoL58_FA, KI_FA_SubjRemoved, 
                  UNC_Seimens_FA, UNSW_FA, VitaSalute_FA , Cardiff_FA]

FA_CaseControl = pd.concat(FA_CaseControl)
#Reset index
FA_CaseControl = FA_CaseControl.reset_index(drop=True)

#Replace / and - with _ in column names
FA_CaseControl.columns = FA_CaseControl.columns.str.replace('-', '_')
FA_CaseControl.columns = FA_CaseControl.columns.str.replace('/', '_')

#Reorder dataframe 
FA_CaseControl = FA_CaseControl[['Site', 'Site_ID', 'Subject_ID', 'Age_at_ToS', 'Sex', 'HC_Pat', 
                                 'ACR', 'ACR_L', 'ACR_R', 'ALIC', 'ALIC_L', 'ALIC_R', 'AverageFA', 'BCC', 
                                 'CC', 'CGC', 'CGC_L', 'CGC_R', 'CGH', 'CGH_L', 'CGH_R', 'CR', 'CR_L', 'CR_R', 'CST', 'CST_L', 
                                 'CST_R', 'EC', 'EC_L', 'EC_R', 'FX', 'FX_ST_L', 'FX_ST_R', 'FXST', 'GCC', 'IC', 'IC_L', 'IC_R',
                                 'IFO', 'IFO_L', 'IFO_R', 'PCR', 'PCR_L', 'PCR_R', 'PLIC', 'PLIC_L', 'PLIC_R', 'PTR', 'PTR_L', 
                                 'PTR_R', 'RLIC', 'RLIC_L', 'RLIC_R', 'SCC', 'SCR', 'SCR_L', 'SCR_R', 'SFO', 'SFO_L', 'SFO_R', 
                                 'SLF', 'SLF_L', 'SLF_R', 'SS', 'SS_L', 'SS_R', 'UNC', 'UNC_L', 'UNC_R']]

FA_CaseControl.to_csv('ENIGMA_FA_Case_Control_Data.csv', index=False)





































